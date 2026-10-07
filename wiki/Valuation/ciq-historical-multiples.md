---
Writer: AI-compiled (Claude)
Source:
  - filings/capitaliq/Financials/Templated/Multiples/SPGlobal_GrupoBimbo,S.A.B.deC.V._Multiples_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Key Stats/SPGlobal_GrupoBimbo,S.A.B.deC.V._KeyStats_19-Sep-2026.xlsx
  - filings/capitaliq/Financials/Key Stats/SPGlobal_GrupoBimbo,S.A.B.deC.V._KeyStats_20-Sep-2026 (1).xlsx
  - filings/capitaliq/Estimates/Estimate Highlights/SPGlobal_GrupoBimbo,S.A.B.deC.V._EstimateHighlights(SentimentAnalysis)_20-Sep-2026.xlsx
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T25.pdf
  - filings/bmv/REPORTE ANUAL 2025 OFICIAL VF.pdf
tags: [Valuation, trading-multiples]
---

# S&P Capital IQ Historical Trading Multiples — BIMBO A (to 18-Sep-2026)

Own-history trading multiples for Grupo Bimbo from S&P Capital IQ, plus the current capitalization that drives them. ==Price basis: MXN 54.20 (last close in the 19/20-Sep-2026 downloads)==. Facts only: whether the stock is "cheap" or "expensive" is a team judgment. Tidy data: `data/capitaliq/multiples.csv` (datasets `multiples_quarterly`, `key_stats_valuation`, `key_stats_capitalization`, `estimate_highlights_multiples`). Related: [[ciq-consensus-estimates]], [[ciq-sell-side-sentiment-facts]], [[bimbo-capital-structure-and-debt]], [[bimbo-valuation-data-gaps]], [[bimbo-balance-sheet-and-leverage]].

How CIQ builds the series `[sourced]` CIQ Multiples, sheet 'Multiples', rows 5–9 and 70:
- Source "S&P Capital IQ – Standard"; TEV standard; diluted shares outstanding; quarterly periods, latest on the right.
- Each quarter has four rows: ==Average== (mean of positive daily closes in the quarter), High, Low, Close. Negative values are excluded; "NM" means not meaningful.
- The last column (dated 18-Sep-2026) is quarter-to-date for 3Q26, not a full quarter.
- LTM = last twelve reported months; NTM = next twelve months of consensus.

## 1. Current capitalization (CIQ Key Stats)

`[sourced]` CIQ Key Stats 19-Sep-2026, sheet 'Key Stats', rows 51–66 (the 20-Sep-2026 "(1)" file has identical values in these rows). MXN millions unless stated.

| Item | Value |
|---|---|
| Closing price | MXN 54.20 |
| Shares outstanding (actual) | 4,296,284,215 |
| Market capitalization | 232,859 |
| + Total debt | 189,679 |
| + Minority interest | 722 |
| − Cash and short-term investments | 16,563 |
| = Total enterprise value (TEV) | ==406,697== |
| Total common equity | 115,272 |

- TEV check: 232,859 + 189,679 + 722 − 16,563 = 406,697 `[calc]`.
- CIQ total debt (189,679) is larger than the company's reported debt of 153,660 at Jun-26 `[sourced]` [[bimbo-valuation-data-gaps]] (2Q26 release p.6). The gap is consistent with CIQ including IFRS 16 lease liabilities, but the export does not break it down `[unverified]`. This lease choice feeds every TEV multiple below.
- The CIQ consensus TEV for FY2026 (373,739, two analysts) is a broker estimate and is not comparable with this TEV `[sourced]` [[ciq-consensus-estimates]].

## 2. Current multiples on current capitalization

`[sourced]` CIQ Key Stats 19-Sep-2026, sheet 'Key Stats', rows 41–49 (price MXN 54.20; forward columns use consensus means).

