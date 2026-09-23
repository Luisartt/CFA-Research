# Extraction guide

## Where the documents are

| Market | Annual report / audited statements |
|---|---|
| Mexico (BMV/BIVA) | Emisnet (bmv.com.mx) and BIVA: "Reporte anual" + "Estados financieros dictaminados"; company IR site |
| Brazil (B3) | CVM (rad.cvm.gov.br): DFP (annual), ITR (quarterly); company IR site |
| Chile | CMF (cmfchile.cl): "Estados financieros" |
| Colombia | SFC / company IR site |
| Peru | SMV (smv.gob.pe) |
| US-listed | SEC EDGAR: 10-K (domestic) or 20-F (foreign private issuer) |

Students download the PDFs into `filings/`. The assistant never guesses a number
that is not in a document there.

## Which number wins

- Use the **most recent** report's comparative columns for earlier years
  (restated figures win over the originally reported ones). Note each restatement
  in `adjustments.md`.
- Use the audited annual statements, not press releases, when both exist.
- Consolidated figures only.

## Mapping rules that matter

- **Operating expenses (`opex`)**: everything between gross profit and operating
  income, netted (other operating income reduces it). Then EBIT = revenue - cogs -
  opex must equal reported operating income after the reclassifications below
  (PTU, associates, discontinued operations); if not, find the missing line.
- **Costs presented by nature** (common for telecoms, airlines, miners): there is
  no "cost of sales" line. Put costs directly tied to delivering the product or
  service in `cogs` (e.g. cost of equipment and services, fuel, raw materials) and
  the rest in `opex`; explain the split in `adjustments.md`. `cogs` must be > 0.
- **D&A**: take it from the cash-flow statement add-backs (it is already inside
  cogs/opex; the model only uses it for EBITDA, PP&E and cash flow).
- **Mexico PTU** (employee profit sharing): an operating cost — keep it in `opex`
  even if the company shows it near taxes.
- **Associates / joint ventures** (share of results): `other_financial_net`.
- **Discontinued operations**: exclude them from revenue and costs; put their
  result in `other_financial_net` and say so.
- **Argentina (IAS 29)**: figures are restated to current purchasing power;
  use the latest restated set for every year and flag it prominently.

## Leases

- **IFRS 16 (and NIF D-5)**: right-of-use assets go in `ppe_net`, lease liabilities
  in `lease_liabilities`, principal paid (financing section of the cash flow) in
  `lease_principal_paid`, lease interest inside `interest_expense`.
- **US GAAP (ASC 842)**: *finance* leases as above. *Operating* lease cost stays in
  `opex`; operating right-of-use assets go in `other_noncurrent_assets` and
  operating lease liabilities in `other_current_liabilities` /
  `other_noncurrent_liabilities` (so they are not counted as debt, consistent with
  their cost sitting in operating expenses). Say this in `adjustments.md` —
  it matters when comparing EBITDA with IFRS peers.
- Under ASC 842, exclude operating-lease right-of-use amortization from `da`
  (it is part of the lease cost in `opex`); only finance leases go in
  `lease_liabilities` / `lease_principal_paid`.

## Tie-outs before writing

For every year: assets = liabilities + equity (after mapping), `total_assets_reported`
and `net_income_reported` equal the reported figures, and EBIT matches reported
operating income after the reclassifications recorded in `adjustments.md` (PTU,
associates, discontinued operations). A difference beyond those means a line was
missed — find it; never force it into a random line.
