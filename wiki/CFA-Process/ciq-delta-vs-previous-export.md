---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Financials/As-Reported/Income Statement/SPGlobal_GrupoBimbo,S.A.B.deC.V._IncomeStatement(AsReported)_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/As-Reported/Cash Flow/SPGlobal_GrupoBimbo,S.A.B.deC.V._CashFlow(AsReported)_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/As-Reported/Balance Sheet/SPGlobal_GrupoBimbo,S.A.B.deC.V._BalanceSheet(AsReported)_19-Sep-2026.xlsx
  - filings/capitaliq/OwnerShip/OwnerShip History/SPGlobal_GrupoBimbo,S.A.B.deC.V._OwnershipHistory_10-Oct-2026.xlsx
  - filings/capitaliq/OwnerShip/OwnerShip Detailed/SPGlobal_GrupoBimbo,S.A.B.deC.V._OwnershipDetailed_10-Oct-2026.xlsx
  - filings/capitaliq/OwnerShip/OwnerShip CrossHoldings/SPGlobal_GrupoBimbo,S.A.B.deC.V._OwnershipCrossholdings_10-Oct-2026.xlsx
  - filings/capitaliq/Sustainability/ESG Profiles/ESG Scores/SPGlobal_GrupoBimbo,S.A.B.deC.V._ESGScores_10-Oct-2026.xlsx
  - filings/capitaliq/Sustainability/ESG Profiles/ESG Scores History/ESG Scores History 2013 - 2016.xlsx
  - filings/capitaliq/Sustainability/Sustainability Overview/SPGlobal_GrupoBimbo,S.A.B.deC.V.BMVBIMBOA(MIKEY4276592;SPCIQKEY877906;TCUID53231)_SustainabilityAndClimateOverview_10-Oct-2026.xlsx
  - filings/capitaliq/Sustainability/Business Involvement  Screens/SPGlobal_GrupoBimbo,S.A.B.deC.V._BusinessInvolvementScreens_10-Oct-2026.xlsx
  - filings/capitaliq/Corporate Issuance/Dividends & Splits/SPGlobal_GrupoBimbo,S.A.B.deC.V._DividendsAndSplits_06-Oct-2026.xlsx
  - filings/capitaliq/Estimates/Guidance/SPGlobal_GrupoBimbo,S.A.B.deC.V._Guidance_20-Sep-2026 (1).xlsx
  - filings/capitaliq/Estimates/Surprises/SPGlobal_GrupoBimbo,S.A.B.deC.V._Surprise_20-Sep-2026.xlsx
  - filings/capitaliq/Estimates/Recent Changes/SPGlobal_GrupoBimbo,S.A.B.deC.V._RecentChanges_06-Oct-2026.xlsx
  - filings/capitaliq/Estimates/Consensus/SPGlobal_GrupoBimbo,S.A.B.deC.V._Consensus_20-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Multiples/SPGlobal_GrupoBimbo,S.A.B.deC.V._Multiples_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Segment Analysis/SPGlobal_GrupoBimbo,S.A.B.deC.V._SegmentAnalysis_19-Sep-2026.xlsx
tags: [CFA-Process, ciq-delta]
---

# Capital IQ Export Delta: What Is New Versus the Earlier `ciq-*` Articles

Diff of the structured Capital IQ exports now in `filings/capitaliq/` (scope: everything except `News, Events and filings` and `Investment and Market research`) against what the 18 earlier `ciq-*` articles state. The earlier articles were compiled from the 131 files committed in `2cf056d` ("~129 files"); the folder now holds 3,220 files, but ==almost all of the growth is documents outside this scope (1,902 news items, 58 market-research files) and format copies==. This page lists what is genuinely new data, which periods and metrics became usable, and, in section 4, the exact claims in existing articles to update or supersede. Under `WIKI.md` the older articles are not edited here; each row names the article and the callout to insert. New articles that carry the new numbers: [[ciq-long-history-income-balance-cashflow]], [[ciq-segment-and-geography-long-history]], [[ciq-long-history-multiples-and-returns]], [[ciq-guidance-and-estimate-history]], [[ciq-ownership-and-holdings-history]], [[ciq-esg-profile-history]].

