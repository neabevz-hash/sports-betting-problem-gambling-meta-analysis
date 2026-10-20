"""Automated searches for the sports-betting problem-gambling prevalence meta-analysis (protocol, sections 9-10).

Runs every automated search and writes the raw records to search/runs/<date>/raw/<source>.jsonl and the run log
(query strings, record counts, timestamps) to search/runs/<date>/search_log.json. dedup.py then merges duplicates
and builds the screening list. Template: papers/ai-dependence-correlates/search/search.py; phrase set from the novelty
check (novelty/fetch_sources.py) without the race-betting terms (race-only betting is not eligible, protocol §8).

The search uses the population concept only (sports betting); no terms for problem gambling or prevalence (§10).

Sources:
  pubmed           PubMed, proximity pairs [tiab:~2] (quoted phrases are silently dropped when missing from
                   PubMed's phrase index);
  europepmc        Europe PMC including preprints, TITLE_ABS phrases;
  openalex         OpenAlex, title-and-abstract phrase search;
  openalex_non_en  OpenAlex, non-English terms;
  s2               Semantic Scholar bulk search;
  crossref         Crossref, relevance-sorted queries, kept when title or abstract matches (posted content, reports);
  datacite         DataCite (theses, OSF, Zenodo, figshare);
  openaire         OpenAIRE Graph (repository publications, theses, reports);
  core             CORE API v3 (repositories);
  citations        OpenAlex: the reference list of Tran et al. (2024) and the records citing it — population gambling
                   surveys that report problem gambling by activity only in tables (§9).
Manual sources (SciELO, Google Scholar via Publish or Perish) go through import_manual.py into the same format.

Run:  .venv/Scripts/python.exe papers/sports-betting-prevalence/search/search.py [sources...] [--date YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
from datetime import date, datetime, timezone
from pathlib import Path

import httpx
from lxml import etree

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def _uniq(xs):
    seen, out = set(), []
    for x in xs:
        if x.lower() not in seen:
            seen.add(x.lower())
            out.append(x)
    return out


# ---------------------------------------------------------------- phrase set (protocol §10)
SPORT = ["sports", "sport", "esports", "e-sports", "football", "soccer", "fantasy sports", "daily fantasy sports"]
BET = ["betting", "bettors", "bettor", "wagering", "gambling", "gamblers", "bets"]
PHRASES = _uniq([f"{s} {b}" for s in SPORT for b in BET] + [
    "betting on sports", "betting on sport", "gambling on sports", "wagering on sports", "bet on sports",
    "fantasy sports", "fantasy sport", "daily fantasy", "sports lottery", "sport lottery", "sports lotteries",
    "in-play betting", "live betting", "in-play sports betting", "sportsbook", "sportsbooks", "esports gambling",
    "match betting", "online betting", "sports pools", "sports tipping"])

PM_SPORT = ["sport", "sports", "esports", "football", "soccer", "fantasy sports"]
PM_BET = ["betting", "bettors", "bettor", "wagering", "gambling", "gamblers", "bet", "bets", "wager", "lottery"]
PM_SINGLE = ['"in-play betting"[tiab]', '"live betting"[tiab]', '"online betting"[tiab:~2]', "sportsbook*[tiab]",
             '"daily fantasy"[tiab]', '"match betting"[tiab]']

NON_EN = ["apostas esportivas", "apostas desportivas", "apostadores esportivos", "bets esportivas",
          "apuestas deportivas", "apostadores deportivos", "paris sportifs", "parieurs sportifs", "Sportwetten",
          "scommesse sportive", "spor bahisleri", "spor bahis", "zakłady sportowe", "ставки на спорт",
          "спортивные ставки", "букмекерские ставки", "体育彩票", "体育博彩", "足球彩票", "竞猜型体育彩票",
          "스포츠 도박", "스포츠토토", "スポーツベッティング", "sportsspill", "sportsvæddemål", "vadslagning"]

# One query per phrase (OpenAIRE: at most four OR operators per query; CORE: no OR lists inside field queries).
CORE_PHRASES = ["sports betting", "sport betting", "sports bettors", "sports wagering", "sports gambling",
                "sports gamblers", "fantasy sports", "daily fantasy sports", "esports betting", "esports gambling",
                "sports lottery", "football betting", "soccer betting", "in-play betting", "online betting",
                "betting on sports", "apostas esportivas", "apuestas deportivas"]

CR_QUERIES = ["sports betting", "sports bettors", "sports wagering", "sports gambling", "sport betting",
              "fantasy sports gambling", "daily fantasy sports", "esports betting", "sports lottery gambling",
              "football betting", "soccer betting", "in-play betting", "online sports betting",
              "sports betting problem gambling", "apostas esportivas"]
CR_KEEP = re.compile(
    r"sports?[- ]?(betting|bettors?|bets?|wager|gambl|lotter|book)|e-?sports?[- ](betting|bettors?|gambl|wager)|"
    r"(betting|wagering|gambling|bets?) on (sports?|football|soccer|e-?sports)|fantasy sports?|daily fantasy|"
    r"(football|soccer|cricket|basketball)[- ](betting|bettors?|gambl|wager|pools?)|in-play|live betting|"
    r"online betting|apostas? (esportiv|desportiv)|apuestas deportiv", re.I | re.S)

# Tran et al. (2024), Lancet Public Health: its reference list (population prevalence surveys) and the records citing it.
TRAN_DOI = "10.1016/s2468-2667(24)00126-9"

UA = "sports-betting-prevalence-search/1.0 (mailto:mrexert@gmail.com)"


def load_env() -> dict[str, str]:
    env = {}
    if not (ROOT / ".env").exists():   # the public release has no keys; the phrase lists still import
        return env
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


ENV = load_env()
client = httpx.Client(headers={"User-Agent": UA}, timeout=90, follow_redirects=True)


def _request(method: str, url: str, params: dict | None = None, data: dict | None = None, tries: int = 6, **kw):
    last = None
    for i in range(tries):
        try:
            r = client.request(method, url, params=params, data=data, **kw)
        except httpx.HTTPError as e:  # network
            last = e
            time.sleep(3 * (i + 1))
            continue
        if r.status_code == 200:
            return r
        last = r
        if r.status_code in (429, 500, 502, 503, 504):
            time.sleep(3 * (i + 1))
            continue
        r.raise_for_status()
    raise RuntimeError(f"{method} failed: {url} {params} -> {last}")


def get(url, params=None, **kw):
    return _request("GET", url, params=params, **kw)


def post(url, data, **kw):
    return _request("POST", url, data=data, **kw)


def chunks(xs: list, n: int):
    for i in range(0, len(xs), n):
        yield xs[i:i + n]


def inv_to_text(inv: dict | None) -> str:
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def norm_doi(d: str | None) -> str:
    d = (d or "").strip().lower()
    for p in ("https://doi.org/", "http://doi.org/", "doi:"):
        if d.startswith(p):
            d = d[len(p):]
    return d


def q(p: str) -> str:
    return f'"{p}"'


# ---------------------------------------------------------------- sources
def pubmed_queries() -> list[str]:
    pairs = [f'"{s} {b}"[tiab:~2]' for s in PM_SPORT for b in PM_BET]
    return [" OR ".join(ch) for ch in chunks(pairs + PM_SINGLE, 33)]


def _pubmed_parse(x: bytes) -> list[dict]:
    out = []
    root = etree.fromstring(x)
    for art in root.findall(".//PubmedArticle"):
        pmid = art.findtext(".//MedlineCitation/PMID")
        node = art.find(".//ArticleTitle")
        title = "".join(node.itertext()) if node is not None else ""
        abstract = " ".join("".join(a.itertext()) for a in art.findall(".//Abstract/AbstractText"))
        doi = next((aid.text or "" for aid in art.findall(".//PubmedData/ArticleIdList/ArticleId")
                    if aid.get("IdType") == "doi"), "")
        year = art.findtext(".//JournalIssue/PubDate/Year") or (art.findtext(".//JournalIssue/PubDate/MedlineDate") or "")[:4]
        au = art.find(".//AuthorList/Author")
        first = (au.findtext("LastName") or au.findtext("CollectiveName") or "") if au is not None else ""
        out.append({
            "source": "pubmed", "source_id": f"PMID:{pmid}", "pmid": pmid, "doi": norm_doi(doi), "title": title,
            "abstract": abstract, "year": year, "venue": art.findtext(".//Journal/Title") or "",
            "first_author": first, "type": ";".join(p.text or "" for p in art.findall(".//PublicationType")),
            "language": ";".join(l.text or "" for l in art.findall(".//Language")),
        })
    for art in root.findall(".//PubmedBookArticle"):
        pmid = art.findtext(".//BookDocument/PMID")
        node = art.find(".//BookDocument/ArticleTitle")
        if node is None:
            node = art.find(".//BookDocument/Book/BookTitle")
        out.append({
            "source": "pubmed", "source_id": f"PMID:{pmid}", "pmid": pmid, "doi": "",
            "title": "".join(node.itertext()) if node is not None else "",
            "abstract": " ".join("".join(a.itertext()) for a in art.findall(".//BookDocument/Abstract/AbstractText")),
            "year": art.findtext(".//BookDocument/Book/PubDate/Year") or "",
            "venue": art.findtext(".//BookDocument/Book/BookTitle") or "", "first_author": "",
            "type": "Book Chapter", "language": "",
        })
    return out


def pubmed() -> tuple[list[dict], dict]:
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    ids, meta = [], []
    for query in pubmed_queries():
        es = post(base + "esearch.fcgi", {"db": "pubmed", "term": query, "retmax": 9999, "retmode": "json"}).json()["esearchresult"]
        ids += es["idlist"]
        meta.append({"query": query, "count": int(es["count"]), "warnings": es.get("warninglist")})
        time.sleep(0.4)
    ids = list(dict.fromkeys(ids))
    out = []
    for ch in chunks(ids, 200):
        out += _pubmed_parse(post(base + "efetch.fcgi", {"db": "pubmed", "id": ",".join(ch), "retmode": "xml"}).content)
        time.sleep(0.4)
    return out, {"queries": meta, "unique_pmids": len(ids)}


def europepmc() -> tuple[list[dict], dict]:
    queries = [" OR ".join(f"TITLE_ABS:{q(p)}" for p in ch) for ch in chunks(PHRASES, 40)]
    out, seen, meta = [], set(), []
    for query in queries:
        cursor, n, hit = "*", 0, None
        while True:
            d = post("https://www.ebi.ac.uk/europepmc/webservices/rest/searchPOST", {
                "query": query, "format": "json", "pageSize": 1000, "cursorMark": cursor, "resultType": "core"}).json()
            hit = d.get("hitCount")
            res = d.get("resultList", {}).get("result", [])
            for it in res:
                key = f"{it.get('source')}:{it.get('id')}"
                n += 1
                if key in seen:
                    continue
                seen.add(key)
                out.append({
                    "source": "europepmc", "source_id": key, "pmid": it.get("pmid") or "",
                    "doi": norm_doi(it.get("doi")), "title": it.get("title", ""), "abstract": it.get("abstractText", ""),
                    "year": it.get("pubYear", ""),
                    "venue": ((it.get("journalInfo") or {}).get("journal") or {}).get("title")
                    or ((it.get("bookOrReportDetails") or {}).get("publisher")) or "",
                    "first_author": (it.get("authorString") or "").split(",")[0].split(" ")[0],
                    "type": ";".join((it.get("pubTypeList") or {}).get("pubType", [])) + f"|src={it.get('source')}",
                    "language": it.get("language", ""),
                })
            nxt = d.get("nextCursorMark")
            if not res or nxt == cursor or n >= (hit or 0):   # a new cursor comes even after the last page
                break
            cursor = nxt
        meta.append({"query": query, "count": hit})
        time.sleep(0.5)
    return out, {"queries": meta}


OA_SELECT = "id,doi,title,publication_year,type,primary_location,abstract_inverted_index,authorships,ids,language,cited_by_count"


def _openalex_page(filter_str: str) -> list[dict]:
    out, cursor = [], "*"
    while cursor:
        d = get("https://api.openalex.org/works", {"filter": filter_str, "per_page": 200, "cursor": cursor,
                                                   "api_key": ENV["OPENALEX_API_KEY"], "select": OA_SELECT}).json()
        out.extend(d["results"])
        cursor = d["meta"].get("next_cursor") if d["results"] else None
    return out


def _openalex_rec(w: dict, source: str, extra: dict | None = None) -> dict:
    loc = w.get("primary_location") or {}
    auth = w.get("authorships") or []
    rec = {
        "source": source, "source_id": w["id"].replace("https://openalex.org/", ""),
        "pmid": ((w.get("ids") or {}).get("pmid") or "").replace("https://pubmed.ncbi.nlm.nih.gov/", ""),
        "doi": norm_doi(w.get("doi")), "title": w.get("title") or "", "abstract": inv_to_text(w.get("abstract_inverted_index")),
        "year": w.get("publication_year"), "venue": (loc.get("source") or {}).get("display_name") or "",
        "first_author": ((auth[0].get("author") or {}).get("display_name") or "").split(" ")[-1] if auth else "",
        "type": w.get("type") or "", "language": w.get("language") or "",
    }
    if extra:
        rec.update(extra)
    return rec


def _openalex_union(filters: list[str], source: str) -> tuple[list[dict], list[dict]]:
    out, seen, meta = [], set(), []
    for flt in filters:
        raw = _openalex_page(flt)
        meta.append({"filter": flt, "count": len(raw)})
        for w in raw:
            if w["id"] not in seen:
                seen.add(w["id"])
                out.append(_openalex_rec(w, source))
        time.sleep(0.3)
    return out, meta


def openalex() -> tuple[list[dict], dict]:
    filters = ["title_and_abstract.search:" + "|".join(q(p) for p in ch) for ch in chunks(PHRASES, 40)]
    out, meta = _openalex_union(filters, "openalex")
    return out, {"filters": meta}


def openalex_non_en() -> tuple[list[dict], dict]:
    out, meta = _openalex_union([f"title_and_abstract.search:{q(t)}" for t in NON_EN], "openalex_non_en")
    return out, {"filters": meta}


def citations() -> tuple[list[dict], dict]:
    """Backward and forward citations of Tran et al. (2024): population prevalence surveys report problem gambling
    by gambling activity only in tables, so their abstracts do not mention sports betting (protocol §9)."""
    key = {"api_key": ENV["OPENALEX_API_KEY"]}
    w = get(f"https://api.openalex.org/works/doi:{TRAN_DOI}", {**key, "select": "id,referenced_works"}).json()
    wid = w["id"].split("/")[-1]
    refs = [r.split("/")[-1] for r in w.get("referenced_works") or []]
    out = []
    for ch in chunks(refs, 50):
        for x in _openalex_page("openalex:" + "|".join(ch)):
            out.append(_openalex_rec(x, "citations", {"cites": "reference of Tran 2024"}))
    citing = _openalex_page(f"cites:{wid}")
    out.extend(_openalex_rec(x, "citations", {"cites": "cites Tran 2024"}) for x in citing)
    return out, {"tran_2024": {"doi": TRAN_DOI, "openalex": wid, "referenced_works": len(refs),
                               "citing_records": len(citing)}}


def semantic_scholar() -> tuple[list[dict], dict]:
    queries = [" | ".join(q(p) for p in ch) for ch in chunks(PHRASES, 30)]
    fields = "title,year,externalIds,publicationTypes,venue,abstract,authors"
    out, seen, meta = [], set(), []
    for query in queries:
        token, n = None, 0
        while True:
            params = {"query": query, "fields": fields}
            if token:
                params["token"] = token
            r = None
            for i in range(10):
                r = client.get("https://api.semanticscholar.org/graph/v1/paper/search/bulk", params=params)
                if r.status_code == 200:
                    break
                time.sleep(4 * (i + 1))
            if r is None or r.status_code != 200:
                raise RuntimeError(f"S2 failed: {r.status_code if r is not None else None}")
            d = r.json()
            for it in d.get("data", []):
                n += 1
                if it["paperId"] in seen:
                    continue
                seen.add(it["paperId"])
                ext = it.get("externalIds") or {}
                out.append({
                    "source": "s2", "source_id": f"S2:{it.get('paperId')}", "pmid": str(ext.get("PubMed") or ""),
                    "doi": norm_doi(ext.get("DOI")), "title": it.get("title") or "", "abstract": it.get("abstract") or "",
                    "year": it.get("year"), "venue": it.get("venue") or "",
                    "first_author": ((it.get("authors") or [{}])[0].get("name") or "").split(" ")[-1] if it.get("authors") else "",
                    "type": ";".join(it.get("publicationTypes") or []), "language": "",
                })
            token = d.get("token")
            if not token:
                break
            time.sleep(1.5)
        meta.append({"query": query, "count": n})
        time.sleep(1.5)
    return out, {"queries": meta}


def crossref() -> tuple[list[dict], dict]:
    """Crossref: posted content (Research Square, SSRN, Preprints.org), INPLASY, conference papers.

    With a cursor Crossref does not sort by relevance, so offset + sort=score; a query stops when a page of 1,000
    yields fewer than five records that match CR_KEEP in title or abstract (fuzzy search: the rest is noise).
    """
    out, seen, meta = [], set(), {}
    for query in CR_QUERIES:
        n, kept = 0, 0
        while n < 3000:
            m = get("https://api.crossref.org/works", {
                "query.bibliographic": query, "rows": 1000, "offset": n, "sort": "score", "order": "desc",
                "mailto": "mrexert@gmail.com",
                "select": "DOI,title,type,issued,container-title,abstract,author,publisher"}).json()["message"]
            items = m["items"]
            keep = [it for it in items if CR_KEEP.search(" ".join(it.get("title") or []) + " " + (it.get("abstract") or ""))]
            for it in keep:
                doi = it["DOI"].lower()
                if doi in seen:
                    continue
                seen.add(doi)
                kept += 1
                yr = ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0]
                out.append({
                    "source": "crossref", "source_id": f"DOI:{doi}", "pmid": "", "doi": norm_doi(doi),
                    "title": " ".join(it.get("title") or []), "abstract": re.sub(r"<[^>]+>", " ", it.get("abstract") or ""),
                    "year": yr or "", "venue": " ".join(it.get("container-title") or []) or it.get("publisher") or "",
                    "first_author": ((it.get("author") or [{}])[0].get("family") or "") if it.get("author") else "",
                    "type": it.get("type") or "", "language": "",
                })
            n += len(items)
            if not items or len(keep) < 5:
                break
            time.sleep(1)
        meta[query] = {"scanned": n, "kept_new": kept}
    return out, {"queries": meta}


def datacite() -> tuple[list[dict], dict]:
    def field_query(terms: str) -> str:
        return f"titles.title:{terms} OR descriptions.description:{terms} OR subjects.subject:{terms}"
    queries = [field_query("(" + " OR ".join(q(p) for p in ch) + ")") for ch in chunks(PHRASES, 40)]
    out, seen, meta = [], set(), []
    for query in queries:
        url, params, total = "https://api.datacite.org/dois", {"query": query, "page[size]": 1000, "page[cursor]": 1}, None
        while url:
            d = get(url, params).json()
            total = (d.get("meta") or {}).get("total", total)
            for it in d.get("data", []):
                a = it["attributes"]
                doi = norm_doi(a.get("doi"))
                if doi in seen:
                    continue
                seen.add(doi)
                types = a.get("types") or {}
                descs = [dd for dd in a.get("descriptions") or [] if isinstance(dd.get("description"), str)]
                abstract = next((dd["description"] for dd in descs if dd.get("descriptionType") == "Abstract"), "") \
                    or " ".join(dd["description"] for dd in descs)
                creator = (a.get("creators") or [{}])[0] if a.get("creators") else {}
                publisher = a.get("publisher")
                out.append({
                    "source": "datacite", "source_id": f"DataCite:{doi}", "pmid": "", "doi": doi,
                    "title": " ".join(t.get("title", "") for t in (a.get("titles") or [])[:1]),
                    "abstract": abstract[:5000], "year": a.get("publicationYear") or "",
                    "venue": (a.get("container") or {}).get("title")
                    or (publisher.get("name") if isinstance(publisher, dict) else publisher) or "",
                    "first_author": creator.get("familyName") or (creator.get("name") or "").split(",")[0],
                    "type": f"{types.get('resourceTypeGeneral') or ''}/{types.get('resourceType') or ''}",
                    "language": a.get("language") or "",
                })
            url = (d.get("links") or {}).get("next")
            params = None
        meta.append({"query": query, "total": total})
        time.sleep(0.5)
    return out, {"queries": meta}


def openaire() -> tuple[list[dict], dict]:
    """OpenAIRE Graph API (at most four OR operators per query: CORE_PHRASES in groups of five)."""
    out, seen, meta = [], set(), {}
    for ch in chunks(CORE_PHRASES, 5):
        query = " OR ".join(q(p) for p in ch)
        cursor, n, found = "*", 0, None
        while cursor:
            d = get("https://api.openaire.eu/graph/v1/researchProducts",
                    {"search": query, "type": "publication", "pageSize": 100, "cursor": cursor}).json()
            head = d.get("header") or {}
            found = head.get("numFound", found)
            res = d.get("results") or []
            for w in res:
                n += 1
                if w.get("id") in seen:
                    continue
                seen.add(w.get("id"))
                pids = {(p.get("scheme") or "").lower(): p.get("value") for p in (w.get("pids") or [])}
                inst = w.get("instances") or []
                for i in inst:
                    for p in (i.get("pids") or []) + (i.get("alternateIdentifiers") or []):
                        pids.setdefault((p.get("scheme") or "").lower(), p.get("value"))
                auth = (w.get("authors") or [{}])[0] if w.get("authors") else {}
                out.append({
                    "source": "openaire", "source_id": f"OpenAIRE:{w.get('id')}", "pmid": str(pids.get("pmid") or ""),
                    "doi": norm_doi(pids.get("doi")), "title": w.get("mainTitle") or "",
                    "abstract": " ".join(w.get("descriptions") or [])[:5000],
                    "year": (w.get("publicationDate") or "")[:4],
                    "venue": (w.get("container") or {}).get("name") or w.get("publisher") or "",
                    "first_author": auth.get("surname") or (auth.get("fullName") or "").split(",")[0],
                    "type": "; ".join(sorted({i.get("type") for i in inst if i.get("type")})) or w.get("type") or "",
                    "language": (w.get("language") or {}).get("code") or "",
                    "url": next((u for i in inst for u in (i.get("urls") or [])), ""),
                })
            cursor = head.get("nextCursor") if res else None
            time.sleep(1)
        meta[query] = {"numFound": found, "retrieved": n}
    return out, {"type": "publication", "queries": meta}


def _fold(text: str) -> str:
    return unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode().lower()


def term_in(term: str, text: str) -> bool:
    """True if the phrase occurs as words; case, accents and plural endings ignored."""
    words = _fold(term.strip('"')).split()
    return re.search(r"\b" + r"\s+".join(re.escape(w) for w in words) + r"\w*", _fold(text)) is not None


def core() -> tuple[list[dict], dict]:
    """CORE API v3, title or abstract, one query per phrase; records without the phrase in title or abstract are
    dropped (CORE matches phrases loosely). At most 10 requests a minute: the client paces itself and honours 429.
    A query stops at the first page of 100 with fewer than five phrase matches (check run 2026-10-16: loose matching
    returned thousands of pages)."""
    out, seen, meta = [], set(), {}
    headers = {"Authorization": f"Bearer {ENV['CORE_API_KEY']}"} if ENV.get("CORE_API_KEY") else {}
    for term in CORE_PHRASES:
        query = f"title:{q(term)} OR abstract:{q(term)}"
        offset, total, dropped = 0, None, 0
        while True:
            for attempt in range(10):
                try:
                    r = client.get("https://api.core.ac.uk/v3/search/works/", headers=headers,
                                   params={"q": query, "limit": 100, "offset": offset, "exclude": "fullText"})
                except httpx.HTTPError as e:   # read timeouts happen (novelty check, 2026-10-18)
                    print(f"core: {e!r}, retrying", flush=True)
                    time.sleep(30 * (attempt + 1))
                    continue
                if r.status_code == 200:
                    break
                until = r.headers.get("x-ratelimit-retry-after")
                try:
                    wait = (datetime.fromisoformat(until.replace("+0000", "+00:00")) - datetime.now(timezone.utc)).total_seconds() + 5
                except (AttributeError, ValueError):
                    wait = 30 * (attempt + 1)
                print(f"core: HTTP {r.status_code}, waiting {max(wait, 5):.0f} s", flush=True)
                time.sleep(min(max(wait, 5), 1200))
            else:
                raise RuntimeError(f"CORE failed for {query!r} at offset {offset}")
            d = r.json()
            total = d.get("totalHits", total)
            res = d.get("results") or []
            kept_page = 0
            for w in res:
                if not term_in(term, f"{w.get('title') or ''} {w.get('abstract') or ''}"):
                    dropped += 1
                    continue
                kept_page += 1
                if w.get("id") in seen:
                    continue
                seen.add(w.get("id"))
                auth = (w.get("authors") or [{}])[0] if w.get("authors") else {}
                journals = w.get("journals") or []
                out.append({
                    "source": "core", "source_id": f"CORE:{w.get('id')}", "pmid": str(w.get("pubmedId") or ""),
                    "doi": norm_doi(w.get("doi")), "title": w.get("title") or "", "abstract": (w.get("abstract") or "")[:5000],
                    "year": w.get("yearPublished") or "",
                    "venue": (journals[0].get("title") if journals else "") or w.get("publisher") or "",
                    "first_author": (auth.get("name") or "").split(",")[0].split(" ")[-1],
                    "type": w.get("documentType") or "", "language": ((w.get("language") or {}).get("code") or ""),
                    "url": w.get("downloadUrl") or "",
                })
            offset += len(res)
            time.sleep(7)
            # CORE matches loosely and ranks by relevance: a page of 100 with fewer than 5 phrase matches ends the query
            if not res or offset >= (total or 0) or kept_page < 5:
                break
        meta[query] = {"totalHits": total, "scanned": offset, "dropped_phrase_not_in_title_or_abstract": dropped}
    return out, {"queries": meta, "authenticated": bool(headers)}


SOURCES = {"pubmed": pubmed, "europepmc": europepmc, "openalex": openalex, "openalex_non_en": openalex_non_en,
           "s2": semantic_scholar, "crossref": crossref, "datacite": datacite, "openaire": openaire, "core": core,
           "citations": citations}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sources", nargs="*", default=list(SOURCES))
    ap.add_argument("--date", default=date.today().isoformat())
    a = ap.parse_args()
    run = HERE / "runs" / a.date
    (run / "raw").mkdir(parents=True, exist_ok=True)
    log_path = run / "search_log.json"
    log = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {}
    log["_phrase_sets"] = {"phrases": PHRASES, "pubmed_pairs": [PM_SPORT, PM_BET], "pubmed_single": PM_SINGLE,
                           "non_en": NON_EN, "core_phrases": CORE_PHRASES, "crossref_queries": CR_QUERIES}
    for name in a.sources:
        t0 = time.time()
        try:
            recs, meta = SOURCES[name]()
        except Exception as e:  # noqa: BLE001
            print(f"{name}: FAILED {e!r}", file=sys.stderr, flush=True)
            log[name] = {"error": repr(e), "at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
            continue
        with (run / "raw" / f"{name}.jsonl").open("w", encoding="utf-8") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        log[name] = {"records": len(recs), "meta": meta,
                     "searched_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                     "seconds": round(time.time() - t0, 1)}
        print(f"{name}: {len(recs)} records", flush=True)
        log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
