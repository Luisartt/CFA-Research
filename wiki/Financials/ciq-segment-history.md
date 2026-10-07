---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Financials/Templated/Segment Analysis/SPGlobal_GrupoBimbo,S.A.B.deC.V._SegmentAnalysis_19-Sep-2026.xlsx
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T25.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T23_VF.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T22_0.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T24.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T21.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%201T26_VFF.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%202T26_VF.pdf
tags: [Financials, segment-history]
---

# Grupo Bimbo — Segment History (Capital IQ)

Regional (geographic) and line-of-business segment data as carried by S&P Capital IQ (CIQ), file downloaded **2026-09-19**, covering quarters 2001FQ4–2026FQ2. CIQ header: "Reporting Basis: Current/Restated", "Magnitude: Thousands (K)", reported currency MXN. Shown here in **MXN millions** (÷1,000). Tidy data: `data/capitaliq/segments.csv` (long format, one row per period × segment × metric; CIQ "NA" kept as text). Filing-based segment narrative: [[bimbo-segments-and-regions]]; consolidated P&L: [[bimbo-income-statement-fy21-fy25]]; quarterly trend: [[bimbo-quarterly-trend-4q21-2q26]]; North America story: [[bimbo-north-america-turnaround-evidence]].

All CIQ figures below: [sourced] CIQ SegmentAnalysis, sheet 'Segment Analysis'. Annual figures are [calc] = sum of the four CIQ quarters (CIQ only provides quarters).

## 1. What the CIQ file contains

| Block | Segments | Metrics populated |
|---|---|---|
| Line of Business | "Bakery Products and Foods" (single segment = consolidated) | Revenue, gross profit, operating income, interest expense, EBT, tax, net income, total assets; D&A and capex only in FQ1/FQ4 of some years |
| Geographic | North America, Mexico, Latin America, Europe Asia & Africa (EAA), Elimination Consolidated, Segment Adjustment | Revenue, EBITDA, operating income, total assets (most quarters); gross profit (sporadic); net income, interest, tax, D&A (FQ1/FQ4 of some years only) |

- The sheet's third block ("Segments", rows 180+) is a re-layout of the same numbers; it was checked cell-for-cell against the first two blocks (identical) and not re-extracted.
- **Label history** [sourced]: "Foreign" 2007FQ3–2010FQ3; "Iberia" 2011FQ4–2014FQ1; "Europe" 2013FQ4–2016FQ1; EAA from 2016FQ2. One stray "Europe" label in 2023FQ3 (revenue 9,919) is the EAA value for that quarter — it is treated as EAA below [calc check: FY23 EAA 30,626 + 9,919 = 40,545 = company 40,545].
- CIQ "EBITDA" by region **equals the company's Adjusted EBITDA** (UAFIDA Ajustada, pre-MEPP charges): FY25 North America 17,117 and Mexico 31,630 match the 4T25 release p.6 exactly.
- The geographic header skips 2008FQ1, 2009FQ1–FQ2 and 2011FQ1–FQ2; geographic **2024FQ4 is entirely "NA"** (all regions, all metrics), and the line-of-business block is also NA for 2024FQ4 except total assets.

## 2. Net sales by region, FY2019–1H26 (MXN m)

| Region | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 (9M only) | FY25 | 1H26 |
|---|---|---|---|---|---|---|---|---|
| North America | 144,005 | 176,395 | 175,368 | 205,591 | 192,535 | 136,317 | 190,211 | 84,901 |
| Mexico | 102,688 | 104,593 | 109,089 | 126,734 | 145,386 | 113,548 | 154,809 | 80,005 |
| EAA | 26,655 | 30,029 | 34,195 | 37,526 | 40,545 | 32,425 | 54,213 | 25,819 |
| Latin America | 27,144 | 29,081 | 31,109 | 38,410 | 36,648 | 28,815 | 44,130 | 23,128 |
| Eliminations (as reported by CIQ) | (4,009) | (4,201) | (3,137) | (2,974) | (7,751) | (3,974) | (7,996) | n/a |
| **Consolidated (LoB "Bakery Products and Foods")** | **291,926** | **331,051** | **338,792** | **398,706** | **399,879** | **298,023** | **426,963** | **205,308** |

