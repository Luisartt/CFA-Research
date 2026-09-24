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
  the value per share it implies (the valuation skill can run it).
- Every risk that could break a thesis pillar should match a kill criterion in
  `research/thesis.md`.
