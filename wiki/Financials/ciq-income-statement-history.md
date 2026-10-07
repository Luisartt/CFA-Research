---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Financials/Templated/Income Statement/SPGlobal_GrupoBimbo,S.A.B.deC.V._IncomeStatement_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Income Statement/SPGlobal_GrupoBimbo,S.A.B.deC.V._IncomeStatement_19-Sep-2026 (1).xlsx
  - filings/capitaliq/Financials/Templated/Financial Highlights/SPGlobal_GrupoBimbo,S.A.B.deC.V._FinancialHighlights_19-Sep-2026 (1).xlsx
  - filings/annual/IA25_GB_EEFF_V10.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T21.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T22_0.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T23_VF.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T24.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T25.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%201T24.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%201T25.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%202T25.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%203T25_VF.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%201T26_VFF.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%202T26_VF.pdf
tags: [Financials, income-statement]
---

# Grupo Bimbo — Income Statement History (Capital IQ)

S&P Capital IQ (CIQ) "Standard" template income statement for BIMBOA, **downloaded 2026-09-19**. Export settings (rows 5-11 of the sheet): fiscal periods, **quarters only** (1995 FQ1 to 2026 FQ2, 120 columns), reporting basis **Current/Restated**, reported currency **MXN**, magnitude **thousands**. Shown here in **MXN millions** (÷1,000). Tidy data: `data/capitaliq/income_statement.csv` (one row per metric × quarter; `NA` cells dropped; CIQ restatement and calculation codes kept per column). Company-reported view: [[bimbo-income-statement-fy21-fy25]], [[bimbo-quarterly-trend-4q21-2q26]]. Ratios: [[ciq-key-ratios-and-performance]].

**Citation key.** `CIQ-IS` = Income Statement file, sheet 'Income Statement'. `CIQ-FH` = Financial Highlights file, sheet 'Financial Highlights'. `IA25-EEFF` = audited FY25 statements (`filings/annual/IA25_GB_EEFF_V10.pdf`, PDF page). `4T25`, `2T26`, etc. = earnings releases (`filings/quarterly/...`, PDF page).

## 1. What the export contains (read before using)

- ==The export has no annual columns.== Every FY figure below is the **sum of four CIQ quarters** and is tagged `[calc]`. CIQ's Q4 is itself derived (calculation code `Q4` = annual less 9M), so Q1-Q4 sums should equal CIQ's annual figure.
- ==2024 FQ4 is empty.== The column carries restatement code `DO` and calculation code `NA` and holds no income-statement values (only "Shares per Depositary Receipt" = 4) [sourced] CIQ-IS col DK. FY2024 therefore cannot be built from CIQ; only 9M24 is available. The same gap runs through the cash flow, highlights and ratio sheets ([[ciq-cash-flow-history]], [[ciq-key-ratios-and-performance]]).
- The two Income Statement files are the same data: the "(1)" copy is a formula-linked version (CIQ plug-in formulas render as `#NAME?` in the header); all 7,800 values match the plain file one-for-one [calc]. Same for the two Financial Highlights files (6,480 values match) [calc].
- Restatement codes in row 90 (not defined in the file; meaning per CIQ convention, not verified here): from 2020 FQ1 to 2025 FQ2 almost every quarter is `RS` (restated); 2025 FQ3 `NC`; 2025 FQ4 and 2026 FQ2 `O` (original); 2026 FQ1 `RS` [sourced] CIQ-IS rows 90-91. Filing dates in row 16 show each quarter was last taken from the following year's filing (e.g., 2024 FQ1 from the filing of 2025-04-29), i.e. ==CIQ carries the comparative-period restated figures, not the originally published ones==.
- CIQ "EBITDA" and "EBIT" are CIQ-standardised. CIQ strips items it classifies as unusual (restructuring, M&A-related, impairments, asset write-downs) out of operating income and books them below EBT-excl.-unusual-items. They are **not** the company's "UAFIDA Ajustada" or "Utilidad de Operación" (see section 5).