All [calc] sums of CIQ quarters. FY24 is 1Q–3Q only because CIQ 2024FQ4 is NA; company 4Q24 net sales were 110,312 [sourced, 4T24 release p.3], giving FY24 408,335 [calc: 298,023 + 110,312], equal to the company FY24 figure (4T24 p.3).

> [!warning] Eliminations are incomplete in CIQ
> CIQ populates "Elimination Consolidated" only in FQ1 and FQ4 (e.g. 2025FQ1 −4,094, 2025FQ4 −3,902); FQ2 and FQ3 are NA. The CIQ "SubTotal – Geographic Segments" for FQ2/FQ3 therefore **overstates** consolidated sales (2025FQ2: geographic subtotal 111,770 vs consolidated 107,389 [sourced]). Use the line-of-business row for consolidated totals and the regional rows only as gross regional sales.

> [!warning] 2026FQ1 "Segment Adjustment" −8,545
> In 2026FQ1 CIQ books a revenue "Segment Adjustment" of −8,545 and no elimination; the geographic subtotal is 95,853 vs the line-of-business revenue 100,282 [sourced] and company net sales 100,319 [sourced, 1T26 release p.3]. Regional rows themselves look right (EAA 12,631 = company, 1T26 p.3). Do not use the 2026FQ1 geographic subtotal.

### Recent quarters (MXN m)

| Region | 1Q25 | 2Q25 | 3Q25 | 4Q25 | 1Q26 | 2Q26 |
|---|---|---|---|---|---|---|
| North America | 46,580 | 49,124 | 47,470 | 47,037 | 40,533 | 44,368 |
| Mexico | 38,018 | 38,475 | 38,897 | 39,419 | 39,726 | 40,279 |
| EAA | 12,042 | 13,436 | 14,369 | 14,366 | 12,631 | 13,188 |
| Latin America | 10,902 | 10,735 | 10,707 | 11,786 | 11,508 | 11,620 |
| Consolidated (LoB) | 103,448 | 107,389 | 107,421 | 108,706 | 100,282 | 105,026 |

All [sourced]. Mexico regional sales rose from 102,688 (FY19) to 154,809 (FY25), +50.8% [calc]; North America from 144,005 to 190,211, +32.1% [calc] in MXN (translation effects not separated in CIQ).

## 3. Adjusted EBITDA by region and margin

| Region | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 (9M) | FY25 | 1H26 |
|---|---|---|---|---|---|---|---|---|
| North America | 16,216 | 22,694 | 21,452 | 22,611 | 20,217 | 12,682 | 17,117 | 7,892 |
| Mexico | 19,839 | 19,165 | 20,770 | 23,320 | 27,484 | 22,622 | 31,630 | 16,502 |
| EAA | 1,669 | 2,295 | 2,704 | 2,626 | 2,931 | 3,007 | 5,830 | 2,658 |
| Latin America | 593 | 1,428 | 1,926 | 3,433 | 3,531 | 2,566 | 3,552 | 1,947 |
| Company consolidated Adj. EBITDA | n/c | n/c | 47,372 (restated) | 53,445 | 54,942 | 55,474 (FY) | 59,456 | 29,149 |

Regional rows [calc] sums of CIQ quarters. Company row [sourced]: FY21 restated and FY22 from 4T22 release p.3; FY23 and FY24 from 4T24 release p.3; FY25 from 4T25 release p.3; 1H26 [calc] = 14,036 (1T26 p.5) + 15,113 (2T26 p.5). n/c = not compiled here.

**Adj. EBITDA margin by region [calc = regional EBITDA ÷ regional sales]:**

