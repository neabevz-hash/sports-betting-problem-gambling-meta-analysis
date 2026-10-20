# Protocol: Prevalence of problem gambling among people who bet on sports — a systematic review and meta-analysis

**Version 1.0, frozen on 2026-10-18** (git tag `sports-betting-prereg-v1.0`) before the final search and before any title/abstract screening. Structured by PRISMA-P 2015 (Moher et al., 2015; Shamseer et al., 2015); item numbers in brackets. Built on the misophonia protocol (`papers/misophonia-prevalence/protocol.md`, v1.0) for the prevalence methods and on the AI-dependence protocol (`papers/ai-dependence-correlates/protocol.md`, v1.0) for the two-pass AI screening. Every reference was verified by DOI via Crossref on 2026-10-18. Changes from the draft v0.1 are listed at the end.

---

## Administrative information

**[1] Title.** Prevalence of problem gambling among people who bet on sports: a systematic review and meta-analysis across case definitions and sample types.

**[2] Registration.** OSF Registries, registered on 2026-10-18 at 13:52 UTC: https://osf.io/6gq48, DOI [10.17605/OSF.IO/6GQ48](https://doi.org/10.17605/OSF.IO/6GQ48) (project https://osf.io/tuwm8); the final search ran before it (`deviations.md`, D1). Generalized Systematic Review Registration form (van den Akker et al., 2023), with the frozen protocol and the registration package (`registration/make_osf_package.py`: protocol, forms, search and screening code, the AI screener prompt, the check-run logs); field texts in `registration/osf.md`. The final search starts after the registration. PROSPERO as well, if its form accepts prevalence reviews at the time of registration (several gambling prevalence reviews were registered there in 2025–2026, for example CRD420261417334). Adding the registration identifiers here is the only change made to this file after freezing.

**[3a] Author and contact.** Martin Rekhert, MA student in clinical psychology, Turan University, Almaty, Kazakhstan. ORCID 0009-0001-2402-2031. mrexert@gmail.com.

**[3b] Contributions.** Single author (R1): conceptualisation, eligibility decisions at every stage, data extraction, risk-of-bias appraisal, interpretation, final manuscript. An AI assistant (Claude Opus 5.5, Anthropic, run through Claude Code; Claude Sonnet 5.5 as the second screening pass) is used as a tool for the tasks in §9–§11 and §15: search code, de-duplication, draft screening labels, draft full-text decisions, draft extraction and risk-of-bias ratings, analysis code, translation and text drafts. It is disclosed in the Methods and in the AI declaration. Every AI output is a draft: R1 checks each AI label, extracted value and rating against the source and accepts or overrides it, so all final decisions are R1's.

**[4] Amendments.** Any change after registration is dated, justified and logged in `deviations.md`, and reported in the registration and in the paper.

**[5] Support.** No funding, no sponsor, no conflicts of interest.

---

## Introduction

**[6] Rationale.**

Sports betting has spread quickly with online and mobile access and with legalisation: in the United States after the Supreme Court struck down the federal ban in 2018 (*Murphy v. NCAA*), in Brazil after Law 14.790/2023, and across sub-Saharan Africa. Sports betting is associated with higher levels of problem gambling than most other gambling forms (Russell et al., 2019; Etuk et al., 2022), and gambling disorder is a recognised mental disorder (ICD-11 6C50; DSM-5). For prevention, regulation and service planning, the key quantity is how common problem gambling is among the people who bet on sports.

Only one pooled estimate exists. In a global meta-analysis of representative population surveys, Tran et al. (2024) estimated that 8.9% (95% CI 5.2–13.5) of adults who bet on sports in the past year had problematic gambling, and 16.3% of adolescents (three samples or fewer). That estimate is one row of a table: it comes only from representative surveys (non-representative samples, which make up most of the sports-betting literature, were excluded), covers studies up to March 2024, uses one case definition, and examines no sources of variation for sports betting. Systematic and scoping reviews of sports betting (Mercier et al., 2018; Winters & Derevensky, 2019; Etuk et al., 2022; Valenciano-Mendoza et al., 2023; Snaychuk et al., 2026) describe correlates and harms but pool no prevalence. No review registered in PROSPERO or OSF up to 2026-10-18 plans to pool it (`novelty/novelty.md`).

Single-study estimates vary widely, probably because samples and definitions differ: subsamples of bettors in national surveys, online panels of regular bettors, university students, school pupils; past-year or more frequent betting as the entry criterion; the PGSI, SOGS, DSM-based screens and others, each with several cut-offs. A pooled, definition-aware estimate that examines this variation is missing.

**[7] Objectives.**

Review question (CoCoPop; Munn et al., 2015):
- **Condition:** problem gambling or gambling disorder, identified by a validated screening instrument or a diagnostic interview.
- **Context:** any country, setting and year.
- **Population:** people who bet on sports (§8), not selected for gambling problems.

Objectives:
1. **Primary.** Estimate the prevalence of problem gambling (levels L3/L4, §13) among people who bet on sports.
2. Estimate the prevalence at each case-definition level: L1 any risk, L2 moderate risk or higher, L3 problem gambling, L4 gambling disorder diagnosed by interview.
3. Estimate prevalence by sample type: bettor subsamples of representative population surveys, bettors recruited as such (panels, operator or venue samples, online recruitment), university students, school pupils, athletes. Compare the estimate from representative surveys with Tran et al. (2024).
4. Examine sources of heterogeneity: instrument, betting mode (online vs land-based; in-play betting; daily fantasy sports; esports betting; sports lotteries), betting frequency required for entry, region, legalisation period, year of data collection, age, sex composition, survey mode, risk of bias.
5. If reported, estimate the sex difference (odds ratio, male vs female) in problem gambling among sports bettors.