**Method.** File inventory by `git ls-files` versus the working tree; spreadsheet comparison cell-by-cell (all sheets) for each 06-Oct versus 10-Oct pair; byte comparison (MD5) for duplicated folders; row/column parsing of every structured sheet and of all 875 ESG question PDFs; spot readability checks of PDF and DOCX copies. Dates are the file dates (financials 19/20-Sep-2026; estimates 20-Sep and 06-Oct-2026; ownership/issuance 06-Oct-2026; ownership/ESG refresh 10-Oct-2026).

## 1. Inventory: old versus new

| Folder (in scope) | Previously committed (xlsx/xls) | New spreadsheets | New PDF / DOCX copies | Status |
|---|---|---|---|---|
| Assets and Operations | 2 | 0 | 2 PDF | unchanged data |
| Business Relationships & Supply Chain | 2 | 0 | 2 PDF + 2 DOCX | unchanged data |
| Corporate Issuance (new top-level folder) | 8 (under OwnerShip/) | 8 | 8 PDF + 8 DOCX | ==byte-identical copy of OwnerShip/Corporate Issuance== (MD5 match on all 8); no new data |
| Estimates | 9 | 0 | 2 PDF + 1 DOCX | unchanged data (Recent Changes PDF is a 4-page excerpt of the 2,368-row sheet; Estimate Highlights PDF/DOCX replicate the xlsx) |
| Financials | 87 (74 Capital Structure Details, 11 other Templated, 2 Key Stats) | 3 (As-Reported IS, BS, CF) | 86 PDF + 87 DOCX | ==As-Reported is the only new financial data==; Templated and Key Stats are the same files (dated 19/20-Sep) |
| Investment (Public Holdings) | 12 | 0 | 12 PDF + 12 DOCX | unchanged data |
| OwnerShip | 12 | 3 (History, Detailed, Cross-holdings dated 10-Oct) | 4 PDF + 4 DOCX | History is a different scope (All History vs 1 Year); Detailed/Cross-holdings are refreshed prices and positions |
| Sustainability (Overview, Business Involvement) | 2 | 2 (10-Oct versions) | 2 PDF + 2 DOCX + 1 PNG | refreshed comparators |
| Sustainability / ESG Profiles | 2 (Scores 06-Oct, History 06-Oct) | 4 (Scores 10-Oct; History 2013-2016, 2017-2021, 2022-2026) | 1 PDF + 1 DOCX; ==875 question PDFs== | new history and question-level data |
| **Total in scope** | **128 spreadsheets** | **20 spreadsheets (148 in total), of which 8 are duplicates = 12 genuinely new** | **236 PDF/DOCX copies + 875 question PDFs** | |

`[sourced]` file inventory `[calc]` from `git ls-files` and directory listing. The Financials folder contains 74 Capital Structure Details workbooks (FY2002-2025 and FQ1 2010 to FQ2 2026) already compiled in [[ciq-debt-evolution-2019-2026]]; they are unchanged.

**Readability.** All 236 PDF/DOCX copies in scope were probed: all 119 PDFs have a text layer (more than 200 characters each), and 6 were read (Estimate Highlights 3 pages, Key Stats 1, Recent Changes 4, As-Reported Cash Flow 79, Balance Sheet 72, Power Plants 1) and match the xlsx; 117 of 117 DOCX are valid OOXML containers with `word/document.xml` (python-docx rejects them for a missing officeDocument relationship, so text must be read from `document.xml`). Nothing was ignored because of format; as-reported Balance Sheet has no PDF copy.

## 2. Periods, years and metrics that are new or newly usable

