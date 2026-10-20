# Problem gambling among people who bet on sports: data and code

This repository contains the records, decisions, extracted data and analysis code for

> Rekhert, M. (2026). *Problem gambling among people who bet on sports: A systematic review and meta-analysis of prevalence across case definitions and sample types* [Manuscript submitted for publication]. Preprint: https://doi.org/10.5281/zenodo.23493615

- Protocol (OSF Registries, registered 18 October 2026 before screening): https://doi.org/10.17605/OSF.IO/6GQ48
- Archived release (Zenodo): https://doi.org/10.5281/zenodo.23493579
- Author: Martin Rekhert, Higher School of Psychology, Turan University, Almaty, Kazakhstan (ORCID [0009-0001-2402-2031](https://orcid.org/0009-0001-2402-2031))

## The review in brief

- **Question.** What proportion of people who bet on sports meet problem-gambling case definitions at each level — any risk (L1, e.g., PGSI ≥ 1), moderate risk or higher (L2, PGSI ≥ 3), problem gambling (L3, PGSI ≥ 8), diagnosis by interview (L4) — and how does it vary by sample type, region, age and betting characteristics?
- **Search.** 18 October 2026: PubMed, Europe PMC, OpenAlex (also non-English phrases), Semantic Scholar, Crossref, DataCite, OpenAIRE and the citation network of Tran et al. (2024); no date or language limits; 20,442 records, 7,728 screened. CORE was planned but its API failed (deviation D2).
- **Selection.** One reviewer (the author) decided every record kept by the AI and every full text. Two AI passes (Claude Opus 5.5 and Claude Sonnet 5.5 through Claude Code 2.1.289, fixed prompt, no tools) labelled titles and abstracts; a blind calibration of 400 records triggered the safeguard, narrowed after calibration to targeted blind re-screening plus a random audit (D6). Full texts (open access only, 488 of 1,824 retrieved) were screened by the reviewer without AI proposals (D7). The AI drafted the extraction and risk-of-bias forms; the reviewer verified every value.
- **Included.** 56 reports, 53 studies, 58 samples; 46 samples (about 30,000 sports bettors) in the meta-analyses.
- **Analysis.** Binomial–normal GLMMs on the logit scale (`metafor`), three-level binomial GLMMs (`lme4`) with a cluster-robust check (`clubSandwich`), GRADE for event rates.
- **Main results.** Any risk 74.2%, moderate risk or higher 46.7%, problem gambling 23.6% (95% CI 18.7–29.4; 42 samples); 15.8% among bettors in representative surveys and 25.7% among bettors recruited as such; Europe 14.1%, Oceania 31.3%, sub-Saharan Africa 42.0%; very low certainty of evidence.

## Repository layout

All study files are under `papers/sports-betting-prevalence/`.

| Path | Contents |
| --- | --- |
| `protocol.md` | Protocol v1.0 (frozen 18 October 2026, git tag `sports-betting-prereg-v1.0` in the working repository; registered on OSF) |
| `deviations.md` | Every change and clarification after registration, dated (D1–D9, C1–C2; Supplementary File S3) |
| `registration/` | The OSF registration form text and the script that built the registration package |
| `search/` | Search, de-duplication and recall scripts; `runs/2026-10-18/`: search log with every query, raw exports (zip), unique records, screening list (CSV, RIS), recall on the seed set |
| `screening/` | AI screening prompt and runner, both AI passes with the SHA-256 of the label files, blind calibration, safeguard re-screening and audit, verification worksheets and final decisions (`decisions/tiab_final.csv`) |
| `fulltext/` | Retrieval scripts and log (open access only), the reviewer's full-text worksheets and decisions (`decisions/ft_R1.csv`), PRISMA counts; the full-text prompt was used only in a five-report pilot |
| `extraction/` | Study map (reports → studies), extraction prompt and runner, AI drafts (`draft/`), the reviewer's verification worksheets (`verify/`) and verified values (`decisions/`), quote and correction audits, `finalize.py` |
| `forms/` | Extraction codebook, levels table (`instrument_thresholds.csv`), risk-of-bias rules, and the analysis tables `samples.csv` and `estimates.csv` |
| `analysis/` | `build_levels.py` (cumulative levels from the extracted categories), `analysis.R` (all analyses), `prisma.R`, `country_lookup.py`; `data/`, `results/` and `figures/` as reported |
| `manuscript/` | Scripts for Tables 1–4 (`make_tables.py` → `tables.md`) and Supplementary Files S1–S9 (`make_supplement.py` → `supplement/`) |
| `harness/` | `llmaudit`: the Claude Code runner used for the AI drafts, agreement statistics (κ, AC1) |

Reviewer worksheets (`*.md` under `screening/`, `fulltext/decisions/`, `extraction/verify/`) have instructions in Russian, the reviewer's working language; records, AI drafts and decisions are in English, and every decision is also in a CSV file.

Not included: full texts and PDFs of the reports (copyright), API keys.

## Reproducing the analysis

The analysis runs from the released files and needs no API access. Tested with Python 3.12 and R 4.6.1 (metafor, lme4, clubSandwich, dplyr, readr, ggplot2, scales, jsonlite).

```bash
# verified extraction -> analysis tables (forms/samples.csv, forms/estimates.csv)
python papers/sports-betting-prevalence/extraction/finalize.py --run 2026-10-18 --draft extract_2026-10-19
# cumulative levels from the extracted categories
python papers/sports-betting-prevalence/analysis/build_levels.py
# meta-analysis -> analysis/results/, analysis/figures/
Rscript papers/sports-betting-prevalence/analysis/analysis.R
Rscript papers/sports-betting-prevalence/analysis/prisma.R
# Tables 1-4 and Supplementary Files S1-S9
python papers/sports-betting-prevalence/manuscript/make_tables.py
python papers/sports-betting-prevalence/manuscript/make_supplement.py
```

Run the commands from the repository root. The release was checked by running them in a clean copy: the analysis tables, the level estimates, all result files, Tables 1–4 and Supplementary Files S1–S9 came out identical (line endings aside).

Re-running the search, retrieval or the AI drafts needs network access and keys (`.env.example`): `OPENALEX_API_KEY` for the search, and `CLAUDE_CODE_OAUTH_TOKEN` (output of `claude setup-token`) for the Claude Code runs. Python packages for those steps: `httpx`, `lxml`, `pyyaml`, `jsonschema`, `pymupdf` (`pip install -e harness`).

## Licenses and citation

Code (`*.py`, `*.R`, `harness/`): MIT (`LICENSE`). Data and documents: CC BY 4.0 (`LICENSE-DATA.md`); bibliographic records, abstracts and quotations from the included reports remain with their copyright holders. Please cite the article and this repository (`CITATION.cff`).