The review is descriptive and tests no confirmatory hypotheses. Expectations stated in advance, to be checked rather than tested: prevalence decreases from L1 to L4; bettor-recruited and online samples give higher estimates than bettor subsamples of representative surveys; online and in-play bettors have higher prevalence than land-based-only bettors; samples that require regular betting give higher estimates than samples of any past-year bettors.

---

## Methods

### [8] Eligibility criteria

**Study designs.** Cross-sectional surveys; the baseline wave of cohort studies; screening phases of other studies; national and regional gambling prevalence surveys (journal articles and government or research reports); any design that reports how many people who bet on sports met a problem-gambling case definition.

**Definition of sports betting.** Wagering money on the outcome of sporting events or on events within them: fixed-odds and pool betting, in-play (live) betting, betting exchanges, daily fantasy sports for money, betting on esports, and sports lotteries in which the bettor predicts match outcomes (for example, football pools, Pro-Line, the quiz-type 竞猜 games of the China Sports Lottery). Not sports betting on its own: horse and greyhound race betting, lotto-type draws sold under a "sports lottery" brand, skin gambling without a sporting outcome. Samples defined by "sports or race betting" together, or by a sports lottery of unclear type, are eligible and coded as mixed (sensitivity analysis 6).

**Inclusion criteria.**
- I1. The sample, or a reported subsample, consists of people who bet on sports in a stated reference period (past 12 months as standard; past month, past 30 days or lifetime coded). Samples that require a minimum betting frequency (for example, at least monthly) are eligible and coded.
- I2. The sample was not recruited for gambling problems: not treatment-seeking, helpline, self-exclusion or recovery samples.
- I3. Problem gambling was assessed with a validated screening instrument (PGSI, SOGS or SOGS-RA, DSM-IV- or DSM-5-based screens such as NODS, DSM-IV-MR-J, the Stinchfield screen, PPGM, BBGS, Lie/Bet, CLiP and others) or a diagnostic interview. Ad hoc or non-validated items are eligible, coded, and tested in a sensitivity analysis.
- I4. The study reports the number or proportion of sports bettors meeting at least one case definition together with the denominator, or enough data to derive them.
- I5. Any language, any publication year, any publication status: journal article, preprint, thesis, conference abstract or report with sufficient data.

**Exclusion criteria.**
- E1. Samples recruited for gambling problems (I2), and samples selected on high-risk betting behaviour other than frequency (for example, "bettors who chase losses").
- E2. Problem gambling assessed only among all gamblers or the whole population, with no figure for sports bettors.
- E3. Case definitions derived from the sample's own distribution (for example, the top 10% of scores): recorded, not pooled.
- E4. Measures of betting involvement or harm that are not problem-gambling instruments (frequency, expenditure, single harm items).
- E5. Reviews, editorials, qualitative studies without counts, case reports.
- E6. Duplicate reports of the same sample; reports are linked and the most complete one supplies the data.
- E7. Operator account data without a problem-gambling instrument (behavioural markers of harm only).

### [9] Information sources

Turan University has no access to Scopus, Web of Science, PsycINFO or Embase. Coverage relies on open indexes, non-English terms and citation searching, as in the misophonia and AI-dependence reviews:

- **PubMed**; **Europe PMC** (MEDLINE, PMC and preprints from medRxiv, Research Square, PsyArXiv, SSRN, Preprints.org, Authorea); **OpenAlex**; **Semantic Scholar**; **Crossref** (posted content, reports, theses); **DataCite** (theses, OSF, Zenodo, figshare); **OpenAIRE Graph** and **CORE** (institutional repositories, theses, reports); **SciELO** (Portuguese and Spanish).
- **Non-English terms** in OpenAlex: Portuguese, Spanish, French, German, Italian, Turkish, Polish, Russian, Chinese, Korean, Japanese, Scandinavian languages (§10).
- **Citation searching:**
  - **population prevalence surveys:** the reference list of Tran et al. (2024; 141 references indexed in OpenAlex) and the records citing it (272 in OpenAlex on 2026-10-18). Many national surveys report problem gambling by gambling activity only in tables, so their abstracts do not mention sports betting and a topic search misses them; this step brings them in;
  - **backward and forward** citation searching of included studies and of the reviews in §6, through OpenAlex.
- **Grey literature:** reports and theses through Crossref, DataCite, OpenAIRE, CORE and OpenAlex; the reports cited by Tran et al. (2024) and by the Lancet Public Health Commission on gambling (Wardle et al., 2024) that are not indexed with a DOI, retrieved from the publishers' web pages.
- **Google Scholar:** two queries, the first 200 results of each (Haddaway et al., 2015), retrieved by R1 with Publish or Perish; only records new to the database set are screened.

