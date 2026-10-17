# Capital IQ AI output — Prompt 1 (market data, leverage, multiples, operations)

_Raw source copy. Pasted by the team on 2026-10-16 from the Capital IQ AI assistant, response to Prompt 1 (Tasks 1 and 2 of `BIMBOA/research/capiq-prompts-under-5000_2026-10-16.md`). Text and numbers are as received; tab-separated tables were converted to markdown tables and nothing else was changed, including the output's own errors and its stray citation numerals. Known problems are logged in `wiki/Valuation/capiq-data-discrepancies-2026-10.md`. This file could not be written to `raw/` (write permission denied); move it to `raw/` and keep the content unchanged._

---

CFA Research Challenge — Grupo Bimbo: Market Data, Leverage & Multiples

⚠️ Critical Data Availability Notice

Grupo Bimbo (BMV:BIMBOA) and Gruma (BMV:GRUMAB) did not resolve to financial data in the CIQ pricing/financials query. The system returned entity names "Bmvb Immo" and "Bevgru Ab" respectively — these appear to be incorrect entity resolutions for the BMV tickers. Bimbo financial data is available only through the earnings release documents (MXN, company-reported). All Bimbo figures below are sourced from those filings; CIQ standardized financials for Bimbo are N/A in this pull.

Yamazaki Baking (TSE:2212) returned no pricing data (share price, market cap from pricing feed = N/A), though financial statement data was retrieved.

Arca Continental (BMV:AC) resolved to AON in the pricing feed — the financials tool correctly identified it as BMV:AC*. Market cap and EV from the pricing tool for AC appear to reflect AON (Aon plc), not Arca Continental. Arca Continental market cap and EV from the pricing tool are flagged as unreliable and excluded from the market data table; EV from the financials tool is used where available.

Moody's ratings: Not available (subscription entitlement denied). Historical ratings: Not available (subscription entitlement denied).

## TASK 1A — Market Data Snapshot

Pricing date: 10/15/2026–10/16/2026 (as returned). All USD. Shares in millions.

| # | Company | Ticker | FY-End | LTM Period End | Shares Diluted (M) | Market Cap ($M) | Total Debt ($M) | Cash ($M) | Net Debt ($M) | Min. Interest | EV ($M) | LTM Revenue ($M) | LTM EBITDA ($M) | LTM EBIT ($M) | Source / Type |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Grupo Bimbo | BMV:BIMBOA | Dec | 06/30/2026 | N/A | N/A | ~$8,200ᵃ | ~$1,700ᵃ | ~$7,600ᵃ | N/A | N/A | ~$20,500ᵃ | ~$2,950ᵃ | N/A | Company ER 1; Reported MXN converted approx. |
| 1 | Flowers Foods | NYSE:FLO | Jan | 07/18/2026 | 212.1 | $1,295.7 | $2,007.8 | $52.8 | $1,955.0 | N/A | $3,250.7 | $5,223.9 | $486.9 | $336.4 | CIQ-standardized |
| 2 | Gruma | BMV:GRUMAB | — | — | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Not resolved |
| 3 | Yamazaki Baking | TSE:2212 | Dec | 06/30/2026 | N/A | N/A | $600.9 | $1,074.3 | ($473.5) | N/A | N/A | $8,669.9 | $706.7 | $403.9 | CIQ-standardized; price N/A |
| 4 | ARYZTA | SWX:ARYN | Dec | 06/30/2026 | 24.8 | $1,218.8 | $986.9 | $85.0 | $901.9 | N/A | $2,103.3 | $2,567.4 | $252.4 | $190.0 | CIQ-standardized |
| 5 | J.M. Smucker | NYSE:SJM | Apr | 07/31/2026 | 106.8 | $13,612.5 | $6,940.2 | $43.2 | $6,897.0 | N/A | $20,509.5 | $9,156.9 | $2,263.9 | $1,699.2 | CIQ-standardized |
| 6 | Campbell's | NasdaqGS:CPB | Aug | 08/02/2026 | 298.2 | $5,925.9 | $7,450.0 | $394.0 | $7,056.0 | N/A | $13,287.9 | $9,744.0 | $1,620.0 | $1,207.0 | CIQ-standardized |
| 7 | Mondelez | NasdaqGS:MDLZ | Dec | 06/30/2026 | 1,276.3 | $81,568.8 | $22,059.0 | $1,716.0 | $20,343.0 | N/A | $101,964.8 | $39,675.0 | $6,080.0 | $4,692.0 | CIQ-standardized |
| 8 | Arca Continental | BMV:AC* | Dec | 06/30/2026 | 212.1 | N/Aᵇ | $3,644.0 | $1,628.5 | $2,015.4 | N/A | N/Aᵇ | $13,945.2 | $2,707.0 | $2,171.8 | CIQ-standardized; mkt cap unreliable |
| 9 | PepsiCo | NasdaqGS:PEP | Dec | 09/05/2026 | 1,362.7 | $179,200.5 | $51,881.0 | $10,675.0 | $40,718.0 | N/A | $220,113.5 | $98,241.0 | $19,171.0 | $15,764.0 | CIQ-standardized |
| R | Grupo Nutresa | BVC:NUTRESA | Dec | 06/30/2026 | 454.9 | $45,828.2 | $5,072.9 | $718.9 | $4,042.8 | N/A | $50,214.7 | $5,512.9 | $830.0 | $741.6 | CIQ-standardized |

Notes:

