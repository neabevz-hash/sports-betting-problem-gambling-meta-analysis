"""Verification files for R1 (protocol §11c, §14): the AI extraction drafts as Markdown, and the parser of R1's corrections.

make  - writes extraction/verify/verify_R1_NN.md from the drafts: one block per study, one sub-block per sample with the
        estimates (key numbers in a table), the key fields, the other fields and the nine JBI items, each with its
        location and quote. Under every sample R1 writes corrections in "Правки" and "да" after "Проверено:".
parse - reads the filled files, applies R1's corrections to the stored drafts and writes
        extraction/decisions/samples_R1.csv, estimates_R1.csv and corrections_R1.csv (AI value vs R1 value, for the
        share of corrected values); lists unverified samples and lines it could not read.

Template: papers/misophonia-prevalence/extraction/verify_md.py. The independent check of the numbers uses R1's own
"Где цифры" lines from full-text screening (fulltext/decisions/ft_R1.csv), since there was no AI full-text pass (D7).

Run: .venv/Scripts/python.exe -I papers/sports-betting-prevalence/extraction/verify_md.py make --run 2026-10-18 --draft extract_<date>
     .venv/Scripts/python.exe -I papers/sports-betting-prevalence/extraction/verify_md.py parse --run 2026-10-18 --draft extract_<date>
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
VERIFY = HERE / "verify"
sys.path.insert(0, str(HERE))
from common import load_records  # noqa: E402
STUDIES_PER_FILE = 10

KEY_SAMPLE = ["n_bettors", "sample_type", "sampling", "betting_period"]
OTHER_SAMPLE = ["parent_population", "min_frequency", "country", "subnational", "data_years", "design", "gambling_disclosed",
                "betting_mode", "pct_online", "pct_inplay", "pct_dfs", "pct_esports", "sports_lottery", "mixed_race",
                "legal_status", "n_invited", "n_responded", "response_rate", "age_mean", "age_sd", "age_min", "age_max",
                "age_group", "pct_male", "mode", "weights", "instruments", "instrument_validated_in_language",
                "industry_funding", "funding_coi", "pub_status", "language"]
SAMPLE_FIELDS = KEY_SAMPLE + OTHER_SAMPLE
EST_FIELDS = ["subgroup", "instrument", "threshold", "cumulative", "threshold_source", "author_label", "level", "table_rule",
              "time_frame", "cases", "n", "derived", "derivation", "weighted_pct", "primary_for_authors", "location",
              "quote", "note"]
KEY_EST = ["instrument", "threshold", "level", "cases", "n"]
JBI_Q = {1: "рамка выборки", 2: "способ отбора", 3: "размер выборки", 4: "описание выборки и условий",
         5: "охват (пропуски)", 6: "валидность определения случая", 7: "единое надёжное измерение",
         8: "статистика (числитель и знаменатель)", 9: "отклик"}
VERIFIED = {"да", "+", "x", "х", "yes", "ok"}

HEADER = """# Проверка выписывания — файл {i} из {n}

Черновик заполнил ИИ (Claude Opus 5.5) по полному тексту; у каждого значения указано место и цитата. Проверяете вы, один проход.

**Как проверять выборку:**
1. Откройте полный текст по ссылке у исследования.
2. **Ключевые числа** — сверить с таблицей или текстом статьи всегда: в таблице оценок шкала, порог, уровень, случаи и n; под таблицей n_bettors, sample_type, sampling, betting_period.
3. Остальные поля и пункты JBI: проверить, что значение есть в цитате и место указано верно.
4. Неверное — исправьте строкой в блоке «Правки» этой выборки (по одной правке на строку):
   - `n_bettors = 1400`, `sampling = convenience` — поле выборки;
   - `E2.cases = 103`, `E2.level = L2` — поле оценки E2 (subgroup, instrument, threshold, cumulative, level, cases, n, time_frame, primary_for_authors и др.);
   - `E2 удалить` — убрать оценку;
   - `+ оценка: subgroup=all; instrument=PGSI; threshold=PGSI>=8; cumulative=yes; level=L3; cases=50; n=300; location=Table 2` — добавить оценку;
   - `jbi_6 = no` — пункт JBI;
   - `выборка удалить: причина` — если это не отдельная выборка или её нельзя брать;
   - после `#` — комментарий для Claude.
