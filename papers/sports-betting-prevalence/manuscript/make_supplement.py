"""Supplementary files built from the logs and the verified tables, so that every number matches the record of the work.

S1_search.md        - search strategies, dates and counts per source (PRISMA-S), de-duplication, seed-set recall
S2_levels.md        - instruments, thresholds and case-definition levels (forms/instrument_thresholds.csv)
S3_deviations.md    - every change and clarification after registration (deviations.md)
S4_ai.md            - AI tools: roles, models, versions, prompts and their hashes, runs, calibration, verification
S5_excluded.md      - reports excluded at full text with the primary reason, and files that were another work
S6_samples.md       - included samples (Table S1) and the reports of each study
S7_estimates.md     - every verified estimate (forms/estimates.csv)
S8_rob.md           - JBI risk-of-bias ratings per sample
S9_analyses.md      - sensitivity analyses, moderators, cluster-robust check, leave-one-out, sex, listed estimates
Template: papers/ai-dependence-correlates/manuscript/make_supplement.py.

Run: .venv/Scripts/python.exe -I papers/sports-betting-prevalence/manuscript/make_supplement.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
OUT = HERE / "supplement"
RUN = PAPER / "search" / "runs" / "2026-10-18"
RES = PAPER / "analysis" / "results"
NOT_BETTORS = {"S009", "S015", "S034"}

SOURCES = {"pubmed": ("PubMed", "NCBI E-utilities; sport and betting terms within two words in title or abstract ([tiab:~2]) and single phrases"),
           "europepmc": ("Europe PMC", "REST API, TITLE_ABS phrases in chunks"),
           "openalex": ("OpenAlex", "API, title_and_abstract.search, phrases joined by OR, in chunks"),
           "openalex_non_en": ("OpenAlex, other languages", "API, title_and_abstract.search, one phrase per query"),
           "s2": ("Semantic Scholar", "Graph API, bulk search, phrases joined by the OR operator"),
           "crossref": ("Crossref", "REST API, query.bibliographic sorted by relevance; records kept only with a sport term near a betting term in title or abstract"),
           "datacite": ("DataCite", "REST API, titles and descriptions"),
           "openaire": ("OpenAIRE Graph", "API, research products of type publication, short OR lists"),
           "citations": ("Citation search of Tran et al. (2024)", "OpenAlex: works in its reference list and works citing it"),
           "core": ("CORE", "planned; not searched (API errors; D2)")}
REASON_TEXT = {"E4_no_pg_instrument": "no problem-gambling instrument", "E2_no_sports_bettor_estimate": "no estimate for sports bettors",
               "E5_design": "design (review, commentary, policy, qualitative)", "no_extractable_counts": "no count or proportion with n",
               "E1_selected_sample": "recruited for gambling problems", "E6_duplicate": "duplicate report of a sample",
               "E7_operator_data_only": "operator account data only", "E3_distribution_cutoff": "cut-off from the sample's distribution",
               "other": "other"}


def fmt(n) -> str:
    return f"{int(float(n)):,}"


def cell(x, n: int | None = None) -> str:
    t = re.sub(r"\s+", " ", str(x or "")).replace("|", "/").strip()
    return t if n is None or len(t) <= n else t[: n - 1] + "…"


def rows(path: Path) -> list[dict]:
    return list(csv.DictReader(path.open(encoding="utf-8-sig")))


def records() -> dict[str, dict]:
    return {json.loads(l)["rec_id"]: json.loads(l) for l in (RUN / "records_unique.jsonl").open(encoding="utf-8")}


def s1() -> str:
    log = json.loads((RUN / "search_log.json").read_text(encoding="utf-8"))
    dd = json.loads((RUN / "dedup_report.json").read_text(encoding="utf-8"))
    rc = json.loads((RUN / "recall_seed_set.json").read_text(encoding="utf-8"))
    started = (RUN / "started_utc.txt").read_text(encoding="utf-8").split()[0].replace("T", " ").rstrip("Z")
    L = ["**Supplementary File S1.** Search strategies, dates and results per source (PRISMA-S)", "",
         f"Final search started {started} (UTC) with the frozen code of protocol v1.0 (git tag `sports-betting-prereg-v1.0`). "
         "The search used the population concept only (sports betting), without terms for problem gambling or prevalence, "
         "and no date or language limits.", "",
         "**Phrase set.** " + "; ".join(log["_phrase_sets"]["phrases"]) + ".", "",
         "| Source | Interface and query form | Searched (UTC) | Records |", "| --- | --- | --- | --- |"]
    for k, (name, how) in SOURCES.items():
        v = log.get(k, {})
        n = fmt(v["records"]) if "records" in v else "not searched"
        when = v.get("searched_at_utc", (v.get("meta") or {}).get("searched_at_utc", ""))
        L.append(f"| {name} | {how} | {cell(when)} | {n} |")
    L += ["", "**Query strings as sent** (from `search/runs/2026-10-18/search_log.json`):", ""]
    for k in ("pubmed", "europepmc", "openalex", "s2", "datacite"):
        meta = log[k].get("meta", {})
        qs = meta.get("queries") or meta.get("filters") or []
        for q in qs[:3]:
            s = q.get("query") or q.get("filter")
            L.append(f"- {SOURCES[k][0]}: `{cell(s)}`" + (f" ({fmt(q['count'])} records)" if "count" in q else ""))
        if len(qs) > 3:
            L.append(f"- {SOURCES[k][0]}: {len(qs) - 3} further queries of the same form (full list in the log)")
    ne = log["openalex_non_en"]["meta"].get("filters", [])
    L.append("- OpenAlex, other languages: " + "; ".join(f"{cell(f['filter'].split(':', 1)[1])} ({f.get('count', '')})" for f in ne))
    cq = log["crossref"]["meta"].get("queries", {})
    L.append("- Crossref: " + "; ".join(f"\"{q}\" (scanned {fmt(v['scanned'])}, kept {fmt(v['kept_new'])})" for q, v in cq.items()))
    oq = log["openaire"]["meta"].get("queries", {})
    L.append("- OpenAIRE: " + "; ".join(f"`{cell(q)}` ({v.get('numFound', '')})" for q, v in oq.items()))
    t = log["citations"]["meta"]["tran_2024"]
    L.append(f"- Citation search: Tran et al. (2024), DOI {t['doi']}, OpenAlex {t['openalex']}: {t['referenced_works']} "
             f"references and {t['citing_records']} citing records.")
    L += ["", "**De-duplication and automatic removal** (`search/dedup.py`):", "",
          f"- Records identified: {fmt(dd['records_total'])}; unique after de-duplication on DOI, PMID and normalized title: "
          f"{fmt(dd['unique_records'])} ({fmt(dd['duplicates_removed'])} duplicates and attached pointer records).",
          f"- Removed automatically: {fmt(dd['auto_removed_non_study_records'])} records typed as non-study by every source "
          f"and {fmt(dd['auto_removed_commercial_deposits'])} Zenodo commercial deposits (bookmaker advertising; rule 6).",
          f"- Records screened: {fmt(dd['records_to_screen'])}; {fmt(dd['unique_only_via_citations_of_tran_2024'])} of them "
          f"only through the citation search of Tran et al. (2024).", "",
          f"**Recall check.** {rc['seed_studies']} empirical studies of sports bettors with a problem-gambling instrument from "
          f"the references of two earlier reviews (Etuk et al., 2022; Valenciano-Mendoza et al., 2023): "
          f"{rc['in_screening_list']} of {rc['seed_studies']} were in the screening list.", ""]
    return "\n".join(L)


def s2() -> str:
    L = ["**Supplementary File S2.** Instruments, thresholds and case-definition levels (fixed in protocol §13 and completed "
         "before extraction, clarification C1)", "",
         "| Instrument | Full name | Range | L1 | L2 | L3 | Brief screen or L4 | Source of the thresholds |",
         "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows(PAPER / "forms" / "instrument_thresholds.csv"):
        L.append(f"| {r['instrument']} | {cell(r['full_name'])} | {r['score_range'] or 'NA'} | {r['L1_rule'] or '—'} | "
                 f"{r['L2_rule'] or '—'} | {r['L3_rule'] or '—'} | {r['screen_or_L4'] or '—'} | "
                 f"{cell(r['threshold_source'])}{'; ' + cell(r['notes']) if r['notes'] else ''} |")
    L += ["", "Levels are cumulative: a sample reporting PGSI categories contributes L1 (≥ 1), L2 (≥ 3) and L3 (≥ 8). "
          "Categories were extracted as printed and cumulative levels were built at analysis from contiguous categories "
          "(`analysis/build_levels.py`).", ""]
    return "\n".join(L)


def s3() -> str:
    t = (PAPER / "deviations.md").read_text(encoding="utf-8")
    t = re.sub(r"(?m)^# .*\n", "", t)
    t = re.sub(r"(?m)^## (.+)$", r"**\1**", t)
    return ("**Supplementary File S3.** Changes after registration (D1–D9) and clarifications (C1–C2), as recorded in "
            "`deviations.md`\n\n" + t.strip() + "\n")


def s4() -> str:
    cal = json.loads((PAPER / "screening" / "decisions" / "calibration_stats.json").read_text(encoding="utf-8"))
    cs = json.loads((PAPER / "extraction" / "decisions" / "correction_stats.json").read_text(encoding="utf-8"))
    qc = json.loads((PAPER / "extraction" / "decisions" / "quote_check.json").read_text(encoding="utf-8"))

    def meta(path: Path):
        n, ids, ver, sha, t0, t1 = 0, set(), set(), set(), "9", "0"
        for line in path.open(encoding="utf-8"):
            d = json.loads(line)
            n += 1
            ids.add(d["conv_id"])
            ver.add(d["judge"]["cli_version"])
            sha.add(d["judge"]["system_prompt_sha"])
            t0, t1 = min(t0, d["judged_at"]), max(t1, d["judged_at"])
        return n, len(ids), ", ".join(sorted(ver)), ", ".join(sorted(sha)), t0, t1

    L = ["**Supplementary File S4.** Use of AI tools", "",
         "All model calls went through headless Claude Code (`claude -p`, no tools, empty working directory, default "
         "sampling parameters) with a fixed system prompt and a JSON schema; the system prompt hash, the schema hash, the "
         "Claude Code version and the model are stored with every output (`harness/llmaudit/judge.py`).", "",
         "| Task | Model, effort | Prompt | Outputs (unique records) | Claude Code | System prompt SHA | Run (UTC) |",
         "| --- | --- | --- | --- | --- | --- | --- |"]
    for task, model, prompt, path in [
            ("Title and abstract, pass 1", "Claude Opus 5.5, high", "`screening/llm_screener_prompt.md`", PAPER / "screening" / "llm" / "2026-10-18_opus.jsonl"),
            ("Title and abstract, pass 2", "Claude Sonnet 5.5, high", "`screening/llm_screener_prompt.md`", PAPER / "screening" / "llm" / "2026-10-18_sonnet.jsonl"),
            ("Extraction and JBI drafts", "Claude Opus 5.5, high", "`extraction/extract_prompt.md` v1.0", PAPER / "extraction" / "draft" / "extract_2026-10-19.jsonl")]:
        n, u, ver, sha, t0, t1 = meta(path)
        L.append(f"| {task} | {model} | {prompt} | {fmt(n)} ({fmt(u)}) | {ver} | {sha} | {t0[:16]} – {t1[:16]} |")
    rule = cal["ai_rule_full_text_unless_both_exclude"]
    L += ["", "Title-and-abstract passes produced duplicate labels for some records because orphaned runners kept running "
          "after a session restart; the earliest label per record was used (D4). The label files were sealed with SHA-256 "
          f"hashes before the calibration was unblinded (Opus {cal['ai_labels_sha256']['opus'][:16]}…, Sonnet "
          f"{cal['ai_labels_sha256']['sonnet'][:16]}…).", "",
          f"**Blind calibration** ({cal['n_calibration']} random records, decided by the author before the AI labels were "
          f"shown): rule \"exclude only if both passes exclude\" — sensitivity {rule['sensitivity']:.2f} "
          f"({rule['counts']['tp']}/{rule['counts']['tp'] + rule['counts']['fn']}), specificity {rule['specificity']:.2f} "
          f"({rule['counts']['tn']}/{rule['counts']['tn'] + rule['counts']['fp']}), κ {rule['kappa']:.2f}, AC1 {rule['ac1']:.2f}; "
          f"agreement between passes κ {cal['passes_agreement_full_text_vs_exclude']['kappa']:.2f}. "
          f"Opus alone: sensitivity {cal['passes']['opus']['full_text_vs_exclude']['sensitivity']:.2f}, specificity "
          f"{cal['passes']['opus']['full_text_vs_exclude']['specificity']:.2f}; Sonnet alone: "
          f"{cal['passes']['sonnet']['full_text_vs_exclude']['sensitivity']:.2f} and "
          f"{cal['passes']['sonnet']['full_text_vs_exclude']['specificity']:.2f}. Safeguard triggered (D5, D6).", "",
          "**Full texts:** screened by the author without AI proposals (D7); the fixed full-text prompt "
          "(`fulltext/ft_prompt.md`, tag `sports-betting-ft-prompt-v1.0`) was used only in a five-report pilot.", "",
          f"**Extraction:** {cs['verified_samples']} samples verified by the author; {cs['values_corrected']} of "
          f"{fmt(cs['drafted_values'])} drafted values corrected ({100 * cs['share_corrected']:.2f}%); key values "
          f"{cs['key_values_corrected']} of {fmt(cs['key_values'])} ({100 * cs['share_key_corrected']:.2f}%). AI quotations "
          f"found verbatim in the source: {100 * qc['estimates']['share_found']:.0f}% of estimates and "
          f"{100 * qc['key_fields']['share_found']:.0f}% of key fields (`extraction/quote_check.py`).", "",
          "**Code and text:** Claude Code wrote the search, screening, extraction, analysis and table code and an outline of "
          "the manuscript (facts and numbers per section). The author wrote the text.", ""]
    return "\n".join(L)


def s5() -> str:
    recs = records()
    ft = rows(PAPER / "fulltext" / "decisions" / "ft_R1.csv")
    inc = rows(PAPER / "fulltext" / "incomplete_texts.csv")
    exc = [r for r in ft if r["decision"] == "not_eligible" and r["rec_id"] not in {x["rec_id"] for x in inc}]
    c = Counter(r["reason"] for r in exc)
    L = [f"**Supplementary File S5.** Reports excluded at full text (n = {len(exc)}), with the primary reason", "",
         "Reasons: " + "; ".join(f"{REASON_TEXT.get(k, k)} {v}" for k, v in c.most_common()) + ". Files that turned out to "
         f"contain another work ({len(inc)}) are counted as not retrieved.", "",
         "| Record | First author, year | Title | Reason | DOI |", "| --- | --- | --- | --- | --- |"]
    for r in sorted(exc, key=lambda x: (REASON_TEXT.get(x["reason"], x["reason"]), x["rec_id"])):
        u = recs[r["rec_id"]]
        L.append(f"| {r['rec_id']} | {cell(u.get('first_author'), 30)} {u.get('year') or ''} | {cell(u.get('title'), 110)} | "
                 f"{REASON_TEXT.get(r['reason'], r['reason'])} | {u.get('doi') or ''} |")
    L += ["", "| Record | Retrieved file | Note |", "| --- | --- | --- |"]
    for r in inc:
        L.append(f"| {r['rec_id']} | {cell(r['what_was_retrieved'])} | {cell(r['note'])} |")
    return "\n".join(L) + "\n"


def s6() -> str:
    t = (HERE / "tables.md").read_text(encoding="utf-8")
    table = t.split("**Table S1.**", 1)[1]
    L = ["**Supplementary File S6.** Included samples", "", "**Table S1.**" + table.strip(), "",
         "**Reports of each study** (`extraction/study_map.csv`; possible overlaps were kept as separate studies):", "",
         "| Study | Report | Role | First author, year | DOI | Link between reports |", "| --- | --- | --- | --- | --- | --- |"]
    for r in rows(PAPER / "extraction" / "study_map.csv"):
        note = r["link_reason"] or r["possible_overlap"]
        L.append(f"| {r['study_id']} | {r['rec_id']} | {cell(r['role'])} | {cell(r['first_author'], 30)} {r['year']} | "
                 f"{r['doi']} | {cell(note, 200)} |")
    return "\n".join(L) + "\n"


def s7() -> str:
    L = ["**Supplementary File S7.** Verified estimates (categories as printed; cumulative levels are built at analysis)", "",
         "| Estimate | Sample | Subgroup | Instrument | Category | Cumulative | Level | Cases | n | Derived | Location |",
         "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows(PAPER / "forms" / "estimates.csv"):
        L.append(f"| {r['estimate_id']} | {r['sample_id']} | {cell(r['subgroup'], 40)} | {r['instrument']} | "
                 f"{cell(r['threshold'], 50)} | {r['cumulative']} | {r['level']} | {r['cases']} | {r['n']} | {r['derived']} | "
                 f"{cell(r['location'], 50)} |")
    return "\n".join(L) + "\n"


def s8() -> str:
    q = {1: "sample frame", 2: "sampling", 3: "sample size", 4: "description", 5: "coverage", 6: "valid measure",
         7: "standard measurement", 8: "statistics", 9: "response"}
    L = ["**Supplementary File S8.** Risk of bias: JBI checklist for prevalence studies (decision rules in protocol §14 "
         "and `forms/rob_jbi.md`; AI draft verified by the author)", "",
         "Items: " + "; ".join(f"{k} {v}" for k, v in q.items()) + ".", "",
         "| Sample | Study | " + " | ".join(str(k) for k in q) + " | Ratings no or unclear |",
         "| --- | --- | " + " | ".join("---" for _ in q) + " | --- |"]
    for s in rows(PAPER / "forms" / "samples.csv"):
        L.append(f"| {s['sample_id']} | {cell(s['first_author'], 25)} {s['year']} | "
                 + " | ".join(s[f"jbi_{k}"] for k in q) + f" | {cell(s['jbi_notes'], 300)} |")
    c = {k: Counter(s[f"jbi_{k}"] for s in rows(PAPER / "forms" / "samples.csv") if s["sample_id"] not in NOT_BETTORS) for k in q}
    L += ["", "Counts over the 55 samples of sports bettors: " +
          "; ".join(f"item {k}: " + ", ".join(f"{v} {n}" for v, n in sorted(c[k].items())) for k in q) + ".", ""]
    return "\n".join(L)


def s9() -> str:
    def pct(x):
        try:
            return f"{100 * float(x):.1f}"
        except ValueError:
            return "NA"

    L = ["**Supplementary File S9.** Additional analyses", "", "**S9.1 Sensitivity analyses of the primary outcome** "
         "(problem gambling, L3/L4; GLMM unless stated)", "",
         "| Analysis | k | Prevalence, % (95% CI) | 95% PI, % | Note |", "| --- | --- | --- | --- | --- |"]
    for r in rows(RES / "sensitivity.csv"):
        est = f"{pct(r['prev'])} ({pct(r['ci.lb'])}–{pct(r['ci.ub'])})" if r["prev"] not in ("NA", "") else "not pooled"
        pi = f"{pct(r['pi.lb'])}–{pct(r['pi.ub'])}" if r["pi.lb"] not in ("NA", "") else ""
        L.append(f"| {cell(r['analysis'])} | {r['k']} | {est} | {pi} | {cell(r['note'])} |")
    loo = rows(RES / "leave_one_out.csv")
    v = [float(r["prev"]) for r in loo]
    infl = [r["sample_id"] for r in rows(RES / "influence.csv") if r["influential"] == "TRUE"]
    L += ["", f"S10 leave-one-out: pooled prevalence {100 * min(v):.1f}%–{100 * max(v):.1f}% (k = {len(loo) - 1} each); "
          f"influential samples (inverse-variance model): {', '.join(infl) or 'none'}.", "",
          "**S9.2 Exploratory moderators** (three-level binomial GLMM, one moderator at a time, adjusted for level; "
          "likelihood-ratio test)", "", "| Moderator | Samples | χ² | df | p | Note |", "| --- | --- | --- | --- | --- | --- |"]
    for r in rows(RES / "moderators_exploratory.csv"):
        L.append(f"| {r['moderator']} | {r['k_samples']} | {r['chisq'][:6] if r['chisq'] != 'NA' else 'NA'} | {r['df']} | "
                 f"{r['p'][:6] if r['p'] != 'NA' else 'NA'} | {cell(r['note'])} |")
    L += ["", "| Moderator | Term | Reference | OR (95% CI) | p | Samples with the term |", "| --- | --- | --- | --- | --- | --- |"]
    for r in rows(RES / "moderators_exploratory_coefs.csv"):
        L.append(f"| {r['moderator']} | {cell(r['term'])} | {cell(r['reference'])} | {float(r['OR']):.2f} "
                 f"({float(r['ci.lb']):.2f}–{float(r['ci.ub']):.2f}) | {float(r['p']):.3f} | {r['n_samples_term']} |")
    L += ["", "**S9.3 Pre-specified three-level model, cluster-robust check** (inverse-variance three-level model on logits, "
          "CR2 small-sample correction, clusters = studies)", "",
          "| Term | Estimate (logit) | SE | t | df | p |", "| --- | --- | --- | --- | --- | --- |"]
    for r in rows(RES / "multilevel_robust.csv"):
        keys = list(r.keys())
        g = lambda *names: next((r[k] for k in names if k in r), "")
        L.append(f"| {cell(g('Coef', 'term', keys[0]))} | {g('beta', 'Est')[:7]} | {g('SE')[:6]} | {g('tstat')[:6]} | "
                 f"{g('df_Satt', 'df')[:6]} | {g('p_Satt', 'p_val', 'p')[:6]} |")
    L += ["", "**S9.4 Sex difference** (male vs female odds ratio at the sample's primary level and instrument)", "",
          "| Sample | Instrument | Level | Threshold | Men: cases / n | Women: cases / n |", "| --- | --- | --- | --- | --- | --- |"]
    for r in rows(RES / "sex_data.csv"):
        L.append(f"| {r['sample_id']} | {r['instrument']} | {r['level']} | {cell(r['threshold'])} | "
                 f"{fmt(r['m_cases'])} / {fmt(r['m_n'])} | {fmt(r['f_cases'])} / {fmt(r['f_n'])} |")
    sx = rows(RES / "sex_or.csv")[0]
    L += ["", f"Pooled OR {float(sx['OR']):.2f} (95% CI {float(sx['ci.lb']):.2f}–{float(sx['ci.ub']):.2f}; 95% PI "
          f"{float(sx['pi.lb']):.2f}–{float(sx['pi.ub']):.2f}; k = {sx['k']}; REML with Hartung–Knapp).", "",
          "**S9.5 Small-study effects and publication type**", "", "| Test | Estimate | p |", "| --- | --- | --- |"]
    for r in rows(RES / "meta_bias.csv"):
        L.append(f"| {cell(r['test'])} | {float(r['estimate']):.3f} | {float(r['p']):.3f} |")
    L += ["", "**S9.6 Estimates listed but not pooled**", "",
          "| Estimate | Sample | Subgroup | Instrument | Category | Level | Cases | n | Reason |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows(RES / "listed_not_pooled.csv"):
        L.append(f"| {r['estimate_id']} | {r['sample_id']} | {cell(r['subgroup'], 40)} | {r['instrument']} | "
                 f"{cell(r['threshold'], 45)} | {r['level']} | {r['cases']} | {r['n']} | {cell(r['reason'])} |")
    L += ["", "**S9.7 Selection of one estimate per sample** (protocol §13): " +
          "; ".join(f"{k} {v}" for k, v in Counter(r["rule"] for r in rows(RES / "selection_log.csv")).most_common()) +
          " (`analysis/results/selection_log.csv`).", ""]
    return "\n".join(L)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.mkdir(exist_ok=True)
    for name, fn in [("S1_search.md", s1), ("S2_levels.md", s2), ("S3_deviations.md", s3), ("S4_ai.md", s4),
                     ("S5_excluded.md", s5), ("S6_samples.md", s6), ("S7_estimates.md", s7), ("S8_rob.md", s8),
                     ("S9_analyses.md", s9)]:
        (OUT / name).write_text(fn(), encoding="utf-8", newline="\n")
        print(name, len((OUT / name).read_text(encoding="utf-8")), "chars")


if __name__ == "__main__":
    main()
