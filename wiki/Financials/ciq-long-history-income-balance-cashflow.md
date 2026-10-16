---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Financials/Templated/Income Statement/SPGlobal_GrupoBimbo,S.A.B.deC.V._IncomeStatement_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Balance Sheet/SPGlobal_GrupoBimbo,S.A.B.deC.V._BalanceSheet_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Cash Flow Statement/SPGlobal_GrupoBimbo,S.A.B.deC.V._CashFlow_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Pension Details/SPGlobal_GrupoBimbo,S.A.B.deC.V._PensionDetails_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Financial Highlights/SPGlobal_GrupoBimbo,S.A.B.deC.V._FinancialHighlights_19-Sep-2026 (1).xlsx
  - filings/capitaliq/Financials/As-Reported/Cash Flow/SPGlobal_GrupoBimbo,S.A.B.deC.V._CashFlow(AsReported)_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/As-Reported/Income Statement/SPGlobal_GrupoBimbo,S.A.B.deC.V._IncomeStatement(AsReported)_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/As-Reported/Balance Sheet/SPGlobal_GrupoBimbo,S.A.B.deC.V._BalanceSheet(AsReported)_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Key Stats/SPGlobal_GrupoBimbo,S.A.B.deC.V._KeyStats_19-Sep-2026.xlsx
  - filings/capitaliq/Estimates/Consensus/SPGlobal_GrupoBimbo,S.A.B.deC.V._Consensus_20-Sep-2026.xlsx
tags: [Financials, long-history]
---

# Grupo Bimbo — Long-History Income Statement, Balance Sheet and Cash Flow (Capital IQ, FY2000-FY2025)

The longest annual series S&P Capital IQ (CIQ) holds for BIMBOA: ==26 fiscal years (FY2000-FY2025) of P&L, 31 years (FY1995-FY2025) of cash flow and 27 year-ends (1999-2025) of balance sheet==, rebuilt from the 19-Sep-2026 exports. The earlier CIQ articles ([[ciq-income-statement-history]], [[ciq-cash-flow-history]], [[ciq-balance-sheet-history]], [[ciq-key-ratios-and-performance]]) stop at FY2019. This article extends them back to FY2000 and closes the two gaps they declared unbuildable (FY2024 P&L and FY2021/FY2024 cash flow) using the **As-Reported** exports that were not used before. Company-filing views of the same years: [[bimbo-income-statement-fy98-fy07]], [[bimbo-income-statement-fy08-fy13]], [[bimbo-income-statement-fy14-fy20]], [[bimbo-income-statement-fy21-fy25]], [[bimbo-cash-flow-and-fcf]]. Delta list for the team: [[ciq-delta-vs-previous-export]].