| Multiple | FY2023 | FY2024 | FY2025 | LTM 2Q26 | FY2026E | FY2027E | FY2028E |
|---|---|---|---|---|---|---|---|
| TEV / Revenue | 0.92x | 1.01x | 0.97x | 0.97x | 0.95x | 0.91x | 0.87x |
| TEV / EBITDA | 6.32x | 6.66x | 6.56x | ==6.29x== | ==6.55x== | 6.27x | 5.89x |
| TEV / EBIT | 9.22x | 10.37x | 10.58x | 9.96x | 10.86x | 10.49x | 9.70x |
| Price / EPS | 15.45x | 18.54x | 20.98x | 19.76x | ==17.66x== | 16.19x | 14.28x |
| Price / Book | 2.20x | 1.86x | 1.95x | 2.02x | 1.85x | 1.68x | 1.56x |
| Price / Tangible book | NM | NM | NM | NM | NA | NA | NA |

Estimate Highlights view (20-Sep-2026) `[sourced]` CIQ Estimate Highlights, sheet 'Multiples', rows 5–13: NTM P/E 17.02x, P/BV n/a, P/CFPS 4.98x, PEG 1.25, TEV/EBIT 10.67x, ==TEV/EBITDA 6.40x==, TEV/Revenue 0.93x, Market cap/Revenue 0.53x; FY2026 / FY2027 / FY2028 P/E 17.66x / 16.19x / 14.28x and TEV/EBITDA 6.55x / 6.27x / 5.89x.

Note: these "historical" columns divide ==today's== TEV or price by past results; they are not the multiples at which the stock traded in those years. Section 3 gives the traded history.

> [!warning] Two different "current" EV/EBITDA figures
> Key Stats LTM 2Q26 = 6.29x; the Multiples sheet 3Q26-to-date average for TEV/LTM EBITDA = 6.58x and the 18-Sep-2026 close = 6.29x `[sourced]` CIQ Multiples rows 20–23. Quote the close (6.29x) with its date, or the quarter average with its window, never mixed.

## 3. Traded history (quarterly averages)

Statistics `[calc]` from the quarterly "Average" rows in `multiples.csv` (CIQ Multiples, sheet 'Multiples', rows 12–67). 10-year window = 39 full quarters, Dec-2016 to Jun-2026; 5-year = 19 quarters, Dec-2021 to Jun-2026. "Now" = 18-Sep-2026 close `[sourced]`.

| Multiple | Now (close) | 3Q26 QTD avg | 10y mean | 10y median | 10y min (quarter) | 10y max (quarter) | 5y mean | 5y min | 5y max |
|---|---|---|---|---|---|---|---|---|---|
| TEV / LTM EBITDA | ==6.29x== | 6.58x | ==7.78x== | 7.67x | 6.03x (2Q21) | 10.71x (4Q16) | 7.68x | 6.62x (2Q26) | 8.99x (3Q23) |
| TEV / NTM EBITDA | 6.40x | 6.71x | 7.98x | 7.66x | 6.76x (1Q25) | 10.59x (4Q16) | 7.69x | 6.76x (1Q25) | 9.18x (1Q23) |
| TEV / LTM revenue | 0.97x | 1.01x | 1.07x | 1.05x | 0.90x (1Q20) | 1.30x (1Q23) | 1.13x | 1.00x (2Q26) | 1.30x (1Q23) |
| TEV / NTM revenue | 0.93x | 0.98x | 1.02x | 1.01x | 0.88x (1Q19) | 1.23x (2Q23) | 1.07x | 0.95x (1Q25) | 1.23x (2Q23) |
| TEV / LTM EBIT | 9.96x | 10.49x | 11.50x | 11.57x | 8.83x (3Q21) | 14.66x (4Q16) | 11.63x | 10.22x (4Q21) | 13.45x (3Q23) |
| TEV / NTM EBIT | 10.67x | 11.21x | 12.35x | 12.02x | 10.76x (2Q21) | 14.92x (4Q16) | 11.91x | 10.87x (1Q25) | 13.33x (1Q23) |
| Price / NTM EPS | ==17.02x== | 18.37x | ==21.04x== | 19.91x | 15.69x (1Q25) | 26.48x (4Q16) | 18.84x | 15.69x (1Q25) | 21.82x (2Q23) |
| Price / LTM EPS | 19.76x | 21.32x | 26.72x | 22.29x | 13.24x (4Q23) | 49.24x (4Q18) | 18.67x | 13.24x (4Q23) | 23.82x (1Q26) |
| Price / LTM normalized EPS | 16.30x | 17.60x | 19.71x | 18.42x | 13.43x (4Q23) | 30.54x (2Q20) | 17.16x | 13.43x (4Q23) | 20.12x (2Q24) |
| Price / Book | 2.02x | 2.14x | 2.65x | 2.45x | 1.88x (2Q20) | 3.66x (3Q23) | 2.77x | 1.89x (1Q25) | 3.66x (3Q23) |
| Price / NTM cash flow | 4.98x | 5.42x | 8.27x | 8.46x | 5.62x (2Q26) | 11.69x (3Q20) | 7.90x | 5.62x (2Q26) | 10.74x (1Q23) |
| TEV / LTM unlevered FCF | 11.70x | 12.68x | 32.03x | 25.65x | 9.90x (2Q21) | 153.06x (1Q24) | 41.64x | 14.45x (2Q26) | 153.06x (1Q24) |
| Mkt cap / LTM levered FCF | 8.93x | 10.16x | 30.41x (36 q) | 25.38x | 7.63x (2Q21) | 80.26x (4Q23) | 33.76x (16 q) | 12.14x (2Q26) | 80.26x (4Q23) |