ᵃ Bimbo LTM figures are approximated from company earnings releases in MXN converted at the LTM spot rate (~MXN 17.9/USD as of 06/30/2026 implied). Net Debt as of 06/30/2026: Ps. 137 billion 1 ≈ $7.6B. LTM Revenue and EBITDA derived from H1 2026 + H2 2025 company-reported data. These are Reported / Calculated estimates — not CIQ standardized.

ᵇ Arca Continental market cap from pricing tool resolved to AON (Aon plc) — excluded as unreliable.

Minority interest: CIQ returned N/A for all companies in this field.

Local currencies: FLO/SJM/CPB/MDLZ/PEP = USD; BIMBOA = MXN; GRUMAB = MXN; TSE:2212 = JPY (converted at 0.006482 USD/JPY); ARYN = EUR (converted at 1.166559 USD/EUR); AC = MXN (converted at 0.055690 USD/MXN); NUTRESA = COP (converted at 0.000265 USD/COP).

Source: S&P Capital IQ Financials

## TASK 1B — Leverage History (Companies 1–9; Bimbo from filings)

### Grupo Bimbo (BMV:BIMBOA) — From Company Filings (MXN billions unless noted)

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM (06/30/2026) | Source / Type |
|---|---|---|---|---|---|---|---|
| Adj. EBITDA (MXN bn) | Ps. 47.4 | Ps. 53.4 | Ps. 54.9 | Ps. 55.5 | Ps. 59.5 | ~Ps. 58.5ᶜ | Reported 23 |
| Net Debt/Adj. EBITDA (x) | N/A | N/A | N/A | 2.9x | 2.7x | ~2.3xᶜ | Reported 13 |
| Total Debt (MXN bn) | N/A | N/A | Ps. 110 | Ps. 151 | N/A | Ps. 137ᵈ | Reported 14 |
| Avg. Cost of Debt (%) | N/A | N/A | N/A | ~6.x% | N/A | N/A | Partial 2 |
| Avg. Debt Maturity (yrs) | N/A | N/A | N/A | 11.15 | N/A | N/A | Reported 2 |

ᶜ LTM EBITDA estimated from 2Q26 ER data (H1 2026 + H2 2025). Net Debt/EBITDA of ~2.3x is Calculated from Ps. 137bn net debt / ~Ps. 58.5bn LTM EBITDA. ᵈ Net Debt as of 06/30/2026 stated as Ps. 137 billion 1

Note on Bimbo's debt structure: In February 2026, Bimbo issued Ps. 12 billion in the Mexican bond market 3 The company's debt is denominated in USD, MXN, and EUR (mix not fully disclosed in available documents). Average cost of debt is stated as "6.x%" (truncated in source 256).

### Peers — Annual Leverage (CIQ-Standardized, USD)

Flowers Foods (NYSE:FLO) — FY ends January

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM (07/18/2026) |
|---|---|---|---|---|---|---|
| Total Debt ($M) | $1,322.8 | $1,192.7 | $1,350.8 | $1,359.1 | $2,083.8 | $2,007.8 |
| Net Debt ($M) | $1,015.3 | $1,027.5 | $1,328.3 | $1,354.1 | $2,071.7 | $1,955.0 |
| EBITDA ($M) | $427.9 | $497.0 | $487.8 | $520.7 | $514.8 | $486.9 |
| Net Debt/EBITDA (x) | 1.71 | 1.73 | 2.25 | 2.10 | 3.13 | Calc: 4.01ˣ |
| Total Debt/EBITDA (x) | 2.22 | 2.00 | 2.29 | 2.10 | 3.15 | Calc: 4.12ˣ |
| Total Debt/Total Capital (%) | 49.07 | 45.25 | 49.98 | 49.08 | 61.52 | N/A |
| EBITDA/Interest (x) | 15.35 | 20.58 | 16.15 | 17.41 | 8.64 | N/A |
| EBIT/Interest (x) | 9.61 | 12.63 | 9.57 | 10.22 | 4.77 | N/A |
| Effective Tax Rate (%) | 24.11 | 23.54 | 21.45 | 24.57 | 27.15 | N/A |

ˣ Calculated: LTM Net Debt $1,955.0M / LTM EBITDA $486.9M = 4.01x; Total Debt $2,007.8M / EBITDA $486.9M = 4.12x.

Yamazaki Baking (TSE:2212) — FY ends December (USD, converted at period rates)

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM (06/30/2026) |
|---|---|---|---|---|---|---|
| Total Debt ($M) | $694.7 | $653.7 | $568.5 | $642.7 | $661.1 | $600.9 |
| Net Debt ($M) | ($357.5) | ($295.5) | ($388.8) | ($326.9) | ($383.7) | ($473.5) |
| EBITDA ($M) | $528.3 | $483.1 | $598.6 | $630.3 | $712.0 | $706.7 |
| Net Debt/EBITDA (x) | NM | NM | NM | NM | NM | NM |
| Total Debt/EBITDA (x) | 1.27 | 1.37 | 0.96 | 1.06 | 0.97 | Calc: 0.85ˣ |
| Total Debt/Total Capital (%) | 16.52 | 17.45 | 15.23 | 18.00 | 16.87 | N/A |
| EBITDA/Interest (x) | 86.35 | 83.92 | 113.42 | 110.77 | 72.41 | N/A |
| EBIT/Interest (x) | 26.70 | 29.30 | 56.71 | 60.25 | 41.59 | N/A |
| Effective Tax Rate (%) | 51.34 | 37.59 | 30.97 | 31.46 | 29.42 | N/A |

