"""Screening decision files in Markdown (protocol, section 11b). Template: papers/misophonia-prevalence/screening/screen_md.py.

R1 screens in Markdown files: one block per record (title, abstract, year, venue, record type, language, DOI link;
no author names) with a line "**Решение:**" for the decision. Codes, the same on Russian and English keyboard layouts:
  +        include (goes to full text)
  ?        unsure (goes to full text)
  -1 … -7  exclude, the digit is the reason (REASONS below); a bare "-" is allowed in re-screening and verification files
  =        verification files only: agree with the AI label shown above the line (only when both AI passes agree)
Anything after the code is a note.

  make  --phase calibration --run RUN   blind calibration sample (calibration/<run>/sample.csv), no AI labels
  make  --phase rescreen --run RUN      safeguard: blind screening of double AI exclusions outside the calibration sample
  make  --phase verify --run RUN        records that at least one AI pass kept, with both labels, in files of FILE_SIZE records
  parse FILE... --out CSV               decisions -> CSV, and a check that every record has a valid code

Run: .venv/Scripts/python.exe papers/sports-betting-prevalence/screening/screen_md.py make --phase calibration --run 2026-10-16
"""
from __future__ import annotations

import argparse
import csv
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent / "search" / "runs"
FILE_SIZE = 150
PASSES = ("opus", "sonnet")
REASONS = {
    "1": ("review", "обзор, комментарий, теоретическая, правовая или регуляторная работа"),
    "2": ("nonempirical", "качественное исследование без опроса людей; рынки ставок, коэффициенты, прогнозы и модели исходов матчей, экономика спорта, договорные матчи"),
    "3": ("measure", "нет инструмента проблемной игры: только частота ставок, траты, мотивы, установки, реклама — или только поведенческие данные оператора"),
    "4": ("sports", "нет ставок на спорт: только скачки и бега, или ставки на спорт не измерялись вовсе"),
    "5": ("selected", "выборка набрана по проблемам с игрой: лечение, горячая линия, самоисключение, сравнение проблемных игроков с контролем"),
    "6": ("offtopic", "не про азартные игры или «ставка/лотерея» в другом смысле"),
    "7": ("other", "другое — напишите почему"),
}
AI_CODE = {"include": "+", "unsure": "?"}
AI_REASON_TO_DIGIT = {"exc_review_or_commentary": "1", "exc_qualitative": "2", "exc_markets_or_prediction": "2",
                      "exc_not_empirical": "2", "exc_no_pg_measure": "3", "exc_behavioural_data_only": "3",
                      "exc_race_only": "4", "exc_selected_for_problems": "5", "exc_other_sense": "6",
                      "exc_off_topic": "6", "exc_other": "7"}
AI_REASON_RU = {"inc_bettors_pg": "беттеры + инструмент", "inc_gamblers_pg_by_activity": "игроки, есть ставки на спорт и инструмент",
                "inc_population_survey": "опрос населения об азартных играх", "inc_instrument_validation": "валидация инструмента",
                "unsure_pg_unclear": "неясно, измеряли ли проблемную игру", "unsure_sports_betting_unclear": "неясно, есть ли ставки на спорт",
                "unsure_no_abstract": "нет аннотации", "unsure_other": "другое"}
GAMBLING_TERM = re.compile(
    r"gambl|\bbet\b|\bbets\b|betting|bettor|wager|bookmak|sportsbook|lotter|casino|apost|apuest|paris sportif|wett|scommess"
    r"|bahis|zakład|ставк|букмекер|彩票|博彩|竞猜|도박|토토|ベッティング|sportsspill|væddemål|vadslag", re.I)