Year-end quarter (4Q) average, TEV / LTM EBITDA `[sourced]` CIQ Multiples row 20: 2016 10.71x; 2017 9.05x; 2018 7.98x; 2019 6.78x; 2020 6.70x; 2021 7.02x; 2022 8.66x; 2023 8.85x; 2024 7.46x; 2025 7.03x; then 1Q26 7.09x, 2Q26 6.62x.

Year-end quarter (4Q) average, P / NTM EPS `[sourced]` row 40: 2016 26.48x; 2017 25.92x; 2018 24.84x; 2019 22.50x; 2020 19.29x; 2021 19.83x; 2022 19.76x; 2023 19.23x; 2024 16.70x; 2025 18.06x; then 1Q26 18.26x, 2Q26 18.15x.

Position vs history `[calc]`: the 18-Sep-2026 TEV/LTM EBITDA close (6.29x) is ==1.49x below the 10-year mean== (7.78x), about 19% lower, and below every full-quarter average of the last five years (5-year low 6.62x in 2Q26). The NTM P/E close (17.02x) is 4.0x below the 10-year mean (21.04x) and above the 1Q25 low (15.69x).

Data caveats:
- Price / tangible book is NM in every quarter since 2016 (goodwill and intangibles exceed equity) `[sourced]` rows 52–55.
- FCF multiples are volatile: FY2023 levered FCF was negative (CIQ FCF actual −2,307 `[sourced]` CIQ Surprise, Free Cash Flow row), so some 4Q23 values are NM or extreme (TEV/unlevered FCF 124.8x average, 159.2x close). Medians are more representative than means for these two rows.
- Full history starts in 1994–2001 depending on the multiple; pre-2010 values include extreme outliers (e.g. TEV/LTM revenue 52.96x in 1Q98), so the "all-history" mean is not meaningful and is not shown.

## 4. Reconciliation of the inputs

The multiples are only as good as CIQ's EBITDA, earnings and debt. Key FY2021–FY2025 inputs were reconciled in [[ciq-consensus-estimates]] (section 5): CIQ net sales, Adj. EBITDA and net income match the filings exactly (FY2021 as first reported, not restated for Ricolino); CIQ net debt exceeds audited net debt by 1,200 (FY2024) and 3,903 (FY2025) `[calc]` vs RA25 p.299. For the TEV here, CIQ uses total debt of 189,679 vs company debt of 153,663 at Dec-25 `[sourced]` 4T25 release p.9; the difference is presumably leases (see section 1) `[unverified]`.

## Key Takeaways

- At MXN 54.20, CIQ shows TEV 406,697 (incl. total debt 189,679, apparently with leases) and market cap 232,859 (MXN millions).
- ==TEV/LTM EBITDA 6.29x (close, 18-Sep-2026) vs a 10-year quarterly-average mean of 7.78x and a 5-year range of 6.62x–8.99x.==
- NTM P/E 17.0x vs 10-year mean 21.0x; the 10-year low was 15.7x in 1Q25.
- Forward TEV/EBITDA on consensus: 6.55x FY2026E, 6.27x FY2027E, 5.89x FY2028E (current capitalization).
- Lease treatment drives the TEV: align it with the EBITDA definition before comparing with peers or with company leverage ratios.