5. Когда выборка проверена, напишите `да` после «Проверено:».

**Как выписаны оценки.** Категории шкалы — как в статье (для PGSI обычно 0, 1–2, 3–7, 8+); суммы «3 и выше» строит анализ, не вы. **cumulative** = yes, если категория открыта вверх («8+», «≥3»), no — закрытая полоса («3–7»). **Уровень** — по нижней границе категории: PGSI 0 → below; 1–2 → L1; 3–7 → L2; 8+ → L3; BBGS и другие короткие скрининги → L3-screen; интервью → L4; самодельные вопросы и нестандартный подсчёт → not_levelled; порог по распределению выборки → E3.

**Подсказки в файле:** «⚠ Проверка скриптом» — где скрипт нашёл повод присмотреться (уровень не совпадает с таблицей порогов, категории не складываются в n, n оценки не равно n_bettors, числа не встречаются в вашей строке «Где цифры» с этапа полных текстов). «Расхождения в тексте» — ошибки самих авторов, которые нашёл ИИ. Посчитанные ИИ значения (% × n, обратные таблицы) выделены строкой **расчёт**.

**sample_type:** rep_survey_subsample (беттеры внутри вероятностного опроса населения или школ), gamblers_survey_subsample (беттеры внутри невероятностного опроса игроков), bettor_recruited (набраны как беттеры), students, school_pupils, athletes, other. **sampling:** probability, census, quota, operator_customers, venue_intercept, convenience, snowball, NR.
"""


def load(run: str, draft: str):
    recs = load_records(run)
    jobs = json.loads((HERE / "jobs.json").read_text(encoding="utf-8"))
    drafts = {}
    for line in (HERE / "draft" / f"{draft}.jsonl").open(encoding="utf-8"):
        if line.strip():
            d = json.loads(line)
            drafts[d["conv_id"]] = d
    return recs, jobs, drafts


def sample_keys(jobs: list[dict], drafts: dict) -> list[tuple[str, dict, int, dict]]:
    """(sample_key, job, index in job, sample) in study order; keys are <study_id>-<n>."""
    out, count = [], {}
    for j in sorted(jobs, key=lambda x: (x["study_id"], x["job_id"])):
        d = drafts.get(j["job_id"])
        if not d:
            continue
        for i, s in enumerate(d["codes"]["samples"]):
            count[j["study_id"]] = count.get(j["study_id"], 0) + 1
            out.append((f"{j['study_id']}-{count[j['study_id']]}", j, i, s))
    return out


def clip(t: str, n: int) -> str:
    t = re.sub(r"\s+", " ", t or "").strip()
    return t if len(t) <= n else t[: n - 1] + "…"


def cell(t: str) -> str:
    return (t or "").replace("|", "/").replace("\n", " ")


def pct(cases: str, n: str) -> str:
    try:
        c, m = float(cases.replace(",", "")), float(n.replace(",", ""))
        return f"{100 * c / m:.1f}" if m > 0 else ""
    except (ValueError, AttributeError):
        return ""


def link(rec: str, label: str) -> str:
    pdf = PAPER / "fulltext" / "pdf" / f"{rec}.pdf"
    parts = [f"[текст](../../fulltext/text/{rec}.txt)"]
    if pdf.exists():
        parts.append(f"[PDF](../../fulltext/pdf/{rec}.pdf)")
    else:
        for ext in (".docx", ".pdf"):
            m = PAPER / "fulltext" / "manual" / f"{rec}{ext}"
            if m.exists():
                parts.append(f"[файл](../../fulltext/manual/{rec}{ext})")
                break
    return f"{label} {rec}: " + " · ".join(parts)


BANDS = {   # lower bound of a category -> level, by the levels table (forms/instrument_thresholds.csv)
    "PGSI": [(8, "L3"), (3, "L2"), (1, "L1"), (0, "below")],
    "SOGS": [(5, "L3"), (3, "L2"), (1, "L1"), (0, "below")],
    "SOGS-RA": [(4, "L3"), (2, "L2"), (1, "L1"), (0, "below")],
    "DSM-IV-MR-J": [(4, "L3"), (2, "L2"), (1, "L1"), (0, "below")],
    "NODS": [(5, "L3"), (3, "L2"), (1, "L1"), (0, "below")],
    "DSM-IV-screen": [(5, "L3"), (3, "L2"), (1, "L1"), (0, "below")],
    "DSM-5-screen": [(4, "L3"), (2, "L2"), (1, "L1"), (0, "below")],
    "CAGI": [(6, "L3"), (2, "L2"), (0, "below")],
}
LEVEL_ORDER = {"below": 0, "L1": 1, "L2": 2, "L3": 3, "L3-screen": 3, "L4": 4}


def lower_bound(threshold: str) -> float | None:
    """Lower bound of a category such as 'PGSI>=8', 'PGSI 3-7', 'PGSI 0', 'SOGS 5+' or 'DSM-5 criteria>=4'."""
    t = re.sub(r"DSM-?(IV|5)(-MR-J)?|NODS(-SA)?|SOGS(-RA)?|GPSS|CPGI|PGSI|CAGI", " ", threshold or "", flags=re.I)
    if re.search(r"\b(percentile|median|top|mean|sd|and|or)\b", t, re.I):
        return None
    if m := re.search(r"(>=|≥|=>)\s*(\d+(?:\.\d+)?)", t):
        return float(m.group(2))
    if m := re.search(r">\s*(\d+)", t):
        return float(m.group(1)) + 1
    if m := re.search(r"(\d+)\s*(?:\+|or more|and above|\s*[-–]\s*\d+)", t):
        return float(m.group(1))
    nums = re.findall(r"\d+(?:\.\d+)?", t)
    return float(nums[0]) if len(nums) == 1 else None


def expected_level(instrument: str, threshold: str) -> str | None:
    """Level implied by the levels table for the category's lower bound, or None if the rule cannot tell."""
    if instrument not in BANDS:
        return None
    x = lower_bound(threshold)
    if x is None:
        return None
    for cut_, lv in BANDS[instrument]:
        if x >= cut_:
            return lv
    return None


