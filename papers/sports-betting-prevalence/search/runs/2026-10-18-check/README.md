# Check run of the v1.0 search code (2026-10-18)

Before registration: does the code run on every source, how many records reach screening, and does it find the seed set?

- `search_log.json` — query strings, record counts and times per source. All sources ran in one pass, except the citation search of Tran et al. (2024), which ran separately the same day with the same code while CORE was still running (its raw file was copied into this run). CORE returned HTTP 500 and 504 errors and read timeouts for more than an hour and was stopped; it is not part of this run and runs again in the final search.
- `dedup_report.json` — 20,443 records, 8,602 unique; removed automatically: 272 non-study records and 602 Zenodo commercial deposits (rule 6 of `dedup.py`, written after this run showed about 750 Zenodo deposits, most of them bookmaker advertising); 7,728 to screen.
- `recall_seed_set.json` — 25 of the 25 seed studies (protocol §9).
- Stand test of the screener prompt on 12 records of this list: `screening/llm/stand_test_2026-10-18-check_opus.jsonl` and `..._sonnet.jsonl`; both passes gave the expected label on all 12.
- Raw exports, `records_unique.jsonl` and `screening.csv` are not committed (git-ignored): the final search is run again after registration.