## 2. Annual history, FY2019-FY2025 (sum of quarters)

MXN millions. All `[calc]` = sum of CIQ-IS quarterly values for the year (inputs in `income_statement.csv`). 2024 = 9M only.

| Line (CIQ label) | FY19 | FY20 | FY21 | FY22 | FY23 | 9M24 | FY25 |
|---|---|---|---|---|---|---|---|
| Total Revenue | 291,926 | 331,051 | 338,792 | 398,706 | 399,879 | 298,023 | 426,963 |
| Cost Of Goods Sold | 137,378 | 152,383 | 157,003 | 192,732 | 193,720 | 140,748 | 202,722 |
| Gross Profit | 154,548 | 178,668 | 181,789 | 205,974 | 206,160 | 157,275 | 224,242 |
| Selling General & Admin Exp. | 127,211 | 146,429 | 147,963 | 167,254 | 165,748 | 127,323 | 184,186 |
| Operating Income (= CIQ EBIT) | 26,531 | 29,690 | 33,589 | 36,464 | 37,455 | 24,908 | 36,272 |
| EBITDA (CIQ) | 36,368 | 40,992 | 45,541 | 50,087 | 51,988 | 37,607 | 54,815 |
| Net Interest Exp. | (7,665) | (8,502) | (7,066) | (6,682) | (8,786) | (8,797) | (13,404) |
| EBT Incl. Unusual Items | 12,108 | 16,743 | 24,854 | 45,878 | 25,324 | 15,995 | 20,143 |
| Income Tax Expense | 4,733 | 6,192 | 8,726 | 14,381 | 8,386 | 5,472 | 7,197 |
| Earnings from Cont. Ops. | 7,375 | 10,551 | 16,128 | 31,497 | 16,938 | 10,523 | 12,946 |
| Earnings of Discontinued Ops. | – | – | 1,224 | 16,586 | 0 | – | – |
| Minority Int. in Earnings | (1,056) | (1,440) | (1,436) | (1,173) | (1,445) | (1,099) | (1,813) |
| **Net Income (to common)** | **6,319** | **9,111** | **15,916** | **46,910** | **15,477** | **9,424** | **11,133** |
| Normalized Net Income (CIQ) | 7,643 | 7,594 | 16,246 | 28,289 | 14,925 | 8,898 | 11,720 |

Derived margins `[calc]` (line ÷ Total Revenue, same inputs):

| Margin | FY19 | FY20 | FY21 | FY22 | FY23 | FY25 |
|---|---|---|---|---|---|---|
| Gross | 52.9% | 54.0% | 53.7% | 51.7% | 51.6% | 52.5% |
| SG&A / revenue | 43.6% | 44.2% | 43.7% | 41.9% | 41.4% | 43.1% |
| EBITDA (CIQ) | 12.5% | 12.4% | 13.4% | 12.6% | 13.0% | 12.8% |
| EBIT (CIQ) | 9.1% | 9.0% | 9.9% | 9.1% | 9.4% | 8.5% |
| Net income | 2.2% | 2.8% | 4.7% | 11.8% | 3.9% | 2.6% |
| Effective tax rate (tax ÷ EBT incl. unusual) | 39.1% | 37.0% | 35.1% | 31.3% | 33.1% | 35.7% |

- FY2022 net income is inflated by discontinued operations (Ricolino sale, 16,586 in CIQ "Earnings of Discontinued Ops." [calc]) and by a non-operating gain CIQ booked in 2022 FQ4 "Other Non-Operating Inc." of 17,887 [sourced] CIQ-IS 2022 FQ4. The company attributes 2022's extraordinary items to the Ricolino sale and the non-cash reversal of the MEPP (multi-employer pension plan) provision [sourced] 4T22 p.2, p.7. CIQ "NI to Common Excl. Extra Items" FY22 = 30,324 [calc].
- FY2021 in CIQ is the **restated** figure (Ricolino reclassified to discontinued ops): quarterly revenue 76,929 + 81,654 + 85,659 + 94,550 = 338,792 [calc]; see Reconciliation.
- Interest burden: CIQ net interest expense rose from 8,786 (FY23) to 13,404 (FY25) [calc], +52.6% [calc].
- Dividends per share sit in the FQ4 column: FY19 0.50; FY20 1.00; FY21 0.65; FY22 0.78; FY23 0.94; FY25 1.075 MXN [sourced] CIQ-IS row 67, FQ4 columns. FY24 not available (empty column). Detail: [[bimbo-shareholder-returns]].
- Weighted average diluted shares (FQ4 column): 4,679 mn (2019) → 4,326 mn (2025 FQ4) [sourced] CIQ-IS row 64.

