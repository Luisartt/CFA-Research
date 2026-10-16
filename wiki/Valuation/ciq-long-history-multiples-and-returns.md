---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Financials/Templated/Multiples/SPGlobal_GrupoBimbo,S.A.B.deC.V._Multiples_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Balance Sheet/SPGlobal_GrupoBimbo,S.A.B.deC.V._BalanceSheet_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Templated/Income Statement/SPGlobal_GrupoBimbo,S.A.B.deC.V._IncomeStatement_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Key Stats/SPGlobal_GrupoBimbo,S.A.B.deC.V._KeyStats_19-Sep-2026.xlsx
  - filings/capitaliq/Corporate Issuance/Dividends & Splits/SPGlobal_GrupoBimbo,S.A.B.deC.V._DividendsAndSplits_06-Oct-2026.xlsx
  - filings/capitaliq/Estimates/Consensus/SPGlobal_GrupoBimbo,S.A.B.deC.V._Consensus_20-Sep-2026.xlsx
tags: [Valuation, multiples-returns-history]
---

# Grupo Bimbo — Long-History Multiples and Returns (Capital IQ, 1999-2026)

The full 27-year traded-multiple history in the CIQ Multiples export, which [[ciq-historical-multiples]] summarised only over the last 10 years (to Dec-2016). Adds: year-by-year valuation since 1999, statistics by accounting regime, where today's multiples rank in each regime, a book-value-based price proxy to size price return, dividends since 2012, and the link between multiples and returns on equity. ==Facts and derived arithmetic only; whether the shares are cheap is a team judgment== (see `notes/` and `research/thesis.md`). Same download as the existing article (19-Sep-2026; last column 18-Sep-2026, close MXN 54.20 `[sourced]` [[ciq-historical-multiples]]).

**Citation key.** `CIQ-MULT` = Multiples file, sheet 'Multiples' (quarterly columns Mar-1994 to Sep-18-2026; four rows per multiple: Average, High, Low, Close; "Diluted TEV Outstanding"). Annual rows below = mean of the quarterly "Average" rows in the year `[calc]`; "Q4 avg" = the December-quarter average `[sourced]`. Multiples before 1999 are excluded: TEV/LTM EBITDA averages 72x-104x in 1996-1998 (160.35x for the Q4-1997 average `[sourced]` CIQ-MULT), which reflects the inflation-accounting data in [[ciq-long-history-income-balance-cashflow]].

## 1. Basis breaks that matter for any comparison across eras

| Break | Effect on the multiple | Evidence |
|---|---|---|
| Mexican GAAP to IFRS (FY2011/FY2012) | EBITDA and EPS are restated; P/E LTM jumps to 31.6x-76.5x in 2012-2013 because IFRS EPS fell (FY2012 EPS normalized 0.43 `[sourced]` CIQ-CONS) | table 2; [[ciq-long-history-income-balance-cashflow]] |
| IFRS 16 (2019) | TEV includes lease liabilities (CIQ debt 189,679 at Jun-26 vs company 153,660 `[sourced]` [[ciq-historical-multiples]]) while EBITDA is stated after the IFRS 16 add-back, so EV/EBITDA is only partly comparable before and after 2019 | [[ciq-debt-evolution-2019-2026]] |
| CIQ EBITDA definition | the EBITDA in TEV/EBITDA is EBIT plus cash-flow D&A, not the income-statement EBITDA line (FY2025 implied 63,356 vs 54,815 vs company 59,456 `[calc]`) | [[ciq-key-ratios-and-performance]] |
| Acquisition years | 2009, 2011, 2014: TEV jumps before LTM EBITDA includes the acquired business, inflating LTM multiples for 2-4 quarters | [[bimbo-history-2008-2013]] |
| Share split | the 4-for-1 split effective 29-Apr-2011 is not in the CIQ splits table (only "1.1:1 split ex 2011-04-25"), so CIQ per-share dividends before 2011 are on a pre-split basis: multiply by 1.1/4 = 0.275 to compare (2010: 0.45455 x 0.275 = 0.125 `[calc]` vs company 0.13 split-adjusted [[bimbo-income-statement-fy08-fy13]]) | CIQ Dividends & Splits rows 30 and 53 `[sourced]` |

## 2. Year-by-year multiples, 1999-2026

