---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Financials/Templated/Segment Analysis/SPGlobal_GrupoBimbo,S.A.B.deC.V._SegmentAnalysis_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Income Statement/SPGlobal_GrupoBimbo,S.A.B.deC.V._IncomeStatement_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Balance Sheet/SPGlobal_GrupoBimbo,S.A.B.deC.V._BalanceSheet_19-Sep-2026.xlsx
  - filings/capitaliq/Estimates/Consensus/SPGlobal_GrupoBimbo,S.A.B.deC.V._Consensus_20-Sep-2026.xlsx
tags: [Financials, segments-long-history]
---

# Grupo Bimbo — Segment and Geography Long History (Capital IQ, 2001-2025)

What the CIQ Segment Analysis export holds **before FY2019**, which [[ciq-segment-history]] did not tabulate: regional net sales, EBITDA, operating income and total assets back to 2001-2003, the mix shift from a Mexico-centred group (about 69% of regional sales in FY2005) to a three-region group in which North America is the largest, and the capital each region absorbs. Same sheet, same download (19-Sep-2026); the earlier article covers FY2019-1H26 and the reconciliation to company releases, which is not repeated. Company-filing view: [[bimbo-segments-and-regions]]; consolidated totals: [[ciq-long-history-income-balance-cashflow]].

**Citation key.** `CIQ-SEG` = Segment Analysis file, sheet 'Segment Analysis' (quarterly columns; the Geographic block has its own header row and its own set of periods). MXN millions (CIQ thousands ÷ 1,000). Annual figures are sums of four quarters `[calc]` and appear only when all four quarters exist; label families are merged `[calc]`: "EAA / Europe" = Europe, Asia and Africa (from 2016 FQ2), "Europe" (2013 FQ4-2016 FQ1 and one stray 2023 FQ3 value) and "Iberia" (2012-2013). "Eliminations + adjustments" = CIQ rows "Elimination Consolidated" plus "Segment Adjustment".

## 1. Coverage: which years can be built

| Metric | Regions populated from | Complete (4-quarter) years | Partial years (quarters present) |
|---|---|---|---|
| Net sales | 2003 FQ1 (Mexico, North America, Latin America); EAA from 2016 FQ2 | FY2003-FY2005, FY2010 (Mexico and consolidated only), FY2015-FY2023, FY2025 | FY2006: Q4 only; FY2007: Q3-Q4; FY2008: Q2-Q4; FY2009: Q3-Q4; FY2011: Q4 only; FY2012-FY2014: Q1 and Q4 only; FY2024: none |
| EBITDA | 2011 FQ4 | FY2015-FY2023, FY2025 | FY2011: Q4; FY2012-FY2014: two quarters; FY2024: 9M only |
| Operating income | 2003 FQ1 | FY2003-FY2005, FY2015-FY2023, FY2025 | FY2006 Q4 only; FY2007-FY2010: none; FY2011-FY2014: 1-2 quarters; FY2024: 9M |
| Total assets (period end) | 2001 FQ4 | every year-end 2001-2025 (Mexico, North America, Latin America); EAA/Europe/Iberia from 2011 FQ4 | – |

`[sourced]` CIQ-SEG coverage by quarter; the 2007-2010 regional split uses a different label set ("Foreign" 2007 FQ3-2010 FQ3) and is not comparable with later years. Geographic 2024 FQ4 is NA in every region and metric (as in [[ciq-segment-history]]); 9M24 values: net sales Mexico 113,548, North America 136,317, Latin America 28,815, EAA 32,425 (consolidated 298,023); EBITDA 22,622 / 12,682 / 2,566 / 3,007; operating income 17,473 / 4,947 / 1,003 / 1,011 `[calc]`.

## 2. Net sales by region