| Dataset | Earlier articles | Now available | Where compiled |
|---|---|---|---|
| Annual P&L | FY2019-FY2025 (FY2024 missing) | FY2000-FY2025; FY2024 completed from As-Reported 4Q24 | [[ciq-long-history-income-balance-cashflow]] |
| Annual cash flow | FY2019-FY2025 (FY2021, FY2024 missing) | FY1995-FY2025 including FY2021 and FY2024 (As-Reported annual columns) | same |
| Balance sheet and leverage | 2019-2026 | year-ends 1999-2025; pension 2004-2025 | same |
| Regional segments | FY2019-1H26 | net sales FY2003-FY2005 and FY2015-FY2025; EBITDA FY2015-FY2025; operating income FY2003-FY2005, FY2011-FY2025; total assets 2001-2025 | [[ciq-segment-and-geography-long-history]] |
| Multiples | last 10 years (quarterly) | 1999-2026 by year and by accounting regime; price proxy; DPS | [[ciq-long-history-multiples-and-returns]] |
| Guidance | FY2024-FY2026 | FY2012-FY2026 (revenue, EBITDA, capex, tax) with first versus last versus actual | [[ciq-guidance-and-estimate-history]] |
| Surprises | 22 quarters (1Q21-2Q26) | 79 quarters (2004-2026) and 26 fiscal years (2000-2025) | same |
| Revision history | 12 months | 2,368 dated rows 24-May-2000 to 28-Sep-2026; consensus target price 2004-2026; rating consensus 2000-2026; FY2026 estimate path from 2020 | same |
| Ownership | one-year history (2025 to Latest) | annual positions 2004-2025 (437 holders), including the family holding companies 2007-2024 | [[ciq-ownership-and-holdings-history]] |
| ESG | methodology years 2022-2026 | 2013-2026 criterion scores; 2020-2026 question-level (875 PDFs) | [[ciq-esg-profile-history]] |

Metrics that remain unavailable: FY2024 EBITDA/EBIT (no CIQ income-statement export carries them); quarterly regional data for 2006-2014; segment data for FY1995-FY2002; recommendation distribution (counts of buys/holds/sells); broker names for most estimate rows ("Not Entitled").

## 3. What did not change (no update needed)

Balance sheet, cash flow, income statement and Financial Highlights (Templated) are the same 19-Sep-2026 files; no restatement of any CIQ financial value occurred between the two exports because the files are the same. The 06-Oct estimate files and the 20-Sep estimate files are unchanged. Capital structure, pension, plant network, customers and suppliers, public holdings, ratings, CDS and listings are unchanged. Differences between "restated" CIQ numbers and company filings are in the long-history articles, not new restatements.

## 4. Claims to update or supersede in existing articles

Format for each row: `> [!warning] Superseded` callout in the older article linking the newer article, keeping the original claim beneath it (`WIKI.md`). "Source" is the CIQ file (path under `filings/capitaliq/`) unless stated.