**Citation key.** `CIQ-IS` / `CIQ-BS` / `CIQ-CF` / `CIQ-PN` = Templated Income Statement, Balance Sheet, Cash Flow, Pension Details sheets (quarters, MXN thousands, "Current/Restated"). `AR-CF` / `AR-IS` = As-Reported Cash Flow (annual columns FY1995-FY2025) and Income Statement (quarterly, mixed units). `CIQ-CONS` = Consensus sheet, "Actuals/Estimates" rows (company-reported actuals with CIQ's accounting-standard flag). Units: ==MXN millions== (÷1,000) unless stated. Every annual P&L figure is the sum of four CIQ quarters `[calc]` unless marked; year-end balances are the FQ4 column `[sourced]` CIQ-BS.

## 1. What is new versus the earlier CIQ articles

| Item | Earlier articles | This export |
|---|---|---|
| P&L history | FY2019-FY2025 only | FY2000-FY2025 (quarters 1995 FQ1 to 2026 FQ2 exist; FY1995-FY1999 unusable, section 7) |
| FY2024 P&L | "cannot be built from CIQ" (2024 FQ4 empty in the Templated file) | ==Built==: 9M24 (CIQ-IS) + 4Q24 from AR-IS 2024 FQ4 (revenue 110,312; gross profit 57,931; net income 3,121) = revenue 408,335, gross profit 215,207, net income 12,545 `[calc]`; EBITDA and EBIT still not in CIQ (company FY24 Adj. EBITDA 55,474 `[sourced]` CIQ-CONS) |
| FY2021 and FY2024 cash flow | "cannot be built" (empty quarter) | ==Built== from AR-CF annual columns: FY2021 CFO 45,776, capex (20,671); FY2024 CFO 39,907, capex (29,402) `[sourced]` AR-CF |
| Cash flow history | FY2019-FY2025 | FY1995-FY2025 annual, with dividends, buybacks, acquisitions, interest and lease payments |
| Leverage history | 2019-2026 | 1999-2025 year-end debt, net debt, equity, pension funded status 2004-2025 |
| EBITDA gap vs company | "CIQ below company, widening" (FY2021-FY2025) | ==Sign flips==: CIQ IS-line EBITDA was **above** the company-basis figure in FY2012-FY2019 and **below** from FY2020 (section 3) |

## 2. Accounting and basis breaks to read before using any series

| Break | Date | Effect on the CIQ series | Evidence |
|---|---|---|---|
| Inflation accounting and Q4 derivation | FY1995-FY1999 | CIQ derives Q4 as annual (constant pesos) less nine-month nominal figures, so 1995 FQ4 revenue is negative (-8,561 `[sourced]` CIQ-IS) and 1997 Q1 equals Q2 (4,176 each); 1998 has no quarters | CIQ-IS rows "Total Revenue", calc codes `Q4`/`YTDQS` |
| Mexican GAAP (NIF) to IFRS | FY2011 to FY2012 | CIQ labels FY1996-FY2011 "Mexican GAAP" and FY2012 onward "IFRS" `[sourced]` CIQ-CONS accounting-standard row; the company's IFRS transition date was 1-Jan-2011 and the first IFRS annual report is FY2012 (see [[bimbo-history-2008-2013]]) | FY2011 revenue differs by basis: 133,496 (CIQ-IS sum `[calc]`) vs 133,732 (CIQ-CONS `[sourced]`) |
| Large acquisitions | 2009, 2011, 2014 | Revenue +41.3% in FY2009 and +29.7% in FY2012 `[calc]` are acquisition steps (Weston Foods US, agreed Dec-2008, then a first full year of Sara Lee North America and Iberia: [[bimbo-history-2008-2013]]); FY2014 acquisitions cash 22,351 (Canada Bread) `[sourced]` AR-CF, see [[bimbo-cash-flow-and-capex-fy14-fy20]] | total assets 58,506 (2008) to 99,666 (2009) `[sourced]` CIQ-BS |
| IFRS 16 | 1-Jan-2019 | Lease liabilities enter CIQ total debt (2019FQ1, see [[ciq-debt-evolution-2019-2026]]); company EBITDA and CFO are stated after the IFRS 16 benefit ([[bimbo-ifrs-adjustments]]). Debt/equity jumps from 115.7% to 152.4% and net debt from 84,589 to 106,157 between FY2018 and FY2019 `[sourced]` CIQ-BS | company FY2019 Adj. EBITDA 33,426 (pre-IFRS 16 headline) vs 37,874 (IFRS 16 basis) `[sourced]` per [[bimbo-income-statement-fy14-fy20]] |
| Ricolino as discontinued | FY2021 restated, FY2022 | CIQ-IS carries FY2021 revenue 338,792 (restated, ex-Ricolino) while FY2020 331,051 is not restated, so the FY2021 y/y of +2.3% understates like-for-like growth `[calc]`; CIQ-CONS keeps the as-first-reported FY2021 (348,887) | [[ciq-consensus-estimates]] section 5 |
| FY2022 one-offs | FY2022 | Net income 46,910 includes discontinued operations and a non-operating gain of 17,887 booked by CIQ in 2022 FQ4 `[sourced]` CIQ-IS | ROE 42.4% in FY2022 is not a run-rate `[calc]` |

## 3. Annual P&L, FY2000-FY2025

`[calc]` sums of CIQ-IS quarters (all four quarters present for every year shown). † FY2024 completed with AR-IS 4Q24 (section 1); EBITDA and EBIT unavailable. Growth and margins `[calc]`. Net income = CIQ "Net Income" (to common). FY2000-FY2008 are CIQ's restated ("Current/Restated") figures and differ from the first-published constant-peso statements (section 6).

| FY | Revenue | y/y | Gross profit | GM | EBITDA (CIQ IS line) | margin | EBIT (CIQ) | margin | Net income (common) | margin |
|---|---|---|---|---|---|---|---|---|---|---|
| 2000 | 32,008 | n/a | 18,069 | 56.5% | 4,456 | 13.9% | 3,089 | 9.7% | 1,976 | 6.2% |
| 2001 | 34,968 | 9.2% | 19,260 | 55.1% | 4,596 | 13.1% | 3,126 | 8.9% | 1,654 | 4.7% |
| 2002 | 44,350 | 26.8% | 23,587 | 53.2% | 4,375 | 9.9% | 2,725 | 6.1% | 1,003 | 2.3% |
| 2003 | 49,100 | 10.7% | 26,175 | 53.3% | 5,064 | 10.3% | 3,181 | 6.5% | 1,041 | 2.1% |
| 2004 | 52,573 | 7.1% | 27,901 | 53.1% | 5,846 | 11.1% | 3,923 | 7.5% | 2,663 | 5.1% |
| 2005 | 58,643 | 11.5% | 31,676 | 54.0% | 6,987 | 11.9% | 5,037 | 8.6% | 2,975 | 5.1% |
| 2006 | 66,836 | 14.0% | 35,637 | 53.3% | 7,650 | 11.4% | 5,635 | 8.4% | 3,681 | 5.5% |
| 2007 | 72,294 | 8.2% | 38,199 | 52.8% | 8,640 | 12.0% | 6,408 | 8.9% | 3,811 | 5.3% |
| 2008 | 82,317 | 13.9% | 42,024 | 51.1% | 9,829 | 11.9% | 7,328 | 8.9% | 4,320 | 5.2% |
| 2009 | 116,353 | 41.3% | 61,420 | 52.8% | 15,837 | 13.6% | 12,054 | 10.4% | 5,956 | 5.1% |
| 2010 | 117,163 | 0.7% | 61,846 | 52.8% | 15,486 | 13.2% | 11,411 | 9.7% | 5,394 | 4.6% |
| 2011 | 133,496 | 13.9% | 68,100 | 51.0% | 13,895 | 10.4% | 9,606 | 7.2% | 4,875 | 3.7% |
| 2012 | 173,139 | 29.7% | 87,785 | 50.7% | 16,018 | 9.3% | 10,551 | 6.1% | 2,028 | 1.2% |
| 2013 | 176,041 | 1.7% | 92,099 | 52.3% | 18,714 | 10.6% | 13,467 | 7.6% | 4,404 | 2.5% |
| 2014 | 187,053 | 6.3% | 98,926 | 52.9% | 21,509 | 11.5% | 15,678 | 8.4% | 3,518 | 1.9% |
| 2015 | 219,186 | 17.2% | 116,765 | 53.3% | 25,386 | 11.6% | 18,336 | 8.4% | 5,171 | 2.4% |
| 2016 | 252,141 | 15.0% | 136,143 | 54.0% | 30,864 | 12.2% | 22,428 | 8.9% | 5,898 | 2.3% |
| 2017 | 267,515 | 6.1% | 142,752 | 53.4% | 30,324 | 11.3% | 21,563 | 8.1% | 4,629 | 1.7% |
| 2018 | 289,320 | 8.2% | 153,651 | 53.1% | 34,944 | 12.1% | 24,944 | 8.6% | 5,808 | 2.0% |
| 2019 | 291,926 | 0.9% | 154,548 | 52.9% | 36,368 | 12.5% | 26,531 | 9.1% | 6,319 | 2.2% |
| 2020 | 331,051 | 13.4% | 178,668 | 54.0% | 40,992 | 12.4% | 29,690 | 9.0% | 9,111 | 2.8% |
| 2021 | 338,792 | 2.3% | 181,789 | 53.7% | 45,541 | 13.4% | 33,589 | 9.9% | 15,916 | 4.7% |
| 2022 | 398,706 | 17.7% | 205,974 | 51.7% | 50,087 | 12.6% | 36,464 | 9.1% | 46,910 | 11.8% |
| 2023 | 399,879 | 0.3% | 206,160 | 51.6% | 51,988 | 13.0% | 37,455 | 9.4% | 15,477 | 3.9% |
| 2024† | 408,335 | 2.1% | 215,207 | 52.7% | n/a | n/a | n/a | n/a | 12,545 | 3.1% |
| 2025 | 426,963 | 4.6% | 224,242 | 52.5% | 54,815 | 12.8% | 36,272 | 8.5% | 11,133 | 2.6% |

Reading `[calc]`:
- ==Gross margin has drifted down ~4 points over 25 years==: 56.5% (FY2000) to 52.5% (FY2025), with a floor of 50.7% in FY2012 (IFRS year, first full Sara Lee year) and a recovery to 54.0% in FY2016 and FY2020.
- CIQ IS-line EBITDA margin has stayed in a 9.3%-13.9% band for 25 years (FY2012 low 9.3%; FY2000 high 13.9%) and sits at 12.8% in FY2025, i.e. ==no secular margin expansion despite a 13x increase in revenue==.
- Net margin is the variable that has changed: 2.1%-6.2% in FY2000-FY2009 (5.1%-5.5% in FY2004-FY2009) and 1.2%-2.8% in FY2012-FY2020, as interest and tax rose with acquisition debt; FY2021-FY2025 are 4.7%, 11.8% (one-offs), 3.9%, 3.1%, 2.6%.
- Growth eras `[calc]` (CAGR of CIQ sums): FY2000-FY2008 revenue 12.5%, EBITDA 10.4%; FY2008-FY2015 revenue 15.0%, EBITDA 14.5% (acquisition era); FY2015-FY2025 revenue 6.9%, EBITDA 8.0%; FY2019-FY2025 revenue 6.5%, EBITDA 7.1%. FY2000-FY2025 overall: revenue 10.9%, EBITDA 10.6%. ==Organic-style growth since 2015 is about half the acquisition-era rate==, and EBITDA has outgrown revenue only modestly.

## 4. EBITDA and EBIT: CIQ line versus company basis

The company-basis figures are the CIQ-CONS "actual" rows (first-published company numbers: Adjusted EBITDA "UAFIDA Ajustada"; operating income). Gap = CIQ IS line less company basis `[calc]`.

| FY | CIQ EBITDA (IS line) | Company-basis EBITDA (a) | Gap | CIQ EBIT | Company-basis operating income (a) | Gap |
|---|---|---|---|---|---|---|
| 2004 | 5,846 | 5,736 | +110 | 3,923 | 4,136 | -213 |
| 2005 | 6,987 | 7,098 | -111 | 5,037 | 4,811 | +226 |
| 2006 | 7,650 | 7,766 | -116 | 5,635 | 5,418 | +217 |
| 2007 | 8,640 | 8,646 | -6 | 6,408 | 6,408 | +0 |
| 2008 | 9,829 | 9,829 | +0 | 7,328 | 7,328 | +0 |
| 2009 | 15,837 | 15,837 | +0 | 12,054 | 12,054 | +0 |
| 2010 | 15,486 | 16,036 | -550 | 11,411 | 11,961 | -550 |
| 2011 | 13,895 | 15,173 | -1,278 | 9,606 | 10,843 | -1,237 |
| 2012 | 16,018 | 14,100 | +1,918 | 10,551 | 10,528 | +23 |
| 2013 | 18,714 | 17,326 | +1,388 | 13,467 | 10,469 | +2,998 |
| 2014 | 21,509 | 18,384 | +3,125 | 15,678 | 10,309 | +5,369 |
| 2015 | 25,386 | 23,369 | +2,017 | 18,336 | 14,121 | +4,216 |
| 2016 | 30,864 | 29,297 | +1,567 | 22,428 | 18,083 | +4,345 |
| 2017 | 30,324 | 27,288 | +3,036 | 21,563 | 17,472 | +4,091 |
| 2018 | 34,944 | 31,705 | +3,239 | 24,944 | 20,629 | +4,315 |
| 2019 | 36,368 | 33,426 | +2,942 | 26,531 | 20,419 | +6,112 |
| 2020 | 40,992 | 45,193 | -4,201 | 29,690 | 25,408 | +4,282 |
| 2021 | 45,541 | 49,178 | -3,637 | 33,589 | 34,126 | -537 |
| 2022 | 50,087 | 53,445 | -3,358 | 36,464 | 53,696 | -17,232 |
| 2023 | 51,988 | 54,942 | -2,954 | 37,455 | 35,455 | +2,000 |
| 2024 | n/a | 55,474 | n/a | n/a | 33,149 | n/a |
| 2025 | 54,815 | 59,456 | -4,641 | 36,272 | 34,146 | +2,126 |

(a) Company basis is as first reported per CIQ-CONS (FY2021 49,178 not the restated 47,372; FY2019 33,426 is the pre-IFRS 16 headline, 37,874 after IFRS 16 per [[bimbo-income-statement-fy14-fy20]]). FY2024 company-basis EBIT 33,149 and EBITDA 55,474 `[sourced]` CIQ-CONS.

- ==FY2008-FY2009 tie to the company to the million== (EBITDA 9,829 and 15,837; EBIT 7,328 and 12,054), and revenue and gross profit for FY2008-FY2009 match [[bimbo-income-statement-fy08-fy13]] (gross profit 42,024 and 61,420) `[calc]` vs `[sourced]`.
- From FY2012 to FY2019 CIQ EBITDA is **above** the company figure by 1.4-3.2 bn and CIQ EBIT is above by 3.0-6.1 bn (FY2013-FY2019): CIQ moves restructuring, impairment and multi-employer pension (MEPP) items below EBIT, which the company keeps inside operating income `[calc]`; the exact reclassification is not itemised in the export `[unverified]`.
- From FY2020 the sign flips: CIQ EBITDA is **below** by 4,201 (FY2020), 3,637, 3,358, 2,954 and 4,641 (FY2025). The company headline switched to the IFRS 16 basis in 1Q20 (same year; [[bimbo-income-statement-fy14-fy20]]), and the CIQ IS line does not add back all right-of-use depreciation `[calc]`, see [[ciq-income-statement-history]] section 5.
- FY2022 company operating income 53,696 vs CIQ EBIT 36,464 (-17,232): the company line contains the MEPP provision reversal and other 2022 one-offs that CIQ books outside EBIT `[calc]`.
- Implication: ==the earlier article's "gap is systematic and widening" holds only for FY2020-FY2025 and is non-monotonic (4,201; 3,637; 3,358; 2,954; 4,641)==; before FY2020 the sign is the opposite. Do not apply one correction factor across the full history.
- FY2024 implied CIQ-ratio EBITDA: CIQ Key Stats TEV/EBITDA of 6.6614x on a TEV of 413,951 (market cap 232,859 + FY24 net debt 179,338 + minority 1,754) gives 62,141 `[calc]`, versus company 55,474; the CIQ ratio EBITDA is a third definition (EBIT plus cash-flow D&A) `[calc]`, see [[ciq-key-ratios-and-performance]].

## 5. Cash flow, FY1995-FY2025 (As-Reported, annual)

`[sourced]` AR-CF annual columns (units mixed in the file: thousands to FY2001, millions from FY2002; converted to MXN millions). CFO − capex `[calc]`. "–" = line not reported. Interest paid and lease payments are financing items in the company statement (interest from FY2008; leases from FY2019, IFRS 16). Acquisitions = business combinations / acquisitions net of cash, purchase of non-controlling interests and, for FY2002, the purchase of assets formerly owned by George Weston Ltd (6,686) (sum of the as-reported lines; other early-year lines are named differently and may be incomplete).

| FY | CFO | Capex | CFO − capex | Dividends | Buybacks | Acquisitions | Interest paid | Lease payments | CFI | CFF |
|---|---|---|---|---|---|---|---|---|---|---|
| 1995 | 937 | – | – | -105 | – | – | – | – | -1,875 | 892 |
| 1996 | 2,246 | -2,299 | -53 | -152 | – | – | – | – | -2,459 | 225 |
| 1997 | 2,823 | -1,563 | 1,261 | -167 | – | – | – | – | -1,626 | -870 |
| 1998 | 3,326 | -1,763 | 1,564 | -1,523 | – | -743 | – | – | -4,995 | 1,571 |
| 1999 | 2,497 | -1,993 | 504 | -42 | – | – | – | – | -1,133 | 337 |
| 2000 | 3,755 | -1,112 | 2,643 | -276 | -57 | – | – | – | -854 | -981 |
| 2001 | 2,040 | -1,578 | 462 | -286 | -4,051 | – | – | – | -2,020 | -3,964 |
| 2002 | 3,536 | -927 | 2,609 | -325 | -2 | -6,686 | – | – | -8,542 | 6,622 |
| 2003 | 3,730 | -713 | 3,017 | -266 | – | – | – | – | -507 | -3,991 |
| 2004 | 5,812 | -1,735 | 4,077 | -1,032 | – | – | – | – | -1,722 | -2,090 |
| 2005 | 6,017 | -3,268 | 2,749 | -367 | – | – | – | – | -4,343 | -1,421 |
| 2006 | 5,863 | -2,972 | 2,891 | -856 | – | – | – | – | -3,438 | -1,214 |
| 2007 | 6,030 | -4,330 | 1,700 | -530 | – | – | – | – | -4,806 | -3,012 |
| 2008 | 8,850 | -3,989 | 4,861 | -615 | – | -2,743 | -830 | – | -7,160 | 1,734 |
| 2009 | 13,449 | -3,613 | 9,836 | -619 | – | -35,140 | -2,682 | – | -38,398 | 22,606 |
| 2010 | 10,958 | -4,091 | 6,867 | -714 | – | -2,012 | -2,675 | – | -5,514 | -7,026 |
| 2011 | 14,750 | -6,425 | 8,325 | -773 | -5 | -13,804 | -2,371 | – | -19,414 | 5,165 |
| 2012 | 13,970 | -6,796 | 7,174 | -841 | 152 | – | -2,553 | – | -6,954 | -6,759 |
| 2013 | 11,394 | -6,766 | 4,628 | -2,707 | 11 | -139 | -3,465 | – | -5,621 | -7,302 |
| 2014 | 18,319 | -6,829 | 11,490 | – | – | -22,351 | -3,128 | – | -31,032 | 13,318 |
| 2015 | 18,116 | -9,604 | 8,512 | – | – | -1,641 | -3,899 | – | -11,404 | -5,634 |
| 2016 | 23,127 | -13,153 | 9,974 | -1,129 | -50 | -3,966 | -4,465 | – | -16,315 | -4,383 |
| 2017 | 21,170 | -13,446 | 7,724 | -1,364 | -53 | -12,482 | -4,429 | – | -27,070 | 6,492 |
| 2018 | 20,982 | -15,067 | 5,915 | -1,646 | -1,107 | -3,600 | -7,280 | – | -18,391 | -2,322 |
| 2019 | 28,520 | -13,117 | 15,403 | -2,103 | -1,748 | -94 | -5,681 | -4,784 | -12,642 | -16,833 |
| 2020 | 43,877 | -13,218 | 30,659 | -2,433 | -3,740 | -3,453 | -6,410 | -5,544 | -16,688 | -24,163 |
| 2021 | 45,776 | -20,671 | 25,105 | -4,636 | -1,901 | -10,637 | -6,781 | -5,372 | -32,459 | -14,116 |
| 2022 | 38,851 | -28,669 | 10,182 | -5,885 | -2,912 | -6,520 | -6,407 | -6,385 | -9,122 | -25,692 |
| 2023 | 31,411 | -34,754 | -3,343 | -3,549 | -3,664 | -6,548 | -7,436 | -6,278 | -42,440 | 5,904 |
| 2024 | 39,907 | -29,402 | 10,505 | -4,234 | -4,433 | -5,988 | -8,376 | -7,072 | -36,138 | -2,696 |
| 2025 | 47,753 | -22,530 | 25,223 | -4,451 | -1,253 | -12,762 | -11,533 | -8,060 | -34,652 | -11,908 |

Free cash flow after interest and leases `[calc]` (= CFO − capex − interest paid − lease payments; consistent with the FY23-FY25 values in [[bimbo-capital-allocation]]):

| FY | CFO − capex | − interest paid | − lease payments | = FCF after interest and leases |
|---|---|---|---|---|
| 2018 | 5,915 | -7,280 | – | -1,365 |
| 2019 | 15,403 | -5,681 | -4,784 | 4,938 |
| 2020 | 30,659 | -6,410 | -5,544 | 18,705 |
| 2021 | 25,105 | -6,781 | -5,372 | 12,952 |
| 2022 | 10,182 | -6,407 | -6,385 | -2,610 |
| 2023 | -3,343 | -7,436 | -6,278 | -17,057 |
| 2024 | 10,505 | -8,376 | -7,072 | -4,943 |
| 2025 | 25,223 | -11,533 | -8,060 | 5,630 |

Era totals `[calc]` from the table above (MXN millions):

| Era | CFO | Capex | CFO − capex | Dividends | Buybacks | Acquisitions (as-reported lines) | Net debt change (CIQ-BS, year-end to year-end) |
|---|---|---|---|---|---|---|---|
| FY2000-FY2008 | 45,632 | (20,624) | 25,008 | (4,553) | (4,110) | (9,429) | +1,631 (2,210 to 3,841) |
| FY2009-FY2013 | 64,521 | (27,691) | 36,830 | (5,654) | +158 | (51,095) | +34,835 (3,841 to 38,676) |
| FY2014-FY2018 | 101,714 | (58,099) | 43,615 | (4,139) | (1,210) | (44,040) | +45,913 (38,676 to 84,589) |
| FY2019-FY2025 | 276,095 | (162,361) | 113,734 | (27,291) | (19,651) | (46,002) | +97,643 (84,589 to 182,232), of which about 34.8 bn is lease debt at FY2025 `[sourced]` [[ciq-balance-sheet-history]] |

- ==FY2019-FY2025 funding gap==: CFO − capex of 113,734 less interest paid 52,624 and lease payments 43,495 leaves 17,615 of free cash flow, against 92,944 of dividends, buybacks and acquisitions in the same seven years `[calc]`. The 75.3 bn shortfall was funded by net borrowing (CIQ net debt ex leases rose from 84,589 to 147,442 `[calc]`, +62.9 bn; the rest is FX, other investing and timing).
- Capex intensity `[calc]`: capex/revenue was 1.5%-6.0% in FY2000-FY2018 (low 1.5% in FY2003, peak 6.0% in FY2007) and 4.0%-8.7% in FY2019-FY2025 (peak FY2023 8.7%, 34,754 on 399,879; FY2025 5.3%). Capex/D&A ran 1.2x-1.6x in FY2011-FY2018, 1.57x and 1.84x in FY2022-FY2023 (28,669 and 34,754 vs D&A 18,282 and 18,929) and 0.91x in FY2025 (22,530 vs 24,838); the 0.91x and 0.81x of FY2019-FY2020 are flattered by IFRS 16 depreciation, which inflates D&A.
- Dividends are small against cash generation: FY2019-FY2025 dividends 27,291 are 24% of CFO − capex `[calc]`; ==no dividend was paid in FY2014 or FY2015== (AR-CF has no line; confirmed by [[bimbo-cash-flow-and-capex-fy14-fy20]]).
- CFO is not comparable across the IFRS 16 break: FY2019 CFO 28,520 vs 20,982 in FY2018 (+36%) while lease payments of 4,784 moved to financing `[sourced]` AR-CF; D&A rose from 10,000 to 14,373.
- FY2021 (new): CFO 45,776, capex (20,671), acquisitions (10,637), dividends (4,636), CFI (32,459), CFF (14,116) `[sourced]` AR-CF; the Templated file has only three quarters (CFO 33,093) `[calc]`.
- FY2024 (new): CFO 39,907, capex (29,402), CFI (36,138), CFF (2,696), interest paid (8,376), lease payments (7,072), buybacks (4,433), acquisitions (5,988) `[sourced]` AR-CF. ==The Templated 9M24 acquisitions line (7,898 `[calc]`) exceeds the as-reported full-year acquisitions line (5,988)==; the two CIQ views classify business purchases and non-controlling-interest payments differently and the gap is not explained in the export `[unverified]`.

## 6. Balance sheet, leverage and returns, 1999-2025

Year-end values `[sourced]` CIQ-BS (FQ4 column) and CIQ-PN (pension, annual from 2004); debt includes IFRS 16 leases from 2019. Debt/equity, net debt/EBITDA, ROE and funded gap `[calc]`: net debt ÷ CIQ IS-line EBITDA of the same year (FY2024 not computable); ROE = net income ÷ average common equity; funded gap = plan assets − projected benefit obligation. "n/a" = not reported.

| Year-end | Total assets | Total debt | Cash & ST inv. | Net debt | Common equity | Debt / equity | Net debt / EBITDA (CIQ IS line) | ROE | Pension PBO | Plan assets | Funded gap |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1999 | 24,333 | 4,712 | 2,503 | 2,210 | 15,852 | 29.7% | n/a | n/a | n/a | n/a | n/a |
| 2000 | 25,035 | 4,150 | 4,465 | -315 | 15,658 | 26.5% | -0.07x | 12.5% | n/a | n/a | n/a |
| 2001 | 23,781 | 5,254 | 811 | 4,443 | 13,107 | 40.1% | 0.97x | 11.5% | n/a | n/a | n/a |
| 2002 | 34,203 | 12,485 | 2,486 | 9,999 | 14,577 | 85.6% | 2.29x | 7.2% | n/a | n/a | n/a |
| 2003 | 33,527 | 9,424 | 1,848 | 7,576 | 16,166 | 58.3% | 1.50x | 6.8% | n/a | n/a | n/a |
| 2004 | 34,670 | 8,779 | 3,885 | 4,894 | 17,242 | 50.9% | 0.84x | 15.9% | 4,676 | 4,315 | -361 |
| 2005 | 38,732 | 8,804 | 4,284 | 4,520 | 20,274 | 43.4% | 0.65x | 15.9% | n/a | n/a | n/a |
| 2006 | 43,939 | 8,806 | 5,690 | 3,116 | 24,439 | 36.0% | 0.41x | 16.5% | n/a | n/a | n/a |
| 2007 | 45,243 | 6,024 | 3,902 | 2,122 | 27,916 | 21.6% | 0.25x | 14.6% | 6,441 | 5,510 | -931 |
| 2008 | 58,506 | 11,180 | 7,339 | 3,841 | 34,264 | 32.6% | 0.39x | 13.9% | n/a | n/a | n/a |
| 2009 | 99,666 | 36,831 | 4,981 | 31,850 | 40,104 | 91.8% | 2.01x | 16.0% | 13,032 | 8,543 | -4,489 |
| 2010 | 99,069 | 33,440 | 3,325 | 30,115 | 43,710 | 76.5% | 1.94x | 12.9% | 13,700 | 8,847 | -4,853 |
| 2011 | 143,235 | 48,015 | 3,966 | 44,049 | 46,664 | 102.9% | 3.17x | 10.8% | 23,108 | 15,860 | -7,248 |
| 2012 | 137,140 | 42,907 | 4,278 | 38,629 | 44,736 | 95.9% | 2.41x | 4.4% | 24,675 | 16,401 | -8,274 |
| 2013 | 134,727 | 41,180 | 2,504 | 38,676 | 45,619 | 90.3% | 2.07x | 9.7% | n/a | n/a | n/a |
| 2014 | 177,761 | 63,744 | 2,572 | 61,172 | 50,975 | 125.0% | 2.84x | 7.3% | 30,086 | 21,723 | -8,363 |
| 2015 | 199,633 | 71,457 | 4,619 | 66,838 | 58,955 | 121.2% | 2.63x | 9.4% | 32,253 | 24,149 | -8,104 |
| 2016 | 245,165 | 85,853 | 6,814 | 79,039 | 71,430 | 120.2% | 2.56x | 9.0% | 35,784 | 26,453 | -9,331 |
| 2017 | 259,249 | 93,444 | 7,216 | 86,228 | 72,767 | 128.4% | 2.84x | 6.4% | 35,018 | 26,214 | -8,804 |
| 2018 | 263,316 | 92,173 | 7,584 | 84,589 | 79,690 | 115.7% | 2.42x | 7.6% | 29,231 | 24,247 | -4,984 |
| 2019 | 279,081 | 112,408 | 6,251 | 106,157 | 73,736 | 152.4% | 2.92x | 8.2% | 37,839 | 29,253 | -8,586 |
| 2020 | 307,651 | 114,341 | 9,268 | 105,073 | 83,713 | 136.6% | 2.56x | 11.6% | 42,386 | 34,790 | -7,596 |
| 2021 | 337,640 | 124,071 | 8,748 | 115,323 | 97,100 | 127.8% | 2.53x | 17.6% | 41,401 | 36,823 | -4,578 |
| 2022 | 347,764 | 113,829 | 12,313 | 101,516 | 124,111 | 91.7% | 2.03x | 42.4% | 27,465 | 24,413 | -3,052 |
| 2023 | 348,102 | 139,539 | 6,353 | 133,186 | 108,322 | 128.8% | 2.56x | 13.3% | 27,163 | 24,788 | -2,375 |
| 2024 | 416,804 | 187,395 | 8,057 | 179,338 | 125,944 | 148.8% | n/a | 10.7% | 28,382 | 26,684 | -1,698 |
| 2025 | 409,805 | 190,767 | 8,535 | 182,232 | 119,512 | 159.6% | 3.32x | 9.1% | 29,033 | 27,509 | -1,524 |

Reading `[calc]`:
- ==Balance-sheet leverage has stepped up in three acquisition waves==: FY2008 net debt 3,841 (0.39x) to FY2009 31,850 (2.01x, Weston Foods US); FY2011 44,049 (3.17x, Sara Lee North America and Iberia) and FY2014 61,172 (Canada Bread) at 2.8x; FY2019 106,157 (IFRS 16) then FY2024 179,338 (+46.2 bn in the year) with FY2025 3.32x on the CIQ IS-line EBITDA (2.7x on the company basis per [[bimbo-capital-structure-and-debt]]).
- Net debt/EBITDA has been at or above 1.9x in every year since FY2009 where computable (range 1.94x-3.32x; FY2024 n/a) and was below 1.0x in FY2004-FY2008 and FY2000-FY2001; the pre-2009 balance sheet is not a guide to the current one.
- ROE averaged about 15% in FY2004-FY2009, 4%-10% in FY2012-FY2019 (4.4% in FY2012, 6.4% in FY2017) and was 9.1% in FY2025, so returns on book equity have not recovered to the pre-acquisition level even though common equity grew 7.6x (15,658 in FY2000 to 119,512) `[calc]`.
- Pension: the unfunded gap widened from 361 (2004) to 9,331 (2016) and narrowed to 1,524 (2025) as the PBO fell from 41,401 (2021) to 27,465 (2022), coinciding with the MEPP reversal ([[ciq-pension-obligations]]). Pension data have gaps in 2005, 2006, 2008 and 2013 (not reported in CIQ-PN).
- Cash and short-term investments are structurally thin relative to debt (8,535 vs 190,767 in FY2025, 4.5%); in FY2000 the company was net cash (cash 4,465 vs debt 4,150).

## 7. Tie-out to first-published company figures (FY2000-FY2011)

Company figures `[sourced]` per [[bimbo-income-statement-fy98-fy07]] and [[bimbo-income-statement-fy08-fy13]] (constant pesos of each report's year for FY1998-FY2007; nominal from FY2008). CIQ = restated sum of quarters `[calc]`.

| FY | CIQ revenue | Company net sales | CIQ − company | CIQ EBIT | Company operating income | CIQ net income | Company majority net income |
|---|---|---|---|---|---|---|---|
| 2000 | 32,008 | 31,477 | +531 | 3,089 | 3,247 | 1,976 | 1,817 |
| 2001 | 34,968 | 33,855 | +1,113 | 3,126 | 3,277 | 1,654 | 1,476 |
| 2002 | 44,350 | 41,373 | +2,977 | 2,725 | 2,997 | 1,003 | 973 |
| 2003 | 49,100 | 46,663 | +2,437 | 3,181 | 3,315 | 1,041 | 964 |
| 2004 | 52,573 | 51,545 | +1,028 | 3,923 | 4,136 | 2,663 | 2,569 |
| 2005 | 58,643 | 56,102 | +2,541 | 5,037 | 5,202 | 2,975 | 2,829 |
| 2006 | 66,836 | 63,633 | +3,203 | 5,635 | 5,857 | 3,681 | 3,535 |
| 2007 | 72,294 | 72,294 | 0 | 6,408 | 6,408 | 3,811 | 3,811 |
| 2008 | 82,317 | 82,317 | 0 | 7,328 | 7,328 | 4,320 | 4,320 |
| 2009 | 116,353 | 116,353 | 0 | 12,054 | 12,054 | 5,956 | 5,956 |
| 2010 | 117,163 | 117,163 | 0 | 11,411 | 11,393 | 5,394 | 5,395 |
| 2011 | 133,496 | 133,712 (NIF) | (216) | 9,606 | 11,151 (NIF) | 4,875 | 5,329 (NIF) |

- CIQ revenue is 2%-7% above the first-published constant-peso statements in FY2000-FY2006, because CIQ carries later restated comparatives (different inflation base and classification) and the company statements were re-expressed each year ==(do not splice constant-peso company data with CIQ restated data)== `[calc]`. From FY2007 the two agree exactly to FY2010.
- FY2011 differs because CIQ holds the IFRS-restated figures (133,496; net income 4,875 majority) while the NIF statement shows 133,712 and 5,329 ([[bimbo-income-statement-fy08-fy13]]).
- CIQ "Net Income" before FY2007 sits 3%-12% above the company's majority net income (e.g., FY2000 1,976 vs 1,817; FY2001 1,654 vs 1,476), consistent with a restated basis or consolidated income before minorities `[unverified]`.

## 8. Data-quality flags and gaps

| Issue | Detail | Tag |
|---|---|---|
| FY1995-FY1999 quarterly series | negative Q4 revenue in 1995 (-8,561); 1997 Q1 = Q2; no 1998 columns; 1999 has only FQ3-FQ4. Use As-Reported annual cash flow for these years and ignore the quarterly P&L sums (e.g., FY1996 18,768 `[calc]`) | [sourced] CIQ-IS |
| As-Reported IS units | mixed per column (thousands, millions, actual); 2015-2025 columns are in actual pesos. Convert before any use | [sourced] AR-IS row "Units" |
| FY2024 EBITDA/EBIT | not in any CIQ income-statement export (Templated FQ4 empty); only company-basis (CIQ-CONS) and ratio-implied (section 4) | [sourced]/[calc] |
| Templated CF pre-2019 | capex, dividend and acquisition cells are populated in only 1-3 quarters (annual figure sits in FQ4, e.g., FY2002 capex 927 in one quarter, equal to AR-CF), and some annual sums differ from AR-CF (FY2005 CFO 5,779 vs 6,017); use AR-CF for annual flows and do not read these cells as quarterly flows | [sourced] CIQ-CF, AR-CF |
| Dividend timing | AR-CF dividends are cash paid in the year; CIQ-IS "Dividends per Share" in FQ4 is the dividend decreed for the fiscal year and paid the next May (FY2025 1.075 paid May-2026 vs 4,451 paid in 2025 = about 1.00 per share) `[calc]`; AR-CF has no dividends in FY2014-FY2015 (none paid) | [sourced] AR-CF, CIQ-IS |
| Balance sheet 1995-1998 | 1995 PP&E is 84 (units artefact), 1998 absent | [sourced] CIQ-BS |
| As-Reported Balance Sheet | exists only as xlsx and docx (no PDF copy); not used for numbers here because the Templated balance sheet is complete | gap |

## Connections
- Company-filing tables for the same years: [[bimbo-income-statement-fy98-fy07]], [[bimbo-income-statement-fy08-fy13]], [[bimbo-income-statement-fy14-fy20]], [[bimbo-income-statement-fy21-fy25]], [[bimbo-balance-sheet-and-debt-fy98-fy07]], [[bimbo-balance-sheet-and-leverage]], [[bimbo-cash-flow-and-fcf]], [[bimbo-cash-flow-and-capex-fy14-fy20]].
- Same data by region: [[ciq-segment-and-geography-long-history]]; valuation overlay: [[ciq-long-history-multiples-and-returns]]; analyst record against these actuals: [[ciq-guidance-and-estimate-history]].
- Supersession and update list: [[ciq-delta-vs-previous-export]]. Capital structure detail: [[ciq-debt-evolution-2019-2026]], [[bimbo-capital-structure-and-debt]]; capital allocation: [[bimbo-capital-allocation]]; acquisitions: [[bimbo-history-2008-2013]], [[bimbo-acquisitions]].

## Key Takeaways

- CIQ now gives ==FY2000-FY2025 P&L, FY1995-FY2025 cash flow and 1999-2025 balance sheets==; FY2024 P&L (408,335 revenue, 12,545 net income) and FY2021/FY2024 cash flow are no longer gaps because the As-Reported exports hold the missing quarter and annual columns.
- EBITDA margin on the CIQ IS line has stayed between 9.3% and 13.9% for 25 years (12.8% in FY2025); revenue grew 10.9% a year but only 6.9% since FY2015, and gross margin has drifted from 56.5% to 52.5%.
- ==CIQ EBITDA was above the company basis in FY2012-FY2019 and below it from FY2020 (gap -4,641 in FY2025)==; one correction factor cannot be applied across the history.
- Net debt/EBITDA has stayed at or above 1.9x since FY2009 and reached 3.32x (CIQ basis, incl. leases) in FY2025; cash is 4.5% of debt.
- In FY2019-FY2025 free cash flow after interest and leases was 17.6 bn against 92.9 bn of dividends, buybacks and acquisitions; the gap was borrowed ([calc]).
- Pre-2007 CIQ data are restated and 2%-7% above the first-published constant-peso statements; FY1995-FY1999 quarterly series are unusable.
