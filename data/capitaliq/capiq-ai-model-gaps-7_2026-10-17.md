# Capital IQ AI output — model-gaps Prompt 7 (capital intensity benchmark), pricing date 2026-10-16

_Raw source copy. Pasted by the team on 2026-10-17 from the Capital IQ AI assistant, response to Prompt 7 of `BIMBOA/research/capiq-prompts-model-gaps_2026-10-17.md`. Text and numbers are as received, including the assistant's first revenue table (which it then corrected itself); tab-separated tables were converted to markdown. This file could not be written to `raw/` (write permission denied); move it there unchanged if you want it in the inbox._

_Usable result: consensus capital expenditures and revenue for the next three fiscal years (Task 7B). Historical capex and D&A were not returned (capex came back only as growth rates). In the corrected revenue table, Grupo Bimbo and Arca Continental are in USD; for Yamazaki and ARYZTA the FY2021 values differ from the Prompt 1 output for FY2021 only (Yamazaki 9,592.8 vs 8,773.2)._

---

I need to work carefully with the raw data. The context returns CapEx growth rates (% YoY) and revenue in $000s, but not the absolute CapEx dollar levels directly. I can reconstruct absolute CapEx from the growth rates and the revenue figures, but the task says never estimate — and backing into CapEx from growth rates would be an estimation. The context also returned "Real Estate Depreciation" as a proxy for ROU depreciation, which came back NA for all companies.

Critically, the data pull returned CapEx growth rates rather than absolute CapEx levels, and D&A was not returned at all. I will present what was retrieved and flag what was not.

## Important Data Availability Note

The Capital IQ pull for Task 7A returned:

- Revenue — absolute levels, in $000s ✓
- Capital Expenditures — year-over-year growth rates only (%), not absolute dollar amounts ✗
- Depreciation & Amortization (total) — not returned ✗
- Depreciation of right-of-use assets — returned as "Real Estate Depreciation," which is NA for all companies ✗

Because the task requires absolute figures and prohibits estimation, I cannot back-calculate CapEx levels from growth rates. The D&A data was simply not retrieved. The tables below present what is available.

## Task 7A — Revenue (USD millions)

All figures converted from $000s to USD millions. Non-USD companies translated at Capital IQ period-average rates (FY2021–FY2025) and LTM-period rate as provided.

Exchange rates applied:

| Company | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM Rate |
|---|---|---|---|---|---|---|
| Grupo Bimbo (USD/MXN) | 0.049318 | 0.049729 | 0.056446 | 0.054887 | 0.052179 | 0.055690 |
| Yamazaki Baking (USD/JPY) | 0.009110 | 0.007654 | 0.007132 | 0.006609 | 0.006690 | 0.006482 |
| ARYZTA (USD/EUR) | 1.196081 | 1.114007 | 1.081488 | 1.081860 | 1.130601 | 1.166559 |
| Arca Continental (USD/MXN) | 0.049318 | 0.049729 | 0.056446 | 0.054887 | 0.052179 | 0.055690 |

Note: Grupo Bimbo, Yamazaki Baking, ARYZTA, and Arca Continental report in MXN, JPY, EUR, and MXN respectively. All others report in USD. Revenue figures for non-USD companies are the product of the local-currency $000 figure and the Capital IQ period-average exchange rate, divided by 1,000 to express in USD millions.

