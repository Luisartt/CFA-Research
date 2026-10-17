# Grupo Bimbo (BMV: BIMBO A) — valuation (assistant draft v3, 2026-10-17)

**Status: v3 integrates the Capital IQ pulls of 16/17-Oct-2026, a country-risk weighting and the peer workbook v3. Every WACC, terminal, forecast and bridge choice below is an assistant PROPOSAL until the team confirms it. `target_price` and `rating` are `null` (team decisions, AGENTS.md).** Valuation date 2026-10-16; MXN millions; IFRS. Tags: `[sourced]` `[guidance]` `[assumption]` `[calc]` `[unverified]`. Block rule: inputs are tagged in §2 and in their tables; every other untagged figure in this file is `[calc]` from `valuation/BIMBOA_DCF_v3.xlsx`, `valuation/BIMBOA_WACC_v3.xlsx`, `valuation/BIMBOA_PeerAnalysis_v3.xlsx` or the replica `valuation/build/dcf_core.py`.

## 0. Publication gate (read this before quoting any number)

Report, deck and pitch read **`valuation/valuation-outputs.yaml`** (v3), not `model/model-summary.json` directly. The verification record (file hashes, formula counts, every check) is `valuation/verification-v3.json`.

- **Published basis** (`valuation/BIMBOA_DCF_v3.xlsx`, DCF sheet) = the engine mechanics plus two technical corrections, unchanged since v2:
  1. FCFF also deducts the growth in the lease liability, held at its FY2025 share of revenue (8.15%).
  2. The exit method subtracts only the claims inside the peer-EV definition: net debt incl. leases, and NCI at market.