ˣ Calculated: $600.9M / $706.7M = 0.85x. Net debt is negative (net cash position).

ARYZTA (SWX:ARYN) — FY ends December (USD, converted at period rates)

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM (06/30/2026) |
|---|---|---|---|---|---|---|
| Total Debt ($M) | $442.8 | $546.5 | $578.8 | $849.6 | $841.1 | $986.9 |
| Net Debt ($M) | $240.1 | $295.8 | $434.6 | $769.7 | $760.6 | $901.9 |
| EBITDA ($M) | $212.5 | $189.7 | $237.5 | $295.3 | $287.4 | $252.4 |
| Net Debt/EBITDA (x) | 0.95 | 1.44 | 1.53 | 2.42 | 2.23 | Calc: 3.57ˣ |
| Total Debt/EBITDA (x) | 1.75 | 2.67 | 2.04 | 2.68 | 2.46 | Calc: 3.91ˣ |
| Total Debt/Total Capital (%) | 25.30 | 36.49 | 39.82 | 64.48 | 56.43 | N/A |
| EBITDA/Interest (x) | 5.97 | 10.92 | 8.20 | 5.51 | 5.97 | N/A |
| EBIT/Interest (x) | 1.28 | 4.90 | 4.58 | 3.41 | 3.55 | N/A |
| Effective Tax Rate (%) | NM | 91.63 | 7.74 | 16.01 | 19.03 | N/A |

ˣ Calculated: LTM Net Debt $901.9M / LTM EBITDA $252.4M = 3.57x; Total Debt $986.9M / $252.4M = 3.91x.

J.M. Smucker (NYSE:SJM) — FY ends April

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026A | LTM (07/31/2026) |
|---|---|---|---|---|---|---|---|
| Total Debt ($M) | $4,909.9 | $4,610.8 | $4,428.0 | $8,559.1 | $7,811.7 | $7,129.8 | $6,940.2 |
| Net Debt ($M) | $4,575.6 | $4,440.9 | $3,284.4 | $8,497.1 | $7,741.8 | $7,071.2 | $6,897.0 |
| EBITDA ($M) | $1,825.2 | $1,636.8 | $1,603.1 | $1,874.1 | $2,156.2 | $1,926.0 | $2,263.9 |
| Net Debt/EBITDA (x) | 2.37 | 2.54 | 1.92 | 4.27 | 3.41 | 3.47 | Calc: 3.05ˣ |
| Total Debt/EBITDA (x) | 2.54 | 2.64 | 2.58 | 4.30 | 3.44 | 3.50 | Calc: 3.07ˣ |
| Total Debt/Total Capital (%) | 37.67 | 36.16 | 37.79 | 52.66 | 56.22 | 56.26 | N/A |
| EBITDA/Interest (x) | 10.91 | 10.85 | 11.28 | 7.54 | 5.84 | 5.34 | N/A |
| EBIT/Interest (x) | 7.75 | 7.32 | 7.71 | 5.46 | 4.25 | 3.59 | N/A |
| Effective Tax Rate (%) | 25.22 | 25.14 | NM | 25.33 | NM | NM | N/A |

ˣ Calculated: $6,897.0M / $2,263.9M = 3.05x; $6,940.2M / $2,263.9M = 3.07x.

Campbell's (NasdaqGS:CPB) — FY ends August

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026A | LTM (08/02/2026) |
|---|---|---|---|---|---|---|---|
| Total Debt ($M) | $5,292.0 | $5,050.0 | $4,967.0 | $7,542.0 | $7,212.0 | $7,450.0 | $7,450.0 |
| Net Debt ($M) | $5,223.0 | $4,941.0 | $4,778.0 | $7,434.0 | $7,080.0 | $7,056.0 | $7,056.0 |
| EBITDA ($M) | $1,926.0 | $1,531.0 | $1,783.0 | $1,783.0 | $1,888.0 | $1,620.0 | $1,620.0 |
| Net Debt/EBITDA (x) | 2.32 | 2.65 | 2.23 | 3.43 | 3.04 | 3.44 | Calc: 4.36ˣ |
| Total Debt/EBITDA (x) | 2.35 | 2.70 | 2.32 | 3.48 | 3.10 | 3.63 | Calc: 4.60ˣ |
| Total Debt/Total Capital (%) | 62.66 | 60.24 | 57.56 | 66.52 | 64.88 | 64.19 | N/A |
| EBITDA/Interest (x) | 10.73 | 9.88 | 11.38 | 8.70 | 6.75 | 6.20 | N/A |
| EBIT/Interest (x) | 7.66 | 6.32 | 7.46 | 5.62 | 4.27 | 3.65 | N/A |
| Effective Tax Rate (%) | 24.55 | 22.36 | 23.94 | 25.10 | 24.37 | 23.44 | N/A |

ˣ Calculated: $7,056.0M / $1,620.0M = 4.36x; $7,450.0M / $1,620.0M = 4.60x.