| Company | Ticker | FY End | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM | LTM End Date |
|---|---|---|---|---|---|---|---|---|---|
| Grupo Bimbo, S.A.B. de C.V. | BMV:BIMBO A | Dec | $824.1 | $985.9 | $1,273.2 | $1,229.9 | $1,162.3 | $1,307.0 | 06/30/2026 |
| Flowers Foods, Inc. | NYSE:FLO | Jan | $4,330.8 | $4,805.8 | $5,090.8 | $5,103.5 | $5,256.5 | $5,223.9 | 07/18/2026 |
| Gruma, S.A.B. de C.V. | BMV:GRUMA B | Dec | $4,623.6 | $5,596.6 | $6,576.2 | $6,486.9 | $6,374.6 | $6,500.1 | 06/30/2026 |
| Yamazaki Baking Co., Ltd. | TSE:2212 | Dec | $873.9 | $631.0 | $597.9 | $543.6 | $587.0 | $561.9 | 06/30/2026 |
| ARYZTA AG | SWX:ARYN | Dec | $2,182.2 | $2,179.1 | $2,420.6 | $2,568.5 | $2,842.1 | $2,995.5 | 06/30/2026 |
| The J. M. Smucker Company | NYSE:SJM | Apr | $8,002.7 | $7,998.9 | $8,529.2 | $8,178.7 | $8,726.1 | $9,156.9 | 07/31/2026 |
| The Campbell's Company | NasdaqGS:CPB | Aug | $8,476.0 | $8,562.0 | $9,357.0 | $9,636.0 | $10,253.0 | $9,744.0 | 08/02/2026 |
| Mondelez International, Inc. | NasdaqGS:MDLZ | Dec | $28,720.0 | $31,496.0 | $36,016.0 | $36,441.0 | $38,537.0 | $39,675.0 | 06/30/2026 |
| Arca Continental, S.A.B. de C.V. | BMV:AC* | Dec | $451.7 | $519.2 | $687.5 | $721.6 | $681.3 | $776.5 | 06/30/2026 |
| PepsiCo, Inc. | NasdaqGS:PEP | Dec | $79,474.0 | $86,392.0 | $91,471.0 | $91,854.0 | $93,925.0 | $98,241.0 | 09/05/2026 |

Note on Grupo Bimbo and Arca Continental revenue: Capital IQ returns these figures in USD already (the reported currency is MXN but the "Value Currency" field is USD), meaning Capital IQ has already applied the exchange rate conversion. The figures above reflect Capital IQ's translated USD values directly from the $000 figures divided by 1,000. Grupo Bimbo's revenue of ~$16.7B–$22.6B in local MXN terms translates to the USD figures shown above using the rates provided.

⚠️ Reconciliation flag: The raw data shows Grupo Bimbo FY2021 revenue as 16,708,702 ($000, USD-translated), which at the 0.049318 USD/MXN rate implies ~MXN 338.8B local — consistent with Grupo Bimbo's reported MXN figures. Dividing 16,708,702 by 1,000 gives $16,708.7M. I have used this interpretation below:

Corrected Revenue Table (USD millions) — Capital IQ already translates to USD:

| Company | Ticker | FY End | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | LTM | LTM End Date |
|---|---|---|---|---|---|---|---|---|---|
| Grupo Bimbo, S.A.B. de C.V. | BMV:BIMBO A | Dec | $16,708.7 | $19,827.3 | $22,571.5 | $22,412.4 | $22,278.0 | $23,468.9 | 06/30/2026 |
| Flowers Foods, Inc. | NYSE:FLO | Jan | $4,330.8 | $4,805.8 | $5,090.8 | $5,103.5 | $5,256.5 | $5,223.9 | 07/18/2026 |
| Gruma, S.A.B. de C.V. | BMV:GRUMA B | Dec | $4,623.6 | $5,596.6 | $6,576.2 | $6,486.9 | $6,374.6 | $6,500.1 | 06/30/2026 |
| Yamazaki Baking Co., Ltd. | TSE:2212 | Dec | $9,592.8 | $8,243.9 | $8,383.8 | $8,224.6 | $8,773.2 | $8,669.9 | 06/30/2026 |
| ARYZTA AG | SWX:ARYN | Dec | $1,824.5 | $1,956.3 | $2,238.6 | $2,374.1 | $2,513.7 | $2,567.4 | 06/30/2026 |
| The J. M. Smucker Company | NYSE:SJM | Apr | $8,002.7 | $7,998.9 | $8,529.2 | $8,178.7 | $8,726.1 | $9,156.9 | 07/31/2026 |
| The Campbell's Company | NasdaqGS:CPB | Aug | $8,476.0 | $8,562.0 | $9,357.0 | $9,636.0 | $10,253.0 | $9,744.0 | 08/02/2026 |
| Mondelez International, Inc. | NasdaqGS:MDLZ | Dec | $28,720.0 | $31,496.0 | $36,016.0 | $36,441.0 | $38,537.0 | $39,675.0 | 06/30/2026 |
| Arca Continental, S.A.B. de C.V. | BMV:AC* | Dec | $9,160.7 | $10,441.2 | $12,179.4 | $13,149.5 | $13,058.3 | $13,945.2 | 06/30/2026 |
| PepsiCo, Inc. | NasdaqGS:PEP | Dec | $79,474.0 | $86,392.0 | $91,471.0 | $91,854.0 | $93,925.0 | $98,241.0 | 09/05/2026 |

