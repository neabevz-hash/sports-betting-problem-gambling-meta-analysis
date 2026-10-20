# Регистрация на OSF: пошагово и тексты полей

Шаблон — **Generalized Systematic Review Registration** (v6 на OSF; van den Akker et al., 2023, https://doi.org/10.1186/s13643-023-02281-7), тот же, что у мизофонии и ИИ-зависимости: 61 текстовое поле, все обязательные, и 2 поля для файлов. Тексты ниже на английском, вставляются как есть. Названия полей совпадают с формой. Числа — из проверочного прогона `search/runs/2026-10-18-check/`.

## Шаги

1. **Проект.** https://osf.io → *Create new project*:
   - Title: `Prevalence of problem gambling among people who bet on sports: systematic review and meta-analysis`;
   - Storage location: любое (по умолчанию).
2. **Файлы.** В проекте *Files → OSF Storage* загрузите из `registration/osf_package/`:
   - `Rekhert_sports_betting_protocol_v1.0.pdf` — протокол;
   - `sports-betting-prereg-v1.0.zip` — весь пакет: протокол, формы, скрипты поиска и отбора, промпт скринера, логи проверочного прогона, README;
   - `llm_screener_prompt.md` и `extraction_codebook.md` — отдельно, их просят поля с файлами.
3. **Регистрация.** Вкладка *Registrations* → *New registration* → **Generalized Systematic Review Registration** → *Create draft*.
4. **Метаданные:** Title — как у проекта; Description — ниже; Category — *Project*; License — *CC-By Attribution 4.0 International*; Subjects — *Social and Behavioral Sciences → Psychology → Clinical Psychology* и *Medicine and Health Sciences → Public Health*; Tags — ниже; Contributors — только вы.
5. **Поля формы** — по разделам ниже. В поля с файлами: `llm_screener_prompt.md` (Screening → после *Screener instructions*), `extraction_codebook.md` (Extraction → после *Extractor instructions*).
6. **Отправка.** *Review* → *Register* → **Make registration public immediately**.
7. **Мне:** ссылку (`https://osf.io/xxxxx`) и DOI (`10.17605/OSF.IO/XXXXX`). Я впишу их в протокол и README; после этого можно начинать калибровку вслепую.

---

## Metadata

**Description.** Protocol (v1.0) of a systematic review and meta-analysis of the prevalence of problem gambling among people who bet on sports (including daily fantasy sports, esports betting and sports lotteries on match outcomes). Estimates are pooled separately for each case-definition level (any risk; moderate risk or higher; problem gambling; gambling disorder diagnosed by interview) across all sample types — bettor subsamples of representative population surveys, bettors recruited as such, university students, school pupils and athletes — and the review examines what drives the variation: sample type, instrument, online and in-play betting, region and legalisation period. The estimate from representative surveys is compared with the one existing pooled figure (8.9%, Tran et al., 2024). Two AI passes (Claude Opus 5.5 and Claude Sonnet 5.5) draft screening labels; the author decides every record either pass keeps and every full text, and verifies every AI-drafted extraction value; a blind calibration sample of 400 records measures the miss rate of double AI exclusions. The files contain the protocol, forms, search and de-duplication code, the frozen screener prompt and the check-run logs.

**Tags.** sports betting; problem gambling; gambling disorder; prevalence; meta-analysis; systematic review; PGSI; daily fantasy sports; esports betting; online gambling; public health; LLM-assisted screening

---

## Review Methods

**Type of review**
Systematic review and meta-analysis of prevalence (proportions), with a random-effects binomial–normal GLMM on the logit scale, a three-level moderator model and meta-regression. The protocol follows PRISMA-P 2015; the review will be reported per PRISMA 2020 and PRISMA-S. Review question framed with CoCoPop (condition: problem gambling; context: any country and year; population: people who bet on sports). Risk of bias: JBI checklist for prevalence studies. Certainty: GRADE adapted for event rates. Full protocol: Rekhert_sports_betting_protocol_v1.0.pdf in this project.

**Review stages**
Preparation (novelty check, protocol, check run of the search) → Registration (OSF; PROSPERO if its form accepts the review) → Final search → Title/abstract screening: blind calibration by the reviewer on 400 random records, two independent AI passes on all records, reviewer decision on every record that either pass keeps, conditional blind screening of double AI exclusions → Full-text screening (AI proposal, reviewer decision) → Completion of the instrument-threshold table and pilot extraction on five studies (prompts and forms frozen; any change logged) → Extraction and risk of bias (AI draft, reviewer verification of every value) → Synthesis → Reporting.

**Current review stage**
Protocol frozen on 18 October 2026 (v1.0, git tag sports-betting-prereg-v1.0, commit b58a670); the files uploaded here are built from that tag, unchanged. The final search ran on 18 October 2026 (start 11:25 UTC) with the frozen code, before this registration (deviations.md, D1): 20,442 records, 7,728 to screen, recall 25 of 25 on the seed set; CORE did not respond and is searched later as a supplementary search (D2). The blind calibration sample (400 records) was drawn and its blank decision files committed. The two AI passes are labelling records; their label files are not shown to the reviewer and are sealed by SHA-256 hashes committed to git when each pass ends, before the reviewer's calibration decisions are unblinded. No human screening decision, full-text assessment, extraction or analysis has been done.

**Start date**
2026-10-18 (novelty check).

**End date**
Not fixed in advance.

**Background**
Sports betting has spread quickly with online and mobile access and with legalisation (United States after 2018, Brazil after Law 14.790/2023, sub-Saharan Africa). Sports betting is associated with higher levels of problem gambling than most other gambling forms, and gambling disorder is a recognised mental disorder (ICD-11 6C50; DSM-5). Only one pooled estimate of problem gambling among sports bettors exists: one row of a global meta-analysis of representative population surveys (Tran et al., 2024, Lancet Public Health): 8.9% (95% CI 5.2–13.5) of adults who bet on sports in the past year, and 16.3% of adolescents based on three samples or fewer. That estimate comes only from representative surveys up to March 2024, uses one case definition and examines no sources of variation for sports betting. Systematic and scoping reviews of sports betting (Mercier et al., 2018; Winters & Derevensky, 2019; Etuk et al., 2022; Valenciano-Mendoza et al., 2023; Snaychuk et al., 2026) do not pool prevalence. No registration in PROSPERO or OSF up to 2026-10-18 plans to pool it.

**Primary research question(s)**
What is the pooled prevalence of problem gambling (problem-gambling category of a validated screen, or gambling disorder diagnosed by interview) among people who bet on sports?

**Secondary research question(s)**
(1) Pooled prevalence at each case-definition level: any risk (e.g., PGSI ≥ 1), moderate risk or higher (PGSI ≥ 3), problem gambling (PGSI ≥ 8, SOGS ≥ 5, DSM-5 ≥ 4 criteria), diagnosed gambling disorder. (2) Prevalence by sample type (bettor subsamples of representative population surveys; bettors recruited as such; university students; school pupils; athletes) and by age group; comparison of the representative-survey estimate with Tran et al. (2024), descriptively. (3) Heterogeneity by instrument, betting mode (online vs land-based; in-play; daily fantasy sports; esports), minimum betting frequency for entry, reference period of betting, region, legal status, legalisation period (US before vs after May 2018; Brazil before vs after Law 14.790/2023), year of data collection, mean age, percentage male, survey mode, gambling named in recruitment, risk of bias, publication status and gambling-industry funding. (4) Sex difference (odds ratio, male vs female), if reported.

**Expectations / hypotheses**
Expectations stated in advance, to be checked rather than tested as confirmatory hypotheses: prevalence decreases from any risk to diagnosed disorder; bettor-recruited and online samples give higher estimates than bettor subsamples of representative surveys; online and in-play bettors have higher prevalence than land-based-only bettors; samples that require regular betting give higher estimates than samples of any past-year bettors. Context: the author is a clinical psychology student with no ties to the gambling industry, to any instrument's developers or to any study likely to be included.

**Dependent variable(s) / outcome(s) / main variables**
Proportion of sports bettors meeting a problem-gambling case definition (cases / N), recorded for every case definition × sample × subgroup. Case-definition levels are fixed in the protocol (§13) and the instrument-threshold table (forms/instrument_thresholds.csv), applied regardless of the authors' labels. Primary outcome: L3 (problem gambling) or L4 (diagnosed gambling disorder).

**Independent variable(s) / intervention(s) / treatment(s)**
Not applicable (prevalence review). The population is people who bet on sports in a stated reference period: fixed-odds and pool betting, in-play betting, betting exchanges, daily fantasy sports for money, esports betting, and sports lotteries on match outcomes. Horse or greyhound race betting alone is not eligible; samples defined by "sports or race betting" together are eligible and coded.

**Additional variable(s) / covariate(s)**
Moderators (protocol §15b): case-definition level and sample type (primary); probability sampling; instrument; betting mode; shares of in-play, daily fantasy sports and esports bettors; minimum betting frequency; reference period; region; legal status; legalisation period; year of data collection; mean age; percentage male; survey mode; gambling named in recruitment; JBI items 2, 6 and 9; publication status; gambling-industry funding. Also extracted: country, design, n, response rate, weights, instrument version and language, time frame of the instrument.

**Software**
Python 3.12 (search via the PubMed E-utilities, Europe PMC, OpenAlex, Semantic Scholar, Crossref, DataCite, OpenAIRE and CORE APIs; de-duplication; calibration sampling) — search/search.py, search/dedup.py, search/recall.py. Publish or Perish (Harzing) for Google Scholar. Markdown decision files written and parsed by screening/screen_md.py. Claude Code in headless mode running Claude Opus 5.5 (claude-opus-5-5) and Claude Sonnet 5.5 (claude-sonnet-5-5) for AI draft labels and drafts (screening/llm_screen.py; the version is stored with every output). R 4.6.1 with metafor, lme4 and clubSandwich. git. Windows 11.

**Funding**
None. The review is unfunded.

**Conflicts of interest**
None. The author has no financial or professional relationship with the gambling industry, with any instrument's developers or with any operator. The AI assistant used as a tool is produced by Anthropic; the author has no relationship with Anthropic beyond a paid subscription.

**Overlapping authorships**
None. The author has not authored or co-authored any study likely to be included.

---

## Search Strategy

**Databases**
PubMed; Europe PMC (MEDLINE, PMC and preprints from medRxiv, Research Square, PsyArXiv, SSRN, Preprints.org, Authorea); OpenAlex (including non-English terms); Semantic Scholar; Crossref (posted content, reports, theses); DataCite (theses, OSF, Zenodo, figshare); OpenAIRE Graph; CORE; SciELO. No access to Scopus, Web of Science, PsycINFO or Embase.

**Interfaces**
PubMed — NCBI E-utilities; Europe PMC — REST API (searchPOST); OpenAlex — API (title_and_abstract.search, openalex: and cites: filters); Semantic Scholar — Graph API bulk search; Crossref — REST API (query.bibliographic, sorted by score); DataCite — REST API; OpenAIRE Graph — API v1 (researchProducts); CORE — API v3; SciELO — SciELO Search in a browser; Google Scholar — Publish or Perish.

**Grey literature**
Reports and theses through Crossref, DataCite, OpenAlex, OpenAIRE and CORE; preprints through Europe PMC, OpenAlex, Crossref and DataCite; the population surveys cited by Tran et al. (2024) and by the Lancet Public Health Commission on gambling (Wardle et al., 2024) that are not indexed with a DOI, retrieved from the publishers' web pages; Google Scholar (first 200 results of two queries, searched by the author with Publish or Perish).

**Inclusion and exclusion criteria**
Framework: CoCoPop. Inclusion: (I1) a sample or reported subsample of people who bet on sports in a stated reference period (minimum betting frequency allowed and coded); (I2) not recruited for gambling problems; (I3) problem gambling assessed with a validated screen (PGSI, SOGS, SOGS-RA, DSM-IV- or DSM-5-based screens, NODS, PPGM, BBGS, Lie/Bet and others) or a diagnostic interview; ad hoc items coded and tested in a sensitivity analysis; (I4) the number or proportion of sports bettors meeting at least one case definition with its denominator, or data to derive them; (I5) any language, year and publication status. Exclusion: (E1) samples recruited for gambling problems or selected on high-risk betting behaviour other than frequency; (E2) problem gambling reported only for all gamblers or the whole population, with no figure for sports bettors; (E3) case definitions derived from the sample's own distribution (recorded, not pooled); (E4) only betting involvement or harm items, no problem-gambling instrument; (E5) reviews, editorials, qualitative studies, case reports; (E6) duplicate reports of one sample (linked, most complete report used); (E7) operator account data without a problem-gambling instrument.

**Query strings**
Population concept only (sports betting), no terms for problem gambling or prevalence. Phrase set (76 phrases): {sports, sport, esports, e-sports, football, soccer, fantasy sports, daily fantasy sports} × {betting, bettors, bettor, wagering, gambling, gamblers, bets}, plus "betting on sports", "betting on sport", "gambling on sports", "wagering on sports", "bet on sports", "fantasy sports", "fantasy sport", "daily fantasy", "sports lottery", "sport lottery", "sports lotteries", "in-play betting", "live betting", "in-play sports betting", "sportsbook", "sportsbooks", "esports gambling", "match betting", "online betting", "sports pools", "sports tipping". The exact strings per source are generated by search/search.py and stored in search_log.json.
OpenAlex: title_and_abstract.search with the phrase set in chunks of 40 phrases.
PubMed: proximity pairs "<sport term> <betting term>"[tiab:~2] for {sport, sports, esports, football, soccer, fantasy sports} × {betting, bettors, bettor, wagering, gambling, gamblers, bet, bets, wager, lottery}, plus "in-play betting"[tiab], "live betting"[tiab], "online betting"[tiab:~2], sportsbook*[tiab], "daily fantasy"[tiab], "match betting"[tiab]. Quoted phrases are not used: PubMed drops phrases missing from its phrase index.
Europe PMC: TITLE_ABS:"<phrase>" with the phrase set, chunks of 40.
Semantic Scholar: bulk search with the phrase set, chunks of 30.
Crossref: 15 queries (sports betting, sports bettors, sports wagering, sports gambling, sport betting, fantasy sports gambling, daily fantasy sports, esports betting, sports lottery gambling, football betting, soccer betting, in-play betting, online sports betting, sports betting problem gambling, apostas esportivas), sorted by score, records kept while title or abstract matches a sport term next to a betting term.
DataCite: titles.title, descriptions.description and subjects.subject with the phrase set.
OpenAIRE Graph (type=publication; at most four OR operators per query) and CORE (title or abstract, one query per phrase; records without the phrase in title or abstract dropped; a query stops at the first page of 100 with fewer than five matches): sports betting, sport betting, sports bettors, sports wagering, sports gambling, sports gamblers, fantasy sports, daily fantasy sports, esports betting, esports gambling, sports lottery, football betting, soccer betting, in-play betting, online betting, betting on sports, apostas esportivas, apuestas deportivas.
OpenAlex, non-English: apostas esportivas, apostas desportivas, apostadores esportivos, bets esportivas, apuestas deportivas, apostadores deportivos, paris sportifs, parieurs sportifs, Sportwetten, scommesse sportive, spor bahisleri, spor bahis, zakłady sportowe, ставки на спорт, спортивные ставки, букмекерские ставки, 体育彩票, 体育博彩, 足球彩票, 竞猜型体育彩票, 스포츠 도박, 스포츠토토, スポーツベッティング, sportsspill, sportsvæddemål, vadslagning.
SciELO: "apostas esportivas" OR "apostas desportivas" OR "apuestas deportivas" OR "sports betting".
Google Scholar: "sports betting" "problem gambling" prevalence; "sports bettors" PGSI OR SOGS.
Citation search (OpenAlex): the reference list of Tran et al. (2024; 10.1016/S2468-2667(24)00126-9) and all records citing it.

**Search validation procedure**
Recall is checked against an independent seed set: 25 empirical studies among the references of Etuk et al. (2022) and Valenciano-Mendoza et al. (2023), which searched PubMed, Web of Science and PsycINFO, that surveyed non-clinical samples including sports bettors with a problem-gambling instrument (search/seed_set.csv, DOIs verified via Crossref). The check run and the final search of the v1.0 code (both 18 October 2026) found all 25, including the five surveys of all gamblers, online gamblers or the population (search/runs/2026-10-18/recall_seed_set.json). CORE returned server errors in both runs and is searched later as a supplementary search (deviations.md, D2); misses, if any appear later, are examined one by one.

**Other search strategies**
Citation search of Tran et al. (2024) (backward and forward), because national prevalence surveys report problem gambling by activity in tables and their abstracts rarely mention sports betting. Backward and forward citation searching of included studies and of the reviews listed in the protocol, through OpenAlex.

**Procedures to contact authors**
Authors are not contacted (the author's decision, as in the author's previous reviews). Studies without extractable counts for sports bettors are listed as such.

**Results of contacting authors**
Not applicable.

**Search expiration and repetition**
If more than six months pass between the final search and submission, the search is updated with the same strings and code; only new records are screened, by the same procedure. No living review is planned.

**Search strategy justification**
The proportion of problem gambling among sports bettors often sits in a sample-description table of studies whose abstracts do not mention problem gambling or prevalence, so the search uses only the population concept. National surveys report it in activity tables without mentioning sports betting in the abstract, so they are reached through the citation search of the most recent global prevalence meta-analysis. Without subscription databases, coverage relies on large open indexes (OpenAlex covers the Crossref corpus and repositories), non-English terms and grey-literature sources.

**Miscellaneous search strategy details**
All automated searches run from search/search.py, which logs query strings, dates, record counts and timings (search_log.json). De-duplication (search/dedup.py, copied from the author's earlier reviews) merges records on DOI (ignoring version suffixes), PMID and exact normalised title with years within ±1; pointer-source records are attached to database records; records that every source types as a non-study record are removed automatically, and so are Zenodo-only commercial deposits (bookmaker advertising, live-stream links, listicles; rule 6, 602 records in the check run).

---

## Screening

**Screening stages**
(1) De-duplication by script. (2) Title and abstract: before seeing any AI label, the reviewer (R1, the author) screens 400 records blind, drawn with random.Random(20261018).sample over the sorted record IDs; the decisions are committed before any AI label is shown. Two AI passes (Claude Opus 5.5 and Claude Sonnet 5.5, same frozen prompt) label every record include / unsure / exclude with a reason code; SHA-256 hashes of both label files are committed before unblinding. R1 decides every record that at least one pass labelled include or unsure. Records that both passes labelled exclude are excluded; if, in the calibration sample, both passes excluded a record that R1 labelled include or unsure, R1 screens all double-excluded records blind, except those without any gambling or betting term in title or abstract (unless the abstract is missing), which cannot meet the eligibility criteria. (3) Full text: the AI drafts a proposal per report (eligible or not, primary exclusion reason, location of the counts for sports bettors); R1 decides each report.

**Screened fields / blinding**
Title, abstract, year, venue, record type, language and DOI link are visible at title/abstract screening; author names are not shown. AI labels are hidden during the calibration and during the conditional blind screening.

**Used exclusion criteria**
Title/abstract stage: the record clearly is (1) a review, commentary, theoretical, legal or policy paper; (2) qualitative without a survey of people, or about betting markets, odds, prediction models, sports economics or match-fixing; (3) a study without any problem-gambling instrument (only betting frequency, expenditure, attitudes, advertising exposure, or operator data with behavioural markers only); (4) without sports betting, or about race betting only; (5) a sample recruited for gambling problems (treatment, helpline, self-exclusion, case–control); (6) not about gambling; (7) other, with a note. Full-text stage: the criteria of the protocol §8, one primary reason per report.

**Screener instructions**
The AI screener's fixed prompt and JSON schema are in screening/llm_screener_prompt.md (attached). R1 applies the same eligibility criteria with the rule "when in doubt, unsure".

**Screening reliability**
One human screener (R1) and two AI passes. In the calibration sample: Cohen's κ and Gwet's AC1 between R1 (blind) and each pass and their union; sensitivity and specificity of the double-exclusion rule against R1 with Clopper–Pearson 95% CIs. Also reported: R1's overrides by direction, whether the safeguard was triggered, and how many included studies were labelled exclude by either pass.

**Screening reconciliation procedure**
There is no second human. R1 resolves every difference between the AI labels and their own judgement against the record (and the full text when needed); R1's decision is final.

**Sampling and sample size**
All eligible studies are included. Only the calibration sample is sampled: 400 records by the seeded procedure above. A pooled estimate requires at least three independent samples.

**Screening procedure justification**
Single-reviewer screening misses about 13% of eligible studies on average (Waffenschmidt et al., 2019); LLM screeners reach high sensitivity on titles and abstracts (Oami et al., 2024). With about 7,700 records, a human check of every AI exclusion would multiply the reviewer's load without changing who decides inclusion: every record kept by either pass and every full text is decided by the reviewer. Two independent passes lower the chance of a miss, and the blind calibration measures the miss rate of the double-exclusion rule; the safeguard returns the double exclusions that mention gambling or betting (or lack an abstract) to the reviewer if the rule misses even one calibration record.

**Data management and sharing**
Search records, raw exports of the final search, R1's decision files (Markdown, with git history) and parsed decisions (CSV), both AI label files with model, prompt hash and Claude Code version (JSONL), and the list of double AI exclusions with reasons are released on GitHub with a Zenodo DOI at submission, under CC BY 4.0 (records of third parties excepted).

**Miscellaneous screening details**
R1 screens in Markdown files generated by screening/screen_md.py: one block per record with a decision line (+ include, ? unsure, -1 to -7 exclude with a reason, = accept the AI label shown). Each file is committed blank before R1 starts and again when R1 finishes.

---

## Extraction

**Entities to extract**
Per sample (forms/samples.csv): report identifiers; publication status; language; country, region and income group; years of data collection; design; sample type; sampling method; gambling named in recruitment; reference period of sports betting; minimum betting frequency; betting mode; shares of in-play, daily fantasy sports and esports bettors; sports lottery; mixed sports-and-race definition; legal status; n of sports bettors; response rate; age; percentage male; survey mode; weights; instruments; industry funding. Per estimate (forms/estimates.csv): subgroup, instrument, threshold, level (L1–L4), time frame, cases, n, derived or reported, weighted %, source location. Risk of bias: JBI nine items (forms/rob_jbi.md).

**Extraction stages**
(1) The instrument-threshold table (forms/instrument_thresholds.csv) is completed for every instrument found at full text, from development and validation papers only. (2) Pilot on five studies; extraction prompt and forms frozen; any rule added goes to deviations.md. (3) The AI pre-fills every field with its source location; the draft is stored unchanged. (4) R1 verifies every value against the source.

**Extractor instructions**
forms/extraction_codebook.md (attached; piloted on five studies before use) defines the two tables, fields and rules; rules include: the sports-betting row of an activity table is the estimate, with the number of sports bettors as denominator; all PGSI categories are extracted and cumulated at analysis; if text and table disagree, take the table; raw counts are pooled and weighted percentages recorded separately.

**Extractor masking**
None; masking is not feasible in a single-author review. The level mapping is fixed before extraction.

**Extraction reliability**
One human extractor (R1) verifying an AI draft of every value. Reported: the share of AI values R1 corrected, overall and for the key fields (denominator of sports bettors, cases, instrument, threshold, reference period, sample type), and the share of AI quotes found verbatim in the source.

**Extraction reconciliation procedure**
R1 resolves every difference between the AI draft and the source by checking the source; R1's value is final. Ambiguous values are coded NR with a note.

**Extraction procedure justification**
Single-author review without a second human extractor: pre-filling by the AI with a source location for every value and verification of every value by R1 gives each number two independent looks.

**Data management and sharing**
AI drafts (JSON), verified tables (CSV) and risk-of-bias ratings are released on GitHub with a Zenodo DOI at submission, under CC BY 4.0. No embargo.

**Miscellaneous extraction details**
Unknown values are coded NR, not applicable NA. Retractions and expressions of concern are checked through Crossref.

---

## Synthesis and Quality Assessment

**Planned data transformations**
Counts and denominators are analysed on the logit scale. Percentages without counts are converted to counts. Instrument thresholds are mapped to case-definition levels L1–L4 by the instrument-threshold table; PGSI categories are cumulated (L1 = 1+, L2 = 3+, L3 = 8+). Country is mapped to region and World Bank income group in the year of data collection. Sex differences are expressed as log odds ratios (male vs female). One estimate per sample is selected per analysis by the rules in protocol §13 (L4 over L3 for the primary outcome; within a level, the authors' primary instrument, then the PGSI, then the threshold recommended in the table, then the median logit; past-12-month bettors as the reference period).

**Missing data**
Authors are not contacted. Estimates without counts or denominators for sports bettors are not pooled, and the studies are listed among studies without extractable counts. Missing moderator values are coded NR; moderator analyses use the samples with data, and the number of samples is reported for each. No imputation.

**Data validation**
Key numbers are always checked against the source table; internal consistency checks by script (cases ≤ n; L4 ≤ L3 ≤ L2 ≤ L1; category counts summing to the total; percentages matching counts within rounding); duplicate samples across reports are linked; retractions and expressions of concern are checked through Crossref at extraction; influential estimates are examined with leave-one-out, studentised residuals and Cook's distance.

**Quality assessment**
JBI Critical Appraisal Checklist for Studies Reporting Prevalence Data (nine items; Munn et al., 2014, 2015) with decision rules adapted to sports bettors (forms/rob_jbi.md); for bettor subsamples of population surveys, items 1, 2 and 9 are rated on the parent survey; items reported individually, no summary score; items 2, 6 and 9 define sensitivity analyses and enter as moderators. Certainty of the main pooled estimates: GRADE adapted for event rates (Iorio et al., 2015); summary-of-findings table.

**Synthesis plan**
Primary model: random-effects binomial–normal generalised linear mixed model on the logit scale (metafor::rma.glmm, measure = "PLO", ML), preferred over inverse-variance pooling of transformed proportions and over the Freeman–Tukey double arcsine. Reported: pooled prevalence with 95% CI and 95% prediction interval, τ² and I² (the prediction interval is interpreted, not I²). A pooled estimate needs at least three independent samples. Subgroups: case-definition level (L1–L4); sample type; age group (adolescents under 18 / adults); region. Benchmark: the L3/L4 estimate from bettor subsamples of representative surveys beside 8.9% (5.2–13.5) of Tran et al. (2024), descriptively. Moderators: three-level binomial model with all estimates (estimates within samples within studies; lme4::glmer, nested random intercepts), checked with metafor::rma.mv on logits with cluster-robust inference. The pre-specified multivariable model contains level, sample type and probability sampling; the other moderators are exploratory, tested one at a time, each only when k ≥ 10. A variance component estimated at zero is dropped and the simpler model reported. Sex difference: random-effects log odds ratios (REML, Hartung–Knapp). Tiers: primary = pooled L3/L4 prevalence; secondary = level-specific, sample-type and age-group estimates, the benchmark and the sex difference; exploratory = single-moderator analyses. If a part of the plan cannot be executed (e.g., fewer than three samples), estimates are tabulated and shown in forest plots without pooling, and the reason is reported.

**Criteria for conclusions / inference criteria**
No significance thresholds drive the conclusions. Prevalence is interpreted through point estimates with 95% CIs and, for heterogeneity, 95% prediction intervals; moderator effects through their estimates and CIs (95%), with exploratory moderators labelled as such. Certainty of each main estimate is stated with GRADE.

**Synthesist blinding**
None. The synthesist is the author, who knows the research questions. The analysis plan, estimate-selection rules and level mapping are fixed in this registration before any data are extracted.

**Synthesis reliability**
One synthesist (the author). The analysis code is drafted by the AI assistant, checked by the author, and released; all results are reproducible from the released data and code.

**Synthesis reconciliation procedure**
Not applicable (one synthesist).

**Publication bias analyses**
Funnel-plot asymmetry tests are unreliable for proportions (Hunter et al., 2014) and are not used for inference. Instead: a plot of logit prevalence against its standard error, a regression of prevalence on 1/√n, and a comparison of peer-reviewed with grey-literature estimates. Selective reporting within studies is checked by comparing the case definitions announced in the methods with those reported. Gambling-industry funding is coded and tested as a moderator.

**Sensitivity analyses / robustness checks**
On the primary outcome: (1) only probability or census samples; (2) only validated instruments with a validated cut-off (JBI item 6 = yes); (3) excluding BBGS and other brief screens; (4) PGSI revised thresholds where category counts allow; (5) response rate ≥ 60% or not applicable; (6) excluding mixed sports-and-race or unclear sports-lottery samples; (7) excluding preprints, theses, conference abstracts and reports; (8) excluding samples with n < 100; (9) inverse-variance random-effects pooling of logits (REML, Hartung–Knapp) instead of the GLMM; (10) leave-one-out and influence diagnostics.

**Synthesis procedure justification**
The binomial–normal GLMM models within-study binomial variation exactly and avoids the bias of transformed proportions for small or extreme prevalences (Stijnen et al., 2010; Lin & Chu, 2020) and the misleading Freeman–Tukey back-transformation (Schwarzer et al., 2019). Prediction intervals describe the spread expected in a new population (IntHout et al., 2016), which matters more than I² in prevalence meta-analyses (Migliavaca et al., 2022). The three-level model uses every reported estimate without double-counting samples. Sample type and case-definition level are the key moderators because recruitment of bettors and the instruments and cut-offs are the main suspected sources of variation.

**Synthesis data management and sharing**
R scripts, their outputs, sessionInfo and the analysis data (CSV) are released on GitHub with a Zenodo DOI at submission, under open licences (code MIT, data CC BY 4.0). No embargo.

**Miscellaneous synthesis details**
Every change to this plan after registration is dated, justified and logged in deviations.md, and reported in the paper. The AI assistant's role is disclosed in the Methods and in the AI declaration.
