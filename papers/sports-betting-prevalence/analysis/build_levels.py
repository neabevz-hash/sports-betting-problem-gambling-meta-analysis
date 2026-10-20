"""Cumulative case-definition levels from the verified estimates (codebook, "PGSI categories"; protocol §13).

The extraction keeps every category of an instrument as printed (for the PGSI usually 0, 1-2, 3-7, 8+). The analysis
needs cumulative levels: L1 = any risk (PGSI >= 1), L2 = moderate risk or higher (PGSI >= 3), L3 = problem gambling
(PGSI >= 8). This script writes one row per cumulative estimate:
- direct: a category the study itself reports as open upward (cumulative = yes), e.g. "PGSI>=8", "PGSI>=3";
- built: the sum of contiguous closed bands from the level's threshold up to an open top category of the same
  instrument, subgroup and denominator, e.g. PGSI>=3 = "3-7" + "8+" (only when no direct estimate with the same
  lower bound exists).
Thresholds per instrument and level come from the levels table (forms/instrument_thresholds.csv), as coded in
extraction/verify_md.py (BANDS). A cumulative estimate whose lower bound is not the instrument's standard threshold for
its level (e.g., PGSI >= 5, the revised moderate-risk threshold) is kept and flagged standard = no.
Whole-sample estimates: subgroup "all", or the denominator equals n_bettors, or an "all ..." subgroup when n_bettors is
not reported.

Writes analysis/data/level_estimates.csv. Run: .venv/Scripts/python.exe -I papers/sports-betting-prevalence/analysis/build_levels.py
"""
from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
sys.path.insert(0, str(PAPER / "extraction"))
from verify_md import BANDS, lower_bound  # noqa: E402

LEVELS = ("L1", "L2", "L3")
STANDARD = {ins: {lv: cut for cut, lv in bands if lv in LEVELS} for ins, bands in BANDS.items()}
RANGE = re.compile(r"(\d+)\s*[-–]\s*(\d+)")
STRIP = re.compile(r"DSM-?(IV|5)(-MR-J)?|NODS(-SA)?|SOGS(-RA)?|GPSS|CPGI|PGSI|CAGI|ICJE", re.I)


def num(v: str) -> float | None:
    try:
        return float((v or "").replace(",", ""))
    except ValueError:
        return None


def upper_bound(threshold: str) -> float | None:
    m = RANGE.search(STRIP.sub(" ", threshold or ""))
    return float(m.group(2)) if m else None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    samples = {s["sample_id"]: s for s in csv.DictReader((PAPER / "forms" / "samples.csv").open(encoding="utf-8"))}
    ests = list(csv.DictReader((PAPER / "forms" / "estimates.csv").open(encoding="utf-8")))
    out = []

    def whole(e) -> bool:
        sub = e["subgroup"].strip().lower()
        nb = num(samples[e["sample_id"]]["n_bettors"])
        return sub == "all" or (nb is not None and num(e["n"]) == nb) or (nb is None and sub.startswith("all"))

    def row(e_list, level, lb, cases, n, how):
        e = e_list[0]
        std = STANDARD.get(e["instrument"], {}).get(level)
        return {"sample_id": e["sample_id"], "subgroup": e["subgroup"], "whole": "yes" if whole(e) else "no",
                "instrument": e["instrument"], "level": level,
                "threshold": f"{e['instrument']}>={lb:g}" if lb is not None else e["threshold"],
                "standard": "yes" if std is None or lb == std else "no",
                "cases": f"{cases:g}", "n": f"{n:g}", "time_frame": e["time_frame"],
                "primary_for_authors": "yes" if any(x["primary_for_authors"] == "yes" for x in e_list) else "no",
                "source": how, "estimate_ids": "+".join(x["estimate_id"] for x in e_list)}

    groups = defaultdict(list)
    for e in ests:
        if num(e["cases"]) is None or num(e["n"]) is None:
            continue
        groups[(e["sample_id"], e["subgroup"], e["instrument"], e["n"])].append(e)

    for key, es in groups.items():
        ins = key[2]
        direct_lbs = set()
        for e in es:   # direct cumulative estimates at a poolable level
            if e["cumulative"] == "yes" and e["level"] in (*LEVELS, "L3-screen", "L4"):
                lb = lower_bound(e["threshold"]) if ins in BANDS else None
                if lb is not None:
                    direct_lbs.add(lb)
                out.append(row([e], e["level"], lb, num(e["cases"]), num(e["n"]), "direct"))
        if ins not in BANDS:
            continue
        closed = {}
        opened = {}
        for e in es:
            if e["level"] == "below":
                continue
            lb = lower_bound(e["threshold"])
            if lb is None:
                continue
            if e["cumulative"] == "no":
                ub = upper_bound(e["threshold"])
                if ub is not None:
                    closed[lb] = (ub, e)
            else:
                opened[lb] = e
        for lv in LEVELS:
            t = STANDARD[ins].get(lv)
            if t is None or t in direct_lbs or t not in closed:
                continue
            chain, cur = [], t
            while cur in closed:
                ub, e = closed[cur]
                chain.append(e)
                cur = ub + 1
            if cur not in opened:
                continue   # the bands do not reach an open top category: not built
            chain.append(opened[cur])
            cases = sum(num(e["cases"]) for e in chain)
            n = num(chain[0]["n"])
            if cases > n:
                print(f"WARNING {key}: built {lv} {cases:g} > n {n:g}")
                continue
            out.append(row(chain, lv, t, cases, n, "built"))

    out.sort(key=lambda r: (r["sample_id"], r["whole"] != "yes", r["subgroup"], r["instrument"], r["level"], r["threshold"]))
    path = HERE / "data" / "level_estimates.csv"
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    wh = [r for r in out if r["whole"] == "yes"]
    print(f"{len(out)} cumulative estimates ({sum(r['source'] == 'built' for r in out)} built from bands); "
          f"whole-sample: {len(wh)} in {len({r['sample_id'] for r in wh})} samples -> {path}")
    for lv in ("L1", "L2", "L3", "L3-screen", "L4"):
        print(f"  {lv}: whole-sample estimates in {len({r['sample_id'] for r in wh if r['level'] == lv})} samples")


if __name__ == "__main__":
    main()