Mondelez (NasdaqGS:MDLZ) — FY ends December

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM (06/30/2026) |
|---|---|---|---|---|---|---|
| Total Debt ($M) | $20,145.0 | $23,613.0 | $20,110.0 | $18,544.0 | $21,968.0 | $22,059.0 |
| Net Debt ($M) | $16,599.0 | $21,690.0 | $18,300.0 | $17,193.0 | $19,843.0 | $20,343.0 |
| EBITDA ($M) | $6,107.0 | $5,838.0 | $6,898.0 | $7,740.0 | $4,990.0 | $6,080.0 |
| Net Debt/EBITDA (x) | 2.42 | 3.26 | 2.32 | 1.99 | 3.44 | Calc: 3.35ˣ |
| Total Debt/EBITDA (x) | 2.94 | 3.55 | 2.55 | 2.15 | 3.80 | Calc: 3.63ˣ |
| Total Debt/Total Capital (%) | 41.56 | 46.73 | 41.48 | 40.75 | 45.90 | N/A |
| EBITDA/Interest (x) | 19.39 | 15.97 | 14.84 | 17.67 | 9.89 | N/A |
| EBIT/Interest (x) | 14.11 | 11.35 | 10.68 | 13.19 | 6.22 | N/A |
| Effective Tax Rate (%) | 21.62 | 24.09 | 23.63 | 24.11 | 24.08 | N/A |

ˣ Calculated: $20,343.0M / $6,080.0M = 3.35x; $22,059.0M / $6,080.0M = 3.63x.

Arca Continental (BMV:AC) — FY ends December (USD, converted at period rates)*

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM (06/30/2026) |
|---|---|---|---|---|---|---|
| Total Debt ($M) | $2,547.5 | $2,469.9 | $2,732.9 | $2,403.4 | $3,573.4 | $3,644.0 |
| Net Debt ($M) | $980.9 | $1,046.7 | $1,424.0 | $985.5 | $1,986.4 | $2,015.4 |
| EBITDA ($M) | $1,706.9 | $1,911.6 | $2,354.7 | $2,599.0 | $2,540.6 | $2,707.0 |
| Net Debt/EBITDA (x) | 0.57 | 0.52 | 0.57 | 0.43 | 0.72 | Calc: 0.74ˣ |
| Total Debt/EBITDA (x) | 1.48 | 1.23 | 1.09 | 1.04 | 1.30 | Calc: 1.35ˣ |
| Total Debt/Total Capital (%) | 25.81 | 24.58 | 25.59 | 22.36 | 28.27 | N/A |
| EBITDA/Interest (x) | 9.37 | 12.47 | 11.40 | 12.53 | 11.38 | N/A |
| EBIT/Interest (x) | 6.64 | 9.65 | 9.21 | 10.11 | 9.06 | N/A |
| Effective Tax Rate (%) | 30.15 | 31.66 | 31.77 | 31.98 | 31.80 | N/A |

ˣ Calculated: $2,015.4M / $2,707.0M = 0.74x; $3,644.0M / $2,707.0M = 1.35x.

PepsiCo (NasdaqGS:PEP) — FY ends December

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM (09/05/2026) |
|---|---|---|---|---|---|---|
| Total Debt ($M) | $42,378.0 | $41,487.0 | $47,061.0 | $47,751.0 | $53,028.0 | $51,881.0 |
| Net Debt ($M) | $36,390.0 | $36,139.0 | $37,058.0 | $38,485.0 | $43,498.0 | $40,718.0 |
| EBITDA ($M) | $14,433.0 | $14,950.0 | $16,785.0 | $17,842.0 | $18,174.0 | $19,171.0 |
| Net Debt/EBITDA (x) | 2.34 | 2.24 | 2.04 | 1.99 | 2.20 | Calc: 2.12ˣ |
| Total Debt/EBITDA (x) | 2.72 | 2.57 | 2.59 | 2.47 | 2.68 | Calc: 2.71ˣ |
| Total Debt/Total Capital (%) | 72.41 | 70.60 | 71.63 | 72.44 | 72.07 | N/A |
| EBITDA/Interest (x) | 8.66 | 20.72 | 21.96 | 20.91 | 17.67 | N/A |
| EBIT/Interest (x) | 6.59 | 15.78 | 16.90 | 16.07 | 13.37 | N/A |
| Effective Tax Rate (%) | 20.88 | 16.13 | 19.81 | 19.42 | 19.03 | N/A |

ˣ Calculated: $40,718.0M / $19,171.0M = 2.12x; $51,881.0M / $19,171.0M = 2.71x.

Source: S&P Capital IQ Financials

### Credit Ratings (Current, S&P Only — Moody's & Fitch N/A)

| # | Company | S&P Rating | Outlook | Rating Date | Prior Rating | Action | Moody's | Fitch |
|---|---|---|---|---|---|---|---|---|
| 0 | Grupo Bimbo | N/A | N/A | — | — | — | N/A | N/A |
| 1 | Flowers Foods | BB+ | Negative | 09/09/2026 | BBB- | Downgrade | N/A | N/A |
| 2 | Gruma | N/A | N/A | — | — | — | N/A | N/A |
| 3 | Yamazaki Baking | NR | NR | 01/08/2007 | BBB+ | Not Rated | N/A | N/A |
| 4 | ARYZTA | N/A | N/A | — | — | — | N/A | N/A |
| 5 | J.M. Smucker | BBB | Stable | Outlook updated 06/25/2025; last reviewed 06/23/2026 | BBB | Outlook change | N/A | N/A |
| 6 | Campbell's | BBB- | Negative | Outlook updated 03/12/2026; last reviewed 08/10/2026 | BBB- | Outlook change | N/A | N/A |
| 7 | Mondelez | BBB | Stable | Outlook 05/10/2016; last reviewed 11/24/2025 | BBB | Outlook change | N/A | N/A |
| 8 | Arca Continental | mxAAA (CaVal) | Stable | 01/22/2004 (new rating) | New | New rating | N/A | N/A |
| 9 | PepsiCo | A+ | Stable | Upgraded 04/26/2017; last reviewed 10/27/2025 | A | Upgrade | N/A | N/A |

