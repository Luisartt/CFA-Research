# Risk framework

Investment risks are worth 15 of 100 report points. Judges reward specific,
quantified risks tied to the thesis, and punish generic lists ("FX risk",
"competition").

## A good risk statement

cause -> effect on the business -> which model driver moves -> effect on value.
Example: "A 20% wheat price spike (cause) squeezes gross margin by ~150 bp
before prices adjust (effect; driver `gross_margin`), cutting our DCF value by
about 8% (value)."

## Scales (used in research/risks.yaml and the risk matrix)

| Score | Probability (next 12-24 months) | Impact on value per share |
|---|---|---|
| 1 | Rare, under 10% | Under 2% |
| 2 | Unlikely, 10-25% | 2-5% |
| 3 | Possible, 25-50% | 5-10% |
| 4 | Likely, 50-75% | 10-20% |
| 5 | Almost certain, over 75% | Over 20% |

## Categories

market (demand, prices, competition), operational (supply chain, execution,
capacity), financial (FX, rates, leverage, refinancing), regulatory (tax,
labeling, concessions, antitrust), ESG (environmental, social), governance
(controlling shareholder, related parties, succession).

## What to write

- 4-6 key risks in the body, each linked to a thesis pillar; the rest in a
  table in the appendix.
- For each: mitigation (what the company does) and whether it is priced in
  (already in the market price, in our forecast, or neither).
- One downside scenario: the risks that matter most, hitting together, with
  the value per share it implies. Run it on a copy, never on the team's base
  model:
  1. Copy the whole project folder to a sibling folder (for example
     `<team folder>-downside`).
  2. In the copy's `model/drivers.yaml`, change only the drivers the scenario
     moves (for example a lower `gross_margin` or `revenue_growth`).
  3. Rebuild the copy with the same engine call as the model skill:
     `<python> "${CLAUDE_PLUGIN_ROOT}/skills/model/engine/build_model.py" --project "<copy>"`.
  4. Record the value per share from the copy's `model/model-summary.json`
     (`valuation.price_gordon` and `valuation.price_exit`) in `research/risks.md`,
     next to the base case and the drivers you changed.
  Never edit the team's base `model/drivers.yaml` for a scenario.
- Every risk that could break a thesis pillar should match a kill criterion in
  `research/thesis.md`.