`[calc]` mean of the quarterly averages in `[sourced]` CIQ-MULT; (nq) = fewer than four quarters; 2026 = Q1-Q2 only.

| Year | EV/EBITDA LTM (mean of qtr avgs) | Q4 avg | EV/EBITDA NTM | EV/Revenue LTM | P/E LTM | P/E NTM | P/B |
|---|---|---|---|---|---|---|---|
| 1999 | 9.36x | 8.77x | n/a | 1.30x | 19.46x | 17.17x | 2.12x |
| 2000 | 6.34x | 5.87x | 5.16x | 0.85x | 11.69x | 11.34x | 1.50x |
| 2001 | 5.97x | 6.95x | 4.97x | 0.81x | 10.16x | 10.88x | 1.19x |
| 2002 | 7.03x | 6.66x | 5.57x | 0.89x | 20.69x | 13.46x | 2.21x |
| 2003 | 6.72x | 7.09x | 4.91x | 0.73x | 18.51x | 14.77x | 1.33x |
| 2004 | 7.49x | 7.61x | 6.21x | 0.80x | 23.44x | 11.68x | 1.82x |
| 2005 | 7.22x | 7.12x | 6.30x | 0.84x | 17.34x | 12.99x | 2.08x |
| 2006 | 7.14x | 7.94x | 6.13x | 0.85x | 14.74x | 12.35x | 2.14x |
| 2007 | 9.47x | 8.54x | 8.28x | 1.14x | 19.84x | 16.86x | 2.92x |
| 2008 | 8.79x | 8.32x | 7.87x | 1.05x | 19.62x | 15.81x | 2.62x |
| 2009 | 9.21x | 9.83x | 7.11x | 1.13x | 17.05x | 13.91x | 2.30x |
| 2010 | 8.93x | 8.86x | 8.29x | 1.25x | 18.95x | 15.65x | 2.80x |
| 2011 | 10.20x | 11.10x | 8.25x | 1.28x | 22.65x | 16.49x | 2.75x |
| 2012 | 11.93x | 11.67x | 10.76x | 1.27x | 31.57x | 20.65x | 3.07x |
| 2013 | 13.30x | 13.48x | 12.35x | 1.28x | 76.54x | 31.39x | 4.10x |
| 2014 | 11.98x | 12.14x | 11.15x | 1.27x | 41.36x | 26.94x | 3.83x |
| 2015 | 12.00x | 12.02x | 11.26x | 1.35x | 45.05x | 28.69x | 3.92x |
| 2016 | 11.94x | 10.71x | 11.51x | 1.41x | 45.13x | 28.52x | 3.87x |
| 2017 | 9.34x | 9.05x | 9.27x | 1.12x | 40.80x | 25.34x | 3.20x |
| 2018 | 8.69x | 7.98x | 8.82x | 1.02x | 45.81x | 24.26x | 2.61x |
| 2019 | 7.38x | 6.78x | 7.88x | 0.96x | 34.18x | 23.14x | 2.29x |
| 2020 | 6.75x | 6.70x | 7.46x | 0.96x | 27.48x | 22.49x | 2.04x |
| 2021 | 6.33x | 7.02x | 7.03x | 0.97x | 18.42x | 18.75x | 2.40x |
| 2022 | 7.90x | 8.66x | 7.97x | 1.16x | 17.56x | 19.18x | 3.08x |
| 2023 | 8.70x | 8.85x | 8.56x | 1.26x | 14.20x | 20.77x | 3.57x |
| 2024 | 7.83x | 7.46x | 7.62x | 1.14x | 20.40x | 18.22x | 2.70x |
| 2025 | 6.84x | 7.03x | 7.00x | 1.03x | 20.52x | 17.25x | 2.02x |
| 2026 (2q) | 6.86x | n/a | 7.05x | 1.02x | 22.67x | 18.20x | 2.15x |

