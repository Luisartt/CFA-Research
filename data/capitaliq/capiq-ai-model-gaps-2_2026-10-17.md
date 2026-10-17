# Capital IQ AI output — model-gaps Prompt 2 (government yields, CDS, FX), pricing date 2026-10-16

_Raw source copy. Pasted by the team on 2026-10-17 from the Capital IQ AI assistant, response to Prompt 2 of `BIMBOA/research/capiq-prompts-model-gaps_2026-10-17.md`. Text and numbers are as received; tab-separated tables were converted to markdown. This file could not be written to `raw/` (write permission denied); move it there unchanged if you want it in the inbox. It is also the retained extract for the 9.26% M-Bono 10Y used as the risk-free rate._

_Two screenshots of the Capital IQ US Treasury bill curve came with the output (images are not stored). Most recent: 8W 4.02, 3M 4.08, 6M 4.20, 1Y 4.24 (4W not shown). One year ago: 4W 4.03, 8W 3.95, 3M 3.86, 6M 3.68, 1Y 3.42. The second image overlays the curves of 16 October for 1996, 2006, 2016, 2019, 2021, 2023, 2024, 2025 and 2026._

---

CFA Research Challenge – Grupo Bimbo | Discount-Rate Inputs | Pricing Date: 10/16/2026

## Task 2A – Government Yields

| Series | Value (%) | Unit | Date | Source |
|---|---|---|---|---|
| Mexico M-Bono 1Y (1y Mexican Benchmark Bill) | 6.679 | % | 10/16/2026 | S&P Capital IQ |
| Mexico M-Bono 2Y | N/A | % | — | S&P Capital IQ |
| Mexico M-Bono 3Y (3y Mexican Benchmark Bond) | 7.016 | % | 10/16/2026 | S&P Capital IQ |
| Mexico M-Bono 5Y (5y Mexican Benchmark Bond) | 8.298 | % | 10/16/2026 | S&P Capital IQ |
| Mexico M-Bono 7Y (7y Mexico Benchmark) | 8.923 | % | 10/16/2026 | S&P Capital IQ |
| Mexico M-Bono 10Y (10y Mexican Benchmark Bond) | 9.260 | % | 10/16/2026 | S&P Capital IQ |
| Mexico M-Bono 20Y (20y Mexican Benchmark Bond) | 9.720 | % | 10/16/2026 | S&P Capital IQ |
| Mexico M-Bono 30Y (30y Mexican Benchmark Bond) | 9.782 | % | 10/16/2026 | S&P Capital IQ |
| Mexico Udibono 10Y Real Yield | N/A | % | — | S&P Capital IQ |
| US Treasury 2Y (2y US T-Note) | 4.740 | % | 10/16/2026 | S&P Capital IQ |
| US Treasury 5Y (5y US T-Note) | 4.890 | % | 10/16/2026 | S&P Capital IQ |
| US Treasury 10Y (10y US T-Note) | 5.090 | % | 10/16/2026 | S&P Capital IQ |
| US Treasury 30Y (30y US T-Bond) | 5.430 | % | 10/16/2026 | S&P Capital IQ |
| Canada Government 10Y (10y Canadian Benchmark Note) | 3.8068 | % | 10/16/2026 | S&P Capital IQ |
| Spain Government 10Y (10y Spanish Benchmark Note) | 4.007 | % | 10/16/2026 | S&P Capital IQ |
| Brazil Local-Currency Government 10Y (10y Brazilian Benchmark Bond) | 13.044 | % | 10/16/2026 | S&P Capital IQ |
| Germany Bund 10Y (10y German Benchmark Note) | 3.407 | % | 10/16/2026 | S&P Capital IQ |

Note on Mexico M-Bono 2Y: The Capital IQ Mexico government curve returns tenors at S/N-O/N, 1W, 1M, 3M, 6M, 9M, 1Y, 3Y, 5Y, 7Y, 10Y, 20Y, and 30Y. A discrete 2Y M-Bono benchmark is not present in the retrieved series.

## Task 2B – Credit and Policy

| Series | Value | Unit | Date | Source |
|---|---|---|---|---|
| Mexico 5Y Sovereign CDS – Mid (Composite) | 95.2953 | bps (USD) | 10/16/2026 | S&P Capital IQ |
| Mexico 5Y Sovereign CDS – Bid (Composite) | 94.2120 | bps (USD) | 10/16/2026 | S&P Capital IQ |
| Mexico 5Y Sovereign CDS – Ask (Composite) | 96.3786 | bps (USD) | 10/16/2026 | S&P Capital IQ |
| Mexico 10Y Sovereign CDS – Mid (Composite) | 164.0839 | bps (USD) | 10/16/2026 | S&P Capital IQ |
| Mexico 10Y Sovereign CDS – Bid (Composite) | 160.5839 | bps (USD) | 10/16/2026 | S&P Capital IQ |
| Mexico 10Y Sovereign CDS – Ask (Composite) | 167.5839 | bps (USD) | 10/16/2026 | S&P Capital IQ |
| Mexico USD Sovereign Bond (UMS) 10Y Yield | N/A | % | — | S&P Capital IQ |
| Banxico Target Rate | N/A | % | — | S&P Capital IQ |
| TIIE 28-Day | N/A | % | — | S&P Capital IQ |
| Mexico CPI YoY – September 2026 (latest actual) | 3.45 | % YoY | 09/30/2026 | S&P Capital IQ |
| US CPI YoY – September 2026 (latest actual) | 3.74 | % YoY | 09/30/2026 | S&P Capital IQ |

CPI notes:

- Mexico: The most recent "As reported ACTUAL" month is September 2026 (3.45%). October 2026 (3.59%) is flagged as a Standardized FORECAST, not yet an actual release.
- US: The most recent "As reported ACTUAL" month is September 2026 (3.74%). October 2026 (3.49%) is flagged as a Standardized FORECAST.
- TIIE 28-Day: Capital IQ returns multiple TIIE-linked MXN swap rate series (various tenors of Act/360 Ann vs. 28D TIIE Float), but all are as of 05/31/2024 — not current. The dedicated "28 Day Mexico TIIE – MXN" interbank rate series returned a NO_DATA error. The value is therefore reported as N/A for the 10/16/2026 pricing date.
- Banxico Target Rate and Mexico UMS 10Y Yield were not resolved in the data feed.

## Task 2C – FX Rates

| Series | Value | Unit | Date | Source |
|---|---|---|---|---|
| USD/MXN Spot | N/A | MXN per USD | 10/16/2026 | S&P Capital IQ |
| USD/MXN 1-Year Forward Rate / Points | N/A | — | — | S&P Capital IQ |
| USD/MXN 5-Year Forward Rate / Points | N/A | — | — | S&P Capital IQ |
| USD/MXN 10-Year Forward Rate / Points | N/A | — | — | S&P Capital IQ |
| USD/MXN 12-Month Average | N/A | MXN per USD | — | S&P Capital IQ |

FX note: All USD/MXN queries (spot, forward rates/points, and historical average) returned an ALL_ENTITIES_UNRESOLVED error — no FX rate data was returned for any of these series in the available data feed.
