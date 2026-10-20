# Data extraction codebook (draft for v1.0)

Two linked tables, as in the misophonia review. `samples.csv` has one row per independent sample of sports bettors. `estimates.csv` has one row per case definition × sample × subgroup (all, male, female, age band, betting mode). Unknown = `NR` (not reported); not applicable = `NA`.

**Procedure (protocol §11c).**
- The AI assistant pre-fills every field of both tables from the full text. For every value it gives the source location (page, table or figure) and a short quote. The draft is stored unchanged in `extraction/draft/`.
- R1 verifies every field against the source in Markdown files (`extraction/verify_md.py`, from the misophonia review) and accepts or corrects it. The verified values go to `samples.csv` and `estimates.csv`.
- Fields marked **[K]** are key fields. R1 always checks them against the source table or text, never accepts them from the draft unseen.
- The share of AI-drafted values that R1 corrected is computed by comparing the stored draft with the verified tables, overall and for the [K] fields; the share of AI quotes found verbatim in the source is reported too.
- The form is piloted on five studies before use. Any rule added in the pilot goes to `deviations.md` with a date.

## samples.csv

| Field | Rule |
| --- | --- |
| `sample_id` | `S###`; one per independent sample of sports bettors. A survey reporting adults and adolescents separately gets two IDs |
| `study_id` | `ST###`; links multiple samples and reports |
| `report_ids` | `rec_id`s of all reports of this sample (report, article, preprint, thesis), `;`-separated; the first one supplies data |
| `first_author`, `year`, `doi` | of the main report |
| `pub_status` | journal / preprint / thesis / conference / report / other |
| `language` | language of the full text |
| `country` | ISO 3166 alpha-3; multi-country samples: `MULTI` + list in `notes` |
| `us_state`, `subnational` | region if the sample is subnational (US state, Canadian province, Australian state, Brazilian state) |
| `region` | North America / Europe / Oceania / Latin America and Caribbean / sub-Saharan Africa / Asia / Middle East and North Africa (filled from country) |
| `income_group` | World Bank group of the country in the year of data collection (filled automatically) |
| `data_years` | years of data collection, e.g. `2021-2022`; `NR` if not stated |
| `design` | cross-sectional / cohort baseline / prevalence survey / validation study / screening phase of another study / other |
| `sample_type` **[K]** | rep_survey_subsample (sports bettors within a probability or census survey of a population) / bettor_recruited (bettors recruited as such: panels, operator customers, venues, social media) / students (university) / school_pupils / athletes / other (state which) |
| `parent_population` | for rep_survey_subsample: the population the survey describes (adults 18+, 16–64, 15+…) |
| `sampling` **[K]** | probability / census / quota or stratified non-random online panel / operator customer sample / venue intercept / convenience / snowball / NR |
| `gambling_disclosed` | yes = invitation or survey title named gambling or betting; no = general health or lifestyle survey; NR |
| `betting_period` **[K]** | reference period for being a sports bettor: past 12 months / past 30 days or month / past week / lifetime / current (not specified) / NR |
| `min_frequency` | minimum betting frequency for entry, as stated (e.g., `at least monthly`); `none` if any bettor in the period counts |
| `betting_mode` | online only / land-based only / both / NR — share online if reported (`pct_online`) |
| `pct_inplay`, `pct_dfs`, `pct_esports` | shares of in-play bettors, daily fantasy sports players, esports bettors, if reported; `all` if the whole sample is defined by it |
| `sports_lottery` | yes (quiz-type sports lottery on match outcomes) / unclear type / no |
| `mixed_race` | yes = the sample is defined as "sports or race betting" together; no |
| `legal_status` | regulated legal market / state monopoly / not legal or unregulated / mixed / NR — at the time and place of data collection, as described by the authors or by the country's law (source in `notes`) |
| `n_invited`, `n_responded` | integers if reported |
| `n_bettors` **[K]** | number of sports bettors analysed = denominator of the main estimate |
| `response_rate` | as reported, or n_responded / n_invited |
| `age_mean`, `age_sd`, `age_min`, `age_max` | years, of the sports bettors if reported, else of the whole sample (say which in `notes`) |
| `age_group` | adolescents (<18) / adults (18+) / mixed |
| `pct_male` | 0–100 |
| `mode` | online / telephone / face-to-face / paper / mixed |
| `weights` | yes = estimates weighted to the population; no |
| `instruments` | all problem-gambling instruments used, `;`-separated, with language version |
| `instrument_validated_in_language` | yes / no / NR, for the instrument of the main estimate |
| `industry_funding` | yes (gambling operator or industry body) / no / NR |
| `funding_coi` | short text |
| `jbi_1` … `jbi_9` | yes / no / unclear / NA (see `rob_jbi.md`) |
| `jbi_notes` | one line per item rated no or unclear |
| `notes` | anything else |