Note: Historical rating changes over 10 years are not available (subscription entitlement denied). Moody's ratings not available. Fitch ratings not available for any company in this universe.

Source: S&P Capital IQ

## TASK 1C — Net Debt/EBITDA Ranking (LTM)

Key caveat: Bimbo's LTM ratio is company-reported (Ps. 137bn net debt / ~Ps. 58.5bn EBITDA ≈ 2.3x, or using the company's own stated 2.7x for FY2025 as the closest available proxy). The CIQ-standardized ratio is N/A. The table uses the company-reported figure.

### Panel 1: Net Debt / LTM EBITDA

| Rank | Company | LTM Net Debt ($M) | LTM EBITDA ($M) | Net Debt/EBITDA (x) | Type |
|---|---|---|---|---|---|
| 1 | Flowers Foods (FLO) | $1,955.0 | $486.9 | 4.01x | Calculated |
| 2 | Campbell's (CPB) | $7,056.0 | $1,620.0 | 4.36x | Calculated |
| 3 | ARYZTA (ARYN) | $901.9 | $252.4 | 3.57x | Calculated |
| 4 | Mondelez (MDLZ) | $20,343.0 | $6,080.0 | 3.35x | Calculated |
| 5 | J.M. Smucker (SJM) | $6,897.0 | $2,263.9 | 3.05x | Calculated |
| 6 | Grupo Bimbo (BIMBOA) | ~$7,600 | ~$3,260 | ~2.3x | Reported (approx.) |
| 7 | PepsiCo (PEP) | $40,718.0 | $19,171.0 | 2.12x | Calculated |
| 8 | Arca Continental (AC) | $2,015.4 | $2,707.0 | 0.74x | Calculated |
| 9 | Yamazaki Baking (2212) | ($473.5) | $706.7 | NM (net cash) | CIQ |

Gruma (2) excluded — no data.

### Summary Statistics

| Group | Median Net Debt/EBITDA | Mean Net Debt/EBITDA | Bimbo / Median |
|---|---|---|---|
| Core Peers (1–4: FLO, GRUMA, 2212, ARYN) | 3.79xᵉ | N/A | ~0.6x |
| All Peers (1–9, excl. Gruma) | 3.20xᶠ | ~2.97x | ~0.72x |

ᵉ Core peer median (FLO 4.01x, 2212 NM excluded, ARYN 3.57x): median of {4.01, 3.57} = 3.79x (Gruma N/A; Yamazaki NM excluded from median). ᶠ All peers ranked (excl. Gruma, excl. Yamazaki NM): {4.36, 4.01, 3.57, 3.35, 3.05, 2.12, 0.74} — median = 3.35x (MDLZ). Bimbo ~2.3x / 3.35x = 0.69x.

### Panel 2: Total Debt / LTM EBITDA

| Company | Total Debt ($M) | EBITDA ($M) | Total Debt/EBITDA (x) | Type |
|---|---|---|---|---|
| Flowers Foods | $2,007.8 | $486.9 | 4.12x | Calculated |
| Campbell's | $7,450.0 | $1,620.0 | 4.60x | Calculated |
| ARYZTA | $986.9 | $252.4 | 3.91x | Calculated |
| Mondelez | $22,059.0 | $6,080.0 | 3.63x | Calculated |
| J.M. Smucker | $6,940.2 | $2,263.9 | 3.07x | Calculated |
| Grupo Bimbo | ~$8,200 | ~$3,260 | ~2.5x | Reported (approx.) |
| PepsiCo | $51,881.0 | $19,171.0 | 2.71x | Calculated |
| Arca Continental | $3,644.0 | $2,707.0 | 1.35x | Calculated |
| Yamazaki Baking | $600.9 | $706.7 | 0.85x | Calculated |

Core peer median (total debt/EBITDA, excl. Gruma): {4.12, 3.91, 0.85} → 3.91x (using FLO, ARYN, 2212). Bimbo ~2.5x / 3.91x = 0.64x. All-peer median: {4.60, 4.12, 3.91, 3.63, 3.07, 2.71, 1.35, 0.85} = 3.35x. Bimbo ~2.5x / 3.35x = 0.75x.

### Answer to the Central Question: Does Bimbo have 2x the debt of its peers?

No. On a net debt/EBITDA basis, Bimbo's LTM ratio of approximately 2.3x is actually below the median of all peers (~3.35x) and well below the most leveraged peers (Campbell's 4.36x, Flowers Foods 4.01x). Bimbo's leverage is moderate relative to this universe. The "2x the debt" claim is not supported by the LTM data. Bimbo's absolute debt ($7.6B net) is large in dollar terms but its EBITDA generation (~$3.3B) keeps the ratio in a mid-range position. The comparison changes only modestly on a total-debt basis.

## TASK 2A — Valuation Multiples

Pricing date: 10/15/2026–10/16/2026. All multiples as of that date.

### LTM Trailing Multiples