`[calc]` sums of CIQ-SEG quarters. "Sum of regions" = regions plus eliminations/adjustments and should equal consolidated net sales when eliminations are complete (CIQ posts eliminations only in some quarters, see [[ciq-segment-history]]): it equals the consolidated income statement exactly in FY2003 (49,100), FY2004 (52,573), FY2005 (58,643) and FY2018 (289,320), is 1.2%-1.4% above it in FY2015-FY2017 and within 2.0% above it in FY2022-FY2025 (FY2023 407,363 vs 399,879; FY2025 435,367 vs 426,963) `[calc]`. FY2003-FY2005 have no EAA/Europe segment (all non-Mexico foreign operations are in North America and Latin America).

| FY | Mexico | North America | Latin America | EAA / Europe | Eliminations + adjustments | Sum of regions |
|---|---|---|---|---|---|---|
| 2003 | 33,197 | 13,344 | 3,405 | – | -846 | 49,100 |
| 2004 | 36,800 | 13,173 | 3,741 | – | -1,141 | 52,573 |
| 2005 | 41,545 | 14,102 | 4,376 | – | -1,380 | 58,643 |
| 2015 | 76,295 | 116,399 | 24,273 | 7,560 | -2,571 | 221,956 |
| 2016 | 81,624 | 135,219 | 29,100 | 12,438 | -3,240 | 255,141 |
| 2017 | 90,367 | 137,661 | 28,602 | 18,658 | -3,952 | 271,336 |
| 2018 | 100,327 | 143,968 | 28,341 | 25,899 | -9,215 | 289,320 |
| 2019 | 102,688 | 144,005 | 27,144 | 26,655 | -4,009 | 296,483 |
| 2020 | 104,593 | 176,395 | 29,081 | 30,029 | -4,201 | 335,897 |
| 2021 | 109,089 | 175,368 | 31,109 | 34,195 | -8,224 | 341,537 |
| 2022 | 126,734 | 205,591 | 38,410 | 37,526 | -2,974 | 405,287 |
| 2023 | 145,386 | 192,535 | 36,648 | 40,545 | -7,751 | 407,363 |
| 2025 | 154,809 | 190,211 | 44,130 | 54,213 | -7,996 | 435,367 |

- ==Mexico was 66.5% of regional sales in FY2003 and 69.2% in FY2005, versus 34.0% in FY2015 and 34.9% in FY2025== `[calc]`. The shift happened in two steps: the Weston Foods US purchase (2009; North America assets 14,221 to 53,361 between FY2008 and FY2009 `[sourced]` CIQ-SEG) and Sara Lee North America (2011; 49,380 to 79,870). The Canada Bread purchase lifted North America assets from 71,790 to 115,427 in FY2014 `[sourced]` (see [[bimbo-history-2008-2013]], [[bimbo-cash-flow-and-capex-fy14-fy20]]).
- North America peaked at 52.3% of regional sales in FY2016 (51.9% in FY2020) and has fallen to 42.9% in FY2025 as Mexico (+7.3% a year, FY2015-FY2025 `[calc]`) and EAA (+17.8% a year from the FY2016 base of 12,438, mostly acquisitions) grew faster; its revenue is 190,211 in FY2025 versus 205,591 in FY2022, a fall of 7.5% in MXN `[calc]` (translation as well as volume; see [[bimbo-fx-exposure]]).
- EAA (Europe/Iberia/Africa/Asia) net sales rose from 7,560 (FY2015, label "Europe") to 54,213 (FY2025), i.e. ==7.2x in ten years== `[calc]`, driven by acquisitions: the FY2025 step (+13,668, +33.7% on FY2023's 40,545 over two years) is separate from organic trend.
- Latin America has been the smallest and slowest region: 24,273 (FY2015) to 44,130 (FY2025), +6.2% a year `[calc]`.

## 3. EBITDA and margins by region

`[sourced]` CIQ-SEG "EBITDA" by region, which equals the company's regional Adjusted EBITDA ([[ciq-segment-history]]); the sum of regions plus adjustments equals company Adjusted EBITDA (reproduces company FY2018 Adjusted EBITDA of 31,705; FY2019 38,520 vs 37,874 on the company's IFRS 16 basis, +646 unexplained `[calc]`; FY2025 58,791 vs 59,456, within 1.1% `[sourced]`). FY2018 and earlier are pre-IFRS 16 for the company headline ([[bimbo-income-statement-fy14-fy20]]), so the 2018-2019 step in every region partly reflects IFRS 16.

