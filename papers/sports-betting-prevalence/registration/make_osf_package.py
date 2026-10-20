"""Build the OSF registration package for protocol v1.0 -> registration/osf_package/ (git-ignored).

    .venv/Scripts/python.exe papers/sports-betting-prevalence/registration/make_osf_package.py

Output:
  Rekhert_sports_betting_protocol_v1.0.pdf   the protocol (pandoc -> docx -> LibreOffice -> PDF)
  sports-betting-prereg-v1.0.zip          protocol, forms, search and screening code, AI screener prompt, logs,
                                         README and SHA-256 manifest, in the repository's folder layout
  llm_screener_prompt.md, extraction_codebook.md   loose copies for the two file fields of the OSF form
Files are taken from the commit tagged sports-betting-prereg-v1.0 (git show), so the package matches the tag byte for byte.
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
ROOT = PAPER.parents[1]
sys.path.insert(0, str(ROOT / "harness"))
from llmaudit.msbuild import make_reference_docx, to_docx  # noqa: E402

OUT = HERE / "osf_package"
TAG = "sports-betting-prereg-v1.0"
P = "papers/sports-betting-prevalence/"
RUN = P + "search/runs/2026-10-18-check/"
FILES = [
    P + "protocol.md",
    P + "deviations.md",
    P + "forms/extraction_codebook.md",
    P + "forms/instrument_thresholds.csv",
    P + "forms/rob_jbi.md",
    P + "novelty/novelty.md",
    P + "search/search.py",
    P + "search/dedup.py",
    P + "search/recall.py",
    P + "search/seed_set.csv",
    RUN + "README.md",
    RUN + "search_log.json",
    RUN + "dedup_report.json",
    RUN + "recall_seed_set.json",
    P + "screening/llm_screener_prompt.md",
    P + "screening/llm_screen.py",
    P + "screening/calibration.py",
    P + "screening/screen_md.py",
    P + "screening/llm/stand_test_2026-10-18-check_opus.jsonl",
    P + "screening/llm/stand_test_2026-10-18-check_sonnet.jsonl",
    "harness/llmaudit/__init__.py",
    "harness/llmaudit/env.py",
    "harness/llmaudit/judge.py",
]

README = """# Prevalence of problem gambling among sports bettors: registration package (protocol v1.0)

Martin Rekhert, Turan University, Almaty, Kazakhstan. ORCID 0009-0001-2402-2031. mrexert@gmail.com

Protocol v1.0 frozen before the final search and before any screening.
Git tag `{tag}`, commit `{commit}`.

## Contents

- `Rekhert_sports_betting_protocol_v1.0.pdf` (outside the zip) and `papers/sports-betting-prevalence/protocol.md`: the protocol (PRISMA-P 2015).
- `papers/sports-betting-prevalence/forms/`: extraction codebook (two linked tables), instrument-threshold table (case-definition levels L1–L4), risk-of-bias rules (JBI checklist for prevalence studies).
- `papers/sports-betting-prevalence/novelty/novelty.md`: the novelty check (competing reviews and registrations, 2026-10-18).
- `papers/sports-betting-prevalence/search/`:
  - `search.py`: automated searches (PubMed, Europe PMC, OpenAlex incl. non-English terms, Semantic Scholar, Crossref, DataCite, OpenAIRE, CORE, citation search of Tran et al. 2024);
  - `dedup.py`: de-duplication, removal of non-study records and of Zenodo commercial deposits, and the screening list;
  - `recall.py` and `seed_set.csv`: recall on the seed set (25 studies from the references of Etuk et al., 2022, and Valenciano-Mendoza et al., 2023);
  - `runs/2026-10-18-check/`: check run of the v1.0 search code: log, de-duplication report, recall.
- `papers/sports-betting-prevalence/screening/`:
  - `llm_screener_prompt.md`: the AI screener's prompt and JSON schema, frozen with the protocol;
  - `llm_screen.py`: its runner (two passes: Claude Opus 5.5 and Claude Sonnet 5.5);
  - `calibration.py`: draws the blind calibration sample (400 records, seed 20261018);
  - `screen_md.py`: the Markdown decision files;
  - `llm/stand_test_2026-10-18-check_*.jsonl`: stand test of the prompt on chosen records with both passes.
