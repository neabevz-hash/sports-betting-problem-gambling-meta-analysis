"""Link the eligible reports into studies and extraction jobs (protocol §11b, codebook "Waves of one panel", "Overlap").

Reports are linked when they describe the same sample: a preprint and its article, a thesis and its article, a dataset
record and its article, or secondary analyses of one dataset. The links below were set from R1's full-text notes and the
texts (same panel, survey, N, years, or an explicit statement), 2026-10-19.
A study is a connected group of linked reports. Each sample is extracted once, from its main report (the most complete
one); other reports of the sample are attached to the job for context while the input stays within MAX_CHARS.

Pairs that only might overlap (same university or lab, no evidence of shared participants) stay separate and are listed
in POSSIBLE, so R1 sees them in the verification file.

Writes extraction/study_map.csv (one row per report) and extraction/jobs.json (one job per main report).
Run: .venv/Scripts/python.exe -I papers/sports-betting-prevalence/extraction/make_study_map.py --run 2026-10-18
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
sys.path.insert(0, str(HERE))
from common import eligible_reports, load_records  # noqa: E402
MAX_CHARS = 400_000

# main report -> (additional reports of the same samples, reason). Every report of a group is listed once.
GROUPS = [
    ("R4056", ["R3634", "R3635"], "Betting and Gaming COVID-19 Impact Study, YouGov cohort of regular sports bettors in Britain: "
     "wave 1 (6-19 July 2020, n = 3,866) is reported in R4056; R3634 uses two waves (T0, T2) and R3635 uses wave 2 "
     "(November 2020) of the same cohort. Waves of one panel: the first wave enters (codebook)"),
    ("R2661", ["R5777"], "Victorian gambling prevalence studies 2008, 2014 and 2018 (R2661); R5777 analyses the 2008 study "
     "(A Study of Gambling in Victoria, August-October 2008, N = 15,000)"),
]

# Samples to extract from a main report when it is not simply "every eligible sample in this report".
SAMPLES = {
    "R2661": "Three independent cross-sectional surveys (2008, 2014, 2018): extract the sports bettors of each survey as a "
             "separate sample. R5777 (attached) reports the 2008 survey by sex: use it for the 2008 sample's subgroups and to "
             "fill values R2661 does not give.",
    "R4056": "One sample: the regular sports bettors of wave 1 (July 2020). Extract wave-1 estimates from R4056; use R3634 "
             "and R3635 only to fill values R4056 does not give, and note their later-wave estimates in the sample notes.",
    "R4528": "One sample: everyone in the emerging adults survey who bet on sports or esports. Esports bettors and other "
             "sports or event bettors are subgroups; if the paper says the groups do not overlap, also give the whole-sample "
             "estimate as their sum (derived = yes).",
}

# Facts the extractor cannot see in the text.
JOB_NOTES = {
    "R4528": "R3635 (attached to the job of R4056) also analyses wave one of this emerging adults survey (n = 3,549).",
}

# Possible overlaps kept as separate studies (no evidence of shared participants); shown to R1.
POSSIBLE = [
    (["R4314", "R4315"], "Both Ipsos web panel samples of Swedish online gamblers (Hakansson); R4314 (May 2020, N = 997) "
     "says it repeats the recruitment of an earlier study, probably R4315 (N = 1,004): different years, panel members may overlap"),
    (["R2429", "R2934"], "Both young Australian sports bettors recruited by Qualtrics panels for Hing et al. (April 2021, "
     "N = 616; June-September 2021, NSW, N = 267): separate surveys, panel members may overlap"),
    (["R5231", "R4617"], "Both EMA studies of regular Australian sports and race bettors by the same group (98 and 279 sports "
     "bettors): separate studies, recruitment may overlap"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    recs = load_records(a.run)
    eligible = set(eligible_reports())

    # union-find over all reports named together in GROUPS
    parent = {k: k for k in eligible}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for main_rec, extra, _ in GROUPS:
        for k in [main_rec, *extra]:
            if k not in eligible:
                raise SystemExit(f"{k} is not an eligible report")
        for k in extra:
            parent[find(k)] = find(main_rec)
    mains = {m for m, _, _ in GROUPS}
    linked = {k for m, extra, _ in GROUPS for k in [m, *extra]}
    singles = sorted(eligible - linked)
    comps: dict[str, list[str]] = {}
    for k in sorted(eligible):
        comps.setdefault(find(k), []).append(k)
    # study order: by the smallest main report id of the group (singletons are their own main)
    def first_main(members):
        return min(k for k in members if k in mains or k in singles)
    order = sorted(comps.values(), key=first_main)
    study_of = {}
    for i, members in enumerate(order, 1):
        for k in members:
            study_of[k] = f"ST{i:03d}"

    possible_of: dict[str, list[str]] = {}
    for members, why in POSSIBLE:
        for k in members:
            others = ", ".join(f"{m} ({study_of[m]})" for m in members if m != k)
            possible_of.setdefault(k, []).append(f"possible overlap with {others}: {why}")

    def chars(k):
        raw = (PAPER / "fulltext" / "text" / f"{k}.txt").read_text(encoding="utf-8")
        return len(raw.split("\n\n", 1)[1] if raw.startswith("REC_ID:") else raw)

    jobs, rows = [], []
    group_of = {m: (extra, why) for m, extra, why in GROUPS}
    for k in [*sorted(mains), *singles]:
        extra, why = group_of.get(k, ([], ""))
        budget = MAX_CHARS - chars(k)
        attached, listed = [], []
        for e in extra:
            if chars(e) <= budget:
                attached.append(e)
                budget -= chars(e)
            else:
                listed.append(e)
        jobs.append({"job_id": k, "study_id": study_of[k], "main": k, "attached": attached, "listed_only": listed,
                     "link_reason": why, "samples": SAMPLES.get(k, "Extract every eligible sample in the main report."),
                     "job_notes": JOB_NOTES.get(k, ""),
                     "possible_overlap": possible_of.get(k, [])})
    roles = {}
    for j in jobs:
        roles.setdefault(j["main"], []).append(f"main of job {j['job_id']}")
        for e in j["attached"] + j["listed_only"]:
            roles.setdefault(e, []).append(f"additional in job {j['job_id']}")
    for k in sorted(eligible, key=lambda x: (study_of[x], x)):
        u = recs[k]
        rows.append({"study_id": study_of[k], "rec_id": k, "role": "; ".join(roles.get(k, [])),
                     "first_author": u.get("first_author") or "", "year": u.get("year") or "",
                     "doi": u.get("doi") or "", "title": u.get("title") or "",
                     "link_reason": next((why for m, extra, why in GROUPS if k == m or k in extra), ""),
                     "possible_overlap": " | ".join(possible_of.get(k, []))})
    with (HERE / "study_map.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    (HERE / "jobs.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    n_studies = len(order)
    print(f"{len(eligible)} reports -> {n_studies} studies, {len(jobs)} extraction jobs "
          f"({sum(1 for j in jobs if j['attached'])} with attached reports, "
          f"{sum(1 for j in jobs if j['listed_only'])} with reports listed only)")


if __name__ == "__main__":
    main()
