# Recreate: Reverse DCF Valuation Model — Roadmap

This document outlines a practical, phased workflow to recreate the repository from scratch. Follow the phases in order; each phase contains actionable steps, example commands (PowerShell), and verification hints.

**Prerequisites**
- Python 3.10+ installed
- Git installed and configured
- Optional: Docker if you plan to containerize

**Phase 1 — Initialize repository & environment**

- Create repo and virtual environment

```powershell
git init reverse-dcf-valuation-model
cd reverse-dcf-valuation-model
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
```

- Add minimal files: `README.md`, `LICENSE`, `.gitignore`, `pyproject.toml` or `requirements.txt`.

Verification: run `python -V` and `pip list`.

**Phase 2 — Project skeleton**

- Create directories and placeholder files

```powershell
mkdir src app data\raw data\processed data\sample_inputs notebooks reports\figures tests scripts
echo "" > data\raw\.gitkeep
echo "" > data\processed\.gitkeep
```

- Add package skeleton under `src/reversedcf` with `__init__.py` and module placeholders: `data.py`, `financials.py`, `dcf.py`, `reverse.py`, `scenarios.py`, `sensitivity.py`, `metrics.py`, `plotting.py`, `report.py`, `cli.py`.

Verification: import package locally with `python -c "import src.reversedcf"` after adjusting `PYTHONPATH` or installing editable.

**Phase 3 — Implement core modules (Minimal MVP)**

- Implement basic I/O (`data.py`) and core calculations (`dcf.py`, `financials.py`). Keep functions small and covered by unit tests.
- Add a simple `reverse.py` solver that inverts DCF inputs for a target price or implied growth.

Suggested development order:
- `data.py` → load/save JSON inputs and canonicalize sample inputs
- `financials.py` → helper transforms (growth rates, margins)
- `dcf.py` → forward DCF valuation function
- `reverse.py` → root-finding wrapper using `scipy.optimize` or `numpy`

Verification: add small unit tests in `tests/` and run `pytest`.

**Phase 4 — CLI, scripts and Streamlit app**

- Add `src/reversedcf/cli.py` exposing key actions (compute, reverse, report).
- Add `app/streamlit_app.py` that imports `src.reversedcf` functions and provides interactive controls.
- Add runnable scripts in `scripts/` for example case studies (`run_aapl_case_study.py`, `run_msft_case_study.py`, `generate_report.py`).

Verification: run `python -m src.reversedcf.cli --help` and `streamlit run app/streamlit_app.py`.

**Phase 5 — Data, reports, and figures**

- Add `data/sample_inputs/*.json` examples (AAPL, MSFT).
- Create `notebooks/` with example workflows (basic DCF, reverse solver, case study).
- Add `reports/` templates and `reports/figures/` placeholder images (or generate via `plotting.py`).

Verification: run notebooks or scripts and confirm example outputs replicate expected plots/reports.

**Phase 6 — Tests, CI and quality tooling**

- Add unit tests in `tests/` covering each module and edge cases.
- Add `pyproject.toml` or `requirements.txt` with pinned deps.
- Add `pre-commit` with hooks (black/ruff/isort) and a GitHub Actions workflow to run tests on push/PR.

Example `pytest` command:
```powershell
pytest -q
```

Verification: Push to remote and confirm Actions run (or run tests locally).

**Phase 7 — Packaging, docs, and release**

- Finalize `pyproject.toml` for packaging or `setup.cfg` and `setup.py` if needed.
- Write `README.md` usage examples and usage badges.
- Optionally add a `Dockerfile` for reproducible runs and a small `Makefile` or `invoke` tasks.

Verification: Build sdist/wheel and run in a clean venv, or build Docker image and run example.

**Phase 8 — Polish and extras**

- Add additional features: sensitivity analysis CLI, extended plotting, more sample reports.
- Improve test coverage and add benchmark examples.

---

Checklist (quick):
- [ ] Repo init & venv
- [ ] Skeleton + placeholders
- [ ] Core modules implemented
- [ ] CLI + Streamlit app
- [ ] Sample data + notebooks
- [ ] Tests + CI
- [ ] Packaging + docs

If you'd like, I can now scaffold the repo structure and create the placeholder files (Phase 1–2). Reply with which phases to scaffold automatically.