- `harness/llmaudit/`: the headless Claude Code runner used by `llm_screen.py`.
- `papers/sports-betting-prevalence/deviations.md`: log of changes after registration (empty at registration).
- `MANIFEST.sha256`: SHA-256 of every file in this package.

## Reproducing

Python 3.12 with httpx and lxml; Claude Code CLI for the AI screener. Keys go into `.env` at the repository root: `OPENALEX_API_KEY`, `CORE_API_KEY`, `CLAUDE_CODE_OAUTH_TOKEN`.

    python papers/sports-betting-prevalence/search/search.py --date YYYY-MM-DD
    python papers/sports-betting-prevalence/search/dedup.py --date YYYY-MM-DD
    python papers/sports-betting-prevalence/search/recall.py --date YYYY-MM-DD
    python papers/sports-betting-prevalence/screening/calibration.py --run YYYY-MM-DD
    python papers/sports-betting-prevalence/screening/llm_screen.py --run YYYY-MM-DD --pass opus
    python papers/sports-betting-prevalence/screening/llm_screen.py --run YYYY-MM-DD --pass sonnet

Raw search exports are not included: the databases change, so a re-run reproduces the procedure, not the exact records. The raw exports of the final search will be archived with the data release.
"""


def blob(path: str, rev: str | None) -> bytes:
    """File content as committed at rev (byte-identical to the tag), or from the working tree without a tag."""
    if rev:
        return subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True, check=True).stdout
    return (ROOT / path).read_bytes()


def protocol_pdf(rev: str | None) -> Path:
    ref = make_reference_docx(OUT / "_reference.docx", double=False)
    md = blob(P + "protocol.md", rev).decode("utf-8")
    docx = to_docx(md, OUT / "protocol_v1.0.docx", ref, PAPER)
    soffice = Path(r"C:\Program Files\LibreOffice\program\soffice.exe")
    subprocess.run([str(soffice), "--headless", "--convert-to", "pdf", "--outdir", str(OUT), str(docx)],
                   check=True, capture_output=True)
    pdf = OUT / "Rekhert_sports_betting_protocol_v1.0.pdf"
    (OUT / "protocol_v1.0.pdf").replace(pdf)
    for tmp in (docx, ref):
        tmp.unlink()
    return pdf


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    tagged = subprocess.run(["git", "rev-list", "-n", "1", TAG], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(["git", "status", "--porcelain", "--"] + FILES, cwd=ROOT, capture_output=True, text=True).stdout.strip()
    rev = tagged or None
    if not tagged:
        print(f"WARNING: no tag {TAG}; packing the working tree (draft only)", file=sys.stderr)
    elif tagged != commit or dirty:
        print(f"note: HEAD {commit[:10]} differs from the tag {tagged[:10]}; packing the tagged files", file=sys.stderr)
    pdf = protocol_pdf(rev)
    readme = README.format(tag=TAG, commit=tagged or commit + " (working tree, untagged)")
    files = {f: blob(f, rev) for f in FILES}
    manifest = [f"{hashlib.sha256(b).hexdigest()}  {f}" for f, b in files.items()]
    manifest.append(f"{hashlib.sha256(readme.encode('utf-8')).hexdigest()}  README.md")
    with zipfile.ZipFile(OUT / f"{TAG}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("README.md", readme)
        for f, b in files.items():
            z.writestr(f, b)
        z.writestr("MANIFEST.sha256", "\n".join(manifest) + "\n")
    for f in (P + "screening/llm_screener_prompt.md", P + "forms/extraction_codebook.md"):
        (OUT / Path(f).name).write_bytes(files[f])
    print(f"{OUT}:")
    for p in sorted(OUT.iterdir()):
        print(f"  {p.name}  {p.stat().st_size:,} bytes")
    print(f"zip sha256: {hashlib.sha256((OUT / f'{TAG}.zip').read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