| Region | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 (9M) | FY25 | 1H26 |
|---|---|---|---|---|---|---|---|---|
| North America | 11.3% | 12.9% | 12.2% | 11.0% | 10.5% | 9.3% | 9.0% | 9.3% |
| Mexico | 19.3% | 18.3% | 19.0% | 18.4% | 18.9% | 19.9% | 20.4% | 20.6% |
| EAA | 6.3% | 7.6% | 7.9% | 7.0% | 7.2% | 9.3% | 10.8% | 10.3% |
| Latin America | 2.2% | 4.9% | 6.2% | 8.9% | 9.6% | 8.9% | 8.0% | 8.4% |

- ==Mexico generated more Adj. EBITDA than North America in every year from FY22 onward== in CIQ data (FY25: 31,630 vs 17,117 [sourced sums]) despite lower sales; North America margin fell from 12.9% (FY20) to 9.0% (FY25) [calc].
- EAA margin roughly doubled from 6.3% (FY19) to 10.8% (FY25) [calc]; FY25 matches the company's "record" 10.8% (4T25 release p.2, as-of 4Q25) [sourced].
- Quarterly Adj. EBITDA 2025FQ1–2026FQ2 (MXN m) [sourced]: North America 3,425 / 4,432 / 4,932 / 4,328 / 3,468 / 4,424; Mexico 7,220 / 7,793 / 7,941 / 8,676 / 8,159 / 8,343; EAA 863 / 1,381 / 1,607 / 1,979 / 1,116 / 1,542; Latin America 1,037 / 994 / 921 / 600 / 1,054 / 893.

## 4. Operating income by region (MXN m)

| Region | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 (9M) | FY25 | 1H26 |
|---|---|---|---|---|---|---|---|---|
| North America | 6,093 | 11,195 | 15,171 | 33,263 | 11,174 | 4,947 | 6,272 | 3,227 |
| Mexico | 15,966 | 14,976 | 16,731 | 18,824 | 21,881 | 17,473 | 23,442 | 12,261 |
| EAA | 136 | 168 | 292 | (485) | 327 | 1,011 | 2,498 | 1,048 |
| Latin America | (1,338) | (402) | 78 | 1,087 | 1,294 | 1,003 | 607 | 263 |
| Consolidated (LoB) | n/a (FY19 NA) | 23,364 (3Q only) | 32,580 | 53,696 | 35,455 | 24,908 | 34,146 | 16,738 |

All [calc] sums of CIQ quarters. FY25 regional values match the company table (North America 6,272; Mexico 23,442; EAA 2,498; Latin America 607) [sourced, 4T25 release p.6].

- North America 4Q22 operating income of 19,343 [sourced] is an outlier: the company flags that 2022 operating income "includes the effect of the MEPPs" (4T23 release p.3) [sourced]. FY22 regional operating income is not comparable with other years.

## 5. Total assets by region (MXN m, period-end)

| Region | Dec-19 | Dec-22 | Dec-25 | Jun-26 |
|---|---|---|---|---|
| North America | 153,634 | 191,504 | 187,490 | 183,375 |
| Mexico | 68,556 | 89,070 | 108,596 | 112,344 |
| EAA | 35,072 | 49,033 | 73,804 | 71,199 |
| Latin America | 23,494 | 31,557 | 48,921 | 50,687 |
| Eliminations | (1,675) | (13,400) | (9,006) | NA |
| **Total** | **279,081** | **347,764** | **409,805** | **409,173** |

All [sourced]. North America's share of regional assets (before eliminations) fell from 54.7% at Dec-19 [calc: 153,634 / 280,756] to 44.8% at Jun-26 [calc: 183,375 / 409,173 — no elimination reported at Jun-26].

## 6. Reconciliation with company releases