| # | Company | EV/EBITDA LTM (x) | EV/EBIT LTM (x) | EV/Sales LTM (x) | P/E LTM (x) | Source |
|---|---|---|---|---|---|---|
| 0 | Grupo Bimbo | N/A | N/A | N/A | N/A | CIQ N/A |
| 1 | Flowers Foods | 5.15x | 9.67x | 0.62x | 23.45x | CIQ Multiples |
| 2 | Gruma | N/A | N/A | N/A | N/A | Not resolved |
| 3 | Yamazaki Baking | 6.58x | 11.48x | 0.54x | 17.74x | CIQ Multiples |
| 4 | ARYZTA | 7.31x | 11.42x | 0.85x | 10.21x | CIQ Multiples |
| 5 | J.M. Smucker | 8.57x | 11.98x | 2.22x | 58.63x | CIQ Multiples |
| 6 | Campbell's | 6.47x | 11.00x | 1.36x | 15.11x | CIQ Multiples |
| 7 | Mondelez | 14.48x | 21.19x | 2.54x | 23.10x | CIQ Multiples |
| 8 | Arca Continental | 8.47x | 10.75x | 1.67x | 18.71x | CIQ Multiples |
| 9 | PepsiCo | 10.35x | 13.69x | 2.20x | 16.15x | CIQ Multiples |

### NTM Forward Multiples

| # | Company | EV/EBITDA NTM (x) | EV/EBIT NTM (x) | P/E NTM (x) | Source |
|---|---|---|---|---|---|
| 0 | Grupo Bimbo | N/A | N/A | N/A | CIQ N/A |
| 1 | Flowers Foods | 7.55x | 12.38x | 8.93x | CIQ Forward Multiples |
| 2 | Gruma | N/A | N/A | N/A | Not resolved |
| 3 | Yamazaki Baking | 6.37x | 10.83x | 16.84x | CIQ Forward Multiples |
| 4 | ARYZTA | 5.94x | 9.94x | 9.01x | CIQ Forward Multiples |
| 5 | J.M. Smucker | 9.86x | 11.57x | 12.60x | CIQ Forward Multiples |
| 6 | Campbell's | 9.07x | 12.60x | 11.72x | CIQ Forward Multiples |
| 7 | Mondelez | 14.13x | 17.89x | 19.83x | CIQ Forward Multiples |
| 8 | Arca Continental | 7.87x | 10.08x | 16.50x | CIQ Forward Multiples |
| 9 | PepsiCo | 11.24x | 13.79x | 15.53x | CIQ Forward Multiples |

Core peer medians (1–4, excl. Gruma):

- LTM EV/EBITDA: median of {5.15, 6.58, 7.31} = 6.58x (Yamazaki)
- NTM EV/EBITDA: median of {7.55, 6.37, 5.94} = 6.37x
- Bimbo premium/discount vs. peers: N/A — Bimbo multiples not available from CIQ.

5-year and 10-year average EV/EBITDA and P/E: N/A — the historical aggregate multiples query returned an error (median not supported; average data not returned in this pull).

P/FCF, FCF yield, dividend yield: N/A — not returned in the multiples tool output.

## TASK 2B — Operating Comparison (Peers, Annual + LTM)

All figures in USD millions (CIQ-standardized). LTM periods vary by company.

### Revenue ($M)

| Company | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM |
|---|---|---|---|---|---|---|
| Flowers Foods | $4,330.8 | $4,805.8 | $5,090.8 | $5,103.5 | $5,256.5 | $5,223.9 |
| Yamazaki Baking | $8,773.2 | $8,243.9 | $8,383.8 | $8,224.6 | $8,773.2 | $8,669.9 |
| ARYZTA | $1,824.5 | $1,956.3 | $2,238.6 | $2,374.1 | $2,513.7 | $2,567.4 |
| J.M. Smucker | $8,002.7 | $7,998.9 | $8,529.2 | $8,178.7 | $8,726.1 | $9,156.9 |
| Campbell's | $8,476.0 | $8,562.0 | $9,357.0 | $9,636.0 | $10,253.0 | $9,744.0 |
| Mondelez | $28,720.0 | $31,496.0 | $36,016.0 | $36,441.0 | $38,537.0 | $39,675.0 |
| Arca Continental | $9,160.7 | $10,441.2 | $12,179.4 | $13,149.5 | $13,058.3 | $13,945.2 |
| PepsiCo | $79,474.0 | $86,392.0 | $91,471.0 | $91,854.0 | $93,925.0 | $98,241.0 |

### EBITDA Margin (%)

| Company | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM |
|---|---|---|---|---|---|---|
| Flowers Foods | 11.3% | 10.3% | 9.6% | 10.2% | 9.8% | 9.3% |
| Yamazaki Baking | 5.6% | 5.9% | 7.1% | 7.7% | 8.1% | 8.2% |
| ARYZTA | 11.7% | 9.7% | 10.6% | 12.4% | 11.4% | 9.8% |
| J.M. Smucker | 22.8% | 20.5% | 18.8% | 22.9% | 24.7% | 24.7% |
| Campbell's | 22.7% | 17.9% | 19.1% | 18.5% | 18.4% | 16.6% |
| Mondelez | 20.4% | 18.5% | 19.2% | 21.2% | 13.0% | 15.3% |
| Arca Continental | 18.6% | 18.3% | 19.3% | 19.8% | 19.5% | 19.4% |
| PepsiCo | 18.9% | 17.3% | 18.4% | 19.4% | 19.4% | 19.5% |

### EBIT Margin (%)