Reading `[calc]`:
- ==TEV/LTM EBITDA peaked at 13.30x on average in 2013 (quarter high 14.22x in Sep-2013) and has fallen in nine of the last twelve years to 6.84x in 2025==. The multiple was 5.97x-7.49x every year from 2000 to 2006 and 6.33x-8.70x in 2019-2025.
- Price/NTM EPS: 10.9x-16.9x through 2011, 20.7x-31.4x in 2012-2018, 17.3x-23.1x in 2019-2025; the 17.0x close (18-Sep-2026) is inside the 2019-2025 range and above every annual mean from 2000 to 2011.
- Price/book was 1.2x-2.9x for 1999-2011, 3.1x-4.1x in 2012-2016 and 2.0x-3.6x since 2017; the 2.02x close equals the 2025 average and is the lowest annual figure since 2004 (1.82x).
- Price/LTM EPS is not a usable long-run series in 2012-2019 (31.6x-76.5x) because of depressed IFRS-era EPS and CIQ's definitions; use the NTM series.

## 3. Statistics by accounting regime

`[calc]` from CIQ-MULT quarterly averages: mean / median; minimum (quarter) to maximum (quarter). "Now" is the 18-Sep-2026 close `[sourced]`.

| Multiple | Now (close, 18-Sep-2026) | FY2000-FY2008 (Mexico GAAP, pre-Weston) | 2009-2011 (Weston, Sara Lee) | 2012-2018 (IFRS, pre-IFRS 16) | 2019-2026 (IFRS 16, leases in TEV) | 2000-2026 (all) |
|---|---|---|---|---|---|---|
| TEV / LTM EBITDA | 6.29x | 7.35x / 7.18x; 5.10x (Jun-01) to 10.29x (Sep-07) | 9.45x / 9.53x; 6.65x (Mar-09) to 11.10x (Dec-11) | 11.31x / 11.87x; 7.98x (Dec-18) to 14.22x (Sep-13) | 7.36x / 7.12x; 6.03x (Jun-21) to 8.99x (Sep-23) | 8.64x / 8.03x; 5.10x (Jun-01) to 14.22x (Sep-13) |
| TEV / NTM EBITDA | 6.40x | 6.27x / 6.03x; 3.79x (Mar-01) to 8.78x (Jun-07) | 7.76x / 7.98x; 5.26x (Mar-09) to 8.52x (Mar-10) | 10.73x / 11.09x; 8.64x (Jun-18) to 12.52x (Sep-13) | 7.61x / 7.54x; 6.76x (Mar-25) to 9.18x (Mar-23) | 8.05x / 7.76x; 3.79x (Mar-01) to 12.52x (Sep-13) |
| TEV / LTM revenue | 0.97x | 0.89x / 0.85x; 0.68x (Mar-01) to 1.21x (Jun-07) | 1.22x / 1.26x; 0.77x (Mar-09) to 1.31x (Dec-11) | 1.24x / 1.27x; 0.95x (Dec-18) to 1.46x (Mar-16) | 1.07x / 1.04x; 0.90x (Jun-21) to 1.30x (Mar-23) | 1.07x / 1.07x; 0.68x (Mar-01) to 1.46x (Mar-16) |
| Price / LTM EPS | 19.76x | 17.07x / 18.33x; 9.84x (Mar-01) to 24.45x (Jun-04) | 19.55x / 18.72x; 15.06x (Mar-09) to 23.42x (Sep-11) | 46.61x / 45.45x; 24.19x (Mar-12) to 98.09x (Sep-13) | 21.88x / 20.64x; 13.24x (Dec-23) to 48.34x (Mar-19) | 27.50x / 20.94x; 9.84x (Mar-01) to 98.09x (Sep-13) |
| Price / NTM EPS | 17.02x | 13.35x / 12.57x; 9.91x (Mar-01) to 18.44x (Jun-07) | 14.97x / 15.07x; 12.05x (Mar-09) to 16.49x (Mar-11) | 26.54x / 25.90x; 19.15x (Mar-12) to 36.60x (Sep-13) | 19.85x / 19.02x; 15.69x (Mar-25) to 25.05x (Mar-19) | 18.97x / 18.26x; 9.91x (Mar-01) to 36.60x (Sep-13) |
| Price / book | 2.02x | 2.08x / 2.08x; 1.16x (Mar-01) to 3.01x (Sep-07) | 2.62x / 2.72x; 1.96x (Mar-09) to 2.91x (Jun-10) | 3.51x / 3.57x; 2.36x (Dec-18) to 4.47x (Sep-13) | 2.56x / 2.32x; 1.88x (Jun-20) to 3.66x (Sep-23) | 2.71x / 2.72x; 1.16x (Mar-01) to 4.47x (Sep-13) |