# Calibration decisions in use: the second, blind re-screening of the same 400 records (deviations.md, D5).
CALIBRATION_DECISIONS = "calibration_R1v2.csv"
# Safeguard scope after D6: targeted double exclusions plus a seeded random audit of the rest.
TARGET_REASONS = {"exc_no_pg_measure", "exc_selected_for_problems", "exc_behavioural_data_only", "exc_qualitative"}
AUDIT_SIZE, AUDIT_SEED = 300, 20261019
HEADER_RE = re.compile(r"^###\s+(\d+)\s*·\s*(R\d{4,5})\b")
DECISION_RE = re.compile(r"^\**\s*Решение\s*:?\s*\**\s*:?\s*(.*)$", re.I)
AI_RE = re.compile(r"^\*\*ИИ:\*\*\s*(\S+)")   # strict: a record title may start with «ИИ»

GUIDE = """**Как размечать.** Под каждой записью есть строка **Решение:** — допишите в неё код, после кода можно оставить заметку.

| Код | Что значит |
| --- | --- |
| `+` | включить: количественное исследование людей, где есть те, кто ставит на спорт (в том числе fantasy sports, киберспорт, спортивные лотереи на исходы матчей), и измерена проблемная игра (PGSI, SOGS, DSM-скрининги, интервью); или опрос населения об азартных играх с инструментом проблемной игры |
| `?` | не уверен — в сомнениях выбирайте это: лишний полный текст дешевле пропущенного исследования |
{reasons}

Пример: `**Решение:** -3 только частота ставок`. Символы `+ ? -` и цифры одинаковы на русской и английской раскладке.

**Что ищем:** долю проблемной игры среди тех, кто ставит на спорт. Она часто лежит в таблице с описанием выборки, а аннотация о ней молчит. Опрос беттеров, где не сказано, измеряли ли проблемную игру, — `?`. Опрос игроков или населения с инструментом проблемной игры, где неясно, спрашивали ли про ставки на спорт, — тоже `?`. Подробно — протокол, §8.
"""


def reasons_rows() -> str:
    return "\n".join(f"| `-{d}` | исключить: {text} |" for d, (_, text) in REASONS.items())


def tidy_types(plain: str) -> str:
    seen = []
    for part in (plain or "").replace("|", ";").split(";"):
        part = part.strip().lower()
        if part and not part.startswith("src=") and part not in seen:
            seen.append(part)
    return ", ".join(seen[:3])


def types_plain(types: str) -> str:
    return "; ".join(sorted({t.split(":", 1)[1] for t in (types or "").split(" | ") if ":" in t and t.split(":", 1)[1]}))


def one_line(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def ai_line(labels: dict | None) -> list[str]:
    """One line with both AI passes. '=' is allowed only when they agree (the line then starts with the code)."""
    if not labels:
        return []

    def code_why(c):
        code = AI_CODE.get(c["decision"]) or f"-{AI_REASON_TO_DIGIT.get(c['reason'], '7')}"
        why = REASONS[code[1:]][1] if code.startswith("-") else AI_REASON_RU.get(c["reason"], c["reason"])
        return code, why
    o, s = labels["opus"]["codes"], labels["sonnet"]["codes"]
    (co, wo), (cs, ws) = code_why(o), code_why(s)
    if co == cs:
        return [f"**ИИ:** {co} · обе модели · {wo} · {one_line(o.get('note'))}", ""]
    return [f"**ИИ:** разошлись — Opus {co} ({wo}: {one_line(o.get('note'))}); Sonnet {cs} ({ws}: {one_line(s.get('note'))})", ""]


def block(n: int, r: dict, ai: dict | None = None, blind: dict | None = None) -> str:
    meta = " · ".join(x for x in [str(r.get("year") or ""), one_line(r.get("venue")), r.get("types_plain") or "",
                                  r.get("language") or "", r.get("link") or ""] if x)
    abstract = one_line(r.get("abstract")) or "_Аннотации нет — решайте по названию или ставьте `?`._"
    lines = ["---", "", f"### {n} · {r['rec_id']}", "", f"**{one_line(r.get('title')) or '[без названия]'}**", "",
             meta, "", abstract, ""]
    if blind is not None:
        lines += [f"**Ваша слепая метка (калибровка):** {blind['code']} {blind.get('note') or ''}".rstrip(), ""]
    lines += ai_line(ai)
    lines += ["**Решение:** ", ""]
    return "\n".join(lines)


def write(path: Path, title: str, intro: str, blocks: list[str], force: bool) -> None:
    if path.exists() and not force:
        sys.exit(f"{path} already exists; refusing to overwrite R1's work (use --force only for an untouched file)")
    path.parent.mkdir(parents=True, exist_ok=True)
    text = f"# {title}\n\n{intro}\n\n{GUIDE.format(reasons=reasons_rows())}\n" + "\n".join(blocks)
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"{path}  ({len(blocks)} records)")


