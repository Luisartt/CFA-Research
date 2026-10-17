# Model review — BIMBOA engine model v2 (2026-10-17)

**File:** `model/BIMBOA_model_v2.xlsx`, an engine build from `data/financials.csv`, `model/drivers.yaml` and `valuation/valuation.yaml`.

**Status: ALL CHECKS OK** (123 checks, 0 errors, 0 warnings in the checks).
- One engine warning remains: `lease_principal_paid` FY2021-FY2025 is tagged `[unverified]`. It is derived as lease payments less lease interest accrued (data/adjustments.md #6).
- v1 is kept as the version Codex audited.

**What changed from v1.** `other_ca_pct_revenue` and `other_cl_pct_revenue` now grow only the operating balances (Codex audit, finding 1). The non-operating balances are held flat in pesos:
- other current assets: 1,405 (derivatives, collateral, held for sale);
- other current liabilities: 9,899 (taxes, accrued interest, derivatives).

Valuation inputs changed too: `debt_like_items` is 37,621, with the provisions incl. uncertain tax positions added, and the Mondelez lease proxy was added.

Forecast drivers are **assistant proposals**. The story drivers (segment growth, gross margin, opex, capex) wait for the team. The published valuation (`valuation/valuation-outputs.yaml`) uses the DCF workbook's published basis. This engine model is the reconciliation anchor.

## Ratios: last three actual years and all forecast years

| | FY23A | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E | FY34E | FY35E |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue growth | 0.3% | 2.1% | 4.6% | -0.8% | 4.5% | 4.4% | 4.4% | 4.4% | 4.4% | 4.3% | 4.3% | 4.3% | 4.2% |
| Gross margin | 51.4% | 52.6% | 52.3% | 52.4% | 52.0% | 52.3% | 52.5% | 52.5% | 52.5% | 52.5% | 52.5% | 52.5% | 52.5% |
| EBITDA margin | 13.6% | 13.8% | 13.8% | 14.7% | 14.5% | 14.9% | 15.1% | 15.3% | 15.3% | 15.3% | 15.3% | 15.3% | 15.3% |
| EBIT margin | 8.9% | 8.1% | 8.0% | 8.8% | 8.6% | 9.0% | 9.2% | 9.4% | 9.4% | 9.4% | 9.4% | 9.4% | 9.4% |
| FCF margin | -2.3% | 1.1% | 4.4% | 3.6% | 3.4% | 3.6% | 3.7% | 3.9% | 4.0% | 4.1% | 4.2% | 4.2% | 4.3% |
| ROIC | 10.4% | 9.2% | 7.2% | 8.2% | 8.4% | 9.1% | 9.6% | 10.2% | 10.4% | 10.7% | 10.9% | 11.1% | 11.3% |
| Net debt / EBITDA (incl. leases) | 2.40x | 3.18x | 3.05x | 2.74x | 2.52x | 2.22x | 1.97x | 1.72x | 1.52x | 1.31x | 1.12x | 0.94x | 0.76x |
| Interest cover (EBIT / interest) | 3.54x | 2.53x | 2.36x | 2.57x | 2.62x | 2.87x | 3.08x | 3.28x | 3.43x | 3.58x | 3.73x | 3.89x | 4.05x |

`[calc]` model/model-summary.json (v2).

## Flags

1. **The EBITDA margin of 15.3% from FY2030 is above the historical best on the reported basis.** History is 13.6-14.4% (FY21-FY25, excluding the FY22 MEPP gain).
   - Driver: `opex_pct_revenue` (pillar 2, new-CEO productivity).
   - The team must say what makes +150 bp vs FY2025 true (North America transformation, Mexico mix).
2. **Cash builds up to Ps 116bn by FY2035**, because `net_new_debt` = 0 and the payout is 38%.
   - Lease-inclusive net debt / EBITDA falls to 0.76x.
   - The DCF is unaffected (it is built on FCFF), but the balance sheet contradicts a "hold" on leverage at 2.0-2.5x.
   - Drivers: `payout_ratio`, `net_new_debt`, `shares_growth` (pillar 3).
3. **Revenue growth converges to ~4.2-4.4%.**
   - That is near the 4.25% terminal growth and below the 5% long-term nominal GDP cap.
   - FY2026 is -0.8% in pesos, because of peso strength on North America.
4. **Capex rises from 4.6% to 6.0% of revenue, while D&A stays at 5.85-5.9%.**
   - On the published basis the lease book also grows with revenue, so total terminal net reinvestment is 29% of NOPAT and the return on new capital is 14.6%. The engine basis gives 17.9%.
   - The capex path is now the largest value lever: +/-50 bp = -/+ Ps 9.7 per share.
5. **Working-capital days are held at FY2025** (DSO 20.3, DIO 30.8, DPO 70.1). DPO fell from 82.7 days in FY21 and is not rebuilt.
6. **Tax on EBIT is 34%**: an effective rate, above the 30% statutory (FY23-25 average 33.8%).
   - Uncertain tax positions (8,537) are in the bridge as a claim.
   - Cash taxes paid exceeded tax expense on average in FY23-25.

## Fixes made

- **Working capital (v2).** Non-operating balances are held flat, and the operating working capital ties to data/adjustments.md in all five years (`valuation/BIMBOA_DCF_v2.xlsx`, Checks).
- **Inputs validated before each build** with `--check`. The v2 build ran clean: 123 checks.

## Open questions for the team

- Which 3-5 drivers carry the thesis (climate → gross margin; CEO → opex; debt → capex/payout)? What number must be true for each?
- How will the excess cash be used in the forecast: buybacks, debt paydown or M&A?

## Coach checkpoint — "Does the model look like the business?"

The three ratio trends that move most from history to forecast:
- EBITDA margin: 13.8% → 15.3%;
- FCF margin: stable at ~4% despite the margin gains, because capex rises;
- net debt / EBITDA: 3.05x → 0.76x.

Question for the team: explain the biggest change in one sentence, and say which pillar causes it.
