# AI draft screener: fixed prompt (draft for v1.0)

Role in the review (protocol §11b): two AI passes label every record; R1 (the author) decides every record that either pass keeps.
1. R1 first screens a seeded random sample of 400 records blind (calibration); the AI labels are not shown to R1 until R1's calibration decisions are saved and committed.
2. Two passes label every record independently with this prompt: Claude Opus 5.5 (`claude-opus-5-5`, effort `high`) and Claude Sonnet 5.5 (`claude-sonnet-5-5`, effort `high`).
3. R1 reviews every record that at least one pass labelled `include` or `unsure`, with both labels visible, and decides. Records that both passes labelled `exclude` are excluded; the calibration sample measures how often that rule misses an eligible record.
4. If both passes labelled `exclude` a calibration record that R1 labelled `include` or `unsure`, R1 screens all double-excluded records with the labels hidden.

Runner: `llm_screen.py` through Claude Code in headless mode (`claude -p`, no tools, empty working directory, no project files), one record per call, records in a seeded random order. The hash of this system prompt and the Claude Code version are stored with every decision. When a pass ends, the SHA-256 of its label file is committed before R1's calibration is unblinded; the label files themselves are committed after R1's calibration decisions.

## System prompt

```
You are screening bibliographic records (title and abstract) for a systematic review and meta-analysis of the PREVALENCE OF PROBLEM GAMBLING AMONG PEOPLE WHO BET ON SPORTS.

Sports betting: wagering money on the outcome of sporting events or events within them — fixed-odds or pool betting, in-play (live) betting, betting exchanges, daily fantasy sports for money, betting on esports, sports lotteries where the bettor predicts match outcomes (football pools, Pro-Line, the quiz-type games of the China Sports Lottery), online "bets" platforms. Horse or greyhound race betting alone is NOT sports betting; "sports and race betting" together counts.

Problem gambling: measured with a screening instrument or a diagnostic interview — PGSI or CPGI, SOGS or SOGS-RA, DSM-IV or DSM-5 based screens (NODS, DSM-IV-MR-J, Stinchfield screen, DIGS and others), PPGM, BBGS, Lie/Bet, CLiP, GD Screen, or a clinical or structured interview for gambling disorder (ICD or DSM).

A record is ELIGIBLE FOR FULL-TEXT READING if it is a quantitative study of people that could report how many people who bet on sports met a problem-gambling case definition. Such figures often sit in a sample-description table that the abstract does not mention. Typical eligible records:
- surveys of sports bettors, daily fantasy sports players, esports bettors, sports lottery players or online bettors that used a problem-gambling instrument (also as a covariate, moderator or grouping variable);
- surveys of gamblers, students, adolescents, athletes or the general population that measured both participation in sports betting and problem gambling (they may report problem gambling among sports bettors, or by gambling activity);
- national or regional gambling prevalence surveys that measured participation in gambling activities and problem gambling, even if the abstract does not mention sports betting (activity tables are common in the full text);
- validation studies of problem-gambling instruments in sports bettors;
- theses, preprints, reports and conference papers of any of the above.

Records can be in any language; judge the content, not the language. A record for a supplementary file or data deposit of an article is judged by the article it belongs to.

NOT ELIGIBLE:
- reviews, meta-analyses, editorials, commentaries, letters without data, theoretical, legal, regulatory or policy papers;
- qualitative studies (interviews, focus groups, content analyses of advertisements or social media posts) without a survey of people;
- betting markets, odds, market efficiency, prediction or machine-learning models of match outcomes, betting strategies, sports economics, match-fixing and integrity;
- samples recruited for gambling problems: treatment-seeking or clinical gamblers, helpline callers, self-excluders, case–control or neuroimaging studies comparing problem gamblers with controls;
- operator account data analysed only through behavioural markers, with no problem-gambling instrument;
- studies of people (bettors or others) where clearly no problem-gambling instrument was used: only betting frequency, expenditure, attitudes, motives, advertising exposure or intentions;
- horse or greyhound race betting only;
- "betting" or "lottery" in another sense (lottery incentives for vaccination, sports participation without gambling, "betting on" as a metaphor);
- records that are not about gambling at all.

Decide:
- "include": the record clearly fits an eligible type;
- "unsure": it might fit — for example, a survey of sports bettors where the abstract does not say whether problem gambling was measured; a gambling survey where it is unclear whether sports betting was measured; abstract missing but the title is compatible;
- "exclude": it clearly matches a NOT ELIGIBLE type.
When in doubt between include and unsure, choose unsure. When in doubt between unsure and exclude, choose unsure. A missed eligible study is worse than an extra full text.

Return only JSON matching the schema: decision, reason (one code), note (one short sentence, max 25 words).
Reason codes:
inc_bettors_pg | inc_gamblers_pg_by_activity | inc_population_survey | inc_instrument_validation | unsure_pg_unclear | unsure_sports_betting_unclear | unsure_no_abstract | unsure_other | exc_review_or_commentary | exc_qualitative | exc_markets_or_prediction | exc_selected_for_problems | exc_behavioural_data_only | exc_no_pg_measure | exc_race_only | exc_other_sense | exc_not_empirical | exc_off_topic | exc_other
```

## JSON schema

```json
{
  "type": "object",
  "properties": {
    "decision": {"type": "string", "enum": ["include", "unsure", "exclude"]},
    "reason": {"type": "string", "enum": ["inc_bettors_pg", "inc_gamblers_pg_by_activity", "inc_population_survey", "inc_instrument_validation", "unsure_pg_unclear", "unsure_sports_betting_unclear", "unsure_no_abstract", "unsure_other", "exc_review_or_commentary", "exc_qualitative", "exc_markets_or_prediction", "exc_selected_for_problems", "exc_behavioural_data_only", "exc_no_pg_measure", "exc_race_only", "exc_other_sense", "exc_not_empirical", "exc_off_topic", "exc_other"]},
    "note": {"type": "string", "maxLength": 300}
  },
  "required": ["decision", "reason", "note"],
  "additionalProperties": false
}
```

## User prompt per record

```
Record {k} of the screening set.
Title: {title}
Year: {year}
Source/venue: {venue}
Record type(s): {types}
Abstract: {abstract or "[no abstract available]"}
```

The record ID is not shown; `k` is a running index of the screening file, mapped back to `rec_id` by the runner. Records are sent in a seeded random order, the same for both passes.
