**Supplementary File S4.** Use of AI tools

All model calls went through headless Claude Code (`claude -p`, no tools, empty working directory, default sampling parameters) with a fixed system prompt and a JSON schema; the system prompt hash, the schema hash, the Claude Code version and the model are stored with every output (`harness/llmaudit/judge.py`).

| Task | Model, effort | Prompt | Outputs (unique records) | Claude Code | System prompt SHA | Run (UTC) |
| --- | --- | --- | --- | --- | --- | --- |
| Title and abstract, pass 1 | Claude Opus 5.5, high | `screening/llm_screener_prompt.md` | 10,477 (7,728) | 2.1.289 (Claude Code) | 0e9f1010b03c7efc | 2026-10-18T11:40 – 2026-10-19T07:00 |
| Title and abstract, pass 2 | Claude Sonnet 5.5, high | `screening/llm_screener_prompt.md` | 10,902 (7,728) | 2.1.289 (Claude Code) | 0e9f1010b03c7efc | 2026-10-18T11:40 – 2026-10-19T06:52 |
| Extraction and JBI drafts | Claude Opus 5.5, high | `extraction/extract_prompt.md` v1.0 | 53 (53) | 2.1.289 (Claude Code) | 739fd562bf972785 | 2026-10-19T17:35 – 2026-10-20T06:10 |

Title-and-abstract passes produced duplicate labels for some records because orphaned runners kept running after a session restart; the earliest label per record was used (D4). The label files were sealed with SHA-256 hashes before the calibration was unblinded (Opus 1826d76d269151ad…, Sonnet 064887ac8e96152d…).

**Blind calibration** (400 random records, decided by the author before the AI labels were shown): rule "exclude only if both passes exclude" — sensitivity 0.85 (51/60), specificity 0.94 (320/340), κ 0.74, AC1 0.90; agreement between passes κ 0.86. Opus alone: sensitivity 0.83, specificity 0.96; Sonnet alone: 0.78 and 0.95. Safeguard triggered (D5, D6).

**Full texts:** screened by the author without AI proposals (D7); the fixed full-text prompt (`fulltext/ft_prompt.md`, tag `sports-betting-ft-prompt-v1.0`) was used only in a five-report pilot.

**Extraction:** 58 samples verified by the author; 9 of 6,419 drafted values corrected (0.14%); key values 8 of 1,697 (0.47%). AI quotations found verbatim in the source: 92% of estimates and 96% of key fields (`extraction/quote_check.py`).

**Code and text:** Claude Code wrote the search, screening, extraction, analysis and table code and an outline of the manuscript (facts and numbers per section). The author wrote the text.