def screening_rows(run: str) -> dict[str, dict]:
    rows = list(csv.DictReader((RUNS / run / "screening.csv").open(encoding="utf-8-sig")))
    return {r["rec_id"]: {**r, "types_plain": tidy_types(types_plain(r["types"]))} for r in rows}


def load_labels(run: str) -> dict[str, dict]:
    """Both passes' labels per record. A record labelled twice by one pass (two runner processes ran at once after a
    session restart on 2026-10-18; deviations.md, D4) keeps its earliest label by judged_at."""
    out: dict[str, dict] = {}
    for p in PASSES:
        for line in (HERE / "llm" / f"{run}_{p}.jsonl").open(encoding="utf-8"):
            if line.strip():
                d = json.loads(line)
                prev = out.setdefault(d["conv_id"], {}).get(p)
                if prev is None or d["judged_at"] < prev["judged_at"]:
                    out[d["conv_id"]][p] = d
    return out


def double_excluded(lab: dict) -> bool:
    return all(lab[p]["codes"]["decision"] == "exclude" for p in PASSES)


def make(a) -> None:
    if a.phase == "calibration":
        rows = list(csv.DictReader((HERE / "calibration" / a.run / "sample.csv").open(encoding="utf-8-sig")))
        total = len(screening_rows(a.run))
        for part, start in enumerate(range(0, len(rows), FILE_SIZE), 1):
            chunk = rows[start:start + FILE_SIZE]
            blocks = [block(start + i, {**r, "types_plain": tidy_types(r.get("types_plain"))}) for i, r in enumerate(chunk, 1)]
            intro = (f"Калибровка вслепую, часть {part}: записи {start + 1}–{start + len(chunk)} из {len(rows)}. "
                     f"Это случайные {len(rows)} записей из {total} в списке к отбору финального поиска {a.run} "
                     "(зерно 20261018, порядок случайный). **Меток ИИ здесь нет.** Размечайте в любом порядке и в несколько заходов. "
                     "Когда закончите все части, скажите: я проверю, что всё размечено, и закоммичу файлы до того, как открою метки ИИ.")
            write(HERE / "calibration" / a.run / f"calibration_{a.screener}_{part:02d}.md", f"Калибровка вслепую, часть {part}",
                  intro, blocks, a.force)
    elif a.phase == "rescreen":
        recs = screening_rows(a.run)
        sample = set(json.loads((HERE / "calibration" / a.run / "sample_meta.json").read_text(encoding="utf-8"))["rec_ids_in_display_order"])
        labels = load_labels(a.run)
        # Scope (protocol §11b, safeguard): double exclusions outside the calibration sample, except records whose title
        # and abstract contain no gambling or betting term at all (they cannot meet I1 and I3), unless the abstract is missing.
        scope = sorted(i for i, lab in labels.items() if double_excluded(lab) and i not in sample
                       and (GAMBLING_TERM.search(f"{recs[i]['title']} {recs[i]['abstract']}") or len(recs[i]["abstract"].strip()) < 50))
        # D6: all double exclusions where either pass gave a reason in TARGET_REASONS, plus a seeded random audit of
        # AUDIT_SIZE records from the rest of the scope; both strata are mixed in one random order, so R1 cannot tell them apart.
        targeted = [i for i in scope if any(labels[i][p]["codes"]["reason"] in TARGET_REASONS for p in PASSES)]
        rest = [i for i in scope if i not in set(targeted)]
        audit = random.Random(AUDIT_SEED).sample(rest, min(AUDIT_SIZE, len(rest)))
        ids = targeted + audit
        random.Random(AUDIT_SEED).shuffle(ids)
        (HERE / "rescreen" / a.run).mkdir(parents=True, exist_ok=True)
        (HERE / "rescreen" / a.run / "scope.json").write_text(json.dumps({
            "rule": "deviations.md, D6", "safeguard_scope": len(scope), "target_reasons": sorted(TARGET_REASONS),
            "targeted": sorted(targeted), "rest": len(rest), "audit_seed": AUDIT_SEED, "audit": sorted(audit),
            "display_order": ids}, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
        for part, start in enumerate(range(0, len(ids), FILE_SIZE), 1):
            chunk = ids[start:start + FILE_SIZE]
            blocks = [block(start + i, recs[rid]) for i, rid in enumerate(chunk, 1)]
            intro = (f"Записи {start + 1}–{start + len(chunk)} из {len(ids)}: записи, которые исключили обе модели (вне калибровочной выборки). "
                     "Отбор вслепую по правилу защиты (протокол, §11b; объём — deviations.md, D6). **Меток ИИ здесь нет** — решайте по тем же критериям, что и в калибровке; "
                     f"в сомнениях — `?`. Порядок случайный (зерно {AUDIT_SEED}).\n\n"
                     "**Быстрый режим:** достаточно одного символа — `+`, `?` или просто `-` (исключить, причина не нужна).")
            write(HERE / "rescreen" / a.run / f"rescreen_{a.screener}_{part:02d}.md",
                  f"Отбор вслепую по правилу защиты, часть {part}", intro, blocks, a.force)
    else:  # verify
        # Scope (protocol §11b): records outside the calibration sample that at least one pass kept, and calibration
        # records where R1's blind label (full text or not) differs from the AI rule (full text unless both passes exclude).
        recs = screening_rows(a.run)
        labels = load_labels(a.run)
        sample = set(json.loads((HERE / "calibration" / a.run / "sample_meta.json").read_text(encoding="utf-8"))["rec_ids_in_display_order"])
        blind = {r["rec_id"]: r for r in csv.DictReader((HERE / "decisions" / CALIBRATION_DECISIONS).open(encoding="utf-8-sig"))}
        ids = sorted(rid for rid in recs if rid not in sample and not double_excluded(labels[rid]))
        ids += sorted(rid for rid in sample
                      if (blind[rid]["decision"] != "exclude") != (not double_excluded(labels[rid])))
        for part, start in enumerate(range(0, len(ids), FILE_SIZE), 1):
            chunk = ids[start:start + FILE_SIZE]
            blocks = [block(start + i, recs[rid], labels.get(rid), blind.get(rid) if rid in sample else None)
                      for i, rid in enumerate(chunk, 1)]
            n_cal = sum(1 for rid in chunk if rid in sample)
            intro = (f"Записи {start + 1}–{start + len(chunk)} из {len(ids)}, с метками обеих моделей над строкой решения. "
                     "Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). "
                     "Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы."
                     + (f" Последние {n_cal} — калибровочные записи, где ваша слепая метка разошлась с правилом ИИ: она показана над метками."
                        if n_cal else ""))
            write(HERE / "verify" / a.run / f"verify_{a.screener}_{part:02d}.md", f"Проверка с метками ИИ, часть {part}",
                  intro, blocks, a.force)


def parse_code(raw: str) -> tuple[str, str, str, str]:
    """-> (code, decision, reason, note); decision '' when the code is missing or invalid."""
    text = raw.strip().replace("−", "-").replace("–", "-").replace("—", "-")
    text = re.sub(r"^-\s+(\d)", r"-\1", text)
    if not text:
        return "", "", "", ""
    head, _, note = text.partition(" ")
    note = note.strip()
    if head == "+":
        return head, "include", "", note
    if head == "?":
        return head, "unsure", "", note
    if head == "=":
        return head, "agree", "", note
    m = re.fullmatch(r"-([1-7])", head)
    if m:
        return head, "exclude", REASONS[m.group(1)][0], note
    if head == "-":   # exclude without a reason: allowed in re-screening and verification files
        return head, "exclude", "", note
    return head, "", "", text


def parse(a) -> None:
    out_rows, problems, seen = [], [], set()
    for f in a.files:
        path = Path(f)
        lines = [x.strip() for x in path.read_text(encoding="utf-8").splitlines()]
        cur = None
        for i, line in enumerate(lines):
            h = HEADER_RE.match(line)
            if h:
                cur = {"file": path.name, "k": int(h.group(1)), "rec_id": h.group(2), "ai_code": ""}
                continue
            if cur is None:
                continue
            m = AI_RE.match(line)
            if m:
                cur["ai_code"] = m.group(1)
                continue
            d = DECISION_RE.match(line)
            if d:
                raw = d.group(1)
                if not raw.strip():   # the code written on the next line instead
                    nxt = next((x for x in lines[i + 1:] if x), "")
                    if nxt and not nxt.startswith("---") and not HEADER_RE.match(nxt):
                        raw = nxt
                code, decision, reason, note = parse_code(raw)
                if decision == "agree":
                    if not cur["ai_code"] or cur["ai_code"] == "разошлись":
                        decision = ""
                        problems.append(f"{cur['rec_id']}: '=' but the AI passes disagree or there is no AI label; write your own code")
                    else:
                        _, decision, reason, _ = parse_code(cur["ai_code"])
                        code = f"={cur['ai_code']}"
                if not code:
                    problems.append(f"{cur['rec_id']}: no decision")
                elif not decision:
                    problems.append(f"{cur['rec_id']}: cannot read the code {code!r}")
                elif reason == "other" and not note:
                    problems.append(f"{cur['rec_id']}: -7 without a note (allowed, but say why)")
                if cur["rec_id"] in seen:
                    problems.append(f"{cur['rec_id']}: appears twice")
                seen.add(cur["rec_id"])
                out_rows.append({**cur, "code": code, "decision": decision, "reason": reason, "note": note})
                cur = None
    counts = {k: sum(1 for r in out_rows if r["decision"] == k) for k in ("include", "unsure", "exclude", "")}
    if a.out:
        out = Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding="utf-8-sig", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["rec_id", "k", "file", "code", "decision", "reason", "note", "ai_code"])
            w.writeheader()
            w.writerows(out_rows)
    print(f"{len(out_rows)} records: include {counts['include']}, unsure {counts['unsure']}, "
          f"exclude {counts['exclude']}, not decided {counts['']}")
    missing = [p.split(":")[0] for p in problems if p.endswith(": no decision")]
    for p in problems:
        if not p.endswith(": no decision"):
            print("  " + p)
    if missing:
        print(f"  no decision yet: {len(missing)} records ({', '.join(missing[:10])}{', …' if len(missing) > 10 else ''})")
    if a.expect and len(out_rows) != a.expect:
        print(f"  expected {a.expect} records, found {len(out_rows)}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make")
    m.add_argument("--phase", required=True, choices=["calibration", "rescreen", "verify"])
    m.add_argument("--run", required=True)
    m.add_argument("--screener", default="R1")
    m.add_argument("--force", action="store_true")
    m.add_argument("--safeguard", action="store_true",
                   help="verify: the safeguard was triggered, so AI-excluded records outside the sample are left to the re-screening")
    p = sub.add_parser("parse")
    p.add_argument("files", nargs="+")
    p.add_argument("--out")
    p.add_argument("--expect", type=int)
    a = ap.parse_args()
    make(a) if a.cmd == "make" else parse(a)


if __name__ == "__main__":
    main()
