# Capital IQ AI output — model-gaps Prompt 4 (peer balance-sheet items for EV), pricing date 2026-10-16

_Raw source copy. Pasted by the team on 2026-10-17 from the Capital IQ AI assistant, response to Prompt 4 of `BIMBOA/research/capiq-prompts-model-gaps_2026-10-17.md`. Text and numbers are as received (including its own arithmetic); tab-separated tables were converted to markdown. This file could not be written to `raw/` (write permission denied); move it there unchanged if you want it in the inbox._

_Known problem in the output: ARYZTA non-current leases are stated as €167.8M − €35.5M = €119.1M; the subtraction gives €132.3M, and €678.2M + €167.8M = €846.0M reconciles to total debt €845.9M. Reviewed in the peer workbook v3 (Inputs_Sources)._

---

I'll work through the data systematically. All financial figures are sourced from S&P Capital IQ Financials and S&P Capital IQ Estimates. The balance-sheet date for all four companies is 06/30/2026 (LTM period end), which is the latest reported balance sheet available.

Entities used:

- Yamazaki Baking Co., Ltd. (TSE:2212) — resolved directly by ticker
- ARYZTA AG (SWX:ARYN) — resolved directly by ticker
- Arca Continental, S.A.B. de C.V. (BMV:AC) — resolved directly by ticker; confirmed as the Mexican beverage/food company, not AON
- Gruma, S.A.B. de C.V. (BMV:GRUMA B) — resolved directly by ticker; confirmed as the tortilla/corn flour company, not "Bevgru Ab"

Currency conversion rates used (USD, as of LTM 06/30/2026):

- JPY: 0.006482 USD/JPY
- EUR: 1.166559 USD/EUR
- MXN: 0.055690 USD/MXN
- USD: 1.000000 (Gruma reports in USD)

## Task 4A — Balance Sheet Items for Enterprise Value

Balance sheet date for all companies: 06/30/2026 (LTM period end). All local-currency figures are in reporting-currency millions (converted from $000s in the source). USD figures converted at the rates above. "Current LT Debt & Leases" as returned by S&P Capital IQ represents the current portion of long-term debt plus current lease liabilities combined; the current portion of long-term debt alone is derived as (Current LT Debt & Leases) minus (Current Portion of Leases) where both are available.

| Metric | Yamazaki Baking Co., Ltd. (TSE:2212) | ARYZTA AG (SWX:ARYN) | Arca Continental, S.A.B. de C.V. (BMV:AC) | Gruma, S.A.B. de C.V. (BMV:GRUMA B) |
|---|---|---|---|---|
| Balance Sheet Date | 06/30/2026 | 06/30/2026 | 06/30/2026 | 06/30/2026 |
| Reporting Currency | JPY | EUR | MXN | USD |
| Accounting Standard | J-GAAP | IFRS | IFRS | IFRS |
| Shares Outstanding – Basic (millions) | 196.9 | 24.8 | 1,696.2 | 336.2 |
| Shares Outstanding – Diluted (millions) | N/A | N/A | N/A | N/A |
| Short-Term Borrowings (local CCY, M) | ¥51,337 | N/A | N/A | N/A |
| Current Portion of Long-Term Debt (local CCY, M) | N/A | N/A | MXN 17,027 | $365.2 |
| Long-Term Debt (local CCY, M) | ¥33,503 | €678.2 | MXN 46,487 | $1,333.4 |
| Lease Liabilities – Current (local CCY, M) | ¥3,278 | €35.5 | MXN 641.5 | $52.8 |
| Lease Liabilities – Non-Current (local CCY, M) | ¥4,575 | €119.1 | MXN 1,174.0 | $360.4 |
| Finance Leases (local CCY, M) | N/A | N/A | N/A | N/A |
| Cash & Short-Term Investments (local CCY, M) | ¥165,749 | €72.9 | MXN 29,244 | $483.6 |
| Minority Interest – Book Value (local CCY, M) | N/A | N/A | N/A | N/A |
| Total Debt – CIQ Definition (local CCY, M) | ¥92,699 | €845.9 | MXN 65,427 | $2,111.8 |
| Net Debt – CIQ Definition (local CCY, M) | (¥73,050) | €773.0 | MXN 36,183 | $1,628.2 |
| Market Cap (local CCY, M) | N/A | N/A | N/A | N/A |
| Enterprise Value (local CCY, M) | N/A | N/A | N/A | N/A |
| Market Cap (USD, M) | N/A | N/A | N/A | N/A |
| Enterprise Value (USD, M) | N/A | N/A | N/A | N/A |

