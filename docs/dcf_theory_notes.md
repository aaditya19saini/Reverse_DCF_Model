# Reverse DCF — Finance Theory Notes

## 1. DCF (Discounted Cash Flow) Basics
A valuation method that projects future free cash flows and discounts them back to present value using a discount rate (WACC).

**Flow:**
1. Project future revenue using a CAGR
2. Apply FCF margin → get free cash flows
3. Discount each cash flow to present value using WACC
4. Calculate terminal value (Gordon Growth Model)
5. Sum discounted FCF + discounted terminal value → **Enterprise Value**
6. Subtract net debt → **Equity Value**
7. Divide by shares outstanding → **Implied Share Price**

---

## 2. Enterprise Value (EV)
The total value of a company's operations — what you'd pay to buy the entire business (debt + equity, before cash).

**Formula:**
```
EV = present value of all future cash flows
```

---

## 3. Equity Value (Market Cap)
What belongs to shareholders after paying off obligations.

**Formula:**
```
Equity Value = Enterprise Value - Net Debt
```

**Net Debt = Debt - Cash**

Debtholders get paid before shareholders, so you subtract net debt from EV to get equity value.

---

## 4. Net Debt
```
Net Debt = Debt - Cash
```

- **Positive net debt**: company has more debt than cash
- **Negative net debt**: company has net cash (cash exceeds debt)

Subtracting net debt from EV: if net debt is negative, equity value is *higher* than EV (because you acquire that cash when buying the company).

**Example:** If EV = $100B, Debt = $20B, Cash = $5B → Net Debt = $15B → Equity = $85B

---

## 5. Implied Share Price
What a DCF says each share is worth.

**Formula:**
```
Implied Share Price = Equity Value ÷ Shares Outstanding
```

---

## 6. Cash on Balance Sheet
Cash is *accumulated* from past profits and financing (equity raises, loans). It is not the same as "earnings" or "revenue."

In the net debt formula, cash simply *reduces* the effective cost of buying a company — when you buy the business, you also acquire its cash.

---

## 7. Gordon Growth Model (Terminal Value)
Values the company's cash flows beyond the forecast period into perpetuity.

**Formula:**
```
Terminal Value = Final FCF × (1 + g) ÷ (WACC - g)
```

Where `g` = terminal growth rate.

**Constraint:** WACC must be > terminal growth, otherwise terminal value becomes infinite/meaningless.

---

## 8. Reverse DCF
Instead of assuming growth to find value (regular DCF), reverse DCF:

1. Starts with the **current stock price** → back-calculates equity value → enterprise value (the **target**)
2. **Backsolves for the implied growth rate** that justifies that price

**Key question:** "What growth rate would make this stock price fair?" Then you judge if that implied growth is realistic.

---

## 9. Target Enterprise Value (Reverse DCF)
The enterprise value derived from the *current market price*, not from projected cash flows.

**Significance:**
- Regular DCF: input growth → output value
- Reverse DCF: input current value (from price) → output implied growth

---

## 10. DCF Input Parameters

| Parameter | Description |
|---|---|
| `current_revenue` | Starting revenue (must be > 0) |
| `revenue_cagr` | Projected annual revenue growth rate (e.g., 0.10 = 10%) |
| `fcf_margin` | Free cash flow as % of revenue (e.g., 0.15 = 15%) |
| `forecast_years` | Projection horizon (must be > 0) |
| `wacc` | Weighted Average Cost of Capital (discount rate) |
| `terminal_growth` | Perpetual growth rate after forecast (must be < WACC) |
| `net_debt` | Debt minus cash (negative = net cash) |
| `shares_outstanding` | Diluted shares (must be > 0) |

All rates must be > -100% (can't lose more than everything).

## 11. Percentage & Currency Formatting
- `format_percentage(0.0357)` → `"3.6%"` (float → percentage string, 1 decimal)
- `format_currency(1_234_567_890_123)` → `"$1.23T"` (uses T/B/M suffixes, 2 decimals)