| Item | CIQ [calc / sourced] | Company [sourced] | Difference [calc] |
|---|---|---|---|
| FY21 net sales (restated, ex-Ricolino) | 338,792 | 338,792 (4T22 p.5) | 0 |
| FY21 regional sales NA / MX / LatAm / EAA | 175,368 / 109,089 / 31,109 / 34,195 | 175,369 / 109,089 / 31,109 / 34,195 (4T22 p.5) | −1 / 0 / 0 / 0 |
| FY22 net sales | 398,706 | 398,706 (4T22 p.5) | 0 |
| FY22 regional NA / MX / LatAm / EAA | 205,591 / 126,734 / 38,410 / 37,526 | 205,674 / 130,401 / 38,411 / 37,536 (4T22 p.5) | −83 / **−3,667** / −1 / −10 |
| FY23 net sales | 399,879 | 399,879 (4T23 p.3) | 0 |
| FY23 regional NA / MX / LatAm / EAA | 192,535 / 145,386 / 36,648 / 40,545 | 192,534 / 145,387 / 36,647 / 40,545 (4T23 p.3) | +1 / −1 / +1 / 0 |
| FY24 net sales | 298,023 (9M) + n/a | 408,335 (4T24 p.3) | 4Q24 missing in CIQ |
| FY25 net sales | 426,963 | 426,952 (4T25 p.3) | +11 |
| FY25 regional NA / MX / EAA / LatAm | 190,211 / 154,809 / 54,213 / 44,130 | 190,211 / 154,809 / 54,214 / 44,120 (4T25 p.4) | 0 / 0 / −1 / +10 |
| 4Q25 Latin America sales | 11,786 | 11,769 (4T25 p.4) | +17 |
| FY25 Adj. EBITDA, sum of regions + CIQ eliminations | 58,791 | 59,456 (4T25 p.3) | −665 (eliminations only in FQ1/FQ4) |
| 1Q26 net sales | 100,282 | 100,319 (1T26 p.3) | −37 |
| 2Q26 net sales | 105,026 | 105,026 (2T26 p.3) | 0 |
| Net income, LoB, FY21 / FY22 / FY25 | 15,916 / 46,910 / 11,133 | 15,916 (4T21 p.2) / 46,910 (4T22 p.3) / 11,133 (4T25 p.3) majority net income | 0 |
| Net income, LoB, FY23 | 22,762 | 15,477 (4T23 p.3) | **+7,285** |

- ==Two material CIQ errors==: (1) **Mexico FY22 sales** are 3,667 below the company figure; the gap sits entirely in 4Q22 (CIQ 31,151 vs company 34,818, 4T22 p.5), possibly a Ricolino-divestiture restatement mismatch [unverified cause]. (2) **FY23 net income**: CIQ 3Q23 is 346 and 4Q23 is 14,378 [sourced] vs company 4Q23 majority net income 3,260 (4T23 p.3); the CIQ FY23 sum overstates by 7,285 [calc]. Use the company figures for both.
- Small differences of 1–37 (LatAm FY25, 1Q26) are rounding or late restatements; CIQ FY25 consolidated sales differ from the release by +11 [calc].

> [!question] Open items
> (1) Cause of the CIQ 4Q22 Mexico gap (3,667) and the 3Q23/4Q23 net income split. (2) Regional 4Q24 data must come from the 4T24 release, not CIQ. (3) CIQ does not split sales into volume, price and FX — use [[bimbo-segments-and-regions]] for that.

## Key Takeaways

- CIQ regional data cover North America, Mexico, EAA and Latin America quarterly from 2016FQ2 (EAA label) with good tie-out to company releases for FY21, FY23 and FY25 (differences ≤17 per region).
- CIQ regional "EBITDA" equals company Adjusted EBITDA; FY25 margins [calc]: Mexico 20.4%, EAA 10.8%, North America 9.0%, Latin America 8.0%.
- Mexico overtook North America as the largest Adj. EBITDA contributor from FY22 (FY25: 31,630 vs 17,117), while North America margin fell from 12.9% (FY20) to 9.0% (FY25).
- Data gaps: 2024FQ4 is NA in both segment blocks; eliminations only appear in FQ1/FQ4; 2026FQ1 has a −8,545 "Segment Adjustment" that breaks the geographic subtotal.
- Do not use CIQ for Mexico FY22 sales (−3,667 vs company) or FY23 net income (+7,285 vs company).
