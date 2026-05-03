# AGENTS.md

Operational guide for coding agents in this repository.

## Scope and Current Layout

- Project focus: mortality analysis in Guatemala (2013-2022).
- Primary implementation: `main.ipynb` (notebook-centric workflow).
- Input data:
  - `data/defunciones/*.sav`
  - `data/variables/definicion.xlsx` (sheet: `CIE-10`)
- Documentation:
  - `README.md`
  - `contexto_proyecto.md`
  - `diccionario.md`
- `src/` exists but is currently empty.

## Cursor/Copilot Rules Status

Checked locations:

- `.cursorrules`
- `.cursor/rules/`
- `.github/copilot-instructions.md`

Result at generation time: none of the above files were found.

If these files appear later:

- Treat them as mandatory constraints.
- Keep this file updated with a short summary of those rules.

## Environment Setup

No formal Python project metadata was found (`pyproject.toml`, `requirements*.txt`, `setup.cfg`, `tox.ini`, `pytest.ini` absent).

Recommended setup (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pandas pyreadstat numpy matplotlib seaborn scipy scikit-learn openpyxl jupyter nbconvert pytest ruff black mypy
```

## Build / Validation Commands

Interpret "build" in this repository as reproducible execution checks.

- Execute notebook end-to-end:
  - `jupyter nbconvert --to notebook --execute main.ipynb --output main.executed.ipynb`
- Validate Python syntax for future extracted modules:
  - `python -m compileall src`
- Check installed dependency consistency:
  - `python -m pip check`

## Lint and Formatting Commands

Use these for `.py` files (especially after logic is moved from notebook to `src/`).

- Format code:
  - `black src`
- Lint code:
  - `ruff check src`
- Type check (best effort):
  - `mypy src`

If only notebook cells changed, at minimum run notebook execution smoke check.

## Test Commands

Current status:

- No test files were found in repository code.

Standard commands to adopt when tests are added:

- Run full suite:
  - `pytest -q`
- Run one test file:
  - `pytest tests/test_pipeline.py -q`
- Run a single test (most important for agents):
  - `pytest tests/test_pipeline.py::test_merge_cie10_mapping -q`
- Run by keyword:
  - `pytest -k "cie10 and merge" -q`

Notebook regression alternative:

- `jupyter nbconvert --to notebook --execute main.ipynb --output smoke.ipynb`

## Coding Standards

These standards are inferred from repository context and should be used for all new code.

### Imports

- Order imports by groups:
  1. Standard library
  2. Third-party
  3. Local modules
- Avoid wildcard imports.
- Keep established aliases where applicable:
  - `pandas as pd`
  - `numpy as np`
  - `matplotlib.pyplot as plt`
  - `seaborn as sns`

### Formatting

- Follow PEP 8 and Black defaults.
- Use 4-space indentation.
- Keep lines near 88 characters.
- Prefer trailing commas in multiline structures.
- Keep notebook cells focused on one logical step.

### Types

- Add type hints to public functions in `.py` modules.
- Use `pd.DataFrame` hints for tabular I/O.
- Document expected input columns in docstrings.
- Validate required columns at function boundaries.

### Naming

- Functions/variables: `snake_case`.
- Constants: `UPPER_SNAKE_CASE`.
- Preserve domain-specific variable vocabulary from INE data when useful.
- If normalizing accented names, centralize that in one helper.

### Error Handling

- Never use bare `except:`.
- Catch specific exceptions.
- Include actionable context in errors (year/file/column).
- Fail fast on schema mismatches.
- For year-batch loops, partial continuation is acceptable only with explicit per-year error reporting and summary.

### Data Handling

- Do not silently coerce invalid values.
- Treat sentinel values explicitly (example: `Edadif == 999` to missing).
- Keep merge keys explicit.
- Check merge expectations where possible.
- Set fixed random seeds for clustering/modeling reproducibility.

### Notebook Practices

- Keep execution order clean (Restart + Run All should work).
- Avoid hidden cross-cell state dependencies.
- Separate feature engineering from visualization where practical.
- Extract reusable logic into `src/` as complexity grows.

### Documentation

- Update `README.md` when setup/commands change.
- Update `diccionario.md` if variable usage or definitions change.
- Comment intent and assumptions, not obvious syntax.

## Agent Working Rules

- Prefer small, reviewable diffs.
- Do not rewrite large notebook sections unless requested.
- Do not modify raw input data under `data/defunciones/`.
- Keep Spanish domain terminology in outputs and labels.

## Suggested Future Test Layout

When refactoring notebook logic into modules, create:

- `tests/test_ingestion.py`
- `tests/test_schema_alignment.py`
- `tests/test_cie10_mapping.py`
- `tests/test_feature_engineering.py`
- `tests/test_clustering_pipeline.py`

Design functions for single-test execution:

- Keep transformations pure when possible.
- Pass DataFrames directly to core functions.
- Keep file I/O at orchestration boundaries.

## Priority Order for Conflicts

1. Direct user instruction
2. Cursor/Copilot rules (if present later)
3. This `AGENTS.md`
4. Existing repository patterns
