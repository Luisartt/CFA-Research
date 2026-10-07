---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Financials/Templated/Performance Analysis/SPGlobal_GrupoBimbo,S.A.B.deC.V._PerformanceAnalysis_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Financial Highlights/SPGlobal_GrupoBimbo,S.A.B.deC.V._FinancialHighlights_19-Sep-2026 (1).xlsx
  - filings/capitaliq/Financials/Templated/Financial Highlights/SPGlobal_GrupoBimbo,S.A.B.deC.V._FinancialHighlights_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Key Stats/SPGlobal_GrupoBimbo,S.A.B.deC.V._KeyStats_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Key Stats/SPGlobal_GrupoBimbo,S.A.B.deC.V._KeyStats_20-Sep-2026 (1).xlsx
  - filings/capitaliq/Financials/Templated/Income Statement/SPGlobal_GrupoBimbo,S.A.B.deC.V._IncomeStatement_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Balance Sheet/SPGlobal_GrupoBimbo,S.A.B.deC.V._BalanceSheet_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Cash Flow Statement/SPGlobal_GrupoBimbo,S.A.B.deC.V._CashFlow_19-Sep-2026.xlsx
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T25.pdf
tags: [Financials, key-ratios]
---

# Grupo Bimbo — Key Ratios and Performance (Capital IQ)

Margins, returns, working-capital days, liquidity and leverage as calculated by S&P Capital IQ (CIQ), plus CIQ Key Stats (valuation multiples, latest capitalization, consensus). Performance Analysis and Financial Highlights **downloaded 2026-09-19**; Key Stats 2026-09-19 (1995 FQ1-2021 FQ2) and 2026-09-20 (2021 FQ1-2027 FQ1 E). Tidy data: `data/capitaliq/performance_analysis.csv`, `financial_highlights.csv`, `key_stats.csv`. Statement detail: [[ciq-income-statement-history]], [[ciq-balance-sheet-history]], [[ciq-cash-flow-history]]. Market multiples context: [[bimbo-valuation-data-gaps]].

**Citation key.** `CIQ-PA` = Performance Analysis file, sheet 'Performance Analysis'. `CIQ-FH` = Financial Highlights, sheet 'Financial Highlights'. `CIQ-KS` = Key Stats file (20-Sep-2026 unless stated), sheet 'Key Stats'.

## 1. How CIQ computes these ratios (read first)

- ==All ratios are on a single-quarter basis, not fiscal-year.== The "FQ4" column is the fourth quarter alone: e.g., 2025 FQ4 EBITDA margin 15.00% = 4Q25 EBITDA 16,307 ÷ 4Q25 revenue 108,706 [calc]. Returns are annualised quarterly figures: 2025 FQ4 ROE 12.16% ≈ 4 × 4Q25 net income to company 3,617 ÷ average total equity (117,748; 120,255) [calc].
- ==The EBITDA inside CIQ's ratios is not the "EBITDA" line of the CIQ income statement.== It equals CIQ EBIT plus cash-flow D&A, annualised: 4Q25 EBIT 11,651 + CF D&A 5,591 = 17,242 [calc]; EBITDA/interest 17,242 ÷ 3,945 = 4.37x (CIQ 4.37) and Total Debt/EBITDA 190,767 ÷ (4 × 17,242) = 2.77x (CIQ 2.77) [calc]. 2Q26 checks the same way (8,827 + 6,097 = 14,924; 189,679 ÷ 59,697 = 3.18x, CIQ 3.18) [calc]. EBIT/interest uses CIQ EBIT directly (4Q25 2.95x) [calc].
- Leverage ratios use CIQ Total Debt / Net Debt, which **include IFRS 16 leases** ([[ciq-balance-sheet-history]]).
- Days metrics use CIQ average balances and annualised quarterly revenue / COGS.
- 2024 FQ4 ratios are `NA` except balance-sheet-only ratios (current, quick, debt/equity, debt/capital, liabilities/assets), because the 2024 FQ4 income statement is empty in CIQ.

## 2. CIQ ratio snapshot (quarter basis)

`[sourced]` CIQ-PA for the quarter shown.

