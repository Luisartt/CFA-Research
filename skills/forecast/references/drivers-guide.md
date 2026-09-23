# Drivers guide

Every forecast number in the model comes from a driver in `model/drivers.yaml`:
one value per forecast year, plus `tag`, `rationale` and `pillar`. A driver not
set is held at its last actual value (a few default to zero) and the engine warns.

## Story drivers vs mechanical drivers

- **Story drivers** (usually 3-5): the ones the thesis depends on — typically
  `revenue_growth` or segment growth, `gross_margin`, `opex_pct_revenue`, sometimes
  `capex_pct_revenue` or `payout_ratio`. **The team decides these.**
- **Mechanical drivers**: working-capital days, other current items, interest
  rates, minority share, lease payments. The assistant sets them from recent
  history and explains the choice in `rationale`.

## Every driver

| Driver | Meaning | How to anchor it | Watch out |
|---|---|---|---|
| `revenue_growth` | Revenue growth vs prior year | Market growth (industry.md) + share change + price/mix; guidance if any | Ignored when revenue segments are set |
| `gross_margin` | Gross profit / revenue | 3-5 year average; move it only with a reason (mix, pricing, input costs) | Above the historical best needs a pillar behind it |
| `opex_pct_revenue` | Operating expenses / revenue | Recent average; operating leverage if growth is strong | Cutting it without a plan is the most common judge challenge |
| `da_pct_revenue` | Total D&A / revenue | Recent average, rising if capex > D&A | Must stay consistent with capex over time |
| `amort_pct_revenue` | Amortization of intangibles / revenue (part of D&A) | Intangible amortization in the notes; 0 if not material | Keeps PP&E from absorbing intangible amortization |
| `capex_pct_revenue` | Capex / revenue | Guidance or history; maintenance capex ~ D&A, growth capex above | Capex below D&A for years means a shrinking asset base |
| `lease_principal_pct_revenue` | Lease principal paid / revenue (IFRS 16) | Recent average | Needed for lease-heavy companies (retail, restaurants, airlines) |
| `dso` | Receivable days | Recent average | Rising days eat cash |
| `dio` | Inventory days | Recent average | 0 for service companies |
| `dpo` | Payable days | Recent average | Rising payables flatter cash flow — don't assume it without evidence |
| `other_ca_pct_revenue` | Other current assets / revenue | Recent average | |
| `other_cl_pct_revenue` | Other current liabilities / revenue | Recent average | |
| `tax_rate` | Effective tax rate | Statutory rate (Mexico 30%, Brazil 34%, Chile 27%, Colombia 35%, Peru 29.5%) adjusted by recent history | Loss years distort the history |
| `interest_rate_debt` | Interest / opening total debt (incl. leases) | Recent history; debt costs note | |
| `interest_rate_cash` | Interest income / opening cash | Local short rates | |
| `payout_ratio` | Dividends / net income to shareholders | Dividend policy; recent history | |
| `nci_share` | Minority share of net income | Recent history | |
| `net_new_debt` | New long-term debt minus repayments (currency) | Debt maturity schedule in the notes; 0 if no plan | Repayments cannot exceed the balance (the engine floors debt at 0) |
| `shares_growth` | Change in diluted shares | 0 unless buybacks or issuance are announced | |
| `min_cash` | Minimum cash balance (currency) | Roughly last actual cash or a few weeks of costs | Below it, the model draws the revolver |

## Revenue by segment

When `financials.csv` has `seg_<key>` rows, set in `drivers.yaml`:

```yaml
revenue_segments:
  - {key: mexico, label: Mexico}
  - {key: usa, label: United States}
```

and one driver per segment: `seg_mexico_growth`, `seg_usa_growth` (same format as
other drivers). Segments must add up to revenue in history (include
eliminations as their own segment).

## Tags

`guidance` when management gave the number (cite where in `rationale`),
`assumption` for team or assistant judgment, `sourced` only for a figure copied
from a document (e.g. a statutory tax rate).

## Sanity rules the assistant checks before writing

- Margins beyond the historical best, or growth above market growth plus a
  credible share gain -> needs a pillar and a sentence in `rationale`.
- Capex below D&A for more than two years -> say why (asset-light shift?).
- Revenue growth converging towards long-term nominal GDP by the last year.
- Working-capital days moving more than 10 days -> evidence required.
