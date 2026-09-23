# Target price and recommendation

The target price and the recommendation are the team's decision. The model
gives the evidence; the team chooses and defends.

## Evidence the model gives

- DCF value per share today (Gordon and exit multiple) and the 12-month target
  (Gordon value x (1 + cost of equity) - next dividend).
- Comps: value per share at the median peer EV / EBITDA and P / E.
- Sensitivity grid (WACC x g) and the football field (all methods, 52-week range,
  current price, the team's target once set).
- Reverse DCF: the terminal growth the market price implies.

## Choosing the target

- Pick a primary method and say why (usually the DCF for a company with visible
  cash flows; comps as the cross-check). Or weight methods and state the weights.
- If methods disagree by more than about 20%, explain why before choosing —
  judges ask.
- The target must sit inside the football-field ranges; if not, say why.

## Recommendation convention (state yours in the report)

The Challenge does not prescribe one. A common convention, measured as expected
12-month total return (price change + dividend yield), computed with the keys in
the `valuation` section of `model/model-summary.json`:
expected return = team target / `share_price` - 1 + `dps_next` / `share_price`.

| Expected return | Recommendation |
|---|---|
| 15% or more | BUY |
| between -10% and 15% | HOLD |
| -10% or less | SELL |

Whatever convention the team uses, the recommendation must follow the thesis
direction and the kill criteria in `research/thesis.md`, and name the catalyst
that closes the gap within 12 months.
