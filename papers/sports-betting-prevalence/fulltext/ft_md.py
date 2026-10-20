"""Full-text decision files in Markdown (protocol, section 11b). Template: papers/misophonia-prevalence/fulltext/ft_md.py.

Each retrieved report is one block: title, year, venue, links to the full text (local PDF or text, and the source
URL), and the AI proposal: decision, primary reason, sample, sports-betting definition, problem-gambling instruments,
and every estimate for sports bettors (case definition, cases, %, n), with its location and a verbatim quote.
Template: papers/ai-dependence-correlates/fulltext/ft_md.py. R1 writes a code in the decision line:
  =        agree with the AI proposal
  +        eligible
  -1 … -9  not eligible, the digit is the primary reason (REASONS below)
  ?        not decided yet (must be resolved before the files are closed)
Anything after the code is a note.

Without AI proposals (R1's decision 2026-10-19, deviations.md D7): `make --no-ai` writes blocks with the title, R1's
title-and-abstract label, clickable links to the local PDF or text and to the online version, and two lines for R1:
"Где цифры:" (table or page with the counts of sports bettors meeting a case definition; for "+") and "Решение:".
"=" is not used then.

  make  --run 2026-10-18 --name ft_2026-10-19   write fulltext/decisions/ft_R1_<nn>.md from fulltext/llm/<name>.jsonl
  make  --run 2026-10-18 --no-ai                the same for every retrieved report, without AI proposals
  parse FILE... --out CSV         decisions -> CSV, and a check that every report has a valid code
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
FILE_SIZE = 50
REASONS = {
    "1": ("E5_design", "обзор, комментарий, право или политика, протокол, качественное без опроса, модели рынков"),
    "2": ("E1_selected_sample", "выборка набрана по проблемам с игрой (лечение, горячая линия, самоисключение, случай–контроль)"),
    "3": ("E7_operator_data_only", "только данные оператора без инструмента проблемной игры"),
    "4": ("E4_no_pg_instrument", "опрос есть, но нет инструмента проблемной игры (только частота, траты, мотивы, вред)"),
    "5": ("E2_no_sports_bettor_estimate", "нет отдельной цифры для тех, кто ставит на спорт (только все игроки), или только скачки"),
    "6": ("E3_distribution_cutoff", "порог по распределению самой выборки (верхние 10%, M + SD)"),
    "7": ("no_extractable_counts", "нет числа или доли с порогом и знаменателем (только средние, коэффициенты)"),
    "8": ("E6_duplicate", "та же выборка, что в другом отчёте (связать)"),
    "9": ("other", "другое — напишите почему"),
}
AI_TO_CODE = {"E5_design": "-1", "E1_selected_sample": "-2", "E7_operator_data_only": "-3", "E4_no_pg_instrument": "-4",
              "E2_no_sports_bettor_estimate": "-5", "E3_distribution_cutoff": "-6", "no_extractable_counts": "-7", "other": "-9"}
HEADER_RE = re.compile(r"^###\s+(\d+)\s*·\s*(R\d{4,5})\b")
DECISION_RE = re.compile(r"^\**\s*Решение\s*:?\s*\**\s*:?\s*(.*)$", re.I)
AI_RE = re.compile(r"^\**\s*ИИ предлагает\s*:?\s*\**\s*:?\s*(\S+)")
WHERE_RE = re.compile(r"^\**\s*Где цифры\s*:?\s*\**\s*:?\s*(.*)$", re.I)

GUIDE = """**Как размечать.** Откройте полный текст (ссылка в блоке), сверьте предложение ИИ и допишите код в строку **Решение:**.

| Код | Что значит |
| --- | --- |
| `=` | согласен с ИИ |
| `+` | подходит: выборка (или подвыборка) тех, кто ставит на спорт, не набранная по проблемам с игрой; инструмент проблемной игры; число или доля с порогом и знаменателем |
{reasons}
| `?` | пока не решил (до закрытия файла нужно решить) |

Оценки ИИ брал из текста, но выписываться они будут на следующем этапе по оригиналу — здесь решаем только «подходит / нет» и причину. В опросах населения доля среди беттеров часто лежит в таблице «проблемная игра по видам игр».
"""


GUIDE_NO_AI = """**Как размечать.** Откройте статью по ссылке в блоке («PDF» — файл у нас; «текст» — то же в виде текста; «онлайн» — страница статьи, там удобнее смотреть таблицы). Решаем только «подходит / нет» и причину; цифры выписываются на следующем этапе.

**Подходит (`+`), если есть всё:** 1) выборка или подвыборка тех, кто ставит на спорт (за год, месяц, жизнь — любой период; esports, fantasy на деньги и спортивные лотереи с прогнозом исхода тоже; одни скачки — нет); 2) набрана не по проблемам с игрой (не лечение, не горячая линия, не самоисключение); 3) проблемная игра измерена инструментом (PGSI/CPGI, SOGS, DSM-шкалы, NODS, PPGM, BBGS и др.) или интервью; 4) есть число или доля беттеров с порогом (риск, проблемная игра, расстройство) и n беттеров — или их можно получить (процент и n подвыборки).