R1_WHERE: dict[str, str] = {}   # rec_id -> R1's "Где цифры" line from full-text screening, filled by make()
INTS = re.compile(r"\d[\d,]*")


def ints(text: str) -> set[int]:
    return {int(x.replace(",", "")) for x in INTS.findall(text or "") if x.replace(",", "")}


def num(v: str) -> float | None:
    try:
        return float((v or "").replace(",", ""))
    except ValueError:
        return None


def flags(s: dict, recs: list[str] | None = None) -> list[str]:
    """Checks by script, shown to R1 next to the estimates; the drafts themselves are not changed."""
    groups: dict[str, list[str]] = {}
    where = " ".join(R1_WHERE.get(r, "") for r in recs or [])
    where_ints = {x for x in ints(where) if x >= 10}
    n_sample = s["n_bettors"]["value"].replace(",", "")
    for i, e in enumerate(s["estimates"], 1):
        c, n = num(e["cases"]), num(e["n"])
        if c is not None and n is not None and c > n:
            groups.setdefault("случаев больше, чем n", []).append(f"E{i}")
        exp = expected_level(e["instrument"], e["threshold"])
        if exp and e["level"] in LEVEL_ORDER and exp != e["level"]:
            groups.setdefault(f"по таблице порогов категория «{e['threshold']}» даёт {exp}, в черновике {e['level']}", []).append(f"E{i}")
        if e["level"] == "L4" and e["instrument"] != "interview":
            groups.setdefault("L4 без интервью: L4 — только диагноз клинициста или структурированное интервью", []).append(f"E{i}")
        if e["subgroup"].strip().lower() == "all" and e["n"] not in ("NR", "NA") and n_sample not in ("NR", "NA") \
                and e["n"].replace(",", "") != n_sample:
            groups.setdefault(f"n оценки не равно n_bettors выборки ({n_sample}): проверьте знаменатель", []).append(f"E{i}")
        if where_ints and e["subgroup"].strip().lower() == "all" and e["derived"] != "yes" and c is not None \
                and n is not None and int(c) not in where_ints and int(n) not in where_ints and c >= 10:
            groups.setdefault("ни случаев, ни n нет в вашей строке «Где цифры» (этап полных текстов) — сверьте", []).append(f"E{i}")
    # categories of one instrument in one subgroup should add up to n when the lowest category is given
    by: dict[tuple, list[tuple[int, dict]]] = {}
    for i, e in enumerate(s["estimates"], 1):
        by.setdefault((e["subgroup"].strip().lower(), e["instrument"], e["n"], e["time_frame"]), []).append((i, e))
    for (sg, ins, n, _), items in by.items():
        if not any(e["level"] == "below" for _, e in items) or num(n) is None:
            continue
        bands = [(i, e) for i, e in items if e["cumulative"] == "no" or e["level"] == "below"]
        top = max((LEVEL_ORDER.get(e["level"], -1) for _, e in bands), default=-1)
        opens = [(i, e) for i, e in items if e["cumulative"] == "yes" and LEVEL_ORDER.get(e["level"], -1) > top]
        parts = bands + sorted(opens, key=lambda x: -LEVEL_ORDER.get(x[1]["level"], -1))[:1]
        vals = [num(e["cases"]) for _, e in parts]
        if None in vals:
            continue
        if abs(sum(vals) - num(n)) > 1:
            groups.setdefault(f"категории ({'+'.join(f'E{i}' for i, _ in parts)}) дают {sum(vals):g}, а n = {n}", []).append(sg)
    return [f"{', '.join(v)}: {k}" for k, v in groups.items()]


