# Reverse DCF Valuation Model (Educational Recreation)

This is an educational recreation of the **Reverse DCF Valuation Model**, a Python-based equity research toolkit. The primary goal of a reverse DCF model is to answer:
> **"What operational and valuation assumptions are already priced into the current stock price?"**

By reverse-engineering these assumptions, analysts can debate whether the market-implied growth rates or margins are realistic relative to a company's historical performance and competitive moat.

---

## 🛠️ Project Structure

The project is structured as a modern Python package:

```text
reverse_dcf/
├── pyproject.toml            # Package metadata & build configuration
├── requirements.txt          # Third-party dependencies
├── recreation_guide.md       # Step-by-step roadmap for educational reconstruction
├── dcf_background_knowledge.md # Core financial formulas & valuation theory
├── src/
│   └── reversedcf/
│       ├── __init__.py       # Package entry point
│       ├── metrics.py        # Financial metrics and string formatters
│       └── dcf.py            # Core DCF projections and valuation engine
├── scripts/                  # Command-line workflows & scripts (in progress)
└── tests/                    # Unit testing suite (in progress)
```

---

## 🚦 Current Reconstruction Status (In Progress)

This codebase is being built using a bottom-up, dependency-first approach:

- [x] **Phase 1: Package Infrastructure** (`pyproject.toml`, `requirements.txt`, `src/reversedcf/__init__.py`)
- [x] **Phase 2: Core Valuation Engine** (`src/reversedcf/metrics.py`, `src/reversedcf/dcf.py`)
- [ ] **Phase 3: Root-Solving & Numerical Analysis** (`src/reversedcf/reverse.py` using Brent's method)
- [ ] **Phase 4: Scenarios & Sensitivity Analysis** (`src/reversedcf/scenarios.py`, `src/reversedcf/sensitivity.py`)
- [ ] **Phase 5: Presentation & Visualization** (`src/reversedcf/plotting.py`, `src/reversedcf/report.py`)
- [ ] **Phase 6: Live Market Data Integration** (`src/reversedcf/data.py` using `yfinance`)
- [ ] **Phase 7: User Interfaces** (Typer CLI and Streamlit Web Dashboard)
- [ ] **Phase 8: Comprehensive Unit Tests** (`tests/` suite)

---

## 💻 Setup & Installation

Follow these steps to set up the development environment:

### 1. Initialize Virtual Environment
Create and activate a virtual environment to manage dependencies cleanly:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies & Editable Package
Install the project dependencies and set up the package in **editable mode** so that imports work across all subdirectories:

```bash
pip install -r requirements.txt
pip install -e .
```

---

## 📈 Implemented Modules

### 1. Utility Metrics (`src/reversedcf/metrics.py`)
Provides formatting and basic formulas to keep the UI layers decoupled from the presentation layer:
* `format_percentage(x)`: Converts decimal values (e.g., `0.155`) to human-readable strings (`15.5%`).
* `format_currency(x)`: Formats large dollar figures into neat abbreviations (e.g., `$1.25B` or `$850.00M`).
* `revenue_cagr(start, end, years)`: Computes the Compound Annual Growth Rate over a time frame.
* `margin(fcf, revenue)`: Computes margins with division-by-zero protection.

### 2. Core Valuation Engine (`src/reversedcf/dcf.py`)
Defines the mathematical foundation of the DCF model:
* `DCFInputs`: A frozen, immutable dataclass holding inputs like revenue, CAGR, FCF margin, forecast years, WACC, terminal growth, net debt, and shares outstanding. Includes rigorous validation checks inside `__post_init__`.
* `DCFProjection`: Keeps projected pandas series of revenue, FCF, and present values.
* `DCFValuation`: Calculates the final Enterprise Value (EV), Equity Value, and Implied Share Price.
* `run_dcf(inputs)`: Performs the complete forward projection and discounting calculations.

---

## 🧪 Next Steps & Testing

To verify the core math as you progress through the recreation:
1. Complete **Phase 3 (Reverse Solvers)**.
2. Add your unit tests under `tests/`.
3. Run the test suite:
   ```bash
   pytest
   ```

*Refer to [recreation_guide.md](file:///C:/Users/Aaditya%20Saini/Desktop/DCF_Model/reverse_dcf/recreation_guide.md) for detailed step-by-step implementation details of each remaining phase.*