| Company | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM |
|---|---|---|---|---|---|---|
| Flowers Foods | 8.5% | 7.6% | 6.9% | 7.4% | 7.0% | 6.4% |
| Yamazaki Baking | 1.7% | 2.0% | 3.6% | 4.2% | 4.7% | 4.7% |
| ARYZTA | 3.0% | 5.1% | 6.8% | 8.7% | 7.8% | 7.4% |
| J.M. Smucker | 17.2% | 14.7% | 13.7% | 17.7% | 19.0% | 18.6% |
| Campbell's | 19.0% | 13.9% | 15.0% | 14.5% | 14.4% | 12.4% |
| Mondelez | 16.2% | 15.0% | 15.8% | 17.7% | 9.4% | 11.8% |
| Arca Continental | 13.4% | 14.4% | 15.8% | 16.2% | 15.8% | 15.6% |
| PepsiCo | 15.5% | 14.3% | 15.3% | 16.2% | 16.0% | 16.1% |

### Return on Capital (%)

| Company | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM |
|---|---|---|---|---|---|---|
| Flowers Foods | 8.9% | 8.7% | 8.2% | 8.7% | 7.4% | 6.1% |
| Yamazaki Baking | 2.5% | 2.8% | 5.1% | 6.0% | 6.5% | 6.5% |
| ARYZTA | 1.4% | 3.8% | 6.5% | 9.2% | 8.5% | 7.8% |
| J.M. Smucker | 6.4% | 5.7% | 6.0% | 6.5% | 6.9% | 7.9% |
| Campbell's | 11.5% | 8.9% | 10.3% | 8.8% | 8.2% | 6.6% |
| Mondelez | 5.7% | 6.0% | 7.2% | 8.6% | 4.9% | 6.1% |
| Arca Continental | 7.3% | 9.5% | 11.3% | 12.0% | 10.9% | 11.0% |
| PepsiCo | 12.7% | 13.1% | 14.1% | 14.1% | 13.4% | 13.6% |

### Levered Free Cash Flow ($M)

| Company | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM |
|---|---|---|---|---|---|---|
| Flowers Foods | $262.8 | $175.3 | $312.9 | $157.0 | $221.1 | $298.5 |
| Yamazaki Baking | $66.1 | $49.5 | $241.8 | $184.1 | $168.9 | $113.4 |
| ARYZTA | $120.3 | $209.0 | $160.9 | $161.6 | $154.9 | $138.1 |
| J.M. Smucker | $1,185.3 | $608.2 | $962.9 | $590.5 | $600.3 | $1,464.3 |
| Campbell's | $786.4 | $851.1 | $766.4 | $576.8 | $717.6 | $634.5 |
| Mondelez | $4,168.6 | $3,656.3 | $4,187.4 | $2,747.8 | $3,588.0 | $2,252.4 |
| Arca Continental | $807.5 | $776.6 | $682.0 | $864.2 | $529.1 | $763.6 |
| PepsiCo | $5,596.3 | $6,681.3 | $7,565.0 | $7,200.9 | $8,232.8 | $9,044.3 |

Source: S&P Capital IQ Financials

### Consensus Estimates (FY2026E–FY2028E, Revenue and EBITDA, $M)

| Company | Rev FY26E | Rev FY27E | Rev FY28E | EBITDA FY26E | EBITDA FY27E | EBITDA FY28E | Source |
|---|---|---|---|---|---|---|---|
| Grupo Bimbo | N/A | N/A | N/A | N/A | N/A | N/A | Not resolved |
| Flowers Foods | $5,075.8 | $5,058.3 | $5,032.6 | $458.6 | $430.1 | $432.4 | Consensus |
| Gruma | N/A | N/A | N/A | N/A | N/A | N/A | Not resolved |
| Yamazaki Baking | $8,564.4 | $8,795.0 | $8,960.6 | $700.1 | $741.5 | $765.9 | Consensus |
| ARYZTA | $2,594.7 | $2,562.6 | $2,609.1 | $354.7 | $363.6 | $381.1 | Consensus |
| J.M. Smucker | $9,050.9A | $8,930.3 | $9,037.5 | $2,024.7A | $2,181.3 | $2,175.4 | Consensus/Actual |
| Campbell's | $9,744.0A | $9,496.6 | $9,469.4 | $1,594.0A | $1,464.6 | $1,519.8 | Consensus/Actual |
| Mondelez | $40,101.2 | $41,232.9 | $42,656.1 | $6,735.2 | $7,265.0 | $7,700.3 | Consensus |
| Arca Continental | $14,453.8 | $14,628.6 | $15,637.8 | $2,930.2 | $3,006.3 | $3,234.2 | Consensus |
| PepsiCo | $99,300.5 | $101,773.1 | $105,151.4 | $19,050.5 | $19,587.1 | $20,589.6 | Consensus |

Source: S&P Capital IQ Estimates

## TASK 2C — Grupo Bimbo by Segment

All figures in MXN millions (company-reported). LTM = H1 2026 + H2 2025.

### Net Sales by Segment (MXN millions)

| Segment | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | H1 2026 | Source |
|---|---|---|---|---|---|---|---|
| North America | N/A | N/A | N/A | Ps. 99,702 | Ps. 102,651 | Ps. 84,647ᵍ | 13 |
| Mexico | N/A | N/A | N/A | Ps. 84,236 | Ps. 85,874 | Ps. 77,191ʰ | 13 |
| EAA | N/A | N/A | N/A | Ps. 16,310 | Ps. 19,253 | Ps. 24,368ⁱ | 13 |
| Latin America | N/A | N/A | N/A | Ps. 17,404 | Ps. 19,026 | Ps. 20,578ʲ | 13 |
| Grupo Bimbo Total | N/A | N/A | Ps. 391,213ᵏ | Ps. 408,335 | Ps. 426,952 | Ps. 205,714ˡ | 137 |