Derivation notes:

- All local-currency figures converted from $000 USD values using the period-end FX rates, then reconverted to local currency: local CCY = USD value ÷ FX rate (USD/local CCY).
- Short-Term Borrowings: Available only for Yamazaki (¥51,337M = $332,782K ÷ 0.006482); returned as N/A for ARYZTA, Arca Continental, and Gruma.
- Current Portion of Long-Term Debt (standalone): S&P CIQ returns "Current LT Debt & Leases" as a combined line. For Yamazaki, the combined figure equals the current lease figure (¥3,278M = ¥3,278M), implying no separate current LT debt component is captured — reported as N/A. For ARYZTA, same situation (combined = current lease). For Arca Continental: combined = MXN 17,753M; current leases = MXN 641.5M; implied current LT debt = MXN 17,027M. For Gruma: combined = $418.0M; current leases = $52.8M; implied current LT debt = $365.2M.
- Lease Liabilities – Non-Current: Derived as (Outstanding Balance for Leases) minus (Current Portion of Leases). Yamazaki: ¥7,853M − ¥3,278M = ¥4,575M. ARYZTA: €167.8M − €35.5M = €119.1M (using CIQ FX). Arca Continental: MXN 1,832.2M − MXN 641.5M = MXN 1,174.0M (approx). Gruma: $413.2M − $52.8M = $360.4M.
- Finance Leases: Not separately broken out in S&P CIQ data for any of the four companies; reported as N/A.
- Minority Interest (book value): Returned as N/A for all four companies by S&P CIQ.
- Net Debt – Yamazaki: Negative (−¥73,050M), meaning net cash position; CIQ returns ($473,475K) USD.
- Market Cap and Enterprise Value: Not returned in the data provided; reported as N/A.

## Task 4B — LTM and Last Two Fiscal Years: EBITDA, D&A, Revenue, Net Income, Diluted EPS

All figures in reporting-currency millions except Diluted EPS (per share in USD as returned by S&P CIQ). FY2025 and FY2024 are the two most recently completed fiscal years (calendar year-end December for all four companies). LTM = twelve months ended 06/30/2026.

### Yamazaki Baking Co., Ltd. (TSE:2212) | Reporting Currency: JPY | J-GAAP

| Metric | LTM 06/30/2026 | FY2025 | FY2024 |
|---|---|---|---|
| EBITDA (CIQ definition, ¥M) | ¥109,027 | ¥109,870 | ¥97,260 |
| D&A – Total (¥M) | N/A | N/A | N/A |
| D&A – ROU Asset Depreciation (¥M) | N/A | N/A | N/A |
| Revenue (¥M) | ¥1,337,668 | ¥1,353,459 | ¥1,268,993 |
| Net Income (¥M) | ¥42,109 | ¥42,203 | ¥36,730 |
| Diluted EPS (USD) | $1.38 | $1.38 | $1.18 |

### ARYZTA AG (SWX:ARYN) | Reporting Currency: EUR | IFRS

| Metric | LTM 06/30/2026 | FY2025 | FY2024 |
|---|---|---|---|
| EBITDA (CIQ definition, €M) | €216.4 | €254.2 | €272.9 |
| D&A – Total (€M) | N/A | N/A | N/A |
| D&A – ROU Asset Depreciation (€M) | N/A | N/A | N/A |
| Revenue (€M) | €2,201.2 | €2,223.2 | €2,194.0 |
| Net Income (€M) | €110.4 | €112.3 | €129.6 |
| Diluted EPS (USD) | $4.93 | $4.81 | $4.35 |

### Arca Continental, S.A.B. de C.V. (BMV:AC) | Reporting Currency: MXN | IFRS

