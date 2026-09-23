# Chart of accounts (what goes in data/financials.csv)

One row per line item per year: `line_item,year,value,tag,source_doc,page,note`.
Values in the units of `company-profile.yaml` (e.g. MXN millions), plain numbers,
no thousands separators. **Costs, capex, taxes and dividends are positive**; the
model subtracts them. Tags: `sourced` (from a filing, with page) or `unverified`.

Rule: components must add up to the reported totals. When the company reports
an item the chart has no line for, fold it into the closest "other" line and
record the fold in `data/adjustments.md`.

## Income statement

| Key | Required | What to put there | Typical source |
|---|---|---|---|
| `revenue` | yes | Net sales / total revenue | Income statement, first line |
| `cogs` | yes | Cost of sales, positive (includes D&A if the company puts it there) | Income statement |
| `opex` | yes | SG&A + other operating expenses - other operating income, positive | Income statement lines between gross profit and operating income |
| `da` | yes | Depreciation + amortization (incl. right-of-use assets), positive | Cash-flow statement, operating section add-backs |
| `interest_expense` | yes | Interest expense incl. lease interest, positive | Financial result note |
| `interest_income` | no | Interest income, positive | Financial result note |
| `other_financial_net` | no | FX result, derivatives, share of associates, other non-operating; income positive, loss negative | Financial result + associates lines |
| `income_tax` | yes | Income tax expense (current + deferred), positive = expense | Income statement |
| `nci_income` | no | Net income attributable to non-controlling interests | Bottom of income statement |
| `shares_diluted` | yes | Weighted-average diluted shares, in the model's share units | EPS note |

## Balance sheet

| Key | Required | What to put there |
|---|---|---|
| `cash` | yes | Cash and equivalents + short-term investments treated as cash |
| `receivables` | yes | Trade receivables, net |
| `inventory` | no | Inventories, net |
| `other_current_assets` | no | Every other current asset |
| `ppe_net` | yes | PP&E net + right-of-use assets (IFRS 16) |
| `intangibles_goodwill` | no | Goodwill + intangibles, net |
| `other_noncurrent_assets` | no | Deferred tax assets, investments in associates, other |
| `payables` | yes | Trade payables (suppliers) |
| `other_current_liabilities` | no | Every other current liability except debt and leases |
| `debt_short` | no | Short-term borrowings + current portion of long-term debt |
| `debt_long` | no | Long-term borrowings (bonds, bank loans) |
| `lease_liabilities` | no | Lease liabilities, current + non-current (IFRS 16) |
| `other_noncurrent_liabilities` | no | Deferred tax liabilities, provisions, pensions, other |
| `equity_parent` | yes | Equity attributable to the parent's shareholders |
| `nci_equity` | no | Non-controlling interests in equity |

## Cash-flow statement

| Key | Required | What to put there |
|---|---|---|
| `cfo` | yes | Net cash from operating activities, as reported |
| `capex` | yes | Purchases of PP&E + intangibles, positive |
| `dividends_paid` | no | Dividends paid to the parent's shareholders, positive |
| `lease_principal_paid` | no | Principal paid on lease liabilities (financing section), positive. **Required in practice if `lease_liabilities` > 0** — without it free cash flow ignores lease payments |

## Tie-out lines (used only for checks)

| Key | What to put there |
|---|---|
| `total_assets_reported` | Total assets exactly as reported |
| `net_income_reported` | Consolidated net income exactly as reported (before NCI split) |

## Revenue segments (optional)

`seg_<key>` rows, e.g. `seg_mexico`, `seg_usa`, `seg_eliminations` (negative).
Segments must add up to `revenue` in every year; declare them in
`model/drivers.yaml` under `revenue_segments` (the forecast skill does this).
