# AI extraction and risk-of-bias draft: fixed prompt (v1.0, frozen 2026-10-19 after the five-job pilot, git tag `sports-betting-extraction-prompt-v1.0`, protocol §11c)

Pilot (2026-10-19, `draft/pilot_2026-10-19.jsonl`): R6580 (sports bettors in a Finnish postal population survey; PGSI categories 0-2 / 3-7 / 8+ from Table 3, overall and by betting frequency), R2661 with R5777 attached (three Victorian population surveys 2008, 2014, 2018 as three samples; 2008 counts from R5777, 2014 and 2018 only weighted percentages without n, kept as NR with the percentages), R4528 (esports and other sports bettors of the YouGov emerging adults survey; weighted percentages times unweighted bases, whole-sample sums of the two mutually exclusive groups), R1768 (reverse table: sports bettors derived as 105 + 103 = 208 from the problem-gambling groups), R5435 (CAGI GPSS categories of regular sports bettors among Croatian schoolgirls, from a reverse table). All five drafts followed the rules, quoted their sources and flagged the authors' own inconsistencies (e.g., R6580: 24 of 33 printed as 72.2%). The prompt was not changed, so the five pilot drafts are the drafts of these jobs in the main run (`draft/extract_2026-10-19.jsonl`); prompt hashes are stored with each draft.

Role (protocol §11c, §14): for every included study the AI drafts every field of `forms/samples.csv` and `forms/estimates.csv` (codebook `forms/extraction_codebook.md`) and the nine JBI items (`forms/rob_jbi.md`), each value with its location and a short quote. The draft is stored unchanged in `extraction/draft/`; R1 verifies every value against the source. Model: Claude Opus 5.5 (`claude-opus-5-5`, effort high) through headless Claude Code (`claude -p`, no tools, empty working directory), one extraction job per call (`extract.py`). A job is one main report with the other reports of the same samples attached (`jobs.json`, built by `make_study_map.py`). The rules sent with every job are this file's preamble plus the levels table (`forms/instrument_thresholds.csv`), inserted by the runner. The system prompt hash, the rendered prompt hash and the Claude Code version are stored with every draft. Template: `papers/misophonia-prevalence/extraction/extract_prompt.md`.

## System prompt

```
You are extracting data for a systematic review and meta-analysis of the PREVALENCE OF PROBLEM GAMBLING AMONG PEOPLE WHO BET ON SPORTS. You read the full text of one study and fill a fixed extraction form and a risk-of-bias checklist. Your output is a draft: a human reviewer checks every value against the source. Accuracy matters more than completeness.

Rules for every value:
- Take values only from the texts given. Never guess or fill from general knowledge. If a value is not reported, write NR; if it does not apply, write NA.
- Give the location of every value: page from the "=== Page N ===" markers, or the section, table or figure label. If the value comes from an attached report rather than the main report, start the location with that report's ID (e.g., "R3634, Table 2").
- Give a short verbatim quote (at most 300 characters) that contains the value or the words it rests on. For a value you computed (a percentage times n, a sum of rows), quote the numbers you used and give the calculation in the "derivation" field.
- If the text is not in English, quote it in the original language and add an English translation in square brackets.
- Numbers: copy counts exactly as printed. If text and table disagree, use the table and describe the disagreement in consistency_notes.

Use the codes and rules in the user message exactly. Return only JSON matching the schema.
```

## User preamble (same for every job; the runner appends the levels table and the job)

