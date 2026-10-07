---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Financials/Templated/Pension Details/SPGlobal_GrupoBimbo,S.A.B.deC.V._PensionDetails_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Balance Sheet/SPGlobal_GrupoBimbo,S.A.B.deC.V._BalanceSheet_19-Sep-2026.xlsx
  - filings/annual/IA25_GB_EEFF_V10.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T22_0.pdf
tags: [Financials, pensions]
---

# Grupo Bimbo — Pension Obligations (Capital IQ)

Defined-benefit (DB) pension roll-forward, plan assets and asset mix as carried by S&P Capital IQ (CIQ), **downloaded 2026-09-19**. MXN **thousands** in the file, shown in **MXN millions**. The DB data sit only in the FQ4 columns (CIQ "Benefit Info Date" = 31 December of each year, 2012-2025, with 2014 missing) [sourced] CIQ-PEN row "Benefit Info Date". Tidy data: `data/capitaliq/pensions.csv`. Balance-sheet context: [[ciq-balance-sheet-history]]; MEPP background: [[bimbo-ifrs-adjustments]], [[bimbo-risk-factors]].

**Citation key.** `CIQ-PEN` = Pension Details file, sheet 'Pension Details'. `CIQ-BS` = Balance Sheet file. `IA25-EEFF` = audited FY25 statements, employee-benefits note on PDF p.77-78.

## 1. Defined-benefit obligation roll-forward, 2019-2025

MXN millions, `[sourced]` CIQ-PEN (FQ4 columns). CIQ's label is "Actuarial Gain" but positive values **increase** the obligation (i.e., they are actuarial losses).

| Line | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Opening DBO | 30,378 | 37,839 | 42,386 | 41,401 | 27,465 | 27,163 | 28,382 |
| Service cost | 717 | 991 | 1,128 | 1,013 | 837 | 942 | 909 |
| Interest cost | 1,618 | 1,851 | 1,745 | 1,867 | 1,821 | 2,073 | 2,140 |
| Actuarial (gain) / loss | 7,709 | 3,515 | (2,536) | (8,382) | 529 | (1,835) | 1,326 |
| Benefits paid | (1,827) | (2,552) | (2,285) | (6,625) | (1,727) | (2,211) | (2,281) |
| FX translation | (756) | 1,372 | 963 | (1,500) | (1,762) | 2,250 | (1,443) |
| Acquisitions / other | – | 1,000 / (631) | – | (309) | – | – | – |
| **Closing DBO (PBO)** | **37,839** | **42,386** | **41,401** | **27,465** | **27,163** | **28,382** | **29,033** |

## 2. Plan assets and funded status

| Line | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Tag |
|---|---|---|---|---|---|---|---|---|
| Opening plan assets | 25,394 | 29,253 | 34,790 | 36,823 | 24,413 | 24,788 | 26,684 | [sourced] CIQ-PEN |
| Actual return | 4,269 | 4,242 | 514 | (6,226) | 1,784 | 676 | 2,943 | [sourced] CIQ-PEN |
| Employer contributions | 1,345 | 1,483 | 2,064 | 1,000 | 897 | 88 | 75 | [sourced] CIQ-PEN |
| Benefits paid from plan | (1,074) | (1,382) | (1,427) | (5,732) | (647) | (932) | (856) | [sourced] CIQ-PEN |
| FX translation | (681) | 1,194 | 882 | (1,452) | (1,659) | 2,064 | (1,337) | [sourced] CIQ-PEN |
| **Closing plan assets** | **29,253** | **34,790** | **36,823** | **24,413** | **24,788** | **26,684** | **27,509** | [sourced] CIQ-PEN |
| Funded status (assets − PBO) | (8,586) | (7,596) | (4,578) | (3,052) | (2,375) | (1,698) | (1,524) | [calc] |
| Funded ratio | 77.3% | 82.1% | 88.9% | 88.9% | 91.3% | 94.0% | 94.8% | [calc] |
| CIQ "Debt equiv. of unfunded PBO" | 8,586 | 7,596 | 4,578 | 3,052 | 2,375 | 1,698 | 1,524 | [sourced] CIQ-BS |

| Asset mix (% of plan assets) | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Equities | 23.5% | 25.8% | 19.7% | 25.6% | 25.6% | 26.0% | 26.8% |
| Fixed income | 69.1% | 66.5% | 69.2% | 66.7% | 63.5% | 65.1% | 64.2% |
| Other | 7.4% | 7.7% | 11.2% | 7.6% | 11.0% | 8.9% | 9.0% |

`[sourced]` CIQ-PEN breakdown rows; 2025 amounts: equities 7,381, fixed income 17,660, other 2,468.