Position of today's close in each distribution `[calc]` (share of quarterly averages below it):

| Multiple (now) | vs 2000-2026 | vs 2012-2026 | vs 2019-2026 |
|---|---|---|---|
| TEV/LTM EBITDA 6.29x | 8th percentile | 5th | 10th |
| TEV/NTM EBITDA 6.40x | 24th | 0th (below every quarter) | 0th |
| Price/NTM EPS 17.02x | 45th | 3rd | 7th |
| Price/book 2.02x | 19th | 7th | 13th |
| TEV/LTM revenue 0.97x | 32nd | 10th | 17th |
| Price/LTM EPS 19.76x | 40th | 22nd | 43rd |

- ==Against the IFRS-era distribution the shares trade at the bottom on every enterprise-value measure; against the full 27-year history they are in the lower quartile on EBITDA but at the median on forward P/E==: TEV/NTM EBITDA 6.40x vs 8.05x mean since 2000 and 6.27x in 2000-2008; P/E NTM 17.0x vs 18.97x mean since 2000, but 13.35x in 2000-2008.
- The 2012-2018 regime (EV/EBITDA 11.3x, P/E NTM 26.5x) is the outlier: it coincided with the acquisition build-out, a net-debt/EBITDA of 2.1x-2.8x and ROE of 4%-10% (table 5). Using 2012-2018 as "normal" biases any mean-reversion argument upward; using 2000-2008 biases it downward because the group was then Mexico-centred with net cash ([[ciq-segment-and-geography-long-history]]).
- Lease treatment: today's TEV includes lease liabilities (34,790 at FY2025 `[sourced]` [[ciq-balance-sheet-history]]; 33,361 at Jun-26), roughly 0.6x EBITDA `[calc]`. A rough pre-IFRS 16 equivalent removes the Jun-26 lease liability from TEV and FY2025 lease principal payments (8,060 `[sourced]` AR-CF) from EBITDA: (406,697 - 33,361) / (64,709 - 8,060) = 6.6x against 6.29x reported `[calc]`, where 64,709 = TEV / 6.2853 (CIQ Key Stats LTM multiple) and lease interest is ignored `[unverified]`. The like-for-like discount to the 2012-2018 series is therefore slightly smaller than the headline, not larger.

## 4. Where the return came from: multiple versus earnings

Price proxy: CIQ prints P/B and the balance sheet gives book value per share, so price = P/B close × latest filed book value per share. Check: 2.02 × 26.83 (Jun-26 BVPS `[sourced]` CIQ-BS) = 54.2, equal to the 18-Sep-2026 close. For year-ends I use the Q3 book value (the latest filed at 31-Dec); using the Q4 book value instead gives results from 4% lower to 14% higher (21% higher in 2022, when Q4 equity included the one-off gain) `[calc]`. Treat the proxy as an approximation (about ±10%) `[unverified]` and do not quote it as an official price series.

| Year-end | Price proxy (MXN) | Price change | Dividend paid in year (CIQ, MXN) | Dividend ÷ prior year-end price | Approx. total return |
|---|---|---|---|---|---|
| 2012 | 33.5 | +17.5% | 0.15 | 0.5% | +18.0% |
| 2013 | 40.2 | +20.1% | 0.515 | 1.5% | +21.6% |
| 2014 | 40.7 | +1.4% | 0 | 0.0% | +1.4% |
| 2015 | 46.0 | +12.8% | 0 | 0.0% | +12.8% |
| 2016 | 47.0 | +2.3% | 0.24 | 0.5% | +2.8% |
| 2017 | 43.6 | -7.3% | 0.29 | 0.6% | -6.7% |
| 2018 | 39.2 | -10.1% | 0.35 | 0.8% | -9.2% |
| 2019 | 34.4 | -12.1% | 0.45 | 1.1% | -10.9% |
| 2020 | 43.2 | +25.4% | 0.50 | 1.5% | +26.8% |
| 2021 | 62.9 | +45.6% | 1.00 | 2.3% | +47.9% |
| 2022 | 82.4 | +31.0% | 1.30 (0.65 May + 0.65 Nov) | 2.1% | +33.1% |
| 2023 | 86.0 | +4.3% | 0.78 | 0.9% | +5.3% |
| 2024 | 55.1 | -35.9% | 0.94 | 1.1% | -34.8% |
| 2025 | 59.1 | +7.2% | 1.00 | 1.8% | +9.0% |
| 18-Sep-2026 | 54.2 `[sourced]` | -8.3% YTD | 1.075 (paid 13-May-2026) | 1.8% | – |