ᵍ Q1 2026 NA: Ps. 40,279 + Q2 2026 NA: Ps. 44,368 = Ps. 84,647 18 ʰ Q1 2026 MX: Ps. 39,752 (implied from 1Q26 ER) + Q2 2026 MX: Ps. 37,439 (implied) — Note: H1 2026 Mexico = 1Q26 Ps. 39,752 + 2Q26 Ps. 37,439 = Ps. 77,191. Derived from 18 ⁱ H1 2026 EAA: 1Q26 Ps. 11,620 + 2Q26 Ps. 12,748 (implied from 8.4% growth on 2Q25 Ps. 13,436 base in constant currency, peso terms -1.8%) = Ps. 24,368. 1 ʲ H1 2026 LatAm: 1Q26 Ps. 10,735 + 2Q26 Ps. 9,843 (implied) = Ps. 20,578. 1 ᵏ FY2023 total derived from FY2024 $408,335M with -4.1% change noted in filings. 7 ˡ H1 2026 total = 1Q26 Ps. 100,658 + 2Q26 Ps. 105,056 = Ps. 205,714 18

### Adjusted EBITDA by Segment (MXN millions) and Margin (%)

| Segment | FY2024 EBITDA | FY2024 Margin | FY2025 EBITDA | FY2025 Margin | 2Q26 EBITDA | 2Q26 Margin | Source |
|---|---|---|---|---|---|---|---|
| North America | Ps. 15,813 | 8.4% | Ps. 17,117 | 9.0% | Ps. 4,424 | 10.0% | 19 |
| Mexico | Ps. 30,762 | 20.3% | Ps. 31,630 | 20.4% | Ps. 8,343 | 20.7% | 19 |
| EAA | Ps. 4,212 | 9.4% | Ps. 5,830 | 10.8% | Ps. 1,542 | 11.7% | 19 |
| Latin America | Ps. 3,603 | 9.0% | Ps. 3,552 | 8.1% | Ps. 893 | 7.7% | 19 |
| Grupo Bimbo | Ps. 55,474 | 13.6% | Ps. 59,456 | 13.9% | Ps. 15,113 | 14.4% | 13 |

Ex-FX Growth (Adj. EBITDA), FY2025 vs FY2024:

- North America: +2.4% 9
- Mexico: +2.8% 9
- EAA: +26.9% 9
- Latin America: -2.2% 9
- Grupo Bimbo: +4.7% 3

FY2021–FY2023 segment data: Not available in the documents retrieved. The annual reports reference FY2022–FY2024 Adj. EBITDA totals (Ps. 47,372 / Ps. 53,446 / Ps. 54,942 / Ps. 55,473) 2 but segment-level breakdowns for FY2021–FY2023 were not included in the available filings.

Source: S&P Global Earnings Releases and Annual Reports for Grupo Bimbo

## What Could Not Be Retrieved

- Grupo Bimbo (BMV:BIMBOA) — CIQ standardized financials, market cap, share price, diluted shares, EV, and all CIQ-derived ratios. The ticker resolved to an incorrect entity ("Bmvb Immo"). All Bimbo data is sourced from company filings only.
- Gruma (BMV:GRUMAB) — All data. Ticker resolved to "Bevgru Ab" — no financial or pricing data returned.
- Yamazaki Baking (TSE:2212) — Share price, market cap, and EV not available from the pricing feed.
- Arca Continental (BMV:AC) — Market cap and EV from the pricing tool are unreliable (resolved to AON/Aon plc). EV from the CIQ financials tool used instead; share price not confirmed.
- Moody's ratings — Entitlement denied for all companies.
- Fitch ratings — Not returned for any company.
- Historical rating changes (10-year) — Entitlement denied.
- Debt by currency (USD/local/EUR) and fixed vs. floating split — Not available in CIQ data returned for any company. Bimbo partial disclosure only (MXN bond issuance noted 3).
- FFO/total debt, debt/equity ratios — Not returned in the leverage query.
- Average cost of debt — Not returned for peers; Bimbo partial ("6.x%", truncated) 2
- 5-year and 10-year average/median EV/EBITDA and P/E — Query returned an error (median not supported; average not returned).
- P/FCF, FCF yield, dividend yield, buybacks, payout ratio — Not returned in the multiples tool.
- Bimbo consensus estimates (FY2026E–FY2028E) — No estimates returned (entity not resolved).
- Bimbo segment data for FY2021–FY2023 — Not in available document extracts.
- Organic/ex-FX revenue growth for peers — Not available in CIQ financials output (available only for Bimbo from company filings).
- Capex absolute values and capex/sales for Bimbo — Not in CIQ standardized data; available only in company filings (not fully extracted here).
- Net debt + leases (IFRS 16) basis — Bimbo discloses Adj. EBITDA excluding IFRS 16 1; lease-adjusted net debt not separately quantified in available data for peers.
- Minority interest dollar values — Returned as N/A for all companies.
- Gruma financial data — Entirely absent.

Footnote: * Deal directly or indirectly involved a private equity investor.
