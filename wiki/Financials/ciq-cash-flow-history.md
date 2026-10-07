---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Financials/Templated/Cash Flow Statement/SPGlobal_GrupoBimbo,S.A.B.deC.V._CashFlow_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Financial Highlights/SPGlobal_GrupoBimbo,S.A.B.deC.V._FinancialHighlights_19-Sep-2026 (1).xlsx
  - filings/annual/IA25_GB_EEFF_V10.pdf
tags: [Financials, cash-flow]
---

# Grupo Bimbo — Cash Flow History (Capital IQ)

S&P Capital IQ (CIQ) "Standard" cash flow statement for BIMBOA, **downloaded 2026-09-19**; fiscal quarters 1995 FQ1-2026 FQ2, Current/Restated basis, MXN **thousands** in the file, shown in **MXN millions**. Tidy data: `data/capitaliq/cash_flow.csv`. Company view: [[bimbo-cash-flow-and-fcf]]. Related: [[ciq-income-statement-history]], [[ciq-balance-sheet-history]], [[bimbo-capital-allocation]].

**Citation key.** `CIQ-CF` = Cash Flow file, sheet 'Cash Flow'. `IA25-EEFF` = audited FY25 statements (`filings/annual/IA25_GB_EEFF_V10.pdf`), consolidated cash flow statement on PDF p.16.

## 1. Coverage and gaps

- Quarterly only; most quarters carry calculation code `CFQ` (CIQ derives the discrete quarter from year-to-date figures) [sourced] CIQ-CF row "CIQ Calculation Type Code".
- ==Two years cannot be built from CIQ==: **FY2021** (2021 FQ2 column empty, restatement code `DO`) and **FY2024** (2024 FQ4 column empty, code `DO`) [sourced] CIQ-CF. Only "Change in Net Working Capital" is populated in those columns.
- Some lines are reported only in some quarters (CIQ `NA`, not zero): acquisitions, dividends and buybacks. Sums below flag how many quarters were reported.
- "Change In Income Taxes" appears only in FQ4 columns (e.g., (8,955) in 4Q25) [sourced] CIQ-CF; CIQ reclassifies the full-year tax-paid line into Q4.

## 2. Annual history (sum of quarters)

MXN millions; every cell `[calc]` = sum of CIQ-CF quarterly values (inputs in `cash_flow.csv`). Bracketed note = quarters reported where fewer than 4.

| Line (CIQ label) | FY19 | FY20 | FY22 | FY23 | 9M24 | FY25 | LTM 2Q26 |
|---|---|---|---|---|---|---|---|
| Cash from Ops. | 28,520 | 43,877 | 38,851 | 31,411 | 26,988 | 47,753 | 51,786 |
| D&A, Total | 14,373 | 16,251 | 18,282 | 18,929 | 16,529 | 24,048 | 23,870 |
| Capital Expenditure | (13,117) | (13,218) | (28,669) | (34,754) | (19,096) | (22,530) | (19,579) |
| Cash Acquisitions | (94) [2/4] | (3,453) | (6,520) [2/4] | (6,548) | (7,898) | (12,762) [3/4] | – |
| Cash from Investing | (12,642) | (16,688) | (9,122) | (42,440) | (26,214) | (34,652) | (20,519) |
| Total Debt Issued | 22,594 | 34,818 | 51,670 | 136,638 | 53,121 | 69,267 | – |
| Total Debt Repaid | (27,424) | (46,289) | (61,927) | (116,125) | (37,579) | (63,537) | – |
| Repurchase of Common Stock | (2,359) [3/4] | (4,388) | (2,912) [3/4] | (3,664) | (3,809) | (1,253) [3/4] | – |
| Total Dividends Paid | (2,400) [3/4] | (2,727) [3/4] | (5,791) | (3,960) [2/4] | (4,234) [1/3] | (4,451) [2/4] | – |
| Other Financing Activities | (7,855) | (6,225) | (6,732) | (6,985) | (6,925) | (11,934) | – |
| Cash from Financing | (16,833) | (24,163) | (25,692) | 5,904 | 574 | (11,908) | (21,644) |
| Cash Interest Paid (suppl.) | 5,681 | 6,410 | 6,407 | 7,436 | 6,925 | 11,533 | 11,779 |
| Cash Taxes Paid (suppl.) | 3,961 | 5,789 | 11,824 | 13,831 | 5,273 | 8,955 | 8,411 |
| Levered FCF (CIQ) | 9,536 | 22,665 | 13,502 | (10,625) | 3,841 | 16,361 | 25,433 |
| Unlevered FCF (CIQ) | 14,677 | 28,220 | 18,141 | (4,628) | 9,841 | 25,299 | 34,117 |

Derived `[calc]` (same inputs; revenue from [[ciq-income-statement-history]]):

| Metric | FY19 | FY20 | FY22 | FY23 | FY25 | LTM 2Q26 |
|---|---|---|---|---|---|---|
| CFO − capex | 15,403 | 30,659 | 10,182 | (3,343) | 25,223 | 32,207 |
| Capex / revenue | 4.5% | 4.0% | 7.2% | 8.7% | 5.3% | 4.6% |
| Capex / D&A | 0.91x | 0.81x | 1.57x | 1.84x | 0.94x | 0.82x |