## 3. Quarterly detail, 1Q25-2Q26

MXN millions, `[sourced]` CIQ-IS (columns DL-DQ) unless tagged. Margins `[sourced]` CIQ Performance Analysis.

| Line | 1Q25 | 2Q25 | 3Q25 | 4Q25 | 1Q26 | 2Q26 |
|---|---|---|---|---|---|---|
| Total Revenue | 103,448 | 107,389 | 107,421 | 108,706 | 100,282 | 105,026 |
| Gross Profit | 54,686 | 56,667 | 56,191 | 56,697 | 53,347 | 55,255 |
| Gross margin | 52.9% | 52.8% | 52.3% | 52.2% | 53.2% | 52.6% |
| Other Operating Expense | 1,692 | 849 | 1,186 | 58 | (949) | 1,049 |
| EBITDA (CIQ) | 11,270 | 13,190 | 14,048 | 16,307 | 14,597 | 13,493 |
| EBITDA margin | 10.9% | 12.3% | 13.1% | 15.0% | 14.6% | 12.8% |
| EBIT (CIQ) | 6,741 | 8,478 | 9,403 | 11,651 | 10,031 | 8,827 |
| Interest Expense | (3,515) | (3,558) | (3,284) | (3,945) | (2,765) | (3,901) |
| Unusual items (net, EBT incl. − excl.) [calc] | 0 | 0 | 0 | (1,510) | (2,120) | 0 |
| Net Income | 1,785 | 2,826 | 3,364 | 3,158 | 2,362 | 2,935 |
| Diluted EPS (MXN) | 0.41 | 0.65 | 0.78 | 0.73 | 0.55 | 0.68 |

- 1H26 vs 1H25 `[calc]`: revenue 205,308 vs 210,836 (−2.6%); CIQ EBITDA 28,089 vs 24,460 (+14.8%); CIQ EBIT 18,858 vs 15,218 (+23.9%); net income 5,297 vs 4,611 (+14.9%).
- LTM to 2Q26 `[calc]` (3Q25-2Q26): revenue 421,435; CIQ EBITDA 58,444 (13.9% margin); CIQ EBIT 39,912; net income 11,819.
- Unusual items in 4Q25: Restructuring Charges (3,908), Merger & Related Restruct. Charges +2,300, Gain on Sale of Assets +122, Asset Writedown (24) [sourced] CIQ-IS 2025 FQ4. 1Q26: Merger & Related (2,076), Gain/Loss on assets (20), Writedown (25) [sourced] CIQ-IS 2026 FQ1.
- CIQ books a restructuring charge in **every** FQ4 of the history checked: FY19 (2,132), FY20 (1,143), FY21 (2,059), FY22 (1,657), FY23 (2,959), FY25 (3,908) [sourced] CIQ-IS row 39. "Merger & Related Restruct. Charges" is a **positive** (income) line in FQ4 of FY20-FY25 (1,082 to 2,300) [sourced] CIQ-IS row 40.

> [!question] Why is CIQ's "Merger & Related Restruct. Charges" a recurring income item in Q4 (e.g., +2,300 in 4Q25)? The file does not say which company line it maps from. Check against the "Otros gastos netos" note in IA25-EEFF before relying on CIQ EBIT.

## 4. Data-quality flags