| Ratio | 4Q23 | 4Q24 | 2Q25 | 4Q25 | 1Q26 | 2Q26 |
|---|---|---|---|---|---|---|
| **Returns (annualised)** | | | | | | |
| Return on Assets | 7.31% | NA | 5.02% | 7.06% | 6.05% | 5.33% |
| Return on Capital | 10.16% | NA | 6.60% | 9.33% | 7.98% | 7.08% |
| Return on Equity | 12.86% | NA | 10.51% | 12.16% | 9.18% | 11.38% |
| **Margins** | | | | | | |
| Gross | 52.00% | NA | 52.77% | 52.16% | 53.20% | 52.61% |
| SG&A | 41.96% | NA | 44.08% | 41.39% | 44.14% | 43.21% |
| EBITDA (IS line) | 10.82% | NA | 12.28% | 15.00% | 14.56% | 12.85% |
| EBIT | 9.96% | NA | 7.89% | 10.72% | 10.00% | 8.40% |
| Net income | 3.20% | NA | 2.63% | 2.90% | 2.36% | 2.79% |
| Levered FCF | −2.98% | NA | 2.22% | 2.48% | 9.49% | 5.54% |
| **Working capital (days)** | | | | | | |
| Days sales outstanding | 19.40 | NA | 20.30 | 20.20 | 21.32 | 20.92 |
| Days inventory outstanding | 31.15 | NA | 32.50 | 30.24 | 32.64 | 31.08 |
| Days payable outstanding | 76.13 | NA | 68.18 | 67.83 | 74.98 | 70.03 |
| Cash conversion cycle | −25.58 | NA | −15.38 | −17.39 | −21.03 | −18.03 |
| **Liquidity** | | | | | | |
| Current ratio | 0.68x | 0.79x | 0.81x | 0.71x | 0.89x | 0.84x |
| Quick ratio | 0.45x | 0.52x | 0.53x | 0.49x | 0.64x | 0.59x |
| **Leverage (incl. leases)** | | | | | | |
| Total debt / equity | 125.0% | 146.8% | 163.2% | 158.6% | 156.9% | 163.5% |
| Total debt / capital | 55.6% | 59.5% | 62.0% | 61.3% | 61.1% | 62.1% |
| Total liabilities / assets | 67.9% | 69.4% | 71.2% | 70.7% | 70.5% | 71.7% |
| EBITDA / interest | 6.09x | NA | 4.14x | 4.37x | 5.81x | 3.83x |
| EBIT / interest | 4.01x | NA | 2.38x | 2.95x | 3.63x | 2.26x |
| Total debt / EBITDA | 2.26x | NA | 3.31x | 2.77x | 3.02x | 3.18x |
| Net debt / EBITDA | 2.16x | NA | 3.19x | 2.64x | 2.71x | 2.90x |

- Quarterly margins swing widely (CIQ IS-line EBITDA margin 10.89% in 1Q25 vs 15.00% in 4Q25) [sourced] CIQ-PA; annualising a single quarter, as CIQ's leverage and return ratios do, makes them move with that swing (Total debt/EBITDA 3.88x in 1Q25 vs 2.77x in 4Q25 on total debt of 198,652 vs 190,767) [sourced] CIQ-PA, CIQ-BS.
- The cash conversion cycle is negative throughout: suppliers are paid ~68-76 days after purchase while receivables plus inventory turn in ~50-54 days combined [sourced] CIQ-PA. It shortened from −25.6 days (4Q23) to −17.4 days (4Q25) as DPO fell 8.3 days [calc].

## 3. Fiscal-year ratios rebuilt from CIQ statements

`[calc]` from sum-of-quarters P&L and year-end balances ([[ciq-income-statement-history]], [[ciq-balance-sheet-history]]); days on year-end (not average) balances, so they differ from CIQ's quarterly figures. FY24 not computable.

| Ratio | FY19 | FY20 | FY21 | FY22 | FY23 | FY25 | LTM 2Q26 |
|---|---|---|---|---|---|---|---|
| Gross margin | 52.9% | 54.0% | 53.7% | 51.7% | 51.6% | 52.5% | 52.6% |
| EBITDA margin (IS line) | 12.5% | 12.4% | 13.4% | 12.6% | 13.0% | 12.8% | 13.9% |
| EBIT margin | 9.1% | 9.0% | 9.9% | 9.1% | 9.4% | 8.5% | 9.5% |
| DSO (AR ÷ revenue × 365) | 20.5 | 18.9 | 20.7 | 19.8 | 19.4 | 20.3 | 21.3 |
| DIO (inventory ÷ COGS × 365) | 26.1 | 26.1 | 31.9 | 32.2 | 30.4 | 30.9 | 31.2 |
| DPO (AP ÷ COGS × 365) | 63.6 | 66.5 | 86.0 | 85.4 | 78.5 | 72.1 | 71.6 |
| Cash conversion cycle | −17.0 | −21.6 | −33.5 | −33.4 | −28.7 | −20.9 | −19.1 |
| EBITDA (IS line) / interest expense | 4.42x | 4.61x | 6.13x | 6.75x | 5.42x | 3.83x | 4.21x |
| Net debt (incl. leases) / EBITDA (IS line) | 2.92x | 2.56x | 2.53x | 2.03x | 2.56x | 3.32x | 2.96x |
| Net debt ex leases / EBITDA (IS line) | 2.22x | 1.85x | 1.85x | 1.44x | 2.05x | 2.69x | 2.39x |