- ==Capex cycle==: capex peaked at 34,754 in FY23 (8.7% of revenue) and fell to 22,530 in FY25 [calc]; 1H26 capex 6,892 vs 9,843 in 1H25 (−30.0%) [calc]. CIQ FY23 levered FCF was negative (−10,625) [calc].
- 1H26 vs 1H25 `[calc]`: CFO 25,186 vs 21,154 (+19.1%); CIQ levered FCF 15,331 vs 6,259.
- Interest paid nearly doubled from 6,407 (FY22) to 11,533 (FY25) [calc]; CIQ "Other Financing Activities" in most quarters equals cash interest paid with the opposite sign (e.g., 1Q25 −3,236.8 vs interest paid 3,236.8) [sourced] CIQ-CF, i.e. interest paid sits in financing, as in the company's own statement [sourced] IA25-EEFF p.16.
- FY2022 investing cash flow was small (−9,122) because CIQ booked +27,961 "Other Investing Activities" in 4Q22 [sourced] CIQ-CF 2022 FQ4, plus a 25,797 "Net Cash From Discontinued Ops. – Investing" supplemental item [sourced] CIQ-CF (Ricolino proceeds per [[bimbo-acquisitions]]).
- CIQ levered/unlevered FCF definitions are not stated in the export; treat them as CIQ-specific.

## 3. Quarterly detail, 1Q25-2Q26

MXN millions, `[sourced]` CIQ-CF.

| Line | 1Q25 | 2Q25 | 3Q25 | 4Q25 | 1Q26 | 2Q26 |
|---|---|---|---|---|---|---|
| Cash from Ops. | 10,591 | 10,563 | 13,309 | 13,291 | 15,111 | 10,075 |
| Capital Expenditure | (5,298) | (4,546) | (4,366) | (8,321) | (2,730) | (4,162) |
| Cash Acquisitions | NA | (9,725) | 429 | (3,467) | NA | 659 |
| Total Dividends Paid | NA | (4,451) | 0 | NA | NA | (4,785) |
| Repurchase of Common Stock | (647) | (537) | (69) | NA | (49) | (447) |
| Levered FCF (CIQ) | 3,869 | 2,389 | 7,404 | 2,698 | 9,517 | 5,815 |
| Net Change in Cash | 9,722 | (10,285) | 6,123 | (5,082) | 11,039 | (3,011) |

- Dividends are paid in Q2: 4,234 (2Q24), 4,451 (2Q25), 4,785 (2Q26) [sourced] CIQ-CF.

## 4. Reconciliation with the audited cash flow statement

| Line | CIQ [calc] | Company audited | Difference | Note |
|---|---|---|---|---|
| CFO FY25 | 47,753 | 47,753 [sourced] IA25-EEFF p.16 | 0 | |
| CFO FY23 | 31,411 | 31,411 [sourced] IA25-EEFF p.16 | 0 | |
| CFO FY24 | n/a (9M 26,988) | 39,907 [sourced] IA25-EEFF p.16 | – | implied 4Q24 12,919 [calc] |
| Capex FY25 | (22,530) | (22,530) [sourced] IA25-EEFF p.16 | 0 | |
| Capex FY24 | n/a (9M 19,096) | (29,402) [sourced] IA25-EEFF p.16 | – | implied 4Q24 10,306 [calc] |
| Capex FY23 | (34,754) | (34,754) [sourced] IA25-EEFF p.16 | 0 | |
| Investing FY25 / FY23 | (34,652) / (42,440) | (34,652) / (42,440) [sourced] IA25-EEFF p.16 | 0 | |
| Financing FY25 / FY23 | (11,908) / 5,904 | (11,908) / 5,904 [sourced] IA25-EEFF p.16 | 0 | |
| Debt issued FY25 | 69,267 | 69,267 "Préstamos obtenidos" [sourced] IA25-EEFF p.16 | 0 | |
| Debt repaid FY25 | (63,537) | (55,477) loans + (8,060) lease payments [sourced] IA25-EEFF p.16 | 0 | ==CIQ "Total Debt Repaid" includes lease principal== [calc] |
| Acquisitions FY25 | (12,762) | (11,294) business acquisitions + (1,468) purchase of non-controlling interest [sourced] IA25-EEFF p.16 | 0 | CIQ combines both [calc] |
| Interest paid FY25 | 11,533 | 11,533 [sourced] IA25-EEFF p.16 | 0 | |
| D&A FY25 | 24,048 + 779 "Other Amortization" (4Q25) = 24,827 | 24,838 [sourced] IA25-EEFF p.16 | (11) | |

> [!question] The IA25-EEFF cash flow page is a two-column layout whose text extraction interleaves figures; the lease-payment (8,060) and non-controlling-interest (1,468) amounts were matched by position and by the fact that they close the CIQ totals exactly. Confirm against the PDF before citing them in the report.

## Key Takeaways

- CIQ cash flow ties to the audited FY25 and FY23 statements line for line (CFO, capex, investing, financing, interest paid).
- FY2021 and FY2024 cannot be built from CIQ because one quarter of each year is empty; use the audited FY24 figures (CFO 39,907; capex 29,402).
- CIQ "Total Debt Repaid" includes lease principal (8,060 in FY25), and interest paid sits in financing; adjust before computing an FCF that deducts leases.
- Capex fell from 34,754 (FY23) to 22,530 (FY25) and 6,892 in 1H26, lifting CFO − capex to 32,207 LTM-2Q26 [calc].
- Cash interest paid rose to 11,533 in FY25 from 6,407 in FY22.