| FY | Mexico | North America | Latin America | EAA / Europe | Eliminations + adjustments | Sum of regions |
|---|---|---|---|---|---|---|
| 2015 | 13,431 | 9,687 | 519 | -335 | 147 | 23,449 |
| 2016 | 15,482 | 12,732 | 280 | 216 | 221 | 28,931 |
| 2017 | 15,931 | 12,641 | 470 | -1,568 | -122 | 27,352 |
| 2018 | 18,200 | 12,994 | 732 | 105 | -326 | 31,705 |
| 2019 | 19,839 | 16,216 | 593 | 1,669 | 203 | 38,520 |
| 2020 | 19,165 | 22,694 | 1,428 | 2,295 | -11 | 45,571 |
| 2021 | 20,770 | 21,452 | 1,926 | 2,704 | 273 | 47,125 |
| 2022 | 23,320 | 22,611 | 3,433 | 2,626 | 749 | 52,739 |
| 2023 | 27,484 | 20,217 | 3,531 | 2,931 | 300 | 54,463 |
| 2025 | 31,630 | 17,117 | 3,552 | 5,830 | 662 | 58,791 |

Margins `[calc]` = region EBITDA ÷ region net sales (before eliminations), and sales mix:

| FY | Mexico | North America | Latin America | EAA / Europe | Mexico share of regional sales | North America share |
|---|---|---|---|---|---|---|
| 2003 | n/a | n/a | n/a | n/a | 66.5% | 26.7% |
| 2004 | n/a | n/a | n/a | n/a | 68.5% | 24.5% |
| 2005 | n/a | n/a | n/a | n/a | 69.2% | 23.5% |
| 2015 | 17.6% | 8.3% | 2.1% | -4.4% | 34.0% | 51.8% |
| 2016 | 19.0% | 9.4% | 1.0% | 1.7% | 31.6% | 52.3% |
| 2017 | 17.6% | 9.2% | 1.6% | -8.4% | 32.8% | 50.0% |
| 2018 | 18.1% | 9.0% | 2.6% | 0.4% | 33.6% | 48.2% |
| 2019 | 19.3% | 11.3% | 2.2% | 6.3% | 34.2% | 47.9% |
| 2020 | 18.3% | 12.9% | 4.9% | 7.6% | 30.8% | 51.9% |
| 2021 | 19.0% | 12.2% | 6.2% | 7.9% | 31.2% | 50.1% |
| 2022 | 18.4% | 11.0% | 8.9% | 7.0% | 31.0% | 50.4% |
| 2023 | 18.9% | 10.5% | 9.6% | 7.2% | 35.0% | 46.4% |
| 2025 | 20.4% | 9.0% | 8.0% | 10.8% | 34.9% | 42.9% |

- ==Mexico is the profit engine in every year but FY2020-FY2021==: Mexico EBITDA exceeded North America in each of FY2015-FY2019 (e.g., 18,200 vs 12,994 in FY2018) and again from FY2022, and North America led only in FY2020 (22,694 vs 19,165) and FY2021 (21,452 vs 20,770) `[calc]`. The earlier statement that Mexico "overtook" North America from FY22 ([[ciq-segment-history]]) is therefore a return to the pre-2020 order, not a new one; see [[ciq-delta-vs-previous-export]].
- Mexico EBITDA margin has been 17.6%-20.4% in every year shown (20.4% in FY2025 is the highest); North America moved 8.3% (FY2015) to 12.9% (FY2020) and back to 9.0% (FY2025) `[calc]`.
- Latin America margin went from 1.0% (FY2016) to 9.6% (FY2023) and 8.0% (FY2025): a turnaround worth about 2.8 bn of EBITDA between FY2018 (732) and FY2025 (3,552) `[calc]`.
- EAA margin was negative in FY2015 (-4.4%) and FY2017 (-8.4%), turned positive in FY2019 (6.3%) and is 10.8% in FY2025, the first year above Latin America and North America `[calc]`.
- Share of regional EBITDA before eliminations `[calc]`: FY2015 Mexico 57.6%, North America 41.6%, Latin America 2.2%, EAA -1.4%; FY2025 Mexico 54.4%, North America 29.4%, EAA 10.0%, Latin America 6.1%.

