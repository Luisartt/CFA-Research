# model/model-summary.json (read by valuation, report and pitch)

Written by every build. Numbers are in the profile's units; `null` means the
cell is blank (e.g. history of forecast-only lines) or not computable.

| Key | Content |
|---|---|
| `company`, `ticker`, `framework`, `currency`, `units` | From company-profile.yaml |
| `model_file`, `version`, `built_on` | The workbook this summary describes |
| `historical_years`, `forecast_years` | Lists of years |
| `status` | `ALL CHECKS OK`, `OK WITH WARNINGS` or `CHECKS FAILING` — the only failure signal (the engine exits 0 even when checks fail) |
| `lines` | Per year: revenue, gross_profit, ebitda, ebit, net_income_parent, eps, fcf, cash, revolver, net_debt, fcff (fcff only with valuation) |
| `ratios` | Per year: r_revenue_growth, r_gross_margin, r_ebitda_margin, r_ebit_margin, r_net_margin, r_fcf_margin, r_roe, r_roic, r_net_debt_ebitda, r_interest_cover, r_ccc |
| `drivers` | Per driver: `label`, `source` (`team` or `engine default`), `values` per year (history implied, forecast input) |
| `valuation` | Single values (only with valuation): wacc, terminal_growth, exit_multiple, ev_gordon, ev_exit, price_gordon, price_exit, share_price, upside_gordon, upside_exit, target_12m_gordon, dps_next, tv_ronic, de_market, tv_share_gordon, implied_exit_multiple, implied_g_exit, implied_g, price_comps_ev_ebitda, price_comps_pe (comps only with peers) |
| `checks` | List of `{check, year, status}`; `year` is null for single-value checks |
| `warnings` | Engine warnings (defaults used, unverified figures, missing files) |

Engine exit codes: 0 built (read `status`), 2 input error, 3 model definition
error, 4 file could not be written (close it in Excel / pause sync).