## estimates.csv

| Field | Rule |
| --- | --- |
| `estimate_id` | `E####` |
| `sample_id` | link |
| `subgroup` | all / male / female / age band (e.g., `18-24`) / online / land-based / in-play / DFS / esports |
| `instrument` **[K]** | short name as in `instrument_thresholds.csv` (PGSI, CPGI, SOGS, SOGS-RA, NODS, NODS-CLiP, NODS-PERC, DSM-IV-MR-J, DSM-IV-screen, DSM-5-screen, Stinchfield, PPGM, BBGS, Lie-Bet, PGSI-short, GD-screen, interview, adhoc, other) |
| `threshold` **[K]** | exactly as applied, e.g. `PGSI>=8`, `SOGS>=5`, `DSM-5 criteria>=4`, `interview: SCID-5` |
| `threshold_source` | standard (instrument developers) / validation paper / study's own / percentile of this sample (→ E3, not pooled) |
| `author_label` | authors' wording, e.g. "problem gambler", "moderate risk", "probable pathological" |
| `level` **[K]** | L1 / L2 / L3 / L3-screen / L4 by the levels table of the protocol (`instrument_thresholds.csv`), whatever the authors' label |
| `cumulative` | yes = "this category and above" (e.g., PGSI ≥ 3); no = a single category (e.g., PGSI 3–7). Single categories are summed into cumulative levels at analysis |
| `time_frame` | time frame of the instrument: past 12 months / past 3 months / lifetime / NR |
| `cases` **[K]** | integer; if only a % is given: round(% × n / 100), and `derived = yes` |
| `n` **[K]** | denominator for this estimate (sports bettors) |
| `derived` | yes / no |
| `weighted_pct` | weighted prevalence if the study reports one |
| `primary_for_authors` | yes, if the authors call this their main estimate |
| `location` | page, table or figure where the numbers are |
| `notes` | |

## Extraction rules

- **Sports bettors as a subgroup.** When a survey reports problem gambling by gambling activity, the sports-betting row is the estimate; the denominator is the number of respondents who bet on sports in the period. If only a % among sports bettors and the % of sports bettors in the whole sample are given, derive both counts and mark `derived = yes`.
- **PGSI categories.** Extract every category reported (0, 1–2, 3–7, 8+). Cumulative levels are built at analysis: L1 = 1+, L2 = 3+, L3 = 8+.
- **"Sports or race betting"** combined: extract, set `mixed_race = yes` (sensitivity analysis 6). Race betting alone: not eligible.
- If the counts in the text and a table disagree, take the table and note it.
- **Weighted estimates:** pool the raw counts; record the weighted % separately. If only weighted % and the unweighted n are given, derive cases from the weighted % and note it.
- **Waves of one panel:** the first wave enters; later waves are noted only.
- **Overlap:** national surveys reported both as a government report and as articles — one sample; the report supplies the data if it has the sports-betting table.
- Any rule added during the five-study pilot goes to `deviations.md` with a date.