Dividends `[sourced]` CIQ Dividends & Splits (pay-year; 2013 = 0.165 in April + 0.35 in December; no dividend in 2014-2015, confirmed by [[bimbo-cash-flow-and-capex-fy14-fy20]]). Approximate total return = (price + dividends) ÷ prior price − 1, no reinvestment `[calc]`.

Cumulative `[calc]` (price proxy; total return in brackets): 2008-2025 +8.6% a year; 2012-2025 +4.5% (5.5%); 2015-2025 +2.6% (3.8%); 2019-2025 +9.4% (11.0%); 2021-2025 -1.5% (-0.1%); 2023-2025 -17.1% (-15.7%). From the 2023 year-end proxy (86.0) to 54.20 the shares are down 37% `[calc]`, with 52-week range 53.03-68.67 `[sourced]` [[ciq-ownership-and-holdings-history]].

- ==Multiple compression absorbed the EBITDA growth of the last decade==: from 2015 to 2025 the mean TEV/LTM EBITDA fell 43% (12.00x to 6.84x) while CIQ income-statement EBITDA grew 2.16x (25,386 to 54,815), so implied TEV rose only 1.23x `[calc]` (approximate: it multiplies CIQ's ratio multiple by the income-statement EBITDA line); the price proxy rose 28% (46.0 to 59.1) and the net debt that sits between TEV and equity rose from 66,838 to 182,232 `[sourced]` CIQ-BS (2.7x).
- The 2019-2023 rally (+150% in the price proxy from 34.4 to 86.0, +26% a year) was a multiple and earnings recovery at the same time (mean EV/EBITDA 7.38x to 8.70x; CIQ EBITDA 36,368 to 51,988, +43% `[calc]`); the 2024 fall (-36%) came with a 7.83x average multiple and company Adjusted EBITDA up 1.0% (55,474 vs 54,942 `[sourced]` CIQ-CONS), i.e. a de-rating while earnings were flat rather than an earnings collapse `[calc]`.

## 5. Multiples and returns on equity

`[calc]` ROE = net income ÷ average common equity ([[ciq-long-history-income-balance-cashflow]] section 6); P/B and P/E = mean of quarterly averages.

| Regime | Mean ROE | Mean P/B | Mean P/E NTM | Mean EV/EBITDA LTM |
|---|---|---|---|---|
| FY2000-FY2008 | 12.7% | 2.08x | 13.35x | 7.35x |
| FY2009-FY2011 | 13.2% | 2.62x | 14.97x | 9.45x |
| FY2012-FY2018 | 7.7% | 3.51x | 26.54x | 11.31x |
| FY2019-FY2025 (ex-FY2022) | 11.8% | 2.56x (2019-2026) | 19.85x (2019-2026) | 7.36x (2019-2026) |

- ==The market paid its highest price-to-book (3.5x) for its lowest ROE (7.7%)== in 2012-2018, capitalising growth that did not reach the income statement (net margin 1.2%-2.8%). Since 2019 ROE is back near 12% and the multiple is about 0.95x lower on book, but ROE is flattered by FY2021-FY2022 one-offs and by leverage (debt/equity 160% in FY2025).
- On FY2025 earnings (EPS 2.58) the P/E at 54.20 is 21.0x `[sourced]` CIQ Key Stats, against 17.0x on NTM consensus: the forward multiple depends on the +19% EPS rebound in FY2026E ([[ciq-consensus-estimates]]).

## 6. Dividend payout and yield

`[calc]` CIQ-IS "Dividends per Share" in the FQ4 column is the dividend declared for the fiscal year and paid the next May; payout = that DPS ÷ CIQ normalized EPS for the same year `[sourced]` CIQ-CONS (FY2022 EPS 6.81 includes the Ricolino gain).

| Fiscal year | DPS declared for the year (MXN) | EPS normalized (MXN) | Payout |
|---|---|---|---|
| FY2019 | 0.50 | 1.36 | 36.8% |
| FY2020 | 1.00 | 2.00 | 50.0% |
| FY2021 | 0.65 | 3.55 | 18.3% |
| FY2022 | 0.78 | 6.81 | 11.5% |
| FY2023 | 0.94 | 3.50 | 26.9% |
| FY2024 | 1.00 | 2.88 | 34.7% |
| FY2025 | 1.075 | 2.58 | 41.7% |

- Payout has risen from 11.5%-18.3% in FY2021-FY2022 to 41.7% in FY2025 `[calc]`; the dividend grew 16% a year from MXN 0.24 (paid 2016) to 1.075 (paid 2026) `[calc]` even though EPS normalized fell from 3.55 (FY2021) to 2.58 (FY2025).
- ==CIQ's consensus-sheet "actual" DPS series is not on one basis==: it shows 0.00 for FY2014, FY2015, FY2019 and FY2021, 1.00 for FY2020, 1.30 for FY2022 and 0.94 twice (FY2023, FY2024) `[sourced]` CIQ-CONS, because it records cash paid by pay year while the income-statement series is by fiscal year. The consensus estimate for FY2026 DPS (1.01 mean, 1.07 median `[sourced]` [[ciq-consensus-estimates]]) is below the 1.075 already paid in May-2026, which supports reading the estimate as a payment-year series and not a decree-year series `[unverified]`; it also bears on the "1.75 per share" item in [[bimbo-valuation-data-gaps]].

## 7. Gaps and flags

| Item | Detail |
|---|---|
| Pre-1999 multiples | extreme TEV values; excluded |
| No price series | CIQ Multiples gives ratios only; price levels above are proxies `[calc]` |
| P/E LTM 2012-2019 | distorted by IFRS-era EPS and CIQ treatment; do not average |
| Total return | no reinvestment, no taxes, no ADR/USD view; ADR (BMBOY) dividends 4.3359 in 2026 `[sourced]` are about four shares' worth |
| Tangible book | P/TBV is NM since 2016 (goodwill and intangibles exceed equity) `[sourced]` [[ciq-historical-multiples]] |

## Connections
- Own-history table for the last 10 years and the 2026 capitalization: [[ciq-historical-multiples]]; consensus and sentiment: [[ciq-consensus-estimates]], [[ciq-sell-side-sentiment-facts]]; estimate record: [[ciq-guidance-and-estimate-history]].
- Earnings, leverage and ROE inputs: [[ciq-long-history-income-balance-cashflow]]; regional mix behind the re-rating: [[ciq-segment-and-geography-long-history]]; shareholder structure: [[ciq-ownership-and-holdings-history]].
- Company-filing views: [[bimbo-shareholder-returns]], [[bimbo-capital-allocation]], [[bimbo-capital-structure-and-debt]], [[bimbo-valuation-data-gaps]]. Update list: [[ciq-delta-vs-previous-export]].

## Key Takeaways

- ==TEV/LTM EBITDA closed at 6.29x on 18-Sep-2026: 8th percentile of all quarterly averages since 2000, but only 0.9x below the 2000-2008 mean (7.35x)==; against the IFRS 16 era (7.36x) it is at the 10th percentile, and TEV/NTM EBITDA (6.40x) is below every quarter since 2012.
- The 2012-2018 regime (EV/EBITDA 11.3x, P/E NTM 26.5x, P/B 3.5x) was paid on ROE of 7.7%; it is not a reasonable "normal" for mean reversion.
- A price proxy (P/B × book value per share) shows +2.6% a year (3.8% with dividends) over 2015-2025 and -37% since the end of 2023: multiple compression (-43% in mean EV/EBITDA) absorbed a 2.16x rise in EBITDA.
- Dividends are small (1.8% yield at 54.20) but payout rose from 11.5% (FY2022) to 41.7% (FY2025); CIQ's consensus DPS series mixes pay-year and decree-year and shows 0.00 for four years.
- Lease liabilities add about 34.8 bn to current TEV; align the lease treatment with the EBITDA definition before quoting any peer or historical comparison.
- CIQ's split table misses the 4-for-1 split of 29-Apr-2011; pre-2011 per-share dividends need the 0.275 factor.