```
EXTRACTION FORM

Sports betting: wagering money on the outcome of sporting events or events within them - fixed-odds or pool betting, in-play (live) betting, betting exchanges, daily fantasy sports for money, esports betting (including betting skins on esports matches), sports lotteries where the bettor predicts match outcomes. Horse or greyhound race betting alone is not sports betting.

Unit of extraction: the SAMPLE OF SPORTS BETTORS. It is either (a) the sports bettors within a larger survey (a population survey, a survey of gamblers, students or pupils) - the subsample of respondents who bet on sports in the reference period - or (b) a group recruited as sports bettors (operator customers, online panels screened for sports betting, bettors at venues). Groups recruited separately (e.g., sports bettors and esports bettors recruited with separate quotas, two school surveys in two regions, surveys in different years) are separate samples. Subgroups inside one sample (by sex, age band, betting mode, esports vs other sports) are subgroup estimates of that sample. Groups recruited for gambling problems (treatment, helplines, self-exclusion) are not eligible: do not extract them; list them in excluded_samples.

Sample fields (codes in brackets; NR = not reported, NA = not applicable):
- label: a short name for the sample (setting, country, years, n)
- reports: the report IDs that describe this sample, e.g., "R4056 (main); R3634; R3635"
- pub_status of the main report [journal / preprint / thesis / conference / report / other]
- language of the full text of the main report
- country: ISO 3166 alpha-3; several countries: "MULTI: GBR, USA, ..."
- subnational: state, province or city if the sample is subnational (e.g., "Victoria", "New South Wales", "Jimma town"); else NA
- data_years: years of data collection, e.g. "2021-2022"
- design [cross-sectional / cohort baseline / prevalence survey / validation study / experiment baseline / EMA baseline / other]
- sample_type [rep_survey_subsample = sports bettors within a probability or census survey of a population (households, residents, all pupils of sampled schools) / gamblers_survey_subsample = sports bettors within a non-probability survey of gamblers or of the public (online panels of gamblers, convenience surveys) / bettor_recruited = recruited as sports bettors (panels screened for sports betting, operator customers, venues, social media of betting communities) / students = university students who bet / school_pupils = pupils who bet / athletes / other]
- parent_population: for subsamples, the population the parent survey describes (e.g., "adults 18+ of Finland aged 15-74", "online gamblers on one platform"); else NA
- sampling [probability / census / quota = quota or stratified non-random online panel / operator_customers / venue_intercept / convenience / snowball / NR] - for subsamples, the sampling of the parent survey
- gambling_disclosed [yes = the invitation or survey title named gambling or betting / no = presented as a general health, lifestyle or other survey / NR]
- betting_period: the reference period that defines a sports bettor [past 12 months / past 30 days or month / past week / lifetime / current / NR]
- min_frequency: minimum betting frequency for entry as stated (e.g., "at least monthly", "regularly = weekly or more"); "none" if any bettor in the period counts
- betting_mode [online only / land-based only / both / NR]
- pct_online: share of the sample who bet online, 0-100 or NR; "all" if the sample is defined as online bettors
- pct_inplay, pct_dfs, pct_esports: shares of in-play bettors, daily-fantasy-sports players, esports bettors, 0-100 or NR; "all" if the sample is defined by it
- sports_lottery [yes = quiz-type sports lottery or pools on match outcomes counted as sports betting / no / unclear]
- mixed_race [yes = the sample or estimate is defined as "sports or race betting" together / no]
- legal_status of sports betting at the time and place of data collection, as described in the texts [regulated legal market / state monopoly / not legal or unregulated / mixed / NR]
- n_invited, n_responded: integers for the whole survey
- n_bettors: the number of sports bettors analysed = denominator of the sample's main estimate
- response_rate: as reported, or n_responded / n_invited as a percentage
- age_mean, age_sd, age_min, age_max: years, of the sports bettors if reported, else of the whole sample (say which in notes)
- age_group [adolescents = under 18 / adults = 18 and over / mixed / NR]
- pct_male: 0-100, of the sports bettors if reported, else of the whole sample (say which in notes)
- mode [online / telephone / face-to-face / paper / mixed / NR]
- weights [yes = estimates weighted to the population / no / NR]
- instruments: every problem-gambling instrument used, with its language version, separated by ";"
- instrument_validated_in_language [yes / no / NR]: for the instrument of the sample's main estimate, whether that language version has a published validation (cited or stated in the text)
- industry_funding [yes = gambling operator, industry body or levy controlled by the industry / no / NR]
- funding_coi: short
- notes: anything a reviewer must know (overlap with another study, later waves, a corrigendum, whose age or sex the fields describe)

Estimate fields (one estimate per case-definition category x subgroup; whole sample first, then subgroups):
- subgroup: all / male / female / an age band such as "18-24" / online / land-based / in-play / DFS / esports / other sports / another subgroup named by the authors
- instrument: one of PGSI, SOGS, SOGS-RA, DSM-IV-MR-J, NODS, NODS-CLiP, DSM-IV-screen, DSM-5-screen, PPGM, BBGS, Lie-Bet, CAGI, interview, adhoc, other. CPGI, ICJE and PGSI versions reworded for sports betting with unchanged 0-3 item scoring are PGSI; NODS-SA is NODS; a PGSI-like scale with other scoring is adhoc (levels table)
- threshold: the category exactly as applied, with the instrument's score range: e.g., "PGSI>=8", "PGSI 3-7", "PGSI 1-2", "PGSI 0", "PGSI>=3", "SOGS>=5", "DSM-5 criteria>=4", "CAGI GPSS>=6 (red light)", "interview: SCID-5"
- cumulative [yes = the category includes every score above its lower bound ("8+", ">=3", "red light") / no = a closed band ("3-7", "1-2", "0", "yellow light")]
- threshold_source [standard = the instrument's developers / validation paper / study's own / percentile of this sample]
- author_label: the authors' own words, e.g. "problem gambler", "moderate risk", "probable pathological"
- level [below / L1 / L2 / L3 / L3-screen / L4 / E3 / not_levelled / NR]: the level of the category's LOWER BOUND by the levels table, whatever the authors call it. PGSI 0 -> below; PGSI 1-2 -> L1; PGSI 3-7 -> L2; PGSI>=8 -> L3; PGSI>=3 -> L2; PGSI>=1 -> L1. BBGS, Lie-Bet and NODS-CLiP positives -> L3-screen. A diagnosis by a clinician or a structured diagnostic interview -> L4. A cut-off taken from the sample's own distribution (top 10%, mean + 1 SD) -> E3. adhoc items and non-standard scoring -> not_levelled. A combined category whose lower bound you cannot place -> NR
- table_rule: the levels-table row used and why, e.g. "PGSI row; 3-7 band starts at L2"; for a DSM-5 category below 4 add "DSM-5 L2 provisional"
- time_frame of the instrument [past 12 months / past 3 months / past month / lifetime / NR]
- cases: integer number of sports bettors in this category
- n: the denominator (sports bettors in this subgroup)
- derived [yes / no] and derivation: how cases or n were computed (e.g., "18% x 121 = 21.8 -> 22"; "103 at-risk/problem bettors + 105 non-problem bettors = 208 sports bettors"); empty if not derived
- weighted_pct: the weighted prevalence if the study reports one (survey weights); else NA
- primary_for_authors [yes / no]: yes if the authors present this as their main problem-gambling estimate
- location and quote: where the numbers are, and a quote with them
- note: anything else (e.g., "denominator unclear: 1,033 answered the PGSI")

Extraction rules:
- Report every category of every instrument as printed, for the whole sample and for subgroups by sex, age band and betting mode: for the PGSI usually 0, 1-2, 3-7 and 8+. Do not build cumulative sums yourself: the analysis builds them from the categories. Give a cumulative estimate only when the study itself reports one (e.g., "PGSI 3+ = 13.1%").
- Sports bettors as a subgroup of a survey: when a table gives problem gambling by gambling activity, the sports-betting row is the estimate and the denominator is the number of respondents who bet on sports in the period.
- Reverse tables: when a table gives, for each problem-gambling group, how many bet on sports (e.g., "sports betting: non-problem gamblers 105 of 281; at-risk/problem gamblers 103 of 170"), derive the sports bettors: n = the sum over groups (105 + 103 = 208) and cases = the count in the problem group (103); derived = yes, and show the calculation. Do this only when the groups cover all gamblers of the survey without overlap.
- If only a percentage is given: cases = round(percentage x n / 100) and derived = yes. If n is unknown, give cases and n as NR and the percentage in note.
- Weighted estimates: give the raw counts in cases and n, and the weighted percentage in weighted_pct. If only weighted percentages and the unweighted n are given, derive cases from the weighted percentage (derived = yes) and say so in note.
- Waves of one panel or repeated measurements: extract the first wave as the sample; later waves only in the sample notes.
- "Sports or race betting" combined: extract, set mixed_race = yes and say so in note.
- Numeric fields (n_invited, n_responded, n_bettors, response_rate, age_mean, age_sd, age_min, age_max, pct_male, pct_online, pct_inplay, pct_dfs, pct_esports, cases, n, weighted_pct): value holds one number, or NR, or NA (or "all" for the pct fields). Explanations go to the sample notes or the estimate note.

RISK OF BIAS: JBI checklist for prevalence studies, rated per sample (yes / no / unclear / NA), with a one-line reason, location and quote. The target population is the population of sports bettors the study claims to describe (sports bettors of a country or state, customers of an operator, students who bet, pupils who bet). For subsamples of a survey, items 1, 2 and 9 are rated on the parent survey.
1. Sample frame appropriate to address the target population? yes: the frame covers the target population (population register or address list of the parent survey; all customers of the operators named; all enrolled students). no: the frame covers only part of it (one operator's customers for "sports bettors in the country", social-media followers of tipster pages, one class for "students"). unclear: frame not described.
2. Participants sampled in an appropriate way? yes: probability sampling or census of the frame (for subsamples: of the parent survey). no: convenience, snowball, volunteer opt-in, online non-probability panel (including quota "representative" panels). unclear: method not described.
3. Sample size adequate? yes: n of sports bettors >= 385. no: below 385.
4. Subjects and setting described in detail? yes: age, sex, setting, country and dates of data collection reported. no: two or more of these missing. unclear: one missing.
5. Data analysis with sufficient coverage of the identified sample? yes: missing problem-gambling data <= 10% of the sports bettors, or handled. no: > 10% missing, not handled. unclear: not reported.
6. Valid methods for the identification of the condition? Rate the definition that supplies the sample's primary-outcome estimate (L4, else L3). yes: diagnostic interview (L4), or a validated instrument (PGSI, SOGS, SOGS-RA, NODS, DSM-IV-MR-J, DSM-based screens, PPGM, CAGI) with its standard threshold, in a language version with published validation. no: ad hoc items, study-specific thresholds, brief screens used as a diagnosis (BBGS, Lie-Bet, NODS-CLiP), or versions without any validation in that language. unclear: version or threshold unclear.
7. Condition measured in a standard, reliable way for all participants? yes: same instrument, time frame, mode and threshold for everyone, and reliability reported in the sample or the source. no: different instruments or modes across participants without a check. unclear: not reported.
8. Appropriate statistical analysis? yes: numerator and denominator of sports bettors clear; CI given or calculable; weights used if the design requires them. no: percentages that cannot be traced to a numerator and a denominator of sports bettors.
9. Response rate adequate, or low response managed? yes: response >= 60%, or responders compared with non-responders, or weights for non-response. no: response < 60% without handling; open online surveys or panels with no denominator of invited people. unclear: not reported.
```

