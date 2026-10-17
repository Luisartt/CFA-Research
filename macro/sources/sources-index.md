# Macro sources index (input of /update-macro)

The macro evidence the team already holds lives elsewhere in the project. This index points to it instead of copying it, so each number keeps one home. Files listed here are read-only inputs.

| Source | Path | What it gives | Date |
|---|---|---|---|
| S&P Capital IQ, model-gaps prompt 2 (raw output) | `data/capitaliq/capiq-ai-model-gaps-2_2026-10-17.md` | Mexico M-Bono curve (1Y-30Y), US Treasury 2Y-30Y, Canada/Spain/Brazil/Germany 10Y, Mexico 5Y and 10Y CDS, Mexico and US CPI YoY (Sep-2026 actual). Banxico rate, TIIE, UMS and USD/MXN returned N/A | 2026-10-16 |
| USD/MXN daily closes | `data/market/usdmxn_daily_2026-09-15_2026-10-16.csv` (checks in `data/market/README.md`) | USD/MXN 18.479 at 16-Oct-2026 (Yahoo Finance MXN=X) | 2026-10-16 |
| Grupo Bimbo annual report 2025 (RA25) | `filings/` (via `wiki/Macro/bimbo-macro-by-region.md`, `wiki/Macro/bimbo-fx-exposure.md`) | Mexico CPI 2023-2025, Banxico rate end-2025, closing and average USD/MXN, Brazil SELIC, Argentina inflation | FY2025 |
| Grupo Bimbo 2Q26 release | `filings/` (via `wiki/Macro/bimbo-fx-exposure.md`) | Closing USD/MXN 17.47 at 30-Jun-2026 | 2026-07-23 |
| IMF World Economic Outlook, October 2026 | DataMapper API, cited in `valuation/inputs/spg_inputs.yaml` (sources) | Mexico real GDP growth 2.1% and CPI 3.0% a year in 2029-31 | 2026-10-08 |
| Banxico private-sector expectations survey, Sep-2026 | cited in `valuation/valuation.yaml` and `valuation/inputs/spg_inputs.yaml` | GDP 2027-36 average 1.88% mean / 1.80% median (Cuadro 6 p.8); long-run inflation 3.7-3.8% (Cuadro 5 p.6) | 2026-10-01 |
| Damodaran, implied ERP and country risk (July 2026) | `valuation/inputs/wacc_inputs.yaml` G1; `valuation/inputs/spg_inputs.yaml` wacc_variants | Implied ERP 4.20% (1-Oct-2026); Mexico default spread 1.75% (Baa3); country CRPs | 2026-07 / 2026-10 |

Not available locally (so nothing was proposed): US growth and inflation forecasts (Fed SEP), commodity price decks (wheat, soybean oil, sugar, polyethylene, natural gas), the Banxico rate at the pricing date, USD/MXN forwards. Drop the documents in this folder and re-run `/research-analyst:update-macro`.