- ==DPO has unwound by ~14 days since FY21== (86.0 → 72.1 at year-end FY25) [calc]; the negative cash cycle shrank from −33.5 to −20.9 days. Each day of FY25 COGS is ~555 MXN mn (202,722 ÷ 365) [calc].
- Interest cover on CIQ inputs fell from 6.75x (FY22) to 3.83x (FY25) [calc] as interest expense rose ([[ciq-income-statement-history]]).
- Company-defined leverage for comparison: Net Debt / Adj. EBITDA (ex IFRS 16) 2.7x at Dec-25 [sourced] 4T25 p.2. CIQ's own quarterly "Net debt / EBITDA" (2.64x at 4Q25) is a different construct (includes leases, annualised Q4).

## 4. Key Stats: valuation multiples, capitalization, consensus

**Latest capitalization** (as of download 2026-09-19/20; CIQ uses the 2026 FQ2 balance sheet) `[sourced]` CIQ-KS rows 51-66:

| Item | Value |
|---|---|
| Closing price | MXN 54.20 |
| Common shares outstanding | 4,296,284,215 |
| Market capitalization | 232,859 |
| + Total debt (incl. leases) | 189,679 |
| + Minority interest | 722 |
| − Cash & ST investments | 16,563 |
| **Total enterprise value (TEV)** | **406,697** |
| Total capital (equity + minority + debt) | 305,674 |

**Valuation multiples "based on current capitalization"** `[sourced]` CIQ-KS rows 43-49 (identical in both Key Stats files):

| Multiple | FY23 | FY24 | FY25 | LTM 2Q26 | FY26E | FY27E | FY28E |
|---|---|---|---|---|---|---|---|
| TEV / revenue | 0.92x | 1.01x | 0.97x | 0.97x | 0.95x | 0.91x | 0.87x |
| TEV / EBITDA | 6.32x | 6.66x | 6.56x | 6.29x | 6.55x | 6.27x | 5.89x |
| TEV / EBIT | 9.22x | 10.37x | 10.58x | 9.96x | 10.86x | 10.49x | 9.70x |
| Price / EPS | 15.45x | 18.54x | 20.98x | 19.76x | 17.66x | 16.19x | 14.28x |
| Price / book | 2.20x | 1.86x | 1.95x | 2.02x | 1.85x | 1.68x | 1.56x |
| Price / tangible book | NM | NM | NM | NM | NA | NA | NA |

- For historical years CIQ pairs today's market cap with **that year-end's** net debt and minority interest: FY23 TEV = 232,859 + 133,186 + 3,306 = 369,351; ÷ 0.92366 = 399,879 = FY23 revenue [calc]. The same back-solve gives FY24 revenue 408,336 (company 408,335) and FY25 revenue 426,952 (company 426,952) [calc] — so ==CIQ holds annual FY24 and FY25 figures internally== even though the quarterly export lacks 2024 FQ4 and its FY25 quarterly sum is 426,963.
- The EBITDA behind TEV/EBITDA is not the CIQ income-statement EBITDA line: implied FY25 EBITDA = 415,834 ÷ 6.5634 = 63,356 vs IS-line 54,815 [calc]. Do not recompute CIQ multiples with the IS-line EBITDA.
- Forward multiples use broker consensus means; CIQ notes these "may not be on a comparable basis as financials" [sourced] CIQ-KS row 34.

**Consensus estimates in Key Stats** (mean, as of 2026-09-20) `[sourced]` CIQ-KS:

| Item | 3Q26E | 4Q26E | 1Q27E |
|---|---|---|---|
| Revenue | 105,833 | 107,617 | NA |
| EBITDA | 16,077 | 16,736 | NA |
| EBIT | 9,703 | 10,214 | NA |
| Net income | 3,479 | 3,944 | NA |
| Diluted EPS (MXN) | 0.866 | 0.901 | 0.62 |

- Consensus EBITDA (16,077 for 3Q26E) is far above CIQ's IS-line EBITDA for 3Q25 (14,048) and closer to the company's adjusted basis; compare consensus only with company-reported Adj. EBITDA. Full consensus detail is compiled from the CIQ estimates exports in the Valuation domain.

## Key Takeaways

- CIQ ratios are single-quarter (annualised) figures; the FQ4 column is Q4 alone, not the fiscal year. Rebuilt FY ratios are in section 3.
- CIQ's ratio EBITDA = EBIT + cash-flow D&A, annualised, and differs from the CIQ income-statement EBITDA line; CIQ leverage ratios also include leases.
- Working capital is a funding source (negative cash cycle), but the cushion shrank: year-end DPO 86.0 days (FY21) → 72.1 (FY25) [calc].
- Interest cover on CIQ inputs fell from 6.75x (FY22) to 3.83x (FY25) [calc].
- At MXN 54.20 (Sep-2026) CIQ shows TEV 406,697, TEV/LTM EBITDA 6.29x and P/E LTM 19.76x on its own definitions [sourced].
- Back-solving the Key Stats multiples shows CIQ's internal FY24/FY25 revenue equals the company's audited figures.