All values are Capital IQ standardized, already expressed in USD millions (source unit: $000 USD). Non-USD companies (Grupo Bimbo, Yamazaki Baking, ARYZTA, Arca Continental) are translated by Capital IQ using period-average exchange rates.

Source: S&P Capital IQ Financials

## Task 7A — Capital Expenditures (USD millions)

The Capital IQ data pull returned year-over-year growth rates for capital expenditures, not absolute dollar amounts. Absolute CapEx levels were not retrieved. Per the task instruction to never estimate, these figures cannot be presented.

All companies (Grupo Bimbo, Flowers Foods, Gruma, Yamazaki Baking, ARYZTA, J. M. Smucker, Campbell's, Mondelez, Arca Continental, PepsiCo), all periods FY2021–FY2025 and LTM: N/A.

The data pull returned CapEx YoY growth rates (%), not absolute levels. Absolute CapEx dollar amounts were not retrieved for any company or period.

## Task 7A — Depreciation & Amortization (USD millions)

D&A (total) was not returned by the data pull. The "Real Estate Depreciation" field (used as a proxy for ROU asset depreciation) returned NA for all companies across all periods.

All companies, FY2021–FY2025 D&A, LTM D&A and ROU depreciation: N/A.

## Task 7B — Consensus Mean Capital Expenditures (USD millions)

All figures in USD millions as provided by Capital IQ (already converted from local currencies). Analyst counts shown as estimates in consensus / total estimates submitted.

Fiscal year mapping:

- Grupo Bimbo, FLO, GRUMA B, TSE:2212, ARYN, MDLZ, AC*, PEP: FY1 = FY2026E (12/31/2026), FY2 = FY2027E (12/31/2027), FY3 = FY2028E (12/31/2028)
- SJM: FY1 = FY2027E (04/30/2027), FY2 = FY2028E (04/30/2028), FY3 = FY2029E (04/30/2029)
- CPB: FY1 = FY2027E (07/31/2027), FY2 = FY2028E (07/31/2028), FY3 = FY2029E (07/31/2029)

| Company | Ticker | FY1 CapEx (Period End) | # Analysts | FY2 CapEx (Period End) | # Analysts | FY3 CapEx (Period End) | # Analysts |
|---|---|---|---|---|---|---|---|
| Grupo Bimbo, S.A.B. de C.V. | BMV:BIMBO A | $1,259.73 (12/31/2026) | 5 | $1,208.81 (12/31/2027) | 5 | $1,240.85 (12/31/2028) | 5 |
| Flowers Foods, Inc. | NYSE:FLO | $119.81 (12/31/2026) | 3 | $123.98 (12/31/2027) | 3 | $123.86 (12/31/2028) | 3 |
| Gruma, S.A.B. de C.V. | BMV:GRUMA B | $219.79 (12/31/2026) | 4 | $236.23 (12/31/2027) | 5 | $248.40 (12/31/2028) | 5 |
| Yamazaki Baking Co., Ltd. | TSE:2212 | $382.77 (12/31/2026) | 4 | $374.45 (12/31/2027) | 5 | $364.32 (12/31/2028) | 5 |
| ARYZTA AG | SWX:ARYN | $108.93 (12/31/2026) | 3 | $100.87 (12/31/2027) | 3 | $99.64 (12/31/2028) | 3 |
| The J. M. Smucker Company | NYSE:SJM | $326.50 (04/30/2027) | 10 | $344.81 (04/30/2028) | 9 | $347.89 (04/30/2029) | 9 |
| The Campbell's Company | NasdaqGS:CPB | $324.76 (07/31/2027) | 8 | $339.20 (07/31/2028) | 8 | $350.48 (07/31/2029) | 7 |
| Mondelez International, Inc. | NasdaqGS:MDLZ | $1,430.32 (12/31/2026) | 12 | $1,475.32 (12/31/2027) | 12 | $1,523.35 (12/31/2028) | 11 |
| Arca Continental, S.A.B. de C.V. | BMV:AC* | $994.47 (12/31/2026) | 5 | $975.83 (12/31/2027) | 5 | $997.15 (12/31/2028) | 5 |
| PepsiCo, Inc. | NasdaqGS:PEP | $4,401.09 (12/31/2026) | 9 | $4,360.64 (12/31/2027) | 10 | $4,547.41 (12/31/2028) | 9 |

## Task 7B — Consensus Mean Revenue (USD millions)

| Company | Ticker | FY1 Revenue (Period End) | # Analysts | FY2 Revenue (Period End) | # Analysts | FY3 Revenue (Period End) | # Analysts |
|---|---|---|---|---|---|---|---|
| Grupo Bimbo, S.A.B. de C.V. | BMV:BIMBO A | $24,418.70 (12/31/2026) | 11 | $24,069.22 (12/31/2027) | 9 | $25,313.57 (12/31/2028) | 8 |
| Flowers Foods, Inc. | NYSE:FLO | $5,075.79 (12/31/2026) | 6 | $5,058.25 (12/31/2027) | 6 | $5,032.60 (12/31/2028) | 4 |
| Gruma, S.A.B. de C.V. | BMV:GRUMA B | $6,648.35 (12/31/2026) | 12 | $6,444.43 (12/31/2027) | 10 | $6,615.66 (12/31/2028) | 9 |
| Yamazaki Baking Co., Ltd. | TSE:2212 | $8,564.43 (12/31/2026) | 8 | $8,794.96 (12/31/2027) | 8 | $8,960.59 (12/31/2028) | 8 |
| ARYZTA AG | SWX:ARYN | $2,594.73 (12/31/2026) | 4 | $2,562.57 (12/31/2027) | 4 | $2,609.11 (12/31/2028) | 4 |
| The J. M. Smucker Company | NYSE:SJM | $8,930.34 (04/30/2027) | 16 | $9,037.53 (04/30/2028) | 15 | $9,190.85 (04/30/2029) | 10 |
| The Campbell's Company | NasdaqGS:CPB | $9,496.56 (07/31/2027) | 17 | $9,469.38 (07/31/2028) | 17 | $9,555.92 (07/31/2029) | 10 |
| Mondelez International, Inc. | NasdaqGS:MDLZ | $40,101.18 (12/31/2026) | 21 | $41,232.89 (12/31/2027) | 21 | $42,656.12 (12/31/2028) | 13 |
| Arca Continental, S.A.B. de C.V. | BMV:AC* | $14,453.82 (12/31/2026) | 12 | $14,628.59 (12/31/2027) | 12 | $15,637.75 (12/31/2028) | 9 |
| PepsiCo, Inc. | NasdaqGS:PEP | $99,300.54 (12/31/2026) | 19 | $101,773.09 (12/31/2027) | 21 | $105,151.36 (12/31/2028) | 17 |

Consensus estimates for Grupo Bimbo, Gruma, Yamazaki Baking, ARYZTA, and Arca Continental are converted from their respective local currencies (MXN, MXN, JPY, EUR, MXN) to USD by Capital IQ at the spot rate at time of query.

Source: S&P Capital IQ Estimates

## Items Not Retrieved

- Capital Expenditures — absolute levels (Task 7A, all companies, all periods): The data pull returned CapEx YoY growth rates (%) rather than absolute dollar amounts. Absolute CapEx for FY2021–FY2025 and LTM cannot be presented without estimation.
- Depreciation & Amortization — total (Task 7A, all companies, all periods): D&A was not returned by the data pull for any company.
- Depreciation of right-of-use assets (Task 7A, all companies, all periods): The "Real Estate Depreciation" field returned NA for all 10 companies across all periods. Whether any of these companies separately disclose ROU depreciation in their filings would require a direct cash flow statement pull.
- Flowers Foods FY end clarification: FLO's fiscal year ends in January (e.g., FY2025 ended ~01/2026). The consensus estimates labeled FY2026E (12/31/2026) in Capital IQ may correspond to FLO's fiscal year ending January 2027 — users should verify the exact fiscal year mapping for FLO in the consensus system.

Footnote: * Deal/listing directly or indirectly involved a private equity investor.