**Seed set.** 25 empirical studies among the references of Etuk et al. (2022; PubMed, Web of Science, PsycINFO) and Valenciano-Mendoza et al. (2023; PubMed, PsycINFO) that surveyed non-clinical samples including sports bettors with a problem-gambling instrument (`search/seed_set.csv`, DOIs verified via Crossref on 2026-10-18, built before the check run). Five of them are surveys of all gamblers, online gamblers or the population, whose abstracts need not mention sports betting, so they also test the reach of the population-concept search. Recall is reported for the check run and for the final search; misses are examined one by one.

### [10] Search strategy

The search uses the population concept only (sports betting), without terms for problem gambling or prevalence: many studies report the PGSI distribution of their bettors only in the sample description or a table. No date or language limits. Strings are reported per PRISMA-S (Rethlefsen et al., 2021); code: `search/search.py`, adapted from `novelty/fetch_sources.py`.

**Phrase set.** {sports, sport, esports, e-sports, football, soccer, fantasy sports, daily fantasy sports} × {betting, bettors, bettor, wagering, gambling, gamblers, bets}, plus "betting / gambling / wagering on sports", "fantasy sport(s)", "daily fantasy", "sports lottery / lotteries", "in-play betting", "live betting", "sportsbook(s)", "esports gambling", "match betting", "online betting", "sports pools", "sports tipping". Race-betting terms used in the novelty check are dropped (race-only betting is not eligible; mixed samples are found through the sports terms).

| Source | Query form |
| --- | --- |
| OpenAlex | `title_and_abstract.search` with the phrase set, in chunks of 40 |
| PubMed | proximity pairs `"<sport term> <betting term>"[tiab:~2]` (6 × 10) and the single phrases in `[tiab]`; quoted phrases are not used, because PubMed silently drops phrases missing from its phrase index |
| Europe PMC | `TITLE_ABS:"…"` with the phrase set, in chunks of 40 |
| Semantic Scholar | bulk search with the phrase set |
| Crossref | relevance-sorted `query.bibliographic` queries, kept while title or abstract contains a sport term near a betting term |
| DataCite | phrase set |
| OpenAIRE, CORE | core phrases, one query per phrase where the API rejects OR lists |
| SciELO | `"apostas esportivas" OR "apostas desportivas" OR "apuestas deportivas" OR "sports betting"` |
| OpenAlex, non-English | apostas esportivas, apostas desportivas, apuestas deportivas, paris sportifs, Sportwetten, scommesse sportive, spor bahisleri, zakłady sportowe, ставки на спорт, спортивные ставки, 体育彩票, 体育博彩, 足球彩票, 竞猜型体育彩票, 스포츠 도박, 스포츠토토, スポーツベッティング, sportsspill, vadslagning and others |
| Google Scholar | `"sports betting" "problem gambling" prevalence`; `"sports bettors" PGSI OR SOGS` |

**Pilot (novelty check, 2026-10-18; `novelty/raw/fetch_log.json`).** Sports-betting records: OpenAlex 6,493, Semantic Scholar 4,419, Crossref 3,888, DataCite 2,162, non-English 977, Europe PMC 619, PubMed 595. About 6,500 unique records on topic, with several hundred spam deposits on Zenodo (bookmaker "reviews"). Records with both a problem-gambling instrument and prevalence wording in the abstract: about 620.

**Check run of the v1.0 code (2026-10-18; `search/runs/2026-10-18-check/`).**

| Source | Records |
| --- | --- |
| OpenAlex | 6,101 |
| Semantic Scholar | 4,106 |
| OpenAIRE | 3,766 |
| DataCite | 2,110 |
| Crossref | 1,811 |
| OpenAlex, non-English | 977 |
| Europe PMC | 589 |
| PubMed | 575 |
| Citation search of Tran et al. (2024) | 408 (137 references indexed in OpenAlex, 271 citing records) |
| **Total** | **20,443** |

- After de-duplication: 8,602 unique records; removed automatically: 272 non-study records and 602 Zenodo commercial deposits (rule 6, §11a); **7,728 to screen**, 359 of them only through the citation search of Tran et al. (2024) and 669 only through pointer sources (DataCite, OpenAIRE).
- About 1,080 of the 7,728 contain no gambling or betting term in title or abstract (fantasy-team optimisation, sports economics, "sports pools" in the swimming sense); they stay in the list for the AI passes and are left out of the safeguard re-screening (§11b).
- Recall on the seed set: **25 of 25**, including the five surveys of all gamblers, online gamblers or the population.
- CORE returned HTTP 500 and 504 errors and read timeouts for more than an hour on 2026-10-18 and was stopped; it is not part of the check run and runs in the final search. In the AI-dependence check run CORE added mostly records already found elsewhere.
- Stand test of the screener prompt (`screening/llm/stand_test_2026-10-18-check_*.jsonl`): 12 records chosen to cover each decision type (seed studies, a population survey, a treatment-seeking sample, a markets review, fantasy-team optimisation, a sports-lottery market paper, a regulation paper, a mixed sports-and-race sample, a record without abstract); both passes gave the expected label on all 12.

The final search runs with the v1.0 code after registration and before screening; dates, counts and software versions go to `search_log.json`. Raw exports are archived with the data release.

### [11] Study records

