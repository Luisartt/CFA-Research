# HOLD rating override — rewrite for report v32 (draft v1, 2026-11-04)

Team decision (2026-11-04, final): HOLD at MXN 64.85. The band rule gives SELL, so HOLD is a stated judgment.
This file replaces the three override reasons in v32 (executive summary p.2; "Football field and rating" p.8)
with one argument plus the dated test. Spanish text for report_es is given to Jorge in chat.

Source of every figure: verification copy
`analisis-dcf-2026-10-26/precio-objetivo/verificacion-v32/BIMBOA_TP12m_v2_copia_verif_v32.xlsx`
(TP12m_v2 + v32 inputs), full Excel recalculation, margin shifted from FY2027E through Assumptions!B350.

## What changes and why

| v32 reason | Keep? | Why |
|---|---|---|
| "The market just re-rated the stock" (+10.7%, 8th percentile EV/EBITDA on 18-Sep) | Drop | A re-rating already paid lowers the expected return: it argues for SELL |
| "Guidance raised three times, leverage 2.4x" | Drop | Already inside the model; it cannot be a reason to overrule the model |
| "SELL line 3.8% below the price" | Fold in | Same fact, stated as margin: 18 bp |
| Dated test (4Q26 call, Feb-2027) | Keep | The trigger is pre-committed |

## Executive summary (replaces "Our rating rule gives SELL ... (Table 7)")

Our rating rule gives SELL at this price: even the optimistic expected return (WACC −0.5 pp), +8.0%, falls short
of the 12.26% cost of equity. We rate HOLD as a judgment and say why. The rule moves to HOLD with an adjusted EBITDA
margin of 15.3% in FY2027E, only 18 bp above our 15.12%, about half the 35 bp width of management's own 2026 margin
guidance (+85 to +120 bp). Selling now would be a bet on a gap smaller than the company's own uncertainty about a year
that is nine months complete. We therefore wait for a dated test: if the 2027 guidance at the 4Q26 call in late
February 2027 implies less than 15.3%, we move to SELL (Table 7); at the consensus margin the target would be
MXN 50.84 (team model).

## Football field and rating (replaces "We rate HOLD ... for three reasons. First ... Third, the decisive test has a date.")

We rate HOLD, a neutral stance, as a judgment rather than an output of the rule, for two reasons. First, the rule
turns on a margin gap smaller than the company's own uncertainty. With an adjusted EBITDA margin of 15.3% in FY2027E,
18 bp above our 15.12%, the 12-month target rises to MXN 61.16 and the SELL line to MXN 64.96, above the price, so the
rule gives HOLD. Those 18 bp are about half the 35 bp width of management's 2026 margin guidance (+85 to +120 bp over
13.93%) (Grupo Bimbo, 3Q26 earnings call; team model). Second, the decisive test has a date. The 4Q26 call in late
February 2027 gives the first formal 2027 guidance: guidance implying 15.3% or more puts the price inside the band;
guidance that only matches our forecast leaves the rule at SELL, and we move to SELL. The rule gives BUY only at about
16.7%, 160 bp above our forecast (team model).

## Table 4, last row (replaces "Guide of 15.3% | 15.29% | MXN 61.05 (−5.9%) | 47.55-64.86 | HOLD")

| Case | Margin | 12-month target | HOLD band | Rule |
|---|---|---|---|---|
| Guidance of 15.3% | 15.30% | MXN 61.16 (−5.7%) | 47.64-64.96 | HOLD |

At exactly 15.29% the SELL line is MXN 64.82, below the price, so the rule still gives SELL; the rule flips at 15.292%.

## Figures [calc, verification copy]

| Item | Value | Cell / method |
|---|---|---|
| Model FY2027E adjusted EBITDA margin | 15.12% | Assumptions!B361 |
| Margin at which the SELL line equals MXN 64.85 | 15.292% | bisection on B350 |
| Target / band at 15.30% | 61.16 / 47.64-64.96 | Valuacion_12m B49, C76, C77 |
| Margin at which the target equals the price | 15.55% | bisection on B350 |
| Margin at which the base return equals ke | 16.01% | bisection on B350 |
| Margin for BUY | 16.73% | bisection on B350 |
| 2026 guidance range | +85 to +120 bp (35 bp wide) | [guidance] 3Q26 earnings call |

## Q&A preparation

- "So the market needs 15.3%?" No. 15.3% is where our rule moves to HOLD. For our target to equal the price the
  margin would be 15.55% (43 bp above ours); for the price to earn the full cost of equity, 16.01%.
- "If 18 bp is noise, why not BUY?" BUY needs about 16.7%, 160 bp above our forecast; the distances are not symmetric.
- "You broke your own rule." The rule's verdict depends on 18 bp of FY2027E margin; we pre-committed to follow it
  after the February 2027 guidance.
- Case against (team must be ready): the 35 bp range is for 2026, a year nine months reported; a judge can say the
  comparison should be with 2027 uncertainty, which is unknown.