- **What changed in v3: the cost-of-capital route.** The base proposal moves from route A (M-Bono 9.26% as the risk-free rate, no country premium) to **route B**: a default-free peso rate (M-Bono 9.26% minus Mexico's default spread of 1.75%, Damodaran July 2026) plus a country risk premium weighted by where Bimbo earns its EBITDA (2.05%). Route A stays as the alternative (§7). Nothing else in the published mechanics changed: route A reproduces the v2 values exactly (35.717554 / 46.604264).
- **Engine basis** (`model/BIMBOA_model_v6.xlsx`, 123 checks OK, 0 warnings) is the untouched reconciliation anchor. The DCF workbook agrees with it on 30 of 30 fields and with the Python replica on 61 of 61 rows.

| Engine field (v6) | Status | Use instead |
|---|---|---|
| `wacc` (10.32%), `terminal_growth`, `exit_multiple`, `de_market` | usable (proposals) | — |
| `price_gordon` (39.48), `ev_gordon`, `tv_ronic` (17.9%), `implied_g`, `implied_exit_multiple`, `tv_share_gordon` | superseded | published Gordon **33.55**; RONIC 14.6%; market-implied g 6.41% (§4) |
| `price_exit` (43.08), `upside_exit` | superseded | published exit **45.72** (§4-5) |
| `dps_next` (1.18), `target_12m_gordon`, `upside_gordon` | superseded | next unpaid dividend Ps 1.05 (consensus DPS FY2027E; the FY2026 dividend of Ps 1.075 was paid on 13-May-2026) `[sourced]` CIQ 2026-09-20. 12-month Gordon value **36.84** `[calc]` |
| `price_comps_ev_ebitda` (71.82), `price_comps_pe` (36.43), football-field comps rows | superseded | peer workbook v3 on peer-EV claims (§6). The engine comps now include Gruma (it passed both eligibility tests in v3) |
| engine sensitivity grid | superseded | published-basis grids (§8) |

## 1. What was built

| File | What it is |
|---|---|
| `data/financials.csv`, `data/adjustments.md` | FY2021-FY2025 history on the engine chart (financials agent) |
| `model/drivers.yaml` | 10-year forecast: FY2026-FY2030 explicit, FY2031-FY2035 fade. Story drivers are proposals |
| `valuation/valuation.yaml` | WACC, terminal, bridge, peers (engine input set) |
| `valuation/inputs/spg_inputs.yaml` | Bridge components, NCI claim, operating working capital, lease basis, Jun-26 bridge, WACC variants, country-risk build, rates and credit evidence, sources |
| `valuation/inputs/peer_extras_v3.yaml` | Peer inputs from Capital IQ prompts 4-7: pricing-date FX, 131 overrides, eligibility, template data, expected results of the independent calculation, judgment calls and open items |
| `valuation/inputs/peers.yaml`, `beta_regression.json` | Peer numbers exported from the recalculated peer workbook v3; Bimbo's own beta regression |
| `model/BIMBOA_model_v6.xlsx`, `model/model-summary.json` | Engine model v6: 123 checks OK, 0 errors, 0 warnings (v1-v5 kept) |
| `valuation/BIMBOA_DCF_v3.xlsx` | S&P "DCF Analysis" layout. DCF sheet: drivers, FCFF, working capital, discounting, TV, bridge, published basis, value walk, lower-return cases, five published grids. Other sheets: **Scenarios** (new: one change at a time against the base), Reverse_DCF, Levers, Dated_Check, Engine_Recon, Inputs_Sources, Checks |
| `valuation/BIMBOA_WACC_v3.xlsx` | S&P "WACC Analysis" layout: route, beta and CRP-basis selectors; **country-risk weighting** (39 country rows, 38 included; four regions, four weight bases, ex-Argentina); rates and credit evidence (M-Bono, CDS, UST, CPI); beta evidence (Damodaran, peers, Bimbo regression); debt securities; grids |
| `valuation/BIMBOA_PeerAnalysis_v3.xlsx` | S&P "Financials & Peer Analysis" layout on v1's reviewed claim-basis logic. v3: Capital IQ prompts 4-7 (gross profit, dividends, price performance, consensus gross margin, FCF, DPS, capex and revenue), pricing-date FX 18.479, Gruma consensus and P/E, a capital-intensity block, and a Checks section that compares 102 results with the independent calculation |
| `*_v3_ES.xlsx` (DCF, WACC, PeerAnalysis) | Spanish copies for the team. Labels and notes translated; formulas, numbers and sheet names unchanged (the numbers are checked equal). The English files stay canonical for the report |
| `valuation/build/*.py`, `recalc_excel.ps1` | Generators, Python replica, Excel recalculation with macros off, error scan, gate writer (`write_outputs.py`) |

**Verification of v3** (detail and SHA-256 hashes in `valuation/verification-v3.json`).
- All six workbooks were recalculated in Excel: 0 formula errors and 0 missing cached results (DCF 1,168 and WACC 182 formula cells; peer workbook 1,751).
- DCF integrity checks 24 of 24 OK (v2 had 23; the new one ties the Scenarios base row to the published outputs). Engine reconciliation 30 of 30; Python replica 61 of 61, at better than 1e-6 relative.
- Peer workbook: 102 of 102 results equal the independent calculation (medians, per-company multiples, price performance) at 1e-6.
- Process: an Opus agent computed every value, a Haiku agent transcribed them into the input files, and scripts checked each transcription. Codex reviewed the integration plan in three rounds and approved it (§10).

## 2. Inputs and sources

| Input | Value | Tag and source |
|---|---|---|
| Share price | MXN 58.60 (16-Oct-2026) | `[sourced]` BMV official close = PPP 58.60 (last trade 58.62; prior close 57.97), BMV "Estadísticas de operación", BIMBO serie A (bmv.com.mx/es/emisoras/estadisticas/BIMBO-5163, retrieved 2026-10-17) |
| 52-week range | 53.03 - 68.67 | `[sourced]` CIQ as of 06-Oct-2026 |
| Shares | 4,294.9m outstanding (29-Jul-2026) | `[sourced]` BMV notice. The engine uses the FY2025 weighted 4,310.5m `[sourced]` EEFF25 p.13 |
| M-Bono 10y | 9.26% | `[sourced]` S&P Capital IQ rates, 16-Oct-2026 (`data/capitaliq/capiq-ai-model-gaps-2_2026-10-17.md`; the extract is now retained) |
| Mexico default spread | 1.75% | `[sourced]` Damodaran July 2026 update (ctrypremJuly26.xlsx, default spreads corrected 9-Jul-2026): Moody's Baa3 (S&P BBB, Fitch BBB-). Cross-check: Mexico 10y CDS 1.64% and 5y CDS 0.95% (Capital IQ, 16-Oct-2026) |
| **Risk-free (route B)** | **7.51%** | `[calc]` 9.26% - 1.75% = the peso rate without Mexico's default risk |
| ERP | 4.20% | `[sourced]` Damodaran implied ERP, 1-Oct-2026. It is the mature-market premium: the US country premium (0.22% in July 2026) is not inside it and enters through the CRP |
| **Country risk premium (route B)** | **2.05%** | `[calc]` weighted by FY2025 Adj. EBITDA over the countries where Bimbo operates (§7) |
| Unlevered beta | 0.53 | `[sourced]` Damodaran Food Processing, Global, January 2026 dataset (betaGlobal.xls dated 5-Jan-2026). Bimbo's own 5-year regression on the IPC corroborates it: 0.54 unlevered (levered 0.82, R-squared 0.30, standard error 0.17; Blume-adjusted 0.58) `[calc]` `valuation/inputs/beta_regression.json`. The 3-year window gives 0.85 (the 2023-24 de-rating). The bottom-up peer median is 0.21, too low to use alone |
| Target D/E | 0.743 | `[calc]` (153,660 + 33,361) / 251,684: current market D/E, debt incl. leases |
| Pre-tax Kd | 9.71% | `[calc]` M-Bono 10y + 0.45pp BIMBO 26 issue spread (matched maturity). Capital IQ bond yields are in the WACC workbook as evidence |
| Marginal tax | 30% | `[sourced]` Mexico statutory |
| Relevered beta / ke / WACC | 0.806 / 12.94% / 10.32% | `[calc]` ke = 7.51% + 0.806 x 4.20% + 2.05% |
| Terminal growth | 4.25% | `[assumption]` Long-run MXN growth of the regional mix (NA ~36% at ~3%, rest ~5%) |
| LT nominal GDP (cap) | 5.0% | `[assumption]` ~2% real + 3% Banxico target. Real growth `[sourced]`: IMF WEO Oct-2026, 2.1% a year for 2029-31; Banxico survey Sep-2026, 10-year average 1.88% mean / 1.80% median. The survey expects 3.7-3.8% long-run inflation, which would give about 5.6% nominal |
| Exit EV/EBITDA | 6.0x (trailing, FY2035) | `[assumption]` Judgment above the core bakery LTM median of **5.53x** (Flowers 5.61x, Gruma 5.44x), for the Mexico mix. All eligible peers: **8.27x**. Bimbo today: 6.94x with NCI at book, 7.12x with NCI at market |
| Mid-year, stub | yes, 0.7918 | `[calc]` 31-Dec-2025 to 16-Oct-2026 |
| USD/MXN | 18.479 | `[sourced]` close 16-Oct-2026 (Yahoo Finance MXN=X; `data/market/usdmxn_daily_2026-09-15_2026-10-16.csv`); the CIQ charts imply about 18.49. Used in the peer workbook only. The 17.46 of v1/v2 was the rate implied in the CIQ consensus dashboard, not a pricing-date rate, and is now used only to test that dashboard |

## 3. Forecast drivers (proposals; team to confirm the story drivers)

Unchanged from v2.

| Driver | FY2025A | FY2026E | FY2027E | FY2030E | FY2035E | Pillar |
|---|---|---|---|---|---|---|
| Revenue growth (sum of segments) | +4.6% | -0.8% | +4.5% | +4.4% | +4.2% | 2 (NA, Mexico) |
| Gross margin | 52.3% | 52.4% | 52.0% | 52.5% | 52.5% | 1 (wheat lag) |
| EBITDA margin (model basis) | 13.8% | 14.7% | 14.5% | 15.3% | 15.3% | 2 (productivity) |
| Capex / revenue | 5.3% | 4.6% | 5.0% | 5.5% | 6.0% | 3 (FCF) |
| New leases / revenue (published basis) | 1.39% principal | 1.33% | 1.75% | 1.76% | 1.73% | mechanical |
| Effective tax on EBIT | 35.7% | 34% | 34% | 34% | 34% | mechanical |

- **FY2026 anchor.** 1H26 actuals and the July 2026 guidance `[guidance]`: sales ex-FX up mid-single digit, flat in pesos; Adj. EBITDA margin +70-120 bp; capex US$1.0-1.2bn.
- **North America in pesos.** The FY2027+ 3.0% MXN growth for North America is about 1.5% USD growth plus about 1.5% a year of peso depreciation `[assumption]` drivers.yaml.
- **Model EBITDA vs consensus.** Within ±1.1% in FY2026-FY2028 (62.3 / 64.2 / 68.9 bn vs 62.1 / 64.9 / 69.0 bn), 3.1% above in FY2029. The gap to the price is not in near-term operations.

## 4. Results by method (assistant proposal set)

| Method | Value per share today (MXN) | vs MXN 58.60 |
|---|---|---|
| **DCF - Gordon, published (route B)** | **33.55** | -42.7% |
| DCF - Gordon, published, 12-month value (x (1 + ke) - next unpaid dividend 1.05) | 36.84 | -37.1% |
| **DCF - exit 6.0x, published (peer-EV claims)** | **45.72** | -22.0% |
| Dated cross-check (30-Jun-2026 anchor), Gordon / exit | 34.11 / 45.60 | +1.7% / -0.3% vs the FYE roll-forward. Open: `ebit_1h` basis (§10), ~+0.33 each |
| Engine basis v6 (reconciliation), Gordon / exit | 39.48 / 43.08 | |
| Lower-return cases (Gordon): RONIC = WACC / 12.5% / 15.0% | 25.45 / 30.25 / 34.05 | |

- EV Gordon, published 342,034 (TV share 54.3%); EV exit 370,094 (TV share 57.8%) `[calc]`.
- The published Gordon value implies a 5.21x exit multiple. The 6.0x exit implies g of 5.08%. WACC - g is 6.1 pp `[calc]`.
- **Terminal economics.** Terminal net reinvestment is 29.1% of NOPAT, so the return on new capital is 14.6% against a 10.32% WACC. If growth earned only the WACC, the Gordon value would be 25.45. The capex path sets this return (§8, §11).
- **Reverse DCF.** The price implies terminal growth of 6.41% (above the 5% cap), or revenue growth 3.42 pp a year higher in every forecast year (Gordon; 1.78 pp for exit).

**Walk from v2 to v3 (MXN per share today)** `[calc]` replica, sequential:

| Step | Gordon | Exit |
|---|---|---|
| v2 published (route A: rf 9.26%, CRP 0; ke 12.64%, WACC 10.15%) | 35.72 | 46.60 |
| Remove Mexico's default spread from the risk-free rate (rf 7.51%, no CRP; ke 10.89%) | +15.51 | +5.25 |
| Add the EBITDA-weighted country risk premium 2.05% (ke 12.94%, WACC 10.32%) | -17.68 | -6.14 |
| **v3 published (route B)** | **33.55** | **45.72** |

The two steps nearly cancel: route B costs Ps 2.17 (Gordon) and Ps 0.89 (exit), because Bimbo's weighted country risk (2.05%) is a little above the 1.75% Mexico spread that route A implicitly charges on the whole group. The v1 to v2 walk (audit corrections) is kept in `valuation-outputs.yaml`: v1 engine 46.14 / 47.42 → v2 published 35.72 / 46.60.

## 5. Equity bridge (31-Dec-2025) - each item once

| Item | MXN m | Per share | Treatment and source |
|---|---|---|---|
| Financial debt | 153,663 | | subtracted `[sourced]` EEFF25 p.12 |
| Lease liabilities (IFRS 16) | 34,790 | | subtracted. FCFF deducts new leases, including the growth in the liability |
| Cash | (8,535) | | added |
| NCI at book | 743 | | subtracted |
| Retirement and post-retirement, net, after tax | 1,515 | 0.39 | Mexico 1,131 x 0.70 + US 485 x 0.75 + EAA/LatAm 514 x 0.70 `[sourced]` EEFF25 p.75, note 18; tax rates `[assumption]` |
| US welfare obligations, long-term, after tax | 2,454 | 0.63 | 3,272 x 0.75 `[sourced]` p.75, p.79 |
| Long-term employee bonuses, after tax | 520 | 0.13 | 743 x 0.70 `[sourced]` p.75 |
| MEPP exit liabilities, after tax | 739 | 0.19 | 985 x 0.75 (US) `[sourced]` p.79 |
| Deferred compensation, after tax | 742 | 0.19 | 1,060 x 0.70 `[sourced]` p.79, note 19; tax `[assumption]` |
| Provisions: uncertain tax positions and litigation | 10,399 | 2.66 | UTP 8,537 + tax 1,196 (no shield) + labour 439 and civil 511 x 0.70 + other 1 `[sourced]` EEFF25 p.80, note 19 |
| Net derivative liabilities | 3,185 | 0.81 | 3,902 - 717 `[sourced]` p.12 |
| NCI market-value uplift | 17,500 | 4.47 | Live at ke: 1,814 / (12.94% - 3%) - 743 = 18,243 - 743. **Provisional** (v2 at route A: 18,067) |
| Investments in associates | (7,018) | | non-operating asset (results below EBIT) |

Per-share amounts are rolled forward to today (x 1.1012 at ke 12.94% / 4,310.5m shares).

- **NCI claim (largest bridge judgement, provisional).** The consolidated BBU independent operators are structured entities (EEFF25 p.35, p.37). Over FY2023-FY2025 their owners took out 7,211 plus dividends of 335 against NCI income of 4,757, and book NCI fell from 3,306 to 743 `[sourced]` EEFF25 p.13, p.15. The claim is valued as a cash claim: annualised 1H26 NCI income 1,814 capitalised at ke - 3%. At zero growth the uplift is 13,272 (Ps +1.08 per share). Without any uplift: Gordon 38.02, exit 50.19.
- **Claim consistency for the exit method.** Peer EVs leave out pensions and other employee claims, MEPP, provisions and derivatives, so the exit value subtracts only net debt and NCI at market. The other 19,554 is added back (Ps 5.00 per share).

## 6. Comparables (peer workbook v3)

**Eligible peers, LTM EV/EBITDA** on an IFRS 16-equivalent claim basis (US GAAP EBITDA + operating lease cost; EV incl. leases and book NCI incl. redeemable) `[calc]` `valuation/BIMBOA_PeerAnalysis_v3.xlsx`:

| Peer | Group | EV/EBITDA LTM | EV/EBITDA NTM | P/E LTM | P/E NTM | In medians |
|---|---|---|---|---|---|---|
| Flowers | core | 5.61x | 6.15x | 23.45x | 8.93x | valuation and P/E |
| Gruma | core | 5.44x | 5.64x | 9.36x | 9.74x | valuation and P/E (new in v3) |
| Smucker | secondary | 8.88x | 9.22x | 58.63x | 12.60x | valuation only (depressed earnings) |
| Campbell's | secondary | 7.66x | 8.36x | 15.11x | 11.72x | valuation and P/E |
| Mondelez | secondary | 16.14x | 13.80x | 23.10x | 19.83x | valuation and P/E |
| PepsiCo | secondary | 11.19x | 11.03x | 16.15x | 15.53x | valuation and P/E |
| Yamazaki | core | 6.06x | 5.84x | 17.74x | 16.84x | excluded: J-GAAP lease basis |
| Aryzta | core | 8.33x | 5.81x | 10.21x | 9.01x | excluded: NCI not verified |
| Arca | secondary | 7.85x | 7.11x | 18.71x | 16.50x | excluded: NCI not verified |

| Median (eligible) | v3 | v2 |
|---|---|---|
| Core bakery EV/EBITDA LTM (n=2) | **5.53x** | 5.64x |
| Core bakery EV/EBITDA NTM (n=2) | 5.89x | 6.15x (n=1) |
| All eligible EV/EBITDA LTM (n=6) | **8.27x** | 8.27x |
| All eligible EV/EBITDA NTM (n=6) | 8.79x | 9.22x (n=5) |
| All eligible P/E LTM (n=5) | 16.15x | 19.63x (n=4) |
| All eligible P/E NTM (n=5) | 11.72x | 13.63x (n=4) |

What moved and why:
- **FX.** The pricing-date rate (18.479) replaces 17.46. It lowers Gruma's USD market cap (4,660 → 4,403) and its LTM multiple (5.67x → 5.44x), so the core median falls to 5.53x. Bimbo's own multiples do not move: they are computed in pesos.
- **Gruma consensus.** Capital IQ returned FY2026E-FY2028E on the company EBITDA basis (FY26E 1,111.4 vs LTM 1,108.9), so Gruma now enters the NTM medians and, with EPS, the P/E medians.
- **Yamazaki, Aryzta and Arca** now have sourced shares and prices and a descriptive EV, but stay out: Yamazaki fails the lease test under J-GAAP; Aryzta and Arca fail on NCI (Capital IQ returns NCI as N/A for every company, so N/A is not zero). Their local-currency multiples are 6.23x (JPY), 8.59x (EUR) and 8.06x (MXN).
- **Template coverage.** Gross profit, dividends, price performance (QTD to 5Y) and consensus gross margin, FCF, DPS, capex and revenue are now filled for the peers. Still blank: peers' 52-week range and 1-day change (not returned).

**Indicative values** on Bimbo's LTM EBITDA of 60,919, the 30-Jun-2026 bridge and peer-EV claims (net debt incl. leases, NCI at market at ke 12.94%) `[calc]`:

| Multiple | Value per share (MXN) |
|---|---|
| 5.53x (core bakery) | 35.95 |
| 6.0x | 42.68 |
| 8.27x (all eligible) | 74.87 |

On the same basis Bimbo trades at 7.12x (6.94x with NCI at book).

**Capital intensity: the benchmark for terminal capex.** Consensus capex / consensus revenue `[calc]` peer workbook v3 (Capital IQ prompt 7):
- peer median 3.66% / 3.82% / 3.79% (FY1-FY3; core bakery 3.75% / 3.80% / 3.79%);
- Bimbo consensus 5.16% / 5.02% / 4.90% (FY2026E-FY2028E);
- the model: 4.6% in FY2026, rising to 6.0% by FY2035.

## 7. Cost of capital: routes, country risk and beta (team chooses)

**Country risk premium, route B** `[calc]` `valuation/BIMBOA_WACC_v3.xlsx`. Countries → regions → company:
1. Each country's equity CRP from Damodaran's July 2026 update `[sourced]`.
2. Each region's CRP is the plant-weighted average of its countries (FY2025 plants by country, RA25 p.114-116) `[sourced]`. Venezuela is excluded (deconsolidated); Argentina is included, with an ex-Argentina sensitivity.
3. The company CRP weights the regions by FY2025 segment Adj. EBITDA, with inter-segment eliminations attributed to Mexico `[sourced]` EEFF25 p.85-86.

| Region | Plants | Region CRP | Adj. EBITDA weight FY2025 | Sales weight FY2025 |
|---|---|---|---|---|
| North America (US 60, Canada 17) | 77 | 0.17% | 28.8% | 44.2% |
| Mexico | 38 | 2.72% | 55.4% | 32.9% |
| Europe, Asia & Africa (21 countries) | 92 | 2.63% | 9.8% | 12.7% |
| Latin America (14 countries; Venezuela excluded; 3.36% ex-Argentina) | 41 | 3.94% | 6.0% | 10.2% |
| **Company** | 248 | **2.05%** (EBITDA FY2025) | 2.02% ex-Argentina; 1.99% EBITDA FY2023-25 | 1.70% sales FY2025; 1.65% sales FY2023-25 |

The CRP is added to ke (ke = rf + beta x ERP + CRP), as in the project guide's formula. Scaling it by beta is a sensitivity (below). Historical note: v2's variant B used Damodaran's January 2026 table with one proxy country per region (NA 0.18%, Mexico 2.46%, EAA 1.55% Spain, LatAm 3.24% Brazil; Mexico spread 1.62%, rf 7.64%). Those figures are superseded by the country build above.

**Scenarios** (published basis; one change at a time; the NCI uplift is recomputed at each ke) `[calc]` DCF v3 'Scenarios' sheet:

| Scenario | WACC | Gordon | Exit (6.0x) |
|---|---|---|---|
| **Base: route B, CRP by FY2025 Adj. EBITDA** | **10.32%** | **33.55** | **45.72** |
| Route A: M-Bono 9.26%, no CRP (v2 base) | 10.15% | 35.72 | 46.60 |
| Route B, CRP by FY2025 sales (1.70%) | 10.13% | 36.05 | 46.74 |
| Route B, CRP by FY2023-25 average Adj. EBITDA (1.99%) | 10.29% | 33.97 | 45.89 |
| Route B, CRP by FY2023-25 average sales (1.65%) | 10.10% | 36.45 | 46.90 |
| Route B, EBITDA weights, Argentina excluded (2.02%) | 10.30% | 33.80 | 45.82 |
| Route B, CRP scaled by beta: ke = rf + beta x (ERP + CRP) | 10.09% | 36.46 | 46.90 |
| Beta: Bimbo 5-year regression, unlevered 0.54 | 10.37% | 33.03 | 45.50 |
| Beta: same, Blume-adjusted 0.58 | 10.51% | 31.37 | 44.77 |
| Beta: Bimbo 3-year regression, unlevered 0.85 | 11.49% | 21.46 | 39.85 |

**North America FX.** The PPP rows **replace** the ~1.5% a year of peso depreciation inside drivers.yaml with the inflation differential, and recompose g with the scenario's own North America share:

| Scenario | NA growth FY2027+ | g | Gordon | Exit |
|---|---|---|---|---|
| PPP at inflation targets (3% vs 2%): 0.98% a year | 2.47% | 4.06% | 31.37 | 44.80 |
| PPP at Banxico survey inflation (3.70% vs 2%): 1.67% a year | 3.17% | 4.31% | 34.30 | 46.01 |

An earlier draft read these rows as upside. That reading counted the 1.5% depreciation twice and is withdrawn: FX moves the value by -2.2 to +0.8 per share, so it is not what separates the DCF from the price.

**Discount rate by region: the company's own rates** `[sourced]` RA25 p.265 (impairment tests, post-tax, local currency): Mexico 10.00%, US 7.27%, Canada 6.50%, Spain 7.00%, Brazil 10.25% (2025). Weighted by FY2025 Adj. EBITDA they give 8.9% as reported, or 9.3% with the US rate converted to pesos through note 18 inflation `[calc]`. These are book rates in five currencies, set for impairment tests: a cross-check, not an input.

## 8. Sensitivity and levers (published basis)

Gordon value per share today, WACC (rows) x g (columns); the NCI claim and the roll factor are held at the base ke `[calc]` DCF v3:

| WACC \ g | 3.25% | 3.75% | 4.25% | 4.75% | 5.25% |
|---|---|---|---|---|---|
| 8.32% | 57.6 | 64.7 | 73.7 | 85.1 | 100.3 |
| 9.32% | 39.9 | 44.3 | 49.7 | 56.2 | 64.3 |
| 10.32% | 27.1 | 30.1 | **33.6** | 37.6 | 42.5 |
| 11.32% | 17.6 | 19.6 | 22.0 | 24.7 | 27.8 |
| 12.32% | 10.1 | 11.6 | 13.2 | 15.1 | 17.2 |

Exit value at 10.32% WACC, by multiple: 4x 27.5, 5x 36.6, **6x 45.7**, 7x 54.8, 8x 63.9.

**Levers (Gordon).**
- Capex: -50 bp of revenue every year = 42.99 (+9.44; terminal RONIC 20.2%); +50 bp = 24.11 (-9.44; RONIC 11.5%).
- Gross margin: +50 bp = 39.69 (+6.13); -50 bp = 27.42 (-6.13).
- Revenue growth: +50 bp a year = 36.79 (+3.24); -50 bp = 30.44 (-3.11).
- WACC: -1 pp = 49.68 (+16.13); +1 pp = 21.96 (-11.59).

**Capex tail (FY2031-35 capex / revenue, which also sets the terminal value):** held at 5.5% = 39.93 / 46.73 (RONIC 20.2%); 5.0% (Bimbo consensus FY2027-28) = 47.05 / 48.48 (RONIC 32.6%); 4.5% = 54.17 / 50.24 (RONIC 85%); the peer median 3.8% = 64.36 / 52.75 (RONIC not meaningful: growth with almost no net reinvestment). The lower the capex, the less credible the implied return on new capital.

**What the price requires (one lever at a time, published basis, Gordon unless noted)** `[calc]` replica:

| Lever | Proposal | Value that gives MXN 58.60 |
|---|---|---|
| Revenue growth, every forecast year | base paths | +3.42 pp (exit: +1.78 pp) |
| EBITDA margin (opex), every year | 15.3% by FY2030 | +201 bp |
| Capex / revenue, every year | 4.6% to 6.0% | -133 bp (FY2026 would be 3.3%, below guidance) |
| Terminal growth | 4.25% | 6.41% (cap 5.0%) |
| WACC (ke-linked items at base) | 10.32% | 8.90% (8.51% for the 6.0x exit) |
| Exit EV/EBITDA | 6.0x | 7.41x (Bimbo today 7.12x with NCI at market) |
| Unlevered beta | 0.53 | 0.11 alone; the peer median 0.21 gives WACC 9.15%, Gordon 51.2, exit 51.8 |

## 9. Model review flags (detail in model/review.md)

- **Leverage falls well below "hold".** Net debt / EBITDA falls from 3.05x (FY2025) to 0.76x by FY2035 because `net_new_debt` = 0 and a 38% payout leave cash piling up. This does not change the FCFF DCF, but it contradicts a "hold" at management's 2.0-2.5x: buybacks, M&A or a higher payout are a team choice (pillar 3).
- **Lease principal is derived (`[calc]`):** payments less interest accrued (`data/adjustments.md` adjustment 6).
- **1Q26 one-off gain** (Grupo La Moderna and Pasta4all stakes): carried at Ps 501.6m `[calc]` from "approximately 50 basis points"; Dated_Check removes it from both halves, so it does not move the value.

## 10. Independent review (Codex) and verification

**v1 audit (rounds 1-3), kept for the record.** Round 1 (cold recomputation of v1) found 14 issues: 3 high, 9 medium and 2 low. All were fixed or documented in v2: working capital without financial balances; exit on peer-EV claims; NCI uplift live at ke (provisional); employee benefits and provisions (UTP 8,537 added); lease growth; Dated_Check bases; peer inputs; tags. Round 2 confirmed the fixes and found the seasonal tax in the 1H26 working capital (fixed). Round 3: AUDIT RESULT: PASS. Detail: git history of this file (v2, 2026-10-17).

**v3 integration plan (rounds 1-3): VERDICT APPROVED.**
- Round 1: the PPP rows counted the peso depreciation twice (fixed by replacement, §7); workbooks rebuilt after recalculation had no cached results (the gate now requires build → translate → recalculate → scan → checks, with hashes).
- Round 2: the CRP inputs needed validation (complete regions, known codes, no duplicates, finite non-negative values, weights adding to 1, stored region CRP equal to the country build); the peer export gate needed to refuse missing caches and incomplete comparisons. Both added, with negative tests.
- Round 3: approved. Clean-up applied in this file: January 2026 country figures and the PPP "upside" are labelled historical; the mature ERP is described as excluding the US premium.

**Still open.**
- `ebit_1h` in Dated_Check mixes bases (CIQ's 1H26 EBIT before restructuring, 18,858.3, vs the BMV's 16,738.3). On the model's basis both dated values would rise by about Ps 0.33. They stay within the 5% check.
- Shares: the BMV shows 4,284.6m against 4,294.9m at 29-Jul (buybacks after July).
- Peers: BMV official close for Gruma; book NCI for Aryzta and Arca; Yamazaki's operating leases; Gruma consensus in its native currency.

## 11. Team decisions open (coach moments)

1. **Cost-of-capital route.**
   - *Recommendation:* route B as the base. It prices the risk of the countries where Bimbo earns its EBITDA, and the default-free rate removes the double count of Mexico's spread in a CRP framework.
   - *Strongest case against:* route A is simpler and is the project guide's local route; the M-Bono already prices Mexico's risk, and 29% of EBITDA comes from North America, where that risk does not apply.
   - *Question:* which framework will you defend when a judge asks why the M-Bono's 9.26% is not your risk-free rate?
2. **Terminal capex (now the decisive story assumption).** 50 bp of capex in every forecast year is worth Ps 9.4; moving only FY2031-35 from 6.0% to 5.5% adds 6.38 and from 5.5% to 5.0% another 7.12 `[calc]`. The model ends at 6.0%; Bimbo's own consensus is about 5.0%; peers run at 3.7-3.8%.
   - *Recommendation:* tie FY2031-35 capex to the D&A run-rate plus the growth you believe; 5.0-5.5% is defensible with a 20-33% return on new capital.
   - *Strongest case against:* FY2021-25 capex averaged 7.0% of revenue, and the new CEO's plan may need more.
   - *Question:* what return on new capital do you defend for the long run?
3. **Exit multiple.** 6.0x sits between the core bakery median (5.53x) and Bimbo today (7.12x); all eligible peers are 8.27x.
   - *Recommendation:* keep 6.0x and show 5.53x and 7.12x as the range.
   - *Strongest case against:* Bimbo has traded above 7x for years; the market may never rate it as a pure bakery.
   - *Question:* why should Bimbo exit at a discount to its own multiple today?
4. **Bridge: NCI uplift (Ps 4.47) and uncertain tax positions at face value (Ps 2.66 in provisions).** Keep both (cash extraction exceeds NCI income every year; IFRIC 23 already measures UTP at the expected amount). Against: provision payments are only 120-233 a year against an 8,537 stock.
5. **Target price, method weights and rating.** These stay null until the team decides. Convention (`references/recommendation-guide.md`): expected return = target / price - 1 + dividend yield; BUY at 15% or more, SELL at -10% or less. On the current proposals both DCF methods sit below the price: Gordon -43%, exit -22%.

**What would change the value most:** capex (±50 bp = ∓Ps 9.4); WACC (±1 pp = -Ps 11.6 / +Ps 16.1); the exit multiple (±1x = ±Ps 9.1); the NCI judgement (Ps 4.5).