**[11a] Data management.** As in the misophonia review: git repository with dated commits; de-duplication on DOI (version suffixes ignored), PMID and normalised title with years within ±1 (`search/dedup.py`); pointer sources attached to the database record with the same title; records that every source types as a non-study record removed automatically and reported as "removed by automation tools". Added rule (6 in `search/dedup.py`), written after the check run found about 750 Zenodo deposits, most of them bookmaker advertising: Zenodo-only records are removed as commercial deposits when the title carries a bookmaker or casino brand, a promo code, bonus, app download, "complete guide", live-stream or listicle wording, when the uploader name is a site, a brand or a random token, or when one uploader has ten or more Zenodo-only records in the set. The removed records stay in `records_unique.jsonl` with the reason, and their number is reported as "removed by automation tools". Data and code are released on GitHub with a Zenodo DOI at submission.

**[11b] Selection process.**
- **Title and abstract: two AI passes, R1 decides every record that either pass keeps; double AI exclusions are audited by a blind calibration sample** (the scheme R1 chose for the AI-dependence review on 2026-10-16).
  1. **Blind calibration.** Before seeing any AI label, R1 screens a random sample of 400 records (`screening/calibration.py`: `random.Random(20261018).sample` over sorted record IDs, shown in the sampled order). Labels: include / unsure / exclude with a reason code. R1 sees title, abstract, year, venue, record type, language and DOI link; no author names. Decisions are committed before any AI label is shown.
  2. **AI draft, two passes.** Claude Opus 5.5 (`claude-opus-5-5`) and Claude Sonnet 5.5 (`claude-sonnet-5-5`), both at effort high, label every record independently with the same frozen prompt (`screening/llm_screener_prompt.md`): include / unsure / exclude, a reason code and a one-sentence note, "unsure" whenever in doubt — in particular when the abstract does not say whether problem gambling was measured. SHA-256 hashes of both label files are committed before unblinding.
  3. **Verification.** R1 reviews, with the AI labels visible, every record that at least one pass labelled include or unsure, and accepts or overrides the labels. R1's decision is final; include and unsure go to full text. Records labelled exclude by both passes are excluded without further human review; their list, with reason codes and notes, is part of the open data.
  4. **Safeguard.** If, in the calibration sample, a record that R1 labelled include or unsure was labelled exclude by both passes, R1 screens all double-excluded records outside the calibration sample with the AI labels hidden, in random order; every record R1 then marks include or unsure goes to full text. Double-excluded records whose title and abstract contain no gambling or betting term at all (`gambl*`, `bet`/`betting`/`bettor*`, `wager*`, `bookmaker*`, `sportsbook*`, `lotter*`, `casino*` and their equivalents in the non-English search terms) are left out of this re-screening, unless the abstract is missing: such a record cannot meet I1 and I3 (about 1,000 of the records in the check run, mostly fantasy-team optimisation, sports economics and sports medicine).
  - **Tool:** Markdown decision files from `screening/screen_md.py` (AI-dependence version, both AI labels shown), codes `+` include, `?` unsure, `-1`…`-7` exclude with a reason (1 review or commentary; 2 qualitative or not about people: markets, odds, prediction models; 3 no problem-gambling instrument; 4 no sports betting or race betting only; 5 sample selected for gambling problems; 6 not about gambling; 7 other, with a note), `=` to accept the AI label when both passes agree. Each file is committed blank before R1 starts and again when R1 finishes.
  - **Reported:** κ and Gwet's AC1 (Gwet, 2008) between R1 (blind) and each AI pass and their union; sensitivity and specificity with Clopper–Pearson 95% CIs; overrides by direction; whether the safeguard was triggered; how many included studies the AI had labelled exclude.
  - **Rationale:** single-reviewer screening misses about 13% of eligible studies (Waffenschmidt et al., 2019); LLM screeners reach high sensitivity on titles and abstracts (Oami et al., 2024). Two independent AI passes lower the chance of a missed record; the blind calibration measures the miss rate of the AI rule, and the safeguard returns the double exclusions to R1 if it misses even one calibration record.