- ==The DB deficit has shrunk from 8,586 (2019) to 1,524 (2025)== [calc], helped by actuarial gains in 2021-2022 and positive asset returns in 2023-2025. With the plan ~95% funded, company contributions have fallen to 88 (2024) and 75 (2025) from 1,000-2,064 in 2019-2022 [sourced] CIQ-PEN.
- 2022 was a step change: PBO fell by 13,936 [calc], driven by an 8,382 actuarial gain and 6,625 of benefits paid (5,732 paid out of plan assets) [sourced] CIQ-PEN.
- CIQ does **not** add the pension deficit into its Net Debt; it reports it separately as a debt equivalent (1,524 at Dec-25) [sourced] CIQ-BS.
- Defined-contribution cost appears only in FQ1 columns: 526 (2019 FQ1), 603 (2020 FQ1), 649 (2022 FQ1), 635 (2023 FQ1), 595 (2024 FQ1), 742 (2025 FQ1) [sourced] CIQ-PEN. Which fiscal year each figure covers is not stated [unverified].

> [!question] The 2022 benefits paid of 6,625 (vs ~1,700-2,600 in other years) looks like a settlement or annuity transfer. The CIQ file does not say. Check the FY22 employee-benefits note (Reporte Anual 2022) before treating 2022 as a normal year in any pension cost trend.

## 3. Balance-sheet pension line vs DB deficit

| Year-end | CIQ-BS "Pension & Other Post-Retire. Benefits" | DB deficit (CIQ-PEN) [calc] | Residual (other plans, MEPP, other benefits) [calc] |
|---|---|---|---|
| 2019 | 32,810 | 8,586 | 24,224 |
| 2020 | 36,407 | 7,596 | 28,811 |
| 2021 | 33,082 | 4,578 | 28,504 |
| 2022 | 11,457 | 3,052 | 8,405 |
| 2023 | 9,250 | 2,375 | 6,875 |
| 2024 | 7,840 | 1,698 | 6,142 |
| 2025 | 7,492 | 1,524 | 5,968 |

- The residual collapsed by ~20,100 in 2022 [calc], the year the company reversed the provision for multi-employer pension plans (MEPPs), a non-cash benefit of US$734 mn in 4Q22 and US$934 mn for the full year ("ajuste al pasivo de los MEPPs") [sourced] 4T22 p.7-8. That the residual mainly represents the MEPP liability is an inference from timing [unverified]; the CIQ files do not label it.

## 4. Reconciliation with the audited FY25 note

| Item (MXN mn) | CIQ 2025 | IA25-EEFF 2025 | CIQ 2024 | IA25-EEFF 2024 | CIQ 2023 | IA25-EEFF 2023 |
|---|---|---|---|---|---|---|
| Present value of DBO | 29,033 | 29,033 | 28,382 | 28,382 | 27,163 | 27,163 |
| Fair value of plan assets | 27,509 | 27,509 | 26,684 | 26,684 | 24,788 | 24,788 |
| Deficit | 1,524 | 1,524 | 1,698 | 1,698 | 2,375 | 2,375 |
| Service cost | 909 | 909 | 942 | 942 | 837 | 837 |
| Interest cost | 2,140 | 2,140 | 2,073 | 2,073 | 1,821 | 1,821 |
| Benefits paid (DBO) | (2,281) | (2,281) | (2,211) | (2,211) | (1,727) | (1,727) |
| FX on DBO | (1,443) | (1,443) | 2,250 | 2,250 | (1,762) | (1,762) |
| Return on assets (interest income + remeasurement) | 2,943 | 2,002 + 941 = 2,943 [calc] | 676 | 1,895 − 1,219 = 676 [calc] | 1,784 | 1,657 + 127 = 1,784 [calc] |

All IA25-EEFF figures `[sourced]` IA25-EEFF p.77-78. ==CIQ pension data tie exactly to the audited note for 2023-2025.==

## Key Takeaways

- CIQ's DB pension data are annual (FQ4) and tie exactly to the audited FY25 note for 2023-2025 (PBO 29,033; assets 27,509; deficit 1,524 at Dec-25).
- The DB plans are ~95% funded at Dec-25, up from 77% in 2019 [calc]; employer contributions have dropped to under MXN 100 mn a year.
- The DB deficit (1.5 bn) is a small part of the 7.5 bn balance-sheet pension line; the remainder is other post-employment / multi-employer obligations not itemised by CIQ.
- The 2022 collapse of the balance-sheet pension line (−21.6 bn) coincides with the MEPP provision reversal; 2022 DB flows (benefits paid 6,625) are atypical.
- CIQ keeps the pension deficit out of Net Debt; add it explicitly if the valuation treats it as debt-like.