| # | Existing article | Old claim | New value | Source |
|---|---|---|---|---|
| 1 | [[ciq-income-statement-history]] | "FY2024 therefore cannot be built from CIQ; only 9M24 is available." | FY2024 can be built: 9M24 (298,023) + 4Q24 from As-Reported 110,312 = revenue 408,335 [calc] (equal to company); gross profit 215,207; net income 12,545 (= company 12,545). EBITDA/EBIT remain unavailable | Financials/As-Reported/Income Statement (2024 FQ4 column) |
| 2 | [[ciq-income-statement-history]] | "The export has no annual columns." | True for the Templated sheets; the As-Reported Cash Flow export is annual (FY1995-FY2025) and Key Stats multiples hold FY2023-FY2025 | Financials/As-Reported/Cash Flow |
| 3 | [[ciq-income-statement-history]] (section 5 and Key Takeaways) | "CIQ EBITDA runs MXN 1.8-4.6 bn below company Adjusted EBITDA (FY21-FY25)"; "The gap is systematic and widening" | Below only from FY2020 (-4,201, -3,637, -3,358, -2,954, -4,641 for FY2020-FY2023, FY2025; not monotonic); above the company basis in FY2012-FY2019 (+1,388 to +3,239 [calc]); EBIT above company by 3.0-6.1 bn in FY2013-FY2019 | Templated IS and Consensus 'Actuals' rows |
| 4 | [[ciq-income-statement-history]] | "Dividends per share ... FY24 not available (empty column)" | FY2024 DPS 1.00 (declared 14-Apr-2025, paid 14-May-2025) | Corporate Issuance/Dividends & Splits |
| 5 | [[ciq-income-statement-history]] vs [[ciq-consensus-estimates]] | IS article: "CIQ carries restated comparative-period figures" and FY2021 = 338,792; consensus article: "CIQ does ==not== carry the 2021 restatement" (348,887) | Both are true for different files: Templated IS = restated (338,792); Consensus, Surprise, Guidance actuals = as first reported (348,887, EBITDA 49,178). State the file when quoting | Templated IS; Estimates/Consensus |
| 6 | [[ciq-cash-flow-history]] | "Two years cannot be built from CIQ: FY2021 ... and FY2024" | FY2021: CFO 45,776, capex (20,671), acquisitions (10,637), dividends (4,636), CFI (32,459), CFF (14,116). FY2024: CFO 39,907, capex (29,402), CFI (36,138), CFF (2,696), interest paid (8,376), lease payments (7,072), buybacks (4,433), acquisitions (5,988), dividends (4,234) | Financials/As-Reported/Cash Flow |
| 7 | [[ciq-cash-flow-history]] section 2 table | Total Dividends Paid FY19 (2,400) [3/4], FY20 (2,727) [3/4], FY22 (5,791), FY23 (3,960) [2/4] | Annual dividends paid: FY19 2,103; FY20 2,433; FY22 5,885; FY23 3,549 (FY25 4,451 and 9M24 4,234 unchanged); the reason for the gaps is not given in the export [unverified]; FY20 includes 147 paid to non-controlling interests per [[bimbo-cash-flow-and-capex-fy14-fy20]] | As-Reported Cash Flow |
| 8 | [[ciq-cash-flow-history]] section 2 table | Repurchase of Common Stock FY19 (2,359) [3/4], FY20 (4,388) | As-reported buyback lines: FY19 1,748; FY20 3,740; the FY20 gap of 648 equals the perpetual-bond coupons in the company's FY20 distribution total (2,433 + 3,740 + 648 = 6,821, [[bimbo-cash-flow-and-capex-fy14-fy20]]) [calc], i.e. CIQ's buyback line includes coupons; the FY19 gap of 611 is close to the 595 implied by the FY19 total 4,446 [calc]; 9M24 buyback 3,809 vs FY24 4,433 | As-Reported Cash Flow |
| 9 | [[ciq-cash-flow-history]] section 2 table | Cash Acquisitions 9M24 (7,898) | Full-year FY2024 as-reported acquisitions line is only (5,988): the two CIQ views are inconsistent; do not add 4Q24 to 9M24 | As-Reported vs Templated CF |
| 10 | [[ciq-key-ratios-and-performance]] | "FY24 not computable" (ratios) and "2024 FQ4 ratios are NA" | Revenue, gross margin and net margin for FY2024 are computable (408,335; 52.7%; 3.1% [calc]); cash flow ratios from As-Reported (FCF 10,505); EBITDA-based ratios still not (Key Stats implies 62,141 on CIQ's ratio definition [calc]) | As-Reported; Key Stats |
| 11 | [[ciq-segment-history]] | "Mexico overtook North America as the largest Adj. EBITDA contributor from FY22" | Mexico was already larger in FY2015-FY2019 (e.g., 18,200 vs 12,994 in FY2018) and North America led only in FY2020-FY2021 | Segment Analysis (EBITDA by region) |
| 12 | [[ciq-segment-history]] | FY2019 onward only; "Iberia 2011FQ4-2014FQ1" label history | Added: regional net sales FY2003-FY2005, FY2015-FY2018; EBITDA FY2015-FY2018; assets since 2001; Iberia revenue exists only 2012 FQ1-2013 FQ1 (assets 2011 FQ4-2014 FQ1) | Segment Analysis |
| 13 | [[ciq-historical-multiples]] | "Full history starts in 1994-2001 ... the 'all-history' mean is not meaningful and is not shown" | Meaningful from 1999/2000: TEV/LTM EBITDA mean 8.64x, median 8.03x (2000-2026); 7.35x (2000-2008), 11.31x (2012-2018), 7.36x (2019-2026); today's 6.29x is the 8th percentile since 2000. Outliers are confined to 1996-1998 (TEV) and 2012-2019 (P/E LTM) | Multiples |
| 14 | [[ciq-historical-multiples]] | "10-year mean 7.78x" as the reference | Reference depends on regime: 2000-2008 mean 7.35x, 2012-2018 11.31x, 2019-2026 7.36x | Multiples |
| 15 | [[ciq-consensus-estimates]] section 4 | FY2024-FY2025 guidance history only (context) | FY2018-FY2026 guidance versus actual: last EBITDA guide missed in FY2022-FY2024 and beaten in FY2025; first guide too high in FY2023 (-4.8%), FY2024 (-2.4%), FY2025 (-10.0%) | Estimates/Guidance (1) |
| 16 | [[ciq-consensus-estimates]] section 2 | "Dividend per share FY2025A 1.00; FY2026E 1.01 (median 1.07)" and the DPS/EPS ratio of 38.8% | CIQ consensus "actual" DPS is a pay-year series (0.00 for FY2014, FY2015, FY2019, FY2021; 1.30 for FY2022); on a declared-year basis FY2025 DPS is 1.075 and payout 41.7% [calc]; FY2026E 1.01 is below the 1.075 already paid in May-2026 | Consensus; Dividends & Splits; Templated IS |
| 17 | [[ciq-estimate-revisions-and-surprises]] | "Recent Changes covers estimate changes to 05-Oct-2026"; hit rates for 22 quarters only | Last dated change in the sheet is 28-Sep-2026 (header range runs to 05-Oct-2026); the sheet holds 2,368 rows from 2000-05-24; EBITDA beat 52 of 79 quarters since 2004 (median +3.4%), EPS normalized 36 beats / 37 misses | Recent Changes; Surprise |
| 18 | [[ciq-sell-side-sentiment-facts]] | "consensus mean target was MXN 94.13 after a change on 21-Jan-2024" as the path anchor | Year-end path 2004-2025: 7.75 (2004), 55.24 (2016), 95.14 (2023 peak), 75.34 (2024), 68.58 (2025); rating consensus Hold or Outperform every year since 2000 (3.20 in 2013, 3.09 in 2024, 2.58 now) | Recent Changes |
| 19 | [[ciq-debt-evolution-2019-2026]] section 4 | "(pre-IFRS for the early years [unverified])" | CIQ flags FY1996-FY2011 as "Mexican GAAP" and FY2012 onward as "IFRS" (Consensus accounting-standard row), matching the company's transition date of 1-Jan-2011 and first IFRS annual report FY2012 [[bimbo-history-2008-2013]]: upgrade to [sourced] | Estimates/Consensus |
| 20 | [[ciq-corporate-issuance-history]] | Splits "1.1:1 (ex 2011-04-25), 20% stock dividend (1999), 1.1:1 (1998)" "not verified" | Pre-2011 CIQ dividend amounts follow the 1.1 factor only; filings show a 4-for-1 split effective 29-Apr-2011 (already noted in [[bimbo-history-2008-2013]]); the 2010 holdings snapshot in the Ownership History is 4.00x overstated, confirming the unadjusted split | Dividends & Splits; Ownership History |
| 21 | [[ciq-corporate-issuance-history]], [[ciq-ownership-structure]] (Source lists) | Cite `OwnerShip/Corporate Issuance/...` | The same eight files now also sit at `Corporate Issuance/...` (identical); cite one path | folder comparison |
| 22 | [[ciq-ownership-structure]] (warning box) | "CIQ misses the controlling shareholders ... reports 0 shares excluded from float" | CIQ history lists Normaciel, Promociones Monser, Philae, Marlupag, Valacci (and Sendamos / Distribuidora Comercial Senda in earlier years) every year 2007-2024 (2,929m shares, 67.7% of CIQ shares at FY2024); they disappear from the 31-Dec-2025 and Latest columns, so the 94.5% "public" is a 2025-refresh artifact | OwnerShip History 10-Oct |
| 23 | [[ciq-ownership-structure]] section 4 and section 1 | Price MXN 55.41, market cap 238,057, institutions 5.49%; BlackRock 104,120,971 (+238,701); Dimensional 11,755,209 (+496,544; 31-Aug-2026); Schwab 5,233,843 rank 5; Deutsche 5,018,549 rank 6; State Street 4,424,954 (+32,209); sum of holders 236,048,640 | 10-Oct: price 55.92, market cap 240,248, institutions 5.48%; BlackRock 104,061,882 (+179,612); Dimensional 11,969,309 (+710,644; 30-Sep-2026); Deutsche rank 5 (5,018,549); Schwab 4,669,676 rank 6 (-413,613; 1-Oct-2026); State Street 4,428,082 (+35,337); sum 235,410,638 | OwnerShip Detailed and Cross-holdings 10-Oct |
| 24 | [[ciq-ownership-structure]] section 6 | "Sum of all listed holders 237,508,121" at 31-Dec-2025; "Vanguard ... -3.7% (entity relabelled)"; "-0.6%" change | 31-Dec-2025 sum is 237,282,121 in the 10-Oct history (Legal & General restated 436,791 to 210,791); Latest change -0.8% [calc]; Vanguard Group Inc. fell from 86.6m (2024) to 52.6m (2025), so the -3.7% understates the 12-month fall on a like-for-like entity basis (the Latest entity holds 50.65m plus 2.50m under Vanguard Asset Management) | OwnerShip History 06-Oct vs 10-Oct |
| 25 | [[ciq-ownership-structure]] open item 3 | "Who is behind Sendamos (in the 2022 register, absent from 2023 onward)?" | CIQ shows Sendamos S.A.P.I. de C.V. 150.0m (135.0m in FY2020) in FY2017-FY2021 and, possibly its predecessor, Distribuidora Comercial Senda 175.0-183.8m in FY2007-FY2015 [unverified]; no entry after FY2021 (the Apr-2022 register still listed 150,000,000) | OwnerShip History |
| 26 | [[ciq-esg-scores-and-profiles]] | "Governance & Economic has been stuck at 43-46 for five years and is the structural drag." | G&E was 47-52 in 2013-2017, 36 in 2018, 44-51 in 2019-2021, then 46, 46, 46, 43, 46: a post-2018 weakness; its weight fell from 42% (2016-2020) to 32% (2026) | ESG Scores History 2013-2021 |
| 27 | [[ciq-esg-scores-and-profiles]] section 3 | Industry average / highest: Corporate Governance (43 / 78), Information Security (19 / 79), Health & Nutrition (12 / 93), Packaging (24 / 91), Materiality (37 / 100), Energy (42 / 98), Water (34 / 90), Policy Influence (17 / 84), Climate Strategy | 10-Oct refresh: Corporate Governance (43 / 82), Information Security (19 / 83), Health & Nutrition (13 / 93), Packaging (25 / 91), Materiality (38 / 100), Energy (43 / 98), Water (35 / 96), Policy Influence (18 / 84), Climate Strategy (33 / 90); company scores and total (59) unchanged | ESG Scores 10-Oct |
| 28 | [[ciq-esg-scores-and-profiles]] section 4 | Industry comparators: biodiversity policy 40.85%; Scope 1 55.28% below average; Paris 3.13%; physical risk 4.33% above; women in management 3.96% below; LTIFR 48.58% below; human rights 69.01%; ethics 76.06% | 44.00%; 54.00%; 2.94%; 3.80%; **6.51% below ("Lagging" instead of "Adequate")**; 46.63%; 70.67%; 77.33% | Sustainability Overview 10-Oct |
| 29 | [[ciq-esg-scores-and-profiles]] section 5 and Key Takeaways | Business Involvement revenue base "MXN 413,096 M" (-3.2% vs FY25 net sales) | 413,359 M in the 10-Oct file (-3.2%); no involvement in screened activities unchanged | Business Involvement Screens 10-Oct |
| 30 | [[ciq-esg-scores-and-profiles]] section 2 | History "2022-2026" | Extended to 2013-2026; 2018 trough 39 and 2013-2014 level 43; 875 question-level PDFs | ESG Scores History; ESG Scores Raw Data |
| 31 | [[ciq-pension-obligations]] | Roll-forward 2019-2025 | Projected benefit obligation and plan assets are available from 2004 (PBO 4,676 and assets 4,315 in 2004; gap 9,331 at 2016; 1,524 at 2025) | Templated Pension Details |

## 5. Contradictions inside the wiki that the new data resolve or expose

| Topic | Statement A | Statement B | Resolution |
|---|---|---|---|
| FY2021 sales basis | [[ciq-income-statement-history]]: 338,792 (restated) | [[ciq-consensus-estimates]]: 348,887 (not restated) | file-dependent (row 5) |
| FY2025 dividend | IS history: 1.075 for FY25 | consensus: 1.00 actual FY2025 | declared-year versus pay-year basis (row 16) |
| Controlling holders in CIQ | [[ciq-ownership-structure]]: CIQ has none | [[ciq-ownership-and-holdings-history]]: CIQ lists them 2007-2024 | dropped in the 2025 refresh (row 22) |
| CIQ EBITDA versus company | "below, widening" | above in FY2012-FY2019 | regime split at FY2020 (row 3) |
| Regional EBITDA leadership | "Mexico overtook North America from FY22" | Mexico led in FY2015-FY2019 | row 11 |

## 6. Gaps and files not usable for numbers

| Item | Why | Impact |
|---|---|---|
| 73 of 875 ESG question PDFs | Performance Summary labels have no values in the text layer (2020: 10, 2021: 11, 2022: 11, 2023: 13, 2024: 13, 2025: 7, 2026: 8) | excluded from question-level counts; 2026 criterion scores remain in ESG Scores |
| As-Reported Balance Sheet | xlsx plus DOCX only; mixed units per column (thousands/millions/actual); 194 line items | not used for numbers; Templated balance sheet complete |
| As-Reported Income Statement | units vary by column (thousands, millions, actual); 1995-1996 and 2005 columns annual-in-FQ4 | used only for 2024 FQ4 and checks |
| Templated Cash Flow before 2019 | annual figures in FQ4 only and incomplete quarter counts | use As-Reported annual |
| Segment 2006-2014 | one or two quarters per year | no annual regional sales |
| Recent Changes | broker names hidden ("Not Entitled") for most rows; only FY2026 and FY2027 periods exported | FY2025-and-earlier revision paths cannot be rebuilt |
| Recommendation distribution | counts of Buy/Hold/Sell absent | only the mean score |
| Estimate Highlights, Key Stats, Recent Changes PDFs | format copies; the Recent Changes PDF is a 4-page excerpt | not needed |
| DOCX copies | open in Word; python-docx fails on package structure | content duplicated in xlsx |
| FY2024 EBITDA/EBIT in CIQ | missing in every income-statement export | use company Adjusted EBITDA 55,474 |

## Connections
- New articles built on these files: [[ciq-long-history-income-balance-cashflow]], [[ciq-segment-and-geography-long-history]], [[ciq-long-history-multiples-and-returns]], [[ciq-guidance-and-estimate-history]], [[ciq-ownership-and-holdings-history]], [[ciq-esg-profile-history]].
- Earlier articles affected: [[ciq-income-statement-history]], [[ciq-cash-flow-history]], [[ciq-key-ratios-and-performance]], [[ciq-segment-history]], [[ciq-historical-multiples]], [[ciq-consensus-estimates]], [[ciq-estimate-revisions-and-surprises]], [[ciq-sell-side-sentiment-facts]], [[ciq-debt-evolution-2019-2026]], [[ciq-corporate-issuance-history]], [[ciq-ownership-structure]], [[ciq-esg-scores-and-profiles]], [[ciq-pension-obligations]].
- Rules for callouts and sources: `WIKI.md`; source map: [[bimbo-filings-source-map]]; team checks: [[cfa-research-standards-checklist]].

## Key Takeaways

- Only 12 new spreadsheets and 875 ESG question PDFs carry new data; the other growth in `filings/capitaliq/` is news, research, duplicate folders and PDF/DOCX copies.
- ==The As-Reported exports close the two declared gaps (FY2024 P&L and FY2021/FY2024 cash flow)== and the Templated files, already in the repo, hold 25 more years of annual data that no earlier article used.
- 31 claims need a Superseded callout or an extension; the most consequential: CIQ EBITDA sign by period (#3), "CIQ misses the controlling shareholders" (#22), the Mexico-versus-North America EBITDA ranking (#11), the dividend basis (#16) and the "stuck at 43-46" Governance claim (#26).
- The 10-Oct refresh changed prices, positions and ESG industry comparators, not Bimbo's own ESG scores or any financial statement value.
- Gaps remain for FY2024 EBITDA/EBIT in CIQ, regional sales 2006-2014, 73 ESG PDFs without values, broker names and the rating distribution.