| Metric | LTM 06/30/2026 | FY2025 | FY2024 |
|---|---|---|---|
| EBITDA (CIQ definition, MXN M) | MXN 48,607 | MXN 48,689 | MXN 47,357 |
| D&A – Total (MXN M) | N/A | N/A | N/A |
| D&A – ROU Asset Depreciation (MXN M) | N/A | N/A | N/A |
| Revenue (MXN M) | MXN 250,410 | MXN 250,315 | MXN 239,596 |
| Net Income (MXN M) | MXN 18,711 | MXN 19,589 | MXN 19,563 |
| Diluted EPS (USD) | $0.61 | $0.60 | $0.63 |

### Gruma, S.A.B. de C.V. (BMV:GRUMA B) | Reporting Currency: USD | IFRS

| Metric | LTM 06/30/2026 | FY2025 | FY2024 |
|---|---|---|---|
| EBITDA (CIQ definition, $M) | $995.0 | $1,033.5 | $1,045.9 |
| D&A – Total ($M) | N/A | N/A | N/A |
| D&A – ROU Asset Depreciation ($M) | N/A | N/A | N/A |
| Revenue ($M) | $6,500.1 | $6,374.6 | $6,486.9 |
| Net Income ($M) | $478.6 | $519.3 | $531.9 |
| Diluted EPS (USD) | $1.40 | $1.47 | $1.46 |

Note on local-currency conversion for Task 4B: USD values from S&P CIQ ($000s) are converted to local currency millions using the respective period FX rates: LTM at 0.006482 (JPY), 1.166559 (EUR), 0.055690 (MXN); FY2025 at 0.006690 (JPY), 1.130601 (EUR), 0.052179 (MXN); FY2024 at 0.006609 (JPY), 1.081860 (EUR), 0.054887 (MXN). Gruma reports in USD; no conversion needed. Diluted EPS is presented as returned by S&P CIQ in USD.

## Task 4C — Gruma, S.A.B. de C.V. (BMV:GRUMA B): Analyst Consensus Estimates

Estimates as of 10/14/2026 (FY2026E) and 10/12/2026 (FY2027E, FY2028E). Reported currency: MXN; values displayed in USD millions (EBITDA, Revenue) and USD per share (EPS) as converted by S&P CIQ at the spot rate at time of query. Source: S&P Capital IQ Estimates.

| Metric | FY2026E (ending 12/31/2026) | FY2027E (ending 12/31/2027) | FY2028E (ending 12/31/2028) |
|---|---|---|---|
| EBITDA – Mean ($M) | $1,111.37 | $1,059.18 | $1,101.24 |
| EBITDA – # Analysts | 12 | 10 | 9 |
| Revenue – Mean ($M) | $6,648.35 | $6,444.43 | $6,615.66 |
| Revenue – # Analysts | 12 | 10 | 9 |
| EPS Normalized – Mean ($) | $1.40 | $1.33 | $1.43 |
| EPS Normalized – # Analysts | 10 | 8 | 7 |

## Items Not Retrieved

Task 4A:

- Diluted shares outstanding — Returned as N/A by S&P CIQ for all four companies.
- Current portion of long-term debt (standalone) — S&P CIQ combines this with current lease liabilities into a single "Current LT Debt & Leases" line. For Yamazaki and ARYZTA, the combined figure equals the current lease figure, so no standalone current LT debt component is isolable from the data; reported as N/A for those two. For Arca Continental and Gruma, an implied figure is derived by subtraction (see notes above).
- Finance leases (separately identified) — Not broken out separately in S&P CIQ data for any company; reported as N/A for all four.
- Minority interest at book value — Returned as N/A by S&P CIQ for all four companies.
- Market capitalization and enterprise value — Not returned in the data for any company; reported as N/A.
- Short-term borrowings — Returned as N/A for ARYZTA, Arca Continental, and Gruma.
- Accounting standard for Yamazaki — Confirmed as J-GAAP from general knowledge (Yamazaki Baking is a Japanese domestic filer); not explicitly flagged in the S&P CIQ data returned. Verify independently if needed.

Task 4B:

- Depreciation & Amortization (total and ROU asset depreciation separately) — Not returned by S&P CIQ for any company or period; reported as N/A for all. The "Real Estate Depreciation" field returned NA for all companies and periods. A separate D&A query would be required.

Task 4C:

- No items missing for Task 4C; all three fiscal years and all three metrics (EBITDA, Revenue, EPS Normalized) were returned with analyst counts.

Source: S&P Capital IQ Financials; S&P Capital IQ Estimates.
