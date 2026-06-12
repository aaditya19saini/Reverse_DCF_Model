# Reverse DCF Valuation Model

An educational reverse DCF toolkit for equity research-style analysis. The model answers a simple question:

> What operational and valuation assumptions are already priced into the current stock price?

The codebase combines a forward DCF engine, reverse-solvers for market-implied assumptions, scenario analysis, sensitivity tables, report generation, and a Streamlit dashboard.

## Project Layout

```text
reverse_dcf/
├── pyproject.toml
├── requirements.txt
├── README.md
├── docs/
├── scripts/
├── src/
│   └── reversedcf/
│       ├── cli.py
│       ├── data.py
│       ├── dcf.py
│       ├── fin.py
│       ├── metrics.py
│       ├── plotting.py
│       ├── report.py
│       ├── reverse.py
│       ├── scenarios.py
│       └── sensitivity.py
├── streamlit.py
└── tests/
```

## Supported Environment

- Python 3.10+
- Core dependencies: `numpy`, `pandas`, `scipy`, `matplotlib`, `yfinance`, `typer`
- Optional app dependency: `streamlit`

## Installation

Create a virtual environment, then install the package and dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

If you want the Streamlit dashboard, install the app extra as well:

```bash
pip install -e .[app]
```

## What's Included

- `src/reversedcf/dcf.py`: forward DCF projections and valuation output
- `src/reversedcf/reverse.py`: reverse-solver helpers for market-implied assumptions
- `src/reversedcf/scenarios.py` and `src/reversedcf/sensitivity.py`: scenario and sensitivity analysis
- `src/reversedcf/data.py`: company data lookup and input helpers
- `src/reversedcf/report.py`: report generation utilities
- `src/reversedcf/cli.py`: Typer-based command-line interface
- `streamlit.py`: interactive dashboard

## Usage

Run the CLI:

```bash
reversedcf --help
```

Common commands:

```bash
reversedcf solve-growth --target-enterprise-value 2850000000000 --current-revenue 391000000000 --fcf-margin 0.27
reversedcf generate-report --input data/sample_inputs/aapl.json --output reports/sample_report.md
```

Run the dashboard directly from the repository root:

```bash
streamlit run streamlit.py
```

## Notes

- The package version is currently `0.1.0`.
- The project is educational in scope and is not intended to provide investment advice.
- See the files in `docs/` for background theory and reconstruction notes.