В опросах населения и всех игроков доля среди беттеров часто лежит в таблице «проблемная игра по видам игр» — такая подвыборка подходит.

**Две строки в каждом блоке:**
- **Где цифры:** для `+` — где лежит доля беттеров с проблемной игрой, например `Table 3, p. 7`. Для `-` можно не писать.
- **Решение:** код из таблицы. После кода через пробел — любая заметка.

| Код | Что значит |
| --- | --- |
| `+` | подходит |
{reasons}
| `?` | пока не решил (до закрытия файла нужно решить) |

Если нужная таблица в приложении, которого нет, или текст неполный — `?` и заметка, я поищу. Если это та же выборка, что в другой статье, — `+` и заметка «та же выборка, что R…» (`-8` — только для явных повторов: тезис и статья, отчёт и статья с теми же цифрами).
"""


def one_line(t: str) -> str:
    return re.sub(r"\s+", " ", t or "").strip()


def block(n: int, rid: str, rec: dict, ret: dict, prop: dict) -> str:
    c = prop["codes"]
    code = "+" if c["decision"] == "eligible" else ("?" if c["decision"] == "unclear" else AI_TO_CODE.get(c["reason"], "-9"))
    local = f"fulltext/pdf/{rid}.pdf" if (HERE / "pdf" / f"{rid}.pdf").exists() else f"fulltext/text/{rid}.txt"
    lines = ["---", "", f"### {n} · {rid}", "", f"**{one_line(rec['title'])}**", "",
             " · ".join(x for x in [str(rec.get('year') or ''), one_line(rec.get('venue')), ret.get('source', '')] if x), "",
             f"Текст: `{local}` · источник: {ret.get('url', '')}", "",
             f"**ИИ предлагает:** {code} · {c['decision']} · {c['reason']}", "",
             f"- Выборка: {one_line(c['sample'])}", f"- Ставки на спорт: {one_line(c['sports_betting_definition'])}",
             f"- Инструменты: {one_line(c['pg_instruments'])}"]
    for d in c["estimates"]:
        lines.append(f"- {one_line(d['group'])}: {one_line(d['instrument'])} {one_line(d['threshold_or_category'])} — "
                     f"{d['cases'] or '—'} ({d['percent'] or '—'}) из n = {d['n'] or '—'}; {d['location']}: «{one_line(d['quote'])}»")
    if one_line(c["possible_duplicate"]):
        lines.append(f"- Возможный дубль: {one_line(c['possible_duplicate'])}")
    if one_line(c["note"]):
        lines.append(f"- Заметка ИИ: {one_line(c['note'])}")
    lines += ["", "**Решение:** ", ""]
    return "\n".join(lines)


def online_url(ret: dict, rec: dict) -> str:
    m = re.search(r"(PMC\d+)", ret.get("url", ""))
    if m:
        return f"https://pmc.ncbi.nlm.nih.gov/articles/{m.group(1)}/"
    if rec.get("doi"):
        return f"https://doi.org/{rec['doi']}"
    return ret.get("url", "")


def block_no_ai(n: int, rid: str, rec: dict, ret: dict, label: str) -> str:
    links = []
    if (HERE / "pdf" / f"{rid}.pdf").exists():
        links.append(f"[PDF](../pdf/{rid}.pdf)")
    links.append(f"[текст](../text/{rid}.txt)")
    url = online_url(ret, rec)
    if url:
        links.append(f"[онлайн]({url})")
    meta = " · ".join(x for x in [str(rec.get("year") or ""), one_line(rec.get("venue"))] if x)
    return "\n".join(["---", "", f"### {n} · {rid}", "", f"**{one_line(rec['title'])}**", "",
                      f"{meta} · ваша метка по аннотации: {label}" if meta else f"ваша метка по аннотации: {label}", "",
                      " · ".join(links), "", "**Где цифры:** ", "", "**Решение:** ", ""])


def make(a) -> None:
    recs = {json.loads(l)["rec_id"]: json.loads(l) for l in
            (PAPER / "search" / "runs" / a.run / "records_unique.jsonl").open(encoding="utf-8")}
    ret = {r["rec_id"]: r for r in csv.DictReader((HERE / "retrieval_log.csv").open(encoding="utf-8-sig"))}
    if a.no_ai:
        tiab = {r["rec_id"]: r["final_decision"] for r in
                csv.DictReader((PAPER / "screening" / "decisions" / "tiab_final.csv").open(encoding="utf-8-sig"))}
        ids = sorted((rid for rid, r in ret.items() if r["status"] == "retrieved"),
                     key=lambda rid: (tiab[rid] != "include", rid))
        label = {rid: "+" if tiab[rid] == "include" else "?" for rid in ids}
    else:
        props = {json.loads(l)["conv_id"]: json.loads(l) for l in (HERE / "llm" / f"{a.name}.jsonl").open(encoding="utf-8")}
        ids = sorted(props)
    out_dir = HERE / "decisions"
    out_dir.mkdir(exist_ok=True)
    reasons = "\n".join(f"| `-{d}` | не подходит: {t} |" for d, (_, t) in REASONS.items())
    for part, start in enumerate(range(0, len(ids), FILE_SIZE), a.first_part):
        chunk = ids[start:start + FILE_SIZE]
        path = out_dir / f"ft_{a.screener}_{part:02d}.md"
        if path.exists() and not a.force:
            sys.exit(f"{path} exists; refusing to overwrite R1's work")
        if a.no_ai:
            blocks = [block_no_ai(start + i, rid, recs[rid], ret[rid], label[rid]) for i, rid in enumerate(chunk, 1)]
            head = (f"# Полные тексты, часть {part}\n\nОтчёты {start + 1}–{start + len(chunk)} из {len(ids)} "
                    f"(сначала те, что вы пометили «+» по аннотации).\n\n{GUIDE_NO_AI.format(reasons=reasons)}\n")
        else:
            blocks = [block(start + i, rid, recs[rid], ret[rid], props[rid]) for i, rid in enumerate(chunk, 1)]
            head = (f"# Полные тексты, часть {part}\n\nОтчёты {start + 1}–{start + len(chunk)} из {len(ids)}. "
                    f"Предложение ИИ — черновик, решаете вы.\n\n{GUIDE.format(reasons=reasons)}\n")
        path.write_text(head + "\n".join(blocks), encoding="utf-8", newline="\n")
        print(f"{path}  ({len(chunk)} reports)")


def parse_code(raw: str) -> tuple[str, str, str, str]:
    text = raw.strip().replace("−", "-").replace("–", "-").replace("—", "-")
    text = re.sub(r"^-\s+(\d)", r"-\1", text)
    if not text:
        return "", "", "", ""
    head, _, note = text.partition(" ")
    if head == "+":
        return head, "eligible", "", note.strip()
    if head == "?":
        return head, "undecided", "", note.strip()
    if head == "=":
        return head, "agree", "", note.strip()
    m = re.fullmatch(r"-([1-9])", head)
    if m:
        return head, "not_eligible", REASONS[m.group(1)][0], note.strip()
    return head, "", "", text


def parse(a) -> None:
    rows, problems = [], []
    for f in a.files:
        lines = [x.strip() for x in Path(f).read_text(encoding="utf-8").splitlines()]
        cur = None
        for i, line in enumerate(lines):
            h = HEADER_RE.match(line)
            if h:
                cur = {"file": Path(f).name, "k": int(h.group(1)), "rec_id": h.group(2), "ai_code": "", "where": ""}
                continue
            if cur is None:
                continue
            w = WHERE_RE.match(line)
            if w:
                cur["where"] = w.group(1).strip()
                continue
            m = AI_RE.match(line)
            if m:
                cur["ai_code"] = m.group(1)
                continue
            d = DECISION_RE.match(line)
            if d:
                raw = d.group(1)
                if not raw.strip():
                    nxt = next((x for x in lines[i + 1:] if x), "")
                    if nxt and not nxt.startswith("---") and not HEADER_RE.match(nxt):
                        raw = nxt
                code, decision, reason, note = parse_code(raw)
                if decision == "agree":
                    ai = cur["ai_code"]
                    _, decision, reason, _ = parse_code(ai) if ai else ("", "", "", "")
                    code = f"={ai}"
                    if decision == "undecided":
                        problems.append(f"{cur['rec_id']}: '=' but the AI proposal is unclear — choose a code")
                if not code:
                    problems.append(f"{cur['rec_id']}: no decision")
                elif not decision:
                    problems.append(f"{cur['rec_id']}: cannot read the code {code!r}")
                elif decision == "undecided":
                    problems.append(f"{cur['rec_id']}: still undecided ('?')")
                rows.append({**cur, "code": code, "decision": decision, "reason": reason, "note": note})
                cur = None
    if a.out:
        with Path(a.out).open("w", encoding="utf-8-sig", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["rec_id", "k", "file", "code", "decision", "reason", "note", "where", "ai_code"])
            w.writeheader()
            w.writerows(rows)
    counts = {k: sum(1 for r in rows if r["decision"] == k) for k in ("eligible", "not_eligible", "undecided", "")}
    print(f"{len(rows)} reports: eligible {counts['eligible']}, not eligible {counts['not_eligible']}, "
          f"undecided {counts['undecided']}, no code {counts['']}")
    for p in problems[:40]:
        print("  " + p)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make")
    m.add_argument("--run", required=True)
    m.add_argument("--name", help="AI proposals fulltext/llm/<name>.jsonl (not with --no-ai)")
    m.add_argument("--no-ai", action="store_true", help="blocks without AI proposals (D7)")
    m.add_argument("--screener", default="R1")
    m.add_argument("--force", action="store_true")
    m.add_argument("--first-part", type=int, default=1, help="number of the first file (continue a series)")
    p = sub.add_parser("parse")
    p.add_argument("files", nargs="+")
    p.add_argument("--out")
    a = ap.parse_args()
    make(a) if a.cmd == "make" else parse(a)


if __name__ == "__main__":
    main()