## 4. Operating income by region

`[sourced]` CIQ-SEG; FY2007-FY2010 unavailable, FY2011-FY2014 partial. Operating income is after depreciation, amortization and the items CIQ keeps in operating income.

| FY | Mexico | North America | Latin America | EAA / Europe | Eliminations + adjustments | Sum of regions |
|---|---|---|---|---|---|---|
| 2003 | 4,067 | -442 | -158 | – | 18 | 3,485 |
| 2004 | 4,632 | -288 | -100 | – | 31 | 4,275 |
| 2005 | 5,261 | 80 | 56 | – | 47 | 5,444 |
| 2015 | 10,896 | 4,541 | -1,357 | -620 | 212 | 13,672 |
| 2016 | 13,095 | 7,161 | -2,453 | -305 | 219 | 17,717 |
| 2017 | 13,753 | 7,701 | -1,284 | -2,395 | -141 | 17,634 |
| 2018 | 15,750 | 5,100 | -529 | -1,481 | -331 | 18,509 |
| 2019 | 15,966 | 6,093 | -1,338 | 136 | 205 | 21,062 |
| 2020 | 14,976 | 11,195 | -402 | 168 | 396 | 26,333 |
| 2021 | 16,731 | 15,171 | 78 | 292 | 242 | 32,514 |
| 2022 | 18,824 | 33,263 | 1,087 | -485 | 543 | 53,232 |
| 2023 | 21,881 | 11,174 | 1,294 | 327 | 309 | 34,985 |
| 2025 | 23,442 | 6,272 | 607 | 2,498 | 891 | 33,710 |

- Latin America operating income was negative in FY2003-FY2004 and in 2011-2013 (-677, -630, -540 for 1-2 quarters each) and in every year FY2015-FY2020 (-1,357; -2,453; -1,284; -529; -1,338; -402), turning positive in FY2021 (78), FY2022 (1,087) and FY2023 (1,294) `[sourced]`; FY2025 is 607 `[sourced]`, half of FY2023 although EBITDA is unchanged (3,552 vs 3,531), so depreciation or one-offs rose `[calc]`.
- EAA operating income was negative in FY2016-FY2018 (-305, -2,395, -1,481) and FY2022 (-485), and reached 2,498 in FY2025 `[sourced]`.
- ==North America FY2022 operating income of 33,263 exceeds its EBITDA of 22,611 by 10,652==, which cannot be a run-rate; it is consistent with the non-cash multi-employer pension (MEPP) provision reversal that the company booked in 2022 ([[ciq-pension-obligations]], [[ciq-income-statement-history]]), but the export does not label the item `[unverified]`. North America FY2023 operating income is 11,174 and FY2025 6,272 (3.3% of its FY2025 net sales) `[calc]`.
- North America operating income fell from 15,171 (FY2021) to 6,272 (FY2025) while its EBITDA fell from 21,452 to 17,117: depreciation and amortization in the region rose from 6,281 to 10,845 (EBITDA less operating income) `[calc]`, the cost of the value-chain investment programme ([[bimbo-north-america-turnaround-evidence]]).

## 5. Capital absorbed by region (year-end total assets)

`[sourced]` CIQ-SEG "Total Assets", FQ4 column; EAA/Europe/Iberia combined from 2011. "Eliminations" are CIQ's inter-segment line; its jump to -17,850 in FY2020 coincides with the IFRS 16 era and is not itemised `[unverified]`.