- **Records from the citation search of Tran et al. (2024)** are screened like the others; the screener prompt keeps population gambling surveys with a problem-gambling instrument (reason `inc_population_survey`), because their activity tables may report sports bettors even when the abstract does not mention sports betting.
- **Full text.** Open-access versions only (Unpaywall, PMC, repositories, preprint servers, publishers' report pages); authors are not contacted. Non-English texts are machine-translated by the AI assistant (Jackson et al., 2019); R1 checks the numbers against the original tables. The AI drafts a proposal per report: eligible or not, the primary exclusion reason, and where the counts for sports bettors are (table, page, quote). R1 checks each proposal and decides. Reports without an open full text are listed as "reports not retrieved".
- **Linking reports.** Reports of one sample are linked and the sample is counted once. National surveys often appear as a government report and one or more articles; the report supplies the data when it has the sports-betting table. Overlap is judged from survey name, year, sample size and sites.
- **AI prompts after screening.** Full-text, extraction and risk-of-bias prompts are written before full-text screening, piloted on five studies, frozen with git tags and committed before use.

**[11c] Data collection process.**
- **Forms.** Two linked tables, as in the misophonia review: `forms/samples.csv` (one row per independent sample of sports bettors) and `forms/estimates.csv` (one row per case definition × sample × subgroup). Codebook: `forms/extraction_codebook.md`. Piloted on five studies.
- **AI draft.** The AI assistant pre-fills every field with its source location (table, page or quote); the draft is stored unchanged (`extraction/draft/`).
- **Verification.** R1 verifies every value against the source in Markdown files (`extraction/verify_md.py`, misophonia); key items (denominator of sports bettors, case counts at each level, instrument and cut-off, reference period of betting, sample type) are always checked against the source table. The share of AI values that R1 corrected and the share of AI quotes found verbatim in the source (`quote_check.py`) are reported.
- **Checks.** Cases ≤ n; cumulative levels consistent (L4 ≤ L3 ≤ L2 ≤ L1); category counts add up to the total; percentages match counts within rounding; retractions and expressions of concern checked through Crossref.

### [12] Data items

Per sample: report details; country; years of data collection; design; sampling method (probability, census, quota or online panel, operator or venue, convenience, snowball); sample type (bettor subsample of a representative survey / bettors recruited as such / university students / school pupils / athletes / other); whether gambling or betting was named in recruitment; reference period of sports betting; minimum betting frequency for entry; betting mode (online only, land-based only, both, not reported); in-play betting, daily fantasy sports, esports betting and sports lotteries (share or whole sample); n analysed; age (mean, SD, range); percentage male; survey mode (online, telephone, face-to-face, paper); for each instrument: name, version, language, validation in that language, time frame (past 12 months, lifetime); for every case definition: threshold, number of cases and denominator, overall and by sex; legal status of sports betting at the time of data collection (legal and regulated / legal state monopoly / not legal or unregulated); funding and gambling-industry funding.

### [13] Outcomes and prioritisation

**Outcome.** Proportion of sports bettors meeting a problem-gambling case definition (cases / N).

**Case-definition levels.** Fixed with the protocol and applied regardless of the label used by study authors. The full table with sources (`forms/instrument_thresholds.csv`) is completed for every instrument found in the included studies before extraction, using only development and validation papers; the completion is logged as a clarification, not a change of rule.

| Level | Definition | Examples |
| --- | --- | --- |
| L1 any risk | at least one problem-gambling symptom or consequence | PGSI ≥ 1; SOGS ≥ 1; DSM-based screens ≥ 1 criterion |
| L2 moderate risk or higher | the instrument's moderate-risk or at-risk category and above | PGSI ≥ 3 (Ferris & Wynne categories; Currie et al., 2013); SOGS ≥ 3; NODS or DSM-IV screens ≥ 3 ("problem" range); PPGM at-risk or higher (Williams & Volberg, 2014) |
| L3 problem gambling | the instrument's problem or probable pathological category | PGSI ≥ 8; SOGS ≥ 5 (Lesieur & Blume, 1987); DSM-IV-based ≥ 5; DSM-5-based ≥ 4; PPGM problem or pathological gambler; BBGS ≥ 1 (Gebauer et al., 2010) is coded L3-screen and tested in sensitivity analysis 3 |
| L4 diagnosed | gambling disorder by a clinician or a structured or semi-structured diagnostic interview applying DSM-5, DSM-IV or ICD criteria | — |

The current table with sources is `forms/instrument_thresholds.csv` (PGSI, SOGS, SOGS-RA, DSM-IV-MR-J, NODS, NODS-CLiP, DSM-IV and DSM-5 screens, PPGM, BBGS, Lie/Bet, interview, ad hoc items).

Levels are cumulative: a sample reporting PGSI categories contributes L1 (≥ 1), L2 (≥ 3) and L3 (≥ 8). Alternative PGSI cut-offs (for example, the revised thresholds 1–4 / 5–7 / 8+) are recorded and used in sensitivity analysis 4.

**Primary outcome.** Prevalence of problem gambling (L3 or L4) among sports bettors, all non-selected samples.

**Secondary outcomes:** prevalence at L1, L2 and L4 separately; prevalence by sample type; odds ratio for L3/L4 in males vs females.

**One estimate per sample for each analysis.**
- Primary outcome: the L4 estimate if the sample has one, else L3.
- Within a level, in this order: the instrument the authors designate as primary; otherwise the PGSI; otherwise the threshold recommended in the levels table; if several remain, the median logit prevalence (with an even number, the lower of the two middle values).
- Reference period: past-12-month bettors; otherwise the period reported (coded).
- Whole-sample estimates in all pooled analyses; subgroup estimates (by sex, betting mode, age band) only in the analyses that need them.

All estimates enter the multilevel moderator analysis (§15b).

### [14] Risk of bias in individual studies

JBI Critical Appraisal Checklist for Studies Reporting Prevalence Data, nine items (Munn et al., 2014, 2015), rated yes / no / unclear with decision rules adapted to sports betting (`forms/rob_jbi.md`):
- item 1 — sampling frame appropriate to the target population of sports bettors;
- item 2 — sampling: probability or census = yes (for bettor subsamples of representative surveys, the parent survey's sampling);
- item 3 — sample size against the precision for an expected prevalence of 10% ± 3 percentage points (n ≥ 385);
- item 6 — valid identification: validated instrument with a validated cut-off, or interview = yes;
- item 7 — standard measurement for all participants;
- item 9 — response rate ≥ 60%, or non-response handled.

The AI drafts each rating with a supporting quote; R1 verifies and decides. No summary score; items 2, 6 and 9 drive the sensitivity analyses.

### [15] Data synthesis

**[15a] Narrative synthesis.** Study characteristics by sample type, region and betting mode; an evidence map of instruments × cut-offs × levels; estimates excluded under E3 listed, not pooled.

**[15b] Meta-analysis.**
- **Primary model.** Random-effects binomial–normal generalised linear mixed model on the logit scale (`metafor::rma.glmm`, `measure = "PLO"`, ML), preferred over inverse-variance pooling of transformed proportions and over the Freeman–Tukey back-transformation (Stijnen et al., 2010; Schwarzer et al., 2019; Lin & Chu, 2020).
- **Reported:** pooled prevalence with 95% CI and 95% prediction interval (IntHout et al., 2016); τ² on the logit scale; I², interpreted through the prediction interval (Migliavaca et al., 2022).
- **Minimum data:** at least three independent samples per pooled estimate.
- **Subgroups:** case-definition level (L1–L4); sample type; age group (adolescents under 18 / adults); region (North America, Europe, Oceania, Latin America, sub-Saharan Africa, Asia, other).
- **Benchmark (descriptive):** the L3/L4 estimate from bettor subsamples of representative surveys set beside 8.9% (5.2–13.5) of Tran et al. (2024), with CIs; no formal test.
- **Moderator analysis using all estimates.** Three-level model (estimates in samples in studies): `lme4::glmer`, binomial likelihood, nested random intercepts; as a check, `metafor::rma.mv` on logits with cluster-robust inference (Van den Noortgate et al., 2013; Pustejovsky & Tipton, 2022).
  - Pre-specified multivariable model: case-definition level, sample type, probability sampling.
  - Exploratory moderators, one at a time, each only when k ≥ 10: instrument within L3; betting mode (online vs land-based only); share of in-play bettors; daily fantasy sports; esports betting; minimum betting frequency for entry; reference period of betting; region; legal status at data collection; US samples collected before vs after May 2018 and Brazilian samples collected before vs after Law 14.790/2023 (when k allows); year of data collection; mean age; percentage male; survey mode; gambling named in recruitment; JBI items 2, 6 and 9; publication status; industry funding.
  - If a variance component is estimated at zero, that level is dropped and the simpler model reported.
- **Sex difference.** Log odds ratio (male vs female) per sample; random-effects model, REML with Hartung–Knapp adjustment.

**[15c] Sensitivity analyses** (on the primary outcome):
1. only probability or census samples (JBI item 2 = yes);
2. only validated instruments with a validated cut-off (JBI item 6 = yes);
3. excluding BBGS and other brief screens coded L3-screen;
4. PGSI revised thresholds where category counts allow;
5. response rate ≥ 60% or not applicable;
6. excluding mixed sports-and-race or unclear sports-lottery samples;
7. excluding preprints, theses, conference abstracts and reports;
8. excluding samples with n < 100;
9. inverse-variance random-effects pooling of logits (REML, Hartung–Knapp) instead of the GLMM;
10. leave-one-out and influence diagnostics.

**[15d] If pooling is not appropriate** (fewer than three samples in a stratum), estimates are tabulated and shown in forest plots without a pooled value.

**Software.** R 4.6.1 with metafor, lme4 and clubSandwich; versions in `analysis/sessionInfo.txt`. Python 3.12 for search, de-duplication, decision files and the AI runner; Claude Code (headless) for AI drafts, with the version stored with every output. Windows 11.

### [16] Meta-biases

- Funnel-plot asymmetry tests are unreliable for proportions (Hunter et al., 2014) and are not used as inference; logit prevalence is plotted against its standard error, prevalence is regressed on 1/√n, and peer-reviewed estimates are compared with grey literature.
- Selective reporting within studies: case definitions announced in the methods compared with those reported.
- Gambling-industry funding is coded and tested as a moderator.

### [17] Confidence in cumulative evidence

GRADE adapted for event rates (Iorio et al., 2015), as in the misophonia review: risk of bias (share of weight from samples with "no" on JBI items 2, 6 or 9), inconsistency (prediction interval width), imprecision (CI half-width above 5 percentage points), indirectness (sample types far from the target population; few regions), publication bias. Summary-of-findings table.

---

## Load for the human reviewer (fixed in advance; one round)

Based on the check run of 2026-10-18 (7,728 records to screen); the final numbers are reported in the PRISMA flow diagram.

| Stage | Who | Approximate volume |
| --- | --- | --- |
| Title and abstract, blind calibration | R1 | 400 records |
| Title and abstract, verification | R1 | about 1,500–2,500 records that at least one AI pass kept. The other double AI exclusions are not reviewed unless the safeguard triggers; then R1 screens about 4,000–5,000 of them blind (those with a gambling term in title or abstract or without an abstract), one character per record |
| Full-text screening | R1 verifies an AI proposal | about 800–1,300 reports, each with the location of the sports-bettor counts |
| Instrument cut-offs | R1 verifies an AI draft | about 15–25 instruments, once each (levels table) |
| Data extraction | R1 verifies an AI draft | about 120–250 samples; per sample about 25 fields and 1–8 estimates, each with its source location |
| Risk of bias | R1 verifies an AI draft | 9 items per included study, each with a quote |

No author contacts. No further human coding rounds are planned. There is no second human reviewer, and double AI exclusions at the title-and-abstract stage are not reviewed by a human unless the safeguard triggers; these are limitations, partly offset by two independent AI passes, the blind calibration sample with a reported miss rate, R1's decision on every record kept and every full text, and verification of every extracted value.

---

## Changes from draft v0.1 (2026-10-18)

- Search code (`search/search.py`), de-duplication with rule 6 for Zenodo commercial deposits (`search/dedup.py`), recall script and the seed set of 25 studies (`search/recall.py`, `search/seed_set.csv`); check run on 2026-10-18 with recall 25 of 25 (§9, §10, §11a).
- Records from the citation search of Tran et al. (2024) are screened at title and abstract like the others, with an explicit eligible type for population gambling surveys, instead of going straight to full text (§11b).
- Screener prompt with two passes and a stand test (`screening/llm_screener_prompt.md`, `screening/llm_screen.py`); calibration seed 20261018; Markdown decision files with seven exclusion reasons (`screening/screen_md.py`) (§11b).
- Safeguard re-screening leaves out double exclusions without any gambling or betting term in title or abstract, unless the abstract is missing (§11b).
- Forms written: `forms/extraction_codebook.md`, `forms/instrument_thresholds.csv` (levels table with sources; L2 for DSM-5 screens provisional until the table is completed), `forms/rob_jbi.md` (§11c, §13, §14).
- Load table updated with the check-run numbers.

---

## References

- Currie, S. R., Hodgins, D. C., & Casey, D. M. (2013). Validity of the Problem Gambling Severity Index interpretive categories. *Journal of Gambling Studies, 29*(2), 311–327. https://doi.org/10.1007/s10899-012-9300-6
- Etuk, R., Xu, T., Abarbanel, B., Potenza, M. N., & Kraus, S. W. (2022). Sports betting around the world: A systematic review. *Journal of Behavioral Addictions, 11*(3), 689–715. https://doi.org/10.1556/2006.2022.00064
- Gebauer, L., LaBrie, R., & Shaffer, H. J. (2010). Optimizing DSM-IV-TR classification accuracy: A brief biosocial screen for detecting current gambling disorders among gamblers in the general household population. *The Canadian Journal of Psychiatry, 55*(2), 82–90. https://doi.org/10.1177/070674371005500204
- Gwet, K. L. (2008). Computing inter-rater reliability and its variance in the presence of high agreement. *British Journal of Mathematical and Statistical Psychology, 61*(1), 29–48. https://doi.org/10.1348/000711006X126600
- Haddaway, N. R., Collins, A. M., Coughlin, D., & Kirk, S. (2015). The role of Google Scholar in evidence reviews and its applicability to grey literature searching. *PLOS ONE, 10*(9), e0138237. https://doi.org/10.1371/journal.pone.0138237
- Hunter, J. P., Saratzis, A., Sutton, A. J., Boucher, R. H., Sayers, R. D., & Bown, M. J. (2014). In meta-analyses of proportion studies, funnel plots were found to be an inaccurate method of assessing publication bias. *Journal of Clinical Epidemiology, 67*(8), 897–903. https://doi.org/10.1016/j.jclinepi.2014.03.003
- IntHout, J., Ioannidis, J. P. A., Rovers, M. M., & Goeman, J. J. (2016). Plea for routinely presenting prediction intervals in meta-analysis. *BMJ Open, 6*(7), e010247. https://doi.org/10.1136/bmjopen-2015-010247
- Iorio, A., Spencer, F. A., Falavigna, M., Alba, C., Lang, E., Burnand, B., et al. (2015). Use of GRADE for assessment of evidence about prognosis: Rating confidence in estimates of event rates in broad categories of patients. *BMJ, 350*, h870. https://doi.org/10.1136/bmj.h870
- Jackson, J. L., Kuriyama, A., Anton, A., Choi, A., Fournier, J.-P., Geier, A.-K., et al. (2019). The accuracy of Google Translate for abstracting data from non–English-language trials for systematic reviews. *Annals of Internal Medicine, 171*(9), 677–679. https://doi.org/10.7326/M19-0891
- Lesieur, H. R., & Blume, S. B. (1987). The South Oaks Gambling Screen (SOGS): A new instrument for the identification of pathological gamblers. *American Journal of Psychiatry, 144*(9), 1184–1188. https://doi.org/10.1176/ajp.144.9.1184
- Lin, L., & Chu, H. (2020). Meta-analysis of proportions using generalized linear mixed models. *Epidemiology, 31*(5), 713–717. https://doi.org/10.1097/EDE.0000000000001232
- Mercier, J., Sévigny, S., Jacques, C., Goulet, A., Cantinotti, M., & Giroux, I. (2018). Sports bettors: A systematic review. *Journal of Gambling Issues, 38*. https://doi.org/10.4309/jgi.2018.38.11
- Migliavaca, C. B., Stein, C., Colpani, V., Barker, T. H., Ziegelmann, P. K., Munn, Z., Falavigna, M., & PERSyst. (2022). Meta-analysis of prevalence: I² statistic and how to deal with heterogeneity. *Research Synthesis Methods, 13*(3), 363–367. https://doi.org/10.1002/jrsm.1547
- Moher, D., Shamseer, L., Clarke, M., Ghersi, D., Liberati, A., Petticrew, M., Shekelle, P., Stewart, L. A., & PRISMA-P Group. (2015). Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015 statement. *Systematic Reviews, 4*, 1. https://doi.org/10.1186/2046-4053-4-1
- Munn, Z., Moola, S., Lisy, K., Riitano, D., & Tufanaru, C. (2015). Methodological guidance for systematic reviews of observational epidemiological studies reporting prevalence and cumulative incidence data. *International Journal of Evidence-Based Healthcare, 13*(3), 147–153. https://doi.org/10.1097/XEB.0000000000000054
- Munn, Z., Moola, S., Riitano, D., & Lisy, K. (2014). The development of a critical appraisal tool for use in systematic reviews addressing questions of prevalence. *International Journal of Health Policy and Management, 3*(3), 123–128. https://doi.org/10.15171/ijhpm.2014.71
- Oami, T., Okada, Y., & Nakada, T. (2024). Performance of a large language model in screening citations. *JAMA Network Open, 7*(7), e2420496. https://doi.org/10.1001/jamanetworkopen.2024.20496
- Pustejovsky, J. E., & Tipton, E. (2022). Meta-analysis with robust variance estimation: Expanding the range of working models. *Prevention Science, 23*(3), 425–438. https://doi.org/10.1007/s11121-021-01246-3
- Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., Ayala, A. P., Moher, D., Page, M. J., Koffel, J. B., & PRISMA-S Group. (2021). PRISMA-S: An extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. *Systematic Reviews, 10*, 39. https://doi.org/10.1186/s13643-020-01542-z
- Russell, A. M. T., Hing, N., & Browne, M. (2019). Risk factors for gambling problems specifically associated with sports betting. *Journal of Gambling Studies, 35*(4), 1211–1228. https://doi.org/10.1007/s10899-019-09848-x
- Schwarzer, G., Chemaitelly, H., Abu-Raddad, L. J., & Rücker, G. (2019). Seriously misleading results using inverse of Freeman-Tukey double arcsine transformation in meta-analysis of single proportions. *Research Synthesis Methods, 10*(3), 476–483. https://doi.org/10.1002/jrsm.1348
- Shamseer, L., Moher, D., Clarke, M., Ghersi, D., Liberati, A., Petticrew, M., Shekelle, P., Stewart, L. A., & PRISMA-P Group. (2015). Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015: Elaboration and explanation. *BMJ, 349*, g7647. https://doi.org/10.1136/bmj.g7647
- Snaychuk, L., Vieira, J., Picco, C., & Kim, H. S. (2026). Beyond the bet: An updated scoping review on sports gambling. *Canadian Journal of Addiction, 17*(3), 6–32. https://doi.org/10.1097/CXA.0000000000000278
- Stijnen, T., Hamza, T. H., & Özdemir, P. (2010). Random effects meta-analysis of event outcome in the framework of the generalized linear mixed model with applications in sparse data. *Statistics in Medicine, 29*(29), 3046–3067. https://doi.org/10.1002/sim.4040
- Tran, L. T., Wardle, H., Colledge-Frisby, S., Taylor, S., Lynch, M., Rehm, J., Volberg, R., Marionneau, V., Saxena, S., Bunn, C., Farrell, M., & Degenhardt, L. (2024). The prevalence of gambling and problematic gambling: A systematic review and meta-analysis. *The Lancet Public Health, 9*(8), e594–e613. https://doi.org/10.1016/S2468-2667(24)00126-9
- Valenciano-Mendoza, E., Mora-Maltas, B., Mestre-Bach, G., Munguía, L., Richard, J., Derevensky, J. L., Potenza, M. N., & Jiménez-Murcia, S. (2023). Clinical correlates of sports betting: A systematic review. *Journal of Gambling Studies, 39*(2), 579–624. https://doi.org/10.1007/s10899-023-10196-0
- van den Akker, O. R., Peters, G.-J. Y., Bakker, C. J., Carlsson, R., Coles, N. A., Corker, K. S., Feldman, G., Moreau, D., Nordström, T., Pickering, J. S., Riegelman, A., Topor, M. K., van Veggel, N., Yeung, S. K., Call, M., Mellor, D. T., & Pfeiffer, N. (2023). Increasing the transparency of systematic reviews: Presenting a generalized registration form. *Systematic Reviews, 12*, 170. https://doi.org/10.1186/s13643-023-02281-7
- Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., & Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect sizes. *Behavior Research Methods, 45*(2), 576–594. https://doi.org/10.3758/s13428-012-0261-6
- Waffenschmidt, S., Knelangen, M., Sieben, W., Bühn, S., & Pieper, D. (2019). Single screening versus conventional double screening for study selection in systematic reviews: A methodological systematic review. *BMC Medical Research Methodology, 19*, 132. https://doi.org/10.1186/s12874-019-0782-0
- Wardle, H., Degenhardt, L., Marionneau, V., Reith, G., Livingstone, C., Sparrow, M., Tran, L. T., Biggar, B., et al. (2024). The Lancet Public Health Commission on gambling. *The Lancet Public Health, 9*(11), e950–e994. https://doi.org/10.1016/S2468-2667(24)00167-1
- Williams, R. J., & Volberg, R. A. (2014). The classification accuracy of four problem gambling assessment instruments in population research. *International Gambling Studies, 14*(1), 15–28. https://doi.org/10.1080/14459795.2013.839731
- Winters, K. C., & Derevensky, J. L. (2019). A review of sports wagering: Prevalence, characteristics of sports bettors, and association with problem gambling. *Journal of Gambling Issues, 43*. https://doi.org/10.4309/jgi.2019.43.7
- Registrations cited: PROSPERO CRD42021251835 and CRD420261417334 (https://www.crd.york.ac.uk/PROSPERO/view/<number>).
