# WACC and terminal value for LatAm companies

Values below are anchors to check, not data: always look up current figures and
cite the source and date in `rationale` / `valuation.md`.

## 1. Pick one currency and stay in it

The model is in the reporting currency (e.g. MXN nominal). The discount rate
must be in the same currency and in nominal terms.

- **Local route (preferred):** local 10-year government bond yield as risk-free
  (it already contains sovereign risk and local inflation) + beta x mature-market
  ERP. No separate country risk premium (set it to 0).
  The local yield embeds the sovereign default spread, not an equity country risk
  premium — be ready to defend that in Q&A.
- **USD route:** compute `k_e(USD) = rf_US + beta_L x ERP + CRP` (beta_L = the
  beta relevered at the target D/E), then convert it with
  `(1 + k_local) = (1 + k_usd) x (1 + inflation_local) / (1 + inflation_us)` to
  get `k_e(local)`. In `valuation.yaml` enter `risk_free` = k_e(local) - beta_L x ERP
  and `country_risk_premium` = 0, so the WACC tab reproduces k_e(local). Convert
  `pre_tax_cost_of_debt` from USD to local the same way. Keep the USD inputs
  (US Treasury, CRP) only if the reporting currency is USD.

| Country | Local 10-year risk-free | Central-bank inflation target |
|---|---|---|
| Mexico | M Bono 10y (Banxico) | 3% |
| Brazil | NTN-F / DI curve 10y (BCB, Tesouro) | 3% |
| Chile | BCP / BTP 10y (Banco Central) | 3% |
| Colombia | TES 10y (Banco de la Republica) | 3% |
| Peru | Sovereign 10y in soles (BCRP) | 2% |

## 2. Equity risk premium and country risk

- ERP: a mature-market ERP (e.g. Damodaran's implied US ERP, updated monthly).
- Country risk premium: only on the USD route (e.g. Damodaran's country table),
  inside k_e(USD); `valuation.yaml` gets 0 unless the reporting currency is USD.

## 3. Beta

Bottom-up: take peers' levered betas, unlever each
`beta_u = beta_l / (1 + (1 - tax) x D/E)` with D including leases, take the
median, and enter it as `beta_unlevered`; the model relevers it at the target D/E.

## 4. Capital structure and cost of debt

- `target_debt_to_equity`: market values, **debt including leases** (the model
  subtracts lease liabilities in net debt). Peer median or the company's own
  long-run target. The WACC tab shows the current market D/E next to it.
- Include only the leases the model counts as debt (`lease_liabilities`). For a
  US GAAP company with operating leases in other liabilities, exclude them from
  D/E, from beta unlevering and from peers' net debt, and use EBITDA after rent
  for peers.
- `pre_tax_cost_of_debt`: yield on the company's bonds, or risk-free + a spread
  for its rating.
- `tax_rate`: statutory marginal rate (Mexico 30%, Brazil 34%, Chile 27%,
  Colombia 35%, Peru 29.5%).

## 5. Terminal value

- `growth` (g): at or below long-term **nominal** GDP growth in the model's
  currency (real growth of roughly 2-2.5% plus the inflation target). The model
  warns if WACC - g is under 2 points and fails if g is above `lt_nominal_gdp_growth`.
- `exit_ev_ebitda`: applied to final-year EBITDA. Anchor on peers' current EV /
  EBITDA, adjusted for where growth will be in the final year. The model shows the
  multiple implied by the Gordon value and warns if the two disagree by more than 2x.
- Check `tv_ronic` on the DCF tab: the return on new capital the terminal value
  assumes. Far above WACC forever needs a moat argument.