| Year-end | Mexico | North America | Latin America | EAA / Europe / Iberia | Eliminations | Total |
|---|---|---|---|---|---|---|
| 2001 | 16,600 | 4,199 | 2,983 | n/a | n/a | 23,781 |
| 2002 | 17,900 | 13,495 | 2,808 | n/a | n/a | 34,203 |
| 2003 | 19,618 | 10,677 | 2,869 | n/a | 363 | 33,527 |
| 2004 | 23,841 | 9,680 | 2,916 | n/a | -1,767 | 34,670 |
| 2005 | 27,056 | 10,436 | 3,406 | n/a | -2,166 | 38,732 |
| 2006 | 30,440 | 11,131 | 4,905 | n/a | -2,537 | 43,939 |
| 2007 | 29,554 | 11,791 | 6,524 | n/a | -2,626 | 45,243 |
| 2008 | 36,529 | 14,221 | 11,360 | n/a | -3,604 | 58,506 |
| 2009 | 36,709 | 53,361 | 13,563 | n/a | -3,967 | 99,666 |
| 2010 | 36,121 | 49,380 | 16,045 | n/a | -2,477 | 99,069 |
| 2011 | 46,585 | 79,870 | 20,169 | 4,101 | -7,490 | 143,235 |
| 2012 | 45,287 | 72,718 | 19,750 | 3,886 | -4,501 | 137,140 |
| 2013 | 42,436 | 71,790 | 19,278 | 3,103 | -1,880 | 134,727 |
| 2014 | 36,449 | 115,427 | 20,176 | 6,844 | -1,135 | 177,761 |
| 2015 | 43,020 | 130,148 | 19,332 | 8,253 | -1,120 | 199,633 |
| 2016 | 47,837 | 154,417 | 27,080 | 17,188 | -1,356 | 245,166 |
| 2017 | 60,640 | 145,155 | 23,265 | 31,822 | -1,633 | 259,249 |
| 2018 | 63,569 | 142,161 | 22,387 | 36,468 | -1,269 | 263,316 |
| 2019 | 68,556 | 153,634 | 23,494 | 35,072 | -1,675 | 279,081 |
| 2020 | 72,528 | 186,298 | 24,586 | 42,089 | -17,850 | 307,651 |
| 2021 | 78,386 | 202,347 | 30,121 | 45,860 | -19,074 | 337,640 |
| 2022 | 89,070 | 191,504 | 31,557 | 49,033 | -13,400 | 347,764 |
| 2023 | 96,617 | 175,929 | 32,882 | 49,988 | -7,314 | 348,102 |
| 2024 | 106,018 | 210,863 | 44,958 | 65,992 | -11,027 | 416,804 |
| 2025 | 108,596 | 187,490 | 48,921 | 73,804 | -9,006 | 409,805 |

Capital intensity `[calc]` (EBITDA ÷ year-end segment assets, before eliminations):

| FY | Mexico | North America | Latin America | EAA | Share of segment assets: North America | Share of EBITDA: North America |
|---|---|---|---|---|---|---|
| 2015 | 31.2% | 7.4% | 2.7% | -4.1% | 64.8% | 41.6% |
| 2018 | 28.6% | 9.1% | 3.3% | 0.3% | 53.7% | 40.6% |
| 2019 | 28.9% | 10.6% | 2.5% | 4.8% | 54.7% | 42.3% |
| 2022 | 26.2% | 11.8% | 10.9% | 5.4% | 53.0% | 43.5% |
| 2023 | 28.4% | 11.5% | 10.7% | 5.9% | 49.5% | 37.3% |
| 2025 | 29.1% | 9.1% | 7.3% | 7.9% | 44.8% | 29.4% |

