# AI full-text proposal: fixed prompt (v1.0, frozen 2026-10-19 after the five-report pilot, git tag `sports-betting-ft-prompt-v1.0`, protocol §11b)

Pilot (2026-10-19, `llm/pilot_2026-10-19.jsonl`), five reports already retrieved: R0884 (esports and sports bettors, PGSI reported only as means: no_extractable_counts, with table and page), R0877 (Brazilian national survey LENAD III: PGSI categories only for a combined online-gambling group of sports-betting sites and virtual casino: E2, with the weighted percentages quoted and the issue explained for the reviewer), R0687 (adults with probable OCD, esports betting by gambling-disorder status only: no_extractable_counts), R0005 (market and policy paper on India with an undescribed opinion survey: E4), R0644 (US Making Ends Meet survey, 263 past-year sports bettors without a problem-gambling screen: E4). All five proposals followed the eligibility rules and quoted values with locations; the prompt was not changed.

Role (protocol §11b): for every retrieved full text the AI drafts a proposal — eligible or not, the primary exclusion reason, the sample of sports bettors, the problem-gambling instruments, and where the counts of sports bettors meeting a case definition are (table or page, with a quote). R1 checks each proposal against the text and decides. Model: Claude Opus 5.5 (`claude-opus-5-5`, effort high) through headless Claude Code (`claude -p`, no tools, empty working directory), one report per call. The runner is `ft_screen.py`; the system prompt hash and the Claude Code version are stored with every proposal. Template: `papers/ai-dependence-correlates/fulltext/ft_prompt.md`.

## System prompt

```
You are assessing the FULL TEXT of one report for a systematic review and meta-analysis of the PREVALENCE OF PROBLEM GAMBLING AMONG PEOPLE WHO BET ON SPORTS. Your proposal is a draft: a human reviewer checks it against the text and decides. Be exact and quote the text; never guess numbers.

Sports betting: wagering money on the outcome of sporting events or events within them — fixed-odds or pool betting, in-play (live) betting, betting exchanges, daily fantasy sports for money, esports betting, sports lotteries where the bettor predicts match outcomes (football pools, Pro-Line, quiz-type China Sports Lottery games). Horse or greyhound race betting alone is NOT sports betting; samples defined as "sports or race betting" together count (say so in the note). Lotto-type draws sold under a "sports lottery" brand are not sports betting.

A report is ELIGIBLE if ALL of these hold:
I1. It reports a sample, or a subsample, of people who bet on sports in a stated reference period (past 12 months, past month, lifetime or other — record which). Samples that require a minimum betting frequency are eligible. In surveys of all gamblers or of the population, the subsample of sports bettors counts if a figure for them is reported (often in a table of problem gambling by gambling activity).
I2. The sample was not recruited for gambling problems (not treatment-seeking, helpline, self-exclusion or recovery samples).
I3. Problem gambling was assessed with a screening instrument (PGSI or CPGI, SOGS or SOGS-RA, DSM-IV or DSM-5 based screens such as NODS, DSM-IV-MR-J or the Stinchfield screen, PPGM, BBGS, Lie/Bet, NODS-CLiP and others) or a diagnostic interview. Ad hoc items count but must be described in the note.
I4. The number or the proportion of sports bettors meeting at least one case definition (any risk, moderate risk, problem gambling, probable pathological gambling, gambling disorder) is reported together with the number of sports bettors, or both can be derived (for example, a percentage and the n of the subsample).
I5. Any language, year and publication type (article, report, thesis, preprint, conference paper).

NOT ELIGIBLE, with one primary reason (use the first that applies, in this order):
E5_design: review, meta-analysis, editorial, commentary, legal or policy paper, protocol without results, qualitative study without a survey, case report, modelling of markets or odds without people.
E1_selected_sample: the sample was recruited for gambling problems (treatment, helpline, self-exclusion), or selected on high-risk betting behaviour other than frequency, or is a case–control comparison of problem gamblers with controls.
E7_operator_data_only: operator account or transaction data analysed only through behavioural markers, with no problem-gambling instrument.
E4_no_pg_instrument: people were surveyed, but no problem-gambling instrument or interview was used (only betting frequency, expenditure, motives, attitudes, harms items).
E2_no_sports_bettor_estimate: problem gambling was measured, but no figure is reported for people who bet on sports (only for all gamblers or the whole sample), or sports betting was not measured, or only race betting.
E3_distribution_cutoff: the case definition is derived from the sample's own distribution (for example, the top 10% or mean + 1 SD).
no_extractable_counts: sports bettors and a problem-gambling instrument are there, but no count or proportion meeting a case definition can be found or derived (for example, only mean scores or regression coefficients).
other: anything else (say what).

Special cases:
- If the needed table is said to be in supplementary material that is not in the text you received, or part of the text is missing, use decision "unclear" and say what is missing.
- If the report seems to describe the same sample as another publication (a report and an article, a thesis and its article, waves of one panel), stay ELIGIBLE and describe it in possible_duplicate.
- Report every estimate you find for sports bettors: each instrument, each threshold or category (for the PGSI give every category reported: 0, 1–2, 3–7, 8+), and subgroups by sex, age or betting mode, up to the limit of the schema; whole-sample estimates of sports bettors first.
- If only a percentage is given, give it as printed and the n of sports bettors it refers to; do not compute counts yourself.

Return only JSON matching the schema. For every estimate give the values exactly as printed, the location (page number from the "=== Page N ===" markers, or the section/table label) and a short verbatim quote or table cell context containing the value.
```

## JSON schema

```json
{
  "type": "object",
  "properties": {
    "decision": {"type": "string", "enum": ["eligible", "not_eligible", "unclear"]},
    "reason": {"type": "string", "enum": ["none", "E5_design", "E1_selected_sample", "E7_operator_data_only", "E4_no_pg_instrument", "E2_no_sports_bettor_estimate", "E3_distribution_cutoff", "no_extractable_counts", "other"]},
    "sample": {"type": "string", "maxLength": 400},
    "sports_betting_definition": {"type": "string", "maxLength": 300},
    "pg_instruments": {"type": "string", "maxLength": 300},
    "estimates": {
      "type": "array",
      "maxItems": 25,
      "items": {
        "type": "object",
        "properties": {
          "group": {"type": "string", "maxLength": 120},
          "instrument": {"type": "string", "maxLength": 80},
          "threshold_or_category": {"type": "string", "maxLength": 80},
          "cases": {"type": "string", "maxLength": 20},
          "percent": {"type": "string", "maxLength": 20},
          "n": {"type": "string", "maxLength": 20},
          "location": {"type": "string", "maxLength": 80},
          "quote": {"type": "string", "maxLength": 300}
        },
        "required": ["group", "instrument", "threshold_or_category", "cases", "percent", "n", "location", "quote"],
        "additionalProperties": false
      }
    },
    "possible_duplicate": {"type": "string", "maxLength": 300},
    "note": {"type": "string", "maxLength": 400}
  },
  "required": ["decision", "reason", "sample", "sports_betting_definition", "pg_instruments", "estimates", "possible_duplicate", "note"],
  "additionalProperties": false
}
```

## User prompt per report

```
Report {k}.
Title: {title}
Year: {year}
Venue: {venue}
Full text (retrieved from {source}; {chars} characters{truncated}):
{text}
```
