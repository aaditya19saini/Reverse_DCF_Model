# Reverse DCF Valuation Model

An educational Python toolkit for answering a central reverse-DCF question:

> What growth, margin, discount-rate, or terminal-growth assumption is implied by
> a company's current enterprise value?

The project includes a forward discounted cash flow engine, numerical
reverse-solvers, scenario and sensitivity analysis, live company-data helpers,
plotting utilities, and Markdown report generation.

> **Disclaimer:** This project is for education and portfolio demonstration only.
> It is not financial advice or an investment recommendation.

## How It Works

The model projects revenue at a constant compound annual growth rate, applies a
constant free cash flow margin, discounts forecast cash flows, and calculates a
terminal value using the Gordon Growth Model.

```text
Projected revenue -> Free cash flow -> Present value
                                      + Discounted terminal value
                                      = Enterprise value

Enterprise value - Net debt = Equity value
Equity value / Shares outstanding = Implied share price
```

A reverse DCF holds the other inputs constant and uses Brent's root-finding
method to solve for the assumption that makes model enterprise value equal the
selected market enterprise value.

## Features

- Forward DCF valuation with yearly revenue, FCF, and discounted-FCF projections
- Reverse-solvers for revenue CAGR, FCF margin, WACC, and terminal growth
- Bear, base, bull, and market-implied scenarios
- WACC, terminal-growth, margin, and growth sensitivity tables
- Best-effort company lookup and financial statement loading through `yfinance`
- Field-level data-quality labels for loaded and estimated values
- Matplotlib charts and Markdown report-generation helpers
- Command-line solver for market-implied revenue growth

## Installation

Python 3.10 or newer is required.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e .
```

Install all development and dashboard dependencies from the repository:

```powershell
pip install -r requirements.txt
pip install -e .
```

The package also defines optional dependency groups:

```powershell
pip install -e ".[app]"  # Streamlit
pip install -e ".[dev]"  # pytest, Jupyter, and ipykernel
```

## Quick Start

Run a forward DCF in Python:

```python
from reversedcf.dcf import DCFInputs, run_dcf

inputs = DCFInputs(
    current_revenue=391_000_000_000,
    revenue_cagr=0.08,
    fcf_margin=0.27,
    forecast_years=5,
    wacc=0.08,
    terminal_growth=0.025,
    net_debt=-50_000_000_000,
    shares_outstanding=15_263_000_000,
)

valuation = run_dcf(inputs)

print(f"Enterprise value: ${valuation.enterprise_value:,.0f}")
print(f"Implied share price: ${valuation.implied_share_price:,.2f}")
```

With the sample assumptions above, the model produces an enterprise value of
approximately `$2.50T` and an implied share price of approximately `$166.76`.

Solve for the revenue CAGR implied by a target enterprise value:

```python
from reversedcf.reverse import solve_required_revenue_cagr

implied_growth = solve_required_revenue_cagr(
    target_enterprise_value=2_850_000_000_000,
    base_inputs=inputs,
)

print(f"Market-implied revenue CAGR: {implied_growth:.1%}")
```

## CLI

After installing the package, inspect the available commands:

```powershell
reversedcf --help
```

Solve for market-implied revenue growth:

```powershell
reversedcf solve-growth `
  --target-enterprise-value 2850000000000 `
  --current-revenue 391000000000 `
  --fcf-margin 0.27
```

Expected output:

```text
Required revenue CAGR: 11.2%
Model enterprise value: $2.85T
```

## Live Company Data

The data module can resolve common company names or ticker symbols and load
best-effort valuation inputs from `yfinance`:

```python
from reversedcf.data import load_company_valuation_inputs

company = load_company_valuation_inputs("AAPL")
print(company)
```

Live financial data may be missing, delayed, inconsistent across companies, or
estimated from other fields. Review every loaded value before using it in a
valuation.

## Model Assumptions

The current DCF is intentionally simple and uses:

- Constant revenue CAGR during the explicit forecast period
- Constant FCF margin during the explicit forecast period
- Constant WACC
- Gordon Growth terminal value
- Net debt defined as debt minus cash
- Consistent monetary units across all inputs

`WACC` must be greater than terminal growth. Percentage inputs are decimals, so
use `0.08` for 8%.

## Project Structure

```text
reverse_dcf/
|-- docs/
|   |-- dcf_background_knowledge.md
|   |-- dcf_theory_notes.md
|   `-- recreation_guide.md
|-- src/reversedcf/
|   |-- cli.py
|   |-- data.py
|   |-- dcf.py
|   |-- fin.py
|   |-- metrics.py
|   |-- plotting.py
|   |-- report.py
|   |-- reverse.py
|   |-- scenarios.py
|   `-- sensitivity.py
|-- pyproject.toml
|-- requirements.txt
`-- streamlit.py
```

## Current Limitations

- The single-stage model does not capture changing margins, cyclicality,
  dilution, buybacks, or changing capital intensity.
- Valuation results can be highly sensitive to WACC and terminal-growth inputs.
- Reverse-solvers only succeed when a solution exists within their configured
  search bounds.
- The `run-case-study` and `generate-report` CLI commands expect supporting
  files that are not currently included in this repository.
- The dashboard entry file is currently named `streamlit.py`, which shadows the
  installed `streamlit` package when launched from the repository root.

## Further Reading

- [`docs/dcf_background_knowledge.md`](docs/dcf_background_knowledge.md) explains
  DCF concepts for readers new to finance.
- [`docs/dcf_theory_notes.md`](docs/dcf_theory_notes.md) provides a compact
  finance-theory reference.
- [`docs/recreation_guide.md`](docs/recreation_guide.md) walks through the
  project's architecture and implementation phases.

## License

MIT