- ==North America holds 44.8% of segment assets (187,490) but produces 29.4% of regional EBITDA in FY2025==; Mexico holds 25.9% of assets and produces 54.4% `[calc]`. A return of 9.1% on assets (EBITDA basis) in North America compares with 29.1% in Mexico.
- Asset base growth FY2015-FY2025 `[calc]`: Mexico 2.5x (43,020 to 108,596), Latin America 2.5x (19,332 to 48,921), North America 1.4x (130,148 to 187,490), EAA 8.9x (8,253 to 73,804). North America assets fell 11.1% in FY2025 (210,863 to 187,490) after +19.9% in FY2024 `[calc]`, which includes currency translation.
- The very first CIQ-SEG year-end (FY2001) had North America at 4,199 of 23,781 total assets (17.7%); FY2002 jumped to 13,495 with the purchase of assets formerly owned by George Weston Ltd (6,686 `[sourced]` [[ciq-long-history-income-balance-cashflow]] cash flow table).

## 6. Data-quality flags and gaps

| Issue | Detail | Tag |
|---|---|---|
| Regional sales FY2006-FY2014 | at most two quarters per year; no annual regional net sales can be built for FY2006-FY2009 and FY2011-FY2014. Use company annual reports ([[bimbo-income-statement-fy98-fy07]], [[bimbo-income-statement-fy08-fy13]]) | [sourced] CIQ-SEG |
| Label changes | "Foreign" 2007-2010; "Iberia" 2012-2013; "Europe" 2013-2016 and one 2023 FQ3 value (9,919) that is EAA; merged here | [sourced] CIQ-SEG |
| FY2021 sum of regions | 341,537 vs consolidated 338,792 (restated) and 348,887 (first reported) because eliminations and the "Segment Adjustment" (-5,087 in one quarter) are incomplete | [calc] |
| FY2019-FY2020 sums | 296,483 and 335,897 vs consolidated 291,926 and 331,051: eliminations posted in 1-2 quarters only | [calc] |
| Line-of-business block | single segment ("Bakery Products and Foods"), identical to consolidated; only total assets 2001-2002 | [sourced] CIQ-SEG |
| 2026 FQ1 Segment Adjustment | -8,545 revenue adjustment breaks the geographic subtotal (see [[ciq-segment-history]]) | [sourced] |
| Operating-income comparability | CIQ regional operating income includes items that CIQ keeps out of consolidated EBIT (FY2022 North America) | [unverified] |

## Connections
- Earlier article on the same file: [[ciq-segment-history]]; company narrative and definitions: [[bimbo-segments-and-regions]], [[bimbo-competitive-position]]; consolidated history: [[ciq-long-history-income-balance-cashflow]].
- Capital allocation and acquisitions behind the asset steps: [[bimbo-capital-allocation]], [[bimbo-history-2008-2013]], [[bimbo-north-america-turnaround-evidence]]; FX translation: [[bimbo-fx-exposure]], [[bimbo-macro-by-region]].
- Valuation overlay: [[ciq-long-history-multiples-and-returns]]; analyst record: [[ciq-guidance-and-estimate-history]]; update list: [[ciq-delta-vs-previous-export]].

## Key Takeaways

- Mexico was about 69% of regional sales in FY2005 and is 34.9% in FY2025; North America (54.7% of segment assets in FY2019, 44.8% in FY2025) is the largest region by sales (42.9%) but only 29.4% of regional EBITDA.
- ==Mexico has produced the larger share of EBITDA in every year in the export except FY2020-FY2021== (FY2025 54.4%); the "Mexico overtook North America in FY22" reading in [[ciq-segment-history]] needs this context.
- Latin America moved from operating losses in every year FY2015-FY2020 to positive FY2021-FY2025 (EBITDA margin 1.0% in FY2016 to 8.0% in FY2025); EAA went from -8.4% (FY2017) to 10.8% margin.
- North America FY2022 operating income (33,263) exceeds EBITDA (22,611), a one-off consistent with the MEPP reversal; do not use that year as a margin base.
- North America earns 9.1% EBITDA on its year-end segment assets against 29.1% in Mexico; asset growth FY2015-FY2025 was 8.9x in EAA, 2.5x in Mexico and Latin America, 1.4x in North America.
- Annual regional sales cannot be built for FY2006-FY2014 from CIQ; use company filings for those years.