| Issue | Detail | Tag |
|---|---|---|
| 2024 FQ4 missing | No P&L values; FY2024 not constructible; Q4 growth rates in CIQ for 4Q25 show `NA` | [sourced] CIQ-IS col DK |
| Share count error 2Q24 | Weighted avg. shares 2,551 mn vs ~4,350 mn in adjacent quarters → EPS 1.30 vs 0.55 / 0.85 around it | [sourced] CIQ-IS 2024 FQ2 row 61, 59 |
| FY2025 revenue +11 vs audited | CIQ sum 426,963 vs audited 426,952 | [calc] vs [sourced] IA25-EEFF p.85 |
| 1Q26 restated in CIQ | CIQ 100,282 (code `RS`, filing 2026-07-24) vs 1T26 release 100,319 | [sourced] CIQ-IS; 1T26 p.9 |
| Non-operating lines incomplete | "Currency Exchange Gains" and "Other Non-Operating Inc." are `NA` in 2Q25 and 2Q26, so FY25 sums are not available | [sourced] CIQ-IS rows 36-37 |
| Payout ratio row | Values such as 163% (2Q26) are CIQ quarterly calculations on dividends paid vs quarterly NI; not meaningful as an annual payout | [sourced] CIQ-IS row 68 |
| "Supplemental" one-offs | Advertising expense (3,329 in 1Q24; 3,832 in 1Q25) and Net Rental Expense appear only in FQ1 columns | [sourced] CIQ-IS rows 84, 87 |

## 5. Reconciliation with company filings

Company figures are as published in the FY earnings release or the audited statements; where a later release restated a year, both are shown. Differences = CIQ − company `[calc]`.

### Net sales

| FY | CIQ (sum of quarters) [calc] | Company | Source | Difference |
|---|---|---|---|---|
| 2021 | 338,792 | 338,792 (restated, Ricolino as discontinued) | [sourced] 4T22 p.3 | 0 |
| 2021 (as first published) | – | 348,887 | [sourced] 4T21 p.9 | −10,095 vs CIQ |
| 2022 | 398,706 | 398,706 | [sourced] 4T22 p.12 | 0 |
| 2023 | 399,879 | 399,879 | [sourced] 4T23 p.10 | 0 |
| 2024 | n/a (9M = 298,023) | 408,335 | [sourced] 4T24 p.10; IA25-EEFF p.86 | implied 4Q24 = 110,312 [calc] = release 4Q24 110,312 [sourced] 4T24 p.10 |
| 2025 | 426,963 | 426,952 | [sourced] 4T25 p.11; IA25-EEFF p.85 | **+11** |

- Quarter-level: CIQ shows the restated comparatives, which differ from first publication: 1Q24 93,641 (first published 93,221 [sourced] 1T24 p.8; restated 93,641 in 1T25 p.8); 1Q25 103,448 (first published 103,726 [sourced] 1T25 p.8; restated 103,448 in 1T26 p.9); 2Q25 107,389 (first published 107,503 [sourced] 2T25 p.8; restated 107,389 in 2T26 p.8). 3Q25 107,421 = 3T25 p.8. 4Q25 CIQ 108,706 vs release 108,688 [sourced] 4T25 p.11 → **+18**. 2Q26 105,026 = 2T26 p.8.

> [!warning] Superseded
> FY2021 net sales of 348,887 and adjusted EBITDA of 49,178 [sourced] 4T21 p.2, p.9 were superseded by 338,792 and 47,372 after Ricolino was classified as discontinued [sourced] 4T22 p.3. CIQ carries the restated basis.

### EBITDA

CIQ EBITDA is **not** the company's "UAFIDA Ajustada" (EBITDA before impairments and MEPPs, per 4T22 p.2 footnote 2). The gap is systematic and widening:

| FY | CIQ EBITDA [calc] | Company Adj. EBITDA | Source | CIQ − company |
|---|---|---|---|---|
| 2021 | 45,541 | 47,372 (restated) | [sourced] 4T22 p.3 | (1,831) |
| 2022 | 50,087 | 53,445 (table); 53,455 in the text | [sourced] 4T22 p.3, p.2 | (3,358) |
| 2023 | 51,988 | 54,942 | [sourced] 4T23 p.3 | (2,954) |
| 2024 | n/a (9M 37,607) | 55,474 | [sourced] 4T24 p.3 | n/a |
| 2025 | 54,815 | 59,456 | [sourced] 4T25 p.3 | (4,641) |

- The 4T22 release itself is internally inconsistent on FY22 adjusted EBITDA (53,445 in the summary table vs "53,455" in the bullet text) [sourced] 4T22 p.2-3.
- Likely drivers (not verified line-by-line): (i) CIQ EBITDA − CIQ EBIT FY25 = 18,543 [calc], well below the D&A in the audited cash flow, 24,838 [sourced] IA25-EEFF p.16, so the IS-line EBITDA does not add back all D&A (right-of-use depreciation is a candidate); (ii) CIQ removes restructuring/M&A items differently from the company's "adjusted" definition.
- CIQ itself uses a different EBITDA in its ratios (EBIT + cash-flow D&A): FY25 36,272 + 24,048 = 60,319 [calc], and the EBITDA implied by its Key Stats TEV/EBITDA multiple is 63,356 [calc] ([[ciq-key-ratios-and-performance]]). Three CIQ "EBITDAs" therefore exist for FY25 (54,815 / 60,319 / 63,356) against the company's 59,456.
- The Key Stats multiples back-solve to FY25 revenue of 426,952 (= audited) [calc], so the +11 difference arises only in CIQ's quarterly series (derived 4Q25). Use the company figure for any comparison with guidance; use CIQ EBITDA only for CIQ-consistent peer screens.
- Operating income: CIQ EBIT FY25 36,272 vs company "Utilidad de Operación" 34,146 [sourced] 4T25 p.11 → +2,126 [calc]. FY23: CIQ 37,455 vs company 35,455 [sourced] 4T23 p.3 → +2,000 [calc].

### Net income (majority / to common)

| FY | CIQ [calc] | Company "Utilidad Neta Mayoritaria" | Source | Difference |
|---|---|---|---|---|
| 2021 | 15,916 | 15,916 | [sourced] 4T21 p.2; 4T22 p.3 | 0 |
| 2022 | 46,910 | 46,910 | [sourced] 4T22 p.3 | 0 |
| 2023 | 15,477 | 15,477 | [sourced] 4T23 p.3; IA25-EEFF p.13 | 0 |
| 2024 | n/a (9M 9,424) | 12,545 (release) / 12,544 (audited) | [sourced] 4T24 p.3; IA25-EEFF p.13 | implied 4Q24 3,121 [calc] = release 4Q24 3,121 [sourced] 4T25 p.3 |
| 2025 | 11,133 | 11,133 | [sourced] 4T25 p.11; IA25-EEFF p.13 | 0 |

Net debt reconciliation: see [[ciq-balance-sheet-history]].

## Key Takeaways

- CIQ income-statement data for BIMBOA are quarterly only; annual figures must be summed, and ==FY2024 is missing because the 2024 FQ4 column is empty==.
- Revenue and net income tie to company filings to within MXN 11 mn (FY25 revenue) on the restated basis; CIQ carries restated comparatives, not first-published numbers.
- CIQ EBITDA runs MXN 1.8-4.6 bn below company Adjusted EBITDA (FY21-FY25); never mix the two in a leverage or multiple calculation.
- CIQ EBIT exceeds company operating income by ~MXN 2 bn (FY23, FY25) because CIQ reclassifies restructuring and M&A-related items below EBIT.
- 1H26 CIQ EBITDA rose 14.8% on 2.6% lower revenue [calc]; LTM-2Q26 CIQ EBITDA margin 13.9% [calc].
- Known CIQ errors: 2Q24 share count (EPS 1.30), 2024 FQ4 gap, incomplete non-operating lines in 2Q25/2Q26.