def render_sample(key: str, s: dict, recs: list[str] | None = None) -> list[str]:
    L = [f"### {key} · {clip(s['label'], 160)}", f"Отчёты: {s['reports']}", ""]
    L.append("**Оценки — ключевые числа сверить по таблице статьи:**")
    L.append("")
    L.append("| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |")
    L.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
    extra = []
    for i, e in enumerate(s["estimates"], 1):
        L.append(f"| E{i} | {cell(e['subgroup'])} | {cell(e['instrument'])} · {cell(e['threshold'])} | **{e['level']}** | "
                 f"**{cell(e['cases'])} / {cell(e['n'])}** | {pct(e['cases'], e['n'])} | {cell(clip(e['location'], 60))} | "
                 f"«{cell(clip(e['quote'], 220))}» |")
        bits = [f"cumulative: {e['cumulative']}", f"источник порога: {e['threshold_source']}",
                f"правило: {clip(e['table_rule'], 120)}",
                f"у авторов: «{clip(e['author_label'], 80)}»", f"главная у авторов: {e['primary_for_authors']}",
                f"период: {e['time_frame']}"]
        if e["derived"] == "yes":
            bits.append(f"**расчёт: {clip(e['derivation'], 160)}**")
        if e["weighted_pct"] not in ("", "NA", "NR"):
            bits.append(f"взвешенная доля: {e['weighted_pct']}")
        if e["note"]:
            bits.append(f"заметка: {clip(e['note'], 300)}")
        extra.append(f"- E{i}: " + "; ".join(bits))
    L += [""] + extra
    fl = flags(s, recs)
    if fl:
        L += ["", "**⚠ Проверка скриптом (обратите внимание):**"] + [f"- {x}" for x in fl]
    L += ["", "**Ключевые поля выборки:**"]
    for f in KEY_SAMPLE:
        v = s[f]
        L.append(f"- **{f}: {v['value']}** — {clip(v['loc'], 80)} — «{clip(v['quote'], 260)}»")
    L += ["", "**Остальные поля:**"]
    for f in OTHER_SAMPLE:
        v = s[f]
        q = f" — «{clip(v['quote'], 160)}»" if v["quote"] else ""
        loc = f" — {clip(v['loc'], 60)}" if v["loc"] else ""
        L.append(f"- {f}: {clip(v['value'], 300)}{loc}{q}")
    if s.get("notes"):
        L.append(f"- notes: {clip(s['notes'], 600)}")
    L += ["", "**Риск смещения (JBI):**"]
    for i in range(1, 10):
        b = s["jbi"][f"jbi_{i}"]
        q = f" — «{clip(b['quote'], 160)}»" if b["quote"] else ""
        L.append(f"{i}. {JBI_Q[i]}: **{b['rating']}** — {clip(b['reason'], 220)} — {clip(b['loc'], 60)}{q}")
    L += ["", "Правки:", "- ", "", "Проверено: ", ""]
    return L