## Job template (the runner fills it)

```
LEVELS TABLE: instruments, thresholds and case-definition levels (forms/instrument_thresholds.csv)
{table1}

JOB {job_id} (study {study_id})
Samples to extract: {samples}
{links}
MAIN REPORT {main_id}
Title: {main_title}
Year: {main_year}; venue: {main_venue}; DOI: {main_doi}
Full text ({main_chars} characters{main_truncated}):
{main_text}
{attached}
```

## Output fields

The runner builds the JSON schema from this block: every sample field is an object {value, loc, quote}; fields with a code list get an enum on value.

```json
{
  "sample_fields": {
    "pub_status": ["journal", "preprint", "thesis", "conference", "report", "other"],
    "language": null,
    "country": null,
    "subnational": null,
    "data_years": null,
    "design": ["cross-sectional", "cohort baseline", "prevalence survey", "validation study", "experiment baseline", "EMA baseline", "other"],
    "sample_type": ["rep_survey_subsample", "gamblers_survey_subsample", "bettor_recruited", "students", "school_pupils", "athletes", "other"],
    "parent_population": null,
    "sampling": ["probability", "census", "quota", "operator_customers", "venue_intercept", "convenience", "snowball", "NR"],
    "gambling_disclosed": ["yes", "no", "NR"],
    "betting_period": ["past 12 months", "past 30 days or month", "past week", "lifetime", "current", "NR"],
    "min_frequency": null,
    "betting_mode": ["online only", "land-based only", "both", "NR"],
    "pct_online": null,
    "pct_inplay": null,
    "pct_dfs": null,
    "pct_esports": null,
    "sports_lottery": ["yes", "no", "unclear"],
    "mixed_race": ["yes", "no"],
    "legal_status": ["regulated legal market", "state monopoly", "not legal or unregulated", "mixed", "NR"],
    "n_invited": null,
    "n_responded": null,
    "n_bettors": null,
    "response_rate": null,
    "age_mean": null,
    "age_sd": null,
    "age_min": null,
    "age_max": null,
    "age_group": ["adolescents", "adults", "mixed", "NR"],
    "pct_male": null,
    "mode": ["online", "telephone", "face-to-face", "paper", "mixed", "NR"],
    "weights": ["yes", "no", "NR"],
    "instruments": null,
    "instrument_validated_in_language": ["yes", "no", "NR"],
    "industry_funding": ["yes", "no", "NR"],
    "funding_coi": null
  },
  "estimate_enums": {
    "instrument": ["PGSI", "SOGS", "SOGS-RA", "DSM-IV-MR-J", "NODS", "NODS-CLiP", "DSM-IV-screen", "DSM-5-screen", "PPGM", "BBGS", "Lie-Bet", "CAGI", "interview", "adhoc", "other"],
    "cumulative": ["yes", "no"],
    "threshold_source": ["standard", "validation paper", "study's own", "percentile of this sample"],
    "level": ["below", "L1", "L2", "L3", "L3-screen", "L4", "E3", "not_levelled", "NR"],
    "time_frame": ["past 12 months", "past 3 months", "past month", "lifetime", "NR"],
    "derived": ["yes", "no"],
    "primary_for_authors": ["yes", "no"]
  },
  "jbi_ratings": ["yes", "no", "unclear", "NA"]
}
```