def make(a):
    recs, jobs, drafts = load(a.run, a.draft)
    for r in csv.DictReader((PAPER / "fulltext" / "decisions" / "ft_R1.csv").open(encoding="utf-8-sig")):
        R1_WHERE[r["rec_id"]] = r.get("where", "")
    missing = [j["job_id"] for j in jobs if j["job_id"] not in drafts]
    if missing and not a.allow_missing:
        raise SystemExit(f"no draft for {len(missing)} jobs: {', '.join(missing)}")
    smap = {}
    for r in csv.DictReader((HERE / "study_map.csv").open(encoding="utf-8")):
        smap.setdefault(r["study_id"], []).append(r)
    keyed = sample_keys(jobs, drafts)
    by_study: dict[str, list] = {}
    for key, j, i, s in keyed:
        by_study.setdefault(j["study_id"], []).append((key, j, s))
    studies = sorted(by_study)
    if a.studies:   # only these studies, in new files numbered from --first-file (files of R1 are never touched)
        studies = [s for s in studies if s in set(a.studies)]
    chunks = [studies[i:i + STUDIES_PER_FILE] for i in range(0, len(studies), STUDIES_PER_FILE)]
    outdir = Path(a.out) if a.out else VERIFY
    outdir.mkdir(exist_ok=True)
    first = a.first_file
    names = [outdir / f"verify_R1_{fi:02d}.md" for fi in range(first, first + len(chunks))]
    clash = [p for p in names if p.exists()]
    if a.studies and clash:
        raise SystemExit(f"refusing to overwrite: {', '.join(p.name for p in clash)}")
    existing = sorted(outdir.glob("verify_R1_*.md"))
    if existing and not a.force and not a.studies:
        raise SystemExit(f"{len(existing)} verification files exist; use --force to overwrite")
    n_samples = n_est = 0
    for fi, chunk in enumerate(chunks, first):
        L = [HEADER.format(i=fi, n=first - 1 + len(chunks))]
        for st in chunk:
            rows = smap[st]
            jobs_here = sorted({j["job_id"] for _, j, _ in by_study[st]})
            first_rec = recs[jobs_here[0]]
            L += ["---", "", f"## {st} · {first_rec.get('first_author') or ''} {first_rec.get('year') or ''} · "
                             f"{clip(first_rec.get('venue') or '', 80)}", ""]
            for jid in jobs_here:
                j = next(x for x in jobs if x["job_id"] == jid)
                d = drafts[jid]["codes"]
                u = recs[jid]
                L.append(link(jid, "Основной отчёт") + f" — «{clip(u['title'], 160)}»" +
                         (f" — [DOI](https://doi.org/{u['doi']})" if u.get("doi") else ""))
                for e in j["attached"]:
                    L.append(link(e, "Приложен") + f" — «{clip(recs[e]['title'], 120)}»")
                for e in j["listed_only"]:
                    L.append(link(e, "Не приложен (длинный)") + f" — «{clip(recs[e]['title'], 120)}»")
                if j["link_reason"]:
                    L.append(f"Связь отчётов: {j['link_reason']}")
                for po in j["possible_overlap"]:
                    L.append(f"⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): {po}")
                if d["excluded_samples"] and not d["excluded_samples"].lower().startswith("none"):
                    L.append(f"Не выписано ИИ: {clip(d['excluded_samples'], 700)}")
                if d["consistency_notes"]:
                    L.append(f"Расхождения в тексте: {clip(d['consistency_notes'], 900)}")
                if d["note"]:
                    L.append(f"Заметка ИИ: {clip(d['note'], 600)}")
                L.append("")
            for key, j, s in by_study[st]:
                L += render_sample(key, s, [j["main"], *j["attached"]])
                n_samples += 1
                n_est += len(s["estimates"])
        out = outdir / f"verify_R1_{fi:02d}.md"
        out.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(studies)} studies, {n_samples} samples, {n_est} estimates -> {len(chunks)} files in {outdir}")
    if missing:
        print(f"WARNING: no draft yet for {len(missing)} jobs: {', '.join(missing)}")


EST_RE = re.compile(r"^E(\d+)\.(\w+)\s*=\s*(.*)$")
DEL_RE = re.compile(r"^E(\d+)\s+удалить\b(.*)$", re.I)
ADD_RE = re.compile(r"^\+\s*оценка\s*:\s*(.*)$", re.I)
JBI_RE = re.compile(r"^jbi_([1-9])\s*=\s*(yes|no|unclear|NA)\b(.*)$", re.I)
DROP_RE = re.compile(r"^выборка\s+удалить\b[:\s]*(.*)$", re.I)
FIELD_RE = re.compile(r"^(\w+)\s*=\s*(.*)$")


def parse(a):
    recs, jobs, drafts = load(a.run, a.draft)
    keyed = {key: (j, s) for key, j, i, s in sample_keys(jobs, drafts)}
    blocks = {}
    for p in sorted((Path(a.out) if a.out else VERIFY).glob("verify_R1_*.md")):
        text = p.read_text(encoding="utf-8")
        for m in re.finditer(r"^### (ST\d{3}-\d+) .*?(?=^### |^---|\Z)", text, re.S | re.M):
            blocks[m.group(1)] = (p.name, m.group(0))
    samples_out, est_out, corr, problems, unverified = [], [], [], [], []
    for key, (j, s) in keyed.items():
        if key not in blocks:
            problems.append(f"{key}: block not found")
            continue
        fname, body = blocks[key]
        pr = re.search(r"^Правки:\s*\n(.*?)^Проверено:(.*)$", body, re.S | re.M)
        if not pr:
            problems.append(f"{fname} {key}: no 'Правки'/'Проверено' lines")
            continue
        ver = pr.group(2).strip().lower()
        if ver not in VERIFIED:
            unverified.append(key)
        fields = {f: s[f]["value"] for f in SAMPLE_FIELDS}
        ests = {i: dict(e) for i, e in enumerate(s["estimates"], 1)}
        jbi = {i: s["jbi"][f"jbi_{i}"]["rating"] for i in range(1, 10)}
        dropped, added, comments = "", [], []
        for raw in pr.group(1).splitlines():
            line = raw.strip().lstrip("-").strip()
            if not line:
                continue
            line, _, comment = line.partition("#")
            line = line.strip()
            if comment.strip():
                comments.append(comment.strip())
            if not line:
                continue
            if m := DEL_RE.match(line):
                k = int(m.group(1))
                if k in ests:
                    corr.append({"sample_key": key, "target": f"E{k}", "field": "*", "ai_value": "estimate",
                                 "r1_value": "deleted", "key_field": "yes"})
                    ests.pop(k)
                else:
                    problems.append(f"{fname} {key}: no estimate E{k}: {raw}")
            elif m := EST_RE.match(line):
                k, f, v = int(m.group(1)), m.group(2), m.group(3).strip()
                if k not in ests or f not in EST_FIELDS:
                    problems.append(f"{fname} {key}: unknown estimate field: {raw}")
                    continue
                corr.append({"sample_key": key, "target": f"E{k}", "field": f, "ai_value": ests[k][f], "r1_value": v,
                             "key_field": "yes" if f in KEY_EST else "no"})
                ests[k][f] = v
            elif m := ADD_RE.match(line):
                e = {f: "" for f in EST_FIELDS}
                for part in m.group(1).split(";"):
                    if "=" in part:
                        f, v = part.split("=", 1)
                        if f.strip() in EST_FIELDS:
                            e[f.strip()] = v.strip()
                        else:
                            problems.append(f"{fname} {key}: unknown field in added estimate: {f.strip()}")
                added.append(e)
                corr.append({"sample_key": key, "target": "new", "field": "*", "ai_value": "", "r1_value": m.group(1),
                             "key_field": "yes"})
            elif m := JBI_RE.match(line):
                i, v = int(m.group(1)), m.group(2).lower().replace("na", "NA")
                corr.append({"sample_key": key, "target": f"jbi_{i}", "field": "rating", "ai_value": jbi[i],
                             "r1_value": v, "key_field": "no"})
                jbi[i] = v
            elif m := DROP_RE.match(line):
                dropped = m.group(1).strip() or "R1"
            elif (m := FIELD_RE.match(line)) and m.group(1) in SAMPLE_FIELDS:
                f, v = m.group(1), m.group(2).strip()
                corr.append({"sample_key": key, "target": "sample", "field": f, "ai_value": fields[f], "r1_value": v,
                             "key_field": "yes" if f in KEY_SAMPLE else "no"})
                fields[f] = v
            else:
                problems.append(f"{fname} {key}: unreadable correction: {raw.strip()}")
        samples_out.append({"sample_key": key, "study_id": j["study_id"], "job_id": j["job_id"], "label": s["label"],
                            "reports": s["reports"], **fields,
                            **{f"jbi_{i}": jbi[i] for i in range(1, 10)},
                            "verified": "yes" if ver in VERIFIED else "no", "dropped": dropped,
                            "r1_comments": " | ".join(comments)})
        for i, e in list(ests.items()) + [(f"new{n}", e) for n, e in enumerate(added, 1)]:
            est_out.append({"sample_key": key, "est": f"E{i}" if isinstance(i, int) else i, **e})
    dec = Path(a.dec) if a.dec else HERE / "decisions"
    dec.mkdir(parents=True, exist_ok=True)
    for name, rows in (("samples_R1.csv", samples_out), ("estimates_R1.csv", est_out), ("corrections_R1.csv", corr)):
        if rows:
            with (dec / name).open("w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
                w.writeheader()
                w.writerows(rows)
    n_vals = sum(len(SAMPLE_FIELDS) + 9 + len(s["estimates"]) * len(EST_FIELDS) for j, s in keyed.values())
    print(f"samples {len(samples_out)} (unverified {len(unverified)}), estimates {len(est_out)}, corrections {len(corr)} "
          f"of about {n_vals} drafted values")
    if unverified:
        print("unverified:", ", ".join(unverified))
    for p in problems:
        print("PROBLEM:", p)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["make", "parse"])
    ap.add_argument("--run", required=True)
    ap.add_argument("--draft", required=True)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--studies", nargs="*", help="make: only these study IDs, into new files")
    ap.add_argument("--first-file", type=int, default=1, help="make: number of the first file")
    ap.add_argument("--allow-missing", action="store_true")
    ap.add_argument("--out", help="folder of the verification files (default extraction/verify)")
    ap.add_argument("--dec", help="output folder for parse (default extraction/decisions)")
    a = ap.parse_args()
    make(a) if a.cmd == "make" else parse(a)


if __name__ == "__main__":
    main()
