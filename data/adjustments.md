# Accounting adjustments and mapping — Grupo Bimbo, S.A.B. de C.V. (BIMBOA)

_Updated 2026-10-17 — framework: IFRS — units: MXN millions. Figures are reported and mapped, not normalised, unless stated._

Read this before Q&A: a judge may ask why a number differs from the annual report.

## Sources

| Document | Years covered | File and PDF pages used |
|---|---|---|
| FY2025 audited statements (EEFF25), with 2023–2025 comparatives | FY2023, FY2024, FY2025 (latest report wins) | filings/annual/IA25_GB_EEFF_V10.pdf: balance sheet p.12; income statement p.13; cash flow p.16; equity statement p.15; note 5 (receivables) p.36; note 9 (leases) pp.41–43; note 10 (associates) p.43; note 14 (other payables) p.52; restructuring and integration p.82; note 19 (other long-term liabilities, MEPP) p.79; segments pp.85–86 |
| FY2023 annual report (RA23), audited statements with 2021–2023 | FY2021 (restated), FY2022 | filings/bmv/Reporte Anual 2023_XBRL_VF.PDF: balance sheet p.256; income statement p.257; cash flow p.260; equity statement p.259; note 5 p.292; note 9 pp.299–301; note 14 p.315; restructuring p.354; segments pp.358–359 |
| Capital IQ export (quarterly rows only) | Cross-check only | data/capitaliq/income_statement.csv, balance_sheet.csv, cash_flow.csv |

All page numbers are PDF page numbers. RA23 prints its balance sheet as statement page 7, which is PDF page 256.

**Rule for which report wins.** The latest report that presents a year is used. FY2023 appears in both EEFF25 and RA23; the income statement, balance sheet and cash flow agree line by line, so FY2023 comes from EEFF25. FY2021–FY2022 come from RA23, which already restates for the Ricolino disposal (continuing operations). RA23 is the only source for the FY2021 balance sheet.

**Wiki used for navigation only.** The wiki (wiki/Financials) gave the page references. Every value in data/financials.csv was re-read from the PDF page listed in the file.

## Capital IQ selection rule and unit conversion (cross-check only)

- **Annual rows.** The export has quarterly rows only; it contains no FY rows. FY flows are the sum of Q1–Q4 and balances are the Q4 (period-end) value. No YTD rows are used.
- **Duplicates.** A quarter can appear twice: once as restated (flag Y) and once as original (flag N). The restated row with the latest filing date is used; the original is ignored.
- **Units.** Each row is converted by its own unit and magnitude. Rows in "Mex$000" with magnitude "thousands" are divided by 1,000 to give MXN millions. Rows with other units (percent, actual, per-share) are excluded. Every row used is in MXN.
- **Gaps.** The FY2024 Q4 is empty in the income statement and cash-flow exports (CIQ restatement code DO), so FY2024 flows cannot be built from CIQ.

Cross-check result. Each cell shows the CIQ rebuild, with the difference to the CSV value in brackets.

| Item | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Reading |
|---|---|---|---|---|---|---|
| Revenue | 338,792 (0) | 398,706 (0) | 399,879 (0) | gap | 426,963 (+11) | Ties (rounding) |
| Income tax | 8,726 (0) | 14,381 (0) | 8,386 (0) | gap | 7,197 (0) | Ties |
| Net income (CIQ = majority) | 15,916 (0) | 46,910 (0) | 15,477 (0) | gap | 11,133 (0) | Ties to majority; consolidated = majority + NCI |
| Minority interest | 1,436 | 1,173 | 1,445 | gap | 1,813 | Equals continuing NCI; discontinued NCI (30 and 402) is outside CIQ |
| Cash | 8,748 (0) | 12,313 (0) | 6,353 (0) | 8,057 (0) | 8,535 (0) | Ties |
| Total assets | 337,640 (0) | 347,764 (0) | 348,102 (0) | 416,804 (0) | 409,805 (0) | Ties |
| Total equity | 101,606 (0) | 127,602 (0) | 111,628 (0) | 127,698 (0) | 120,255 (0) | Ties |
| Accounts receivable | 19,184 (0) | 21,600 (0) | 21,268 (0) | 23,555 (0) | 23,784 (0) | Equals note 5 trade receivables, net |
| Inventories | 13,710 (0) | 16,989 (0) | 16,120 (0) | 18,832 (0) | 17,151 (0) | Ties |
| Accounts payable | 36,991 (+1,239) | 45,068 (+1,010) | 41,643 (+1,234) | 41,884 (+1,069) | 40,028 (+954) | CIQ definition differs; statement line used |
| Operating income | 33,589 (+1,009) | 36,464 (−17,232) | 37,455 (+2,000) | gap | 36,272 (+2,126) | CIQ classifies items differently; not used |
| Interest expense, absolute | 7,429 (−394) | 7,422 (−627) | 9,595 (−411) | gap | 14,302 (−162) | CIQ definition differs; not used |
| Cash from operations | gap | 38,851 (0) | 31,411 (0) | gap | 47,753 (0) | Ties |
| D&A, cash flow | gap | 18,282 (0) | 18,929 (0) | gap | 24,048 (−790) | FY2025 difference unexplained; CSV uses 24,838 |
| Total debt repaid | gap | 61,927 (0) | 116,125 (0) | gap | 63,537 (0) | CIQ = loan repayments + lease payments, so CIQ's debt line includes leases |

## How reported lines map to the model

| Model line | Reported lines included | Years |
|---|---|---|
| revenue | Net sales | FY2021–FY2025 |
| cogs | Cost of sales | all |
| opex | Distribution and selling + administration + integration expenses + other (income) expenses, net | all |
| da | Depreciation and amortisation, continuing operations (segment note); cash-flow D&A shown as a memo | all |
| interest_expense | Interest expense, including lease interest | all |
| interest_income | Interest income | all |
| other_financial_net | Share of associates − FX loss − monetary-position (gain) loss + discontinued operation after tax | all |
| income_tax | Income tax, continuing operations | all |
| nci_income | Non-controlling interest, consolidated | all |
| shares_diluted | Weighted-average shares (basic; no dilutive instruments reported) | all |
| cash | Cash and cash equivalents | all |
| receivables | Trade receivables, net (customers less expected credit losses, note 5) | all |
| inventory | Inventories | all |
| other_current_assets | Other receivables + prepayments + current derivatives + derivative collateral deposits + held for sale | all |
| ppe_net | PP&E, net + right-of-use assets | all |
| intangibles_goodwill | Intangible assets, net + goodwill | all |
| other_noncurrent_assets | Investments in associates + non-current derivatives + deferred tax assets + other assets | all |
| payables | Trade payables to suppliers | all |
| other_current_liabilities | Other payables and accruals + related-party payables + income tax payable + employee profit sharing (PTU) + current derivatives + other short-term liabilities | all |
| debt_short, debt_long | Current portion of long-term debt; long-term debt | all |
| lease_liabilities | Lease liabilities, current + non-current | all |
| other_noncurrent_liabilities | Non-current derivatives + employee benefits + deferred tax liabilities + other long-term liabilities | all |
| equity_parent, nci_equity | Equity attributable to owners; non-controlling interests | all |
| cfo, capex | Operating cash flow; PP&E purchases + intangible purchases (cash basis) | all |
| lease_principal_paid | Derived: financing "lease payments" less lease interest accrued (tagged unverified) | all |
| dividends_paid | Dividends decreed to owners of the parent (statement of changes in equity) | all |
| total_assets_reported, net_income_reported | Total assets; consolidated net income (tie-out only) | all |
| seg_* | Net sales by region before eliminations; eliminations | all |

## Adjustments (each one in plain words)

### 1. Ricolino (confectionery) shown as discontinued
- **What:** FY2021 and FY2022 income-statement figures are the restated continuing figures. Ricolino was sold in November 2022; its after-tax result sits in discontinued operations.
- **Why:** The skill keeps discontinued operations out of revenue and costs and puts their result in other_financial_net.
- **Effect:** FY2021 revenue is 338,792. The originally reported figure (348,887, 4Q21 release, cited in the wiki) is not used. Discontinued after-tax result: 1,254 (FY2021) and 16,988 (FY2022).
- **If a judge asks:** "Our 2021 sales are restated for Ricolino. The forecast uses the continuing business."

### 2. Other financial result (other_financial_net)
- **What:** Associates' share of results, FX loss, monetary-position result and the discontinued after-tax result are combined: associates − FX loss − monetary (gain) loss + discontinued after tax.
- **Effect:** FY2021 988; FY2022 16,479; FY2023 (950); FY2024 (133); FY2025 (436). The components are in the note column of the CSV.
- **If a judge asks:** "With the discontinued result included here, net income ties to the reported consolidated figure in every year."

### 3. Financing cost kept as reported
- **What:** Interest expense includes lease interest; interest income is shown separately. Reported profit before tax (continuing) is rebuilt from EBIT, interest, FX, monetary position and associates, and matches in all five years.

### 4. PTU (employee profit sharing) stays in opex
- **What:** PTU has no separate income-statement line; it sits inside the distribution, selling and administrative lines, so it is inside opex. The PTU payable (1,592 at Dec-25) is an operating accrual. PTU cash paid is in the operating section of the cash flow (159 in FY2025).

### 5. D&A on a continuing basis (decided; FY2021–FY2022 differ from the cash flow)
- **What:** da uses the segment-note D&A, which covers continuing operations: 16,126 (FY2021), 18,038 (FY2022), 18,929, 23,051 and 24,838. The cash-flow add-back is 16,375 and 18,282 in those two years. The difference is discontinued Ricolino D&A: 249 for FY2021 (computed from the two sources) and 244 for FY2022 (footnoted in RA23 p.359). FY2023–FY2025 are identical in both.
- **Why:** EBIT, cogs and opex are continuing figures, so the D&A inside them must be continuing too. The skill's rule ("already inside cogs/opex") implies this basis; the cash-flow figure is kept as a memo in the EBITDA bridge.
- **Effect:** Historical EBIT + da is 249 (FY2021) and 244 (FY2022) lower than with cash-flow D&A.

### 6. Lease principal: the reported lease line includes interest (derived; tagged calc)
- **What:** The financing line "Pagos de arrendamiento" is 5,372; 6,385; 6,278; 7,072; 8,060. The same amounts are the "payments" column of the lease-liability roll-forward (note 9), where interest accrues separately (2,137 in FY2025) and payments reduce the liability in full. The reported line therefore includes lease interest. The CSV carries principal alone: payments less lease interest accrued, which is 4,117; 5,056; 4,802; 5,321; 5,923.
- **Why principal:** The chart defines lease_principal_paid as principal. The engine uses it in two places where interest would be double-counted. Forecast FCF is CFO − capex − lease principal, while forecast net income already carries an interest charge calibrated on total interest expense, which includes lease interest. The DCF deducts "new leases = lease principal repaid" from NOPAT, which is struck before lease interest.
- **Cash split: not disclosed (searched 2026-10-17).** No filing states the interest part of the lease cash paid. Searched: EEFF25 note 9 roll-forward (p.43: "Intereses devengados" 2,137, "Pagos" 8,060, no split), cash-flow statement (p.16), note 13 debt reconciliation (p.52, excludes interest and leases), note 14 accrued interest (p.52), note 23 interest expense (p.83), policy note 3 (p.22, p.31–32); RA23 cash flow (p.260) and note 23 (p.355) for FY2021–FY2022; BMV XBRL Dic-25 [520000] (filings/bmv/Reporte_Definitivo_BMV_XBRL_Español_Dic_25.pdf p.20) and its lease note (pp.106–110). The XBRL splits the cash only by lease type: "Pagos de pasivos por arrendamientos financieros" 1,486 and "Pagos de pasivos por arrendamientos" 6,574, the two note 9 columns.
- **Evidence that the lease line carries the interest.** "Intereses pagados" is 11,533 / 8,376 / 7,436 (FY2025 / FY2024 / FY2023, p.16) against debt interest of 11,372 / 10,495 / 7,469 (note 23, p.83). With lease interest inside, it would be near 13,509 / 12,246 / 8,945. Lease interest is therefore paid inside "Pagos de arrendamiento", which note 9 deducts from the liability in full.
- **Basis (tag calc).** Principal = payments `[sourced]` less interest accrued `[sourced]`. The only gap to a true cash split is the change in lease interest accrued but not yet paid. That amount stays inside the lease liability and is at most about one month of interest (about 180 in FY2025), so the year-on-year change is smaller still. The 1H26 roll-forward (BMV 2Q26 XBRL p.100: interest accrued 1,042, payments 3,948) gives principal 2,906 on the same basis (valuation/inputs/spg_inputs.yaml dated_bridge.lease_1h).
- **If a judge asks:** "Lease cash payments of 8.1bn include about 2.1bn of interest. Principal is about 5.9bn."

### 7. IFRS 16 mapping
- Lease interest (1,255; 1,329; 1,476; 1,751; 2,137) is inside interest_expense. Right-of-use assets are inside ppe_net (30,754 at Dec-21; 32,757 at Dec-25). Lease liabilities (current + non-current) are in lease_liabilities. Right-of-use depreciation is inside da (segment note).

### 8. Receivables: trade only
- **What:** receivables is trade receivables, net (customers less expected credit losses, note 5). Other receivables go to other_current_assets: 7,986 (Dec-21) and 11,998 (Dec-25).
- **Why:** The chart defines receivables as trade receivables. The balance-sheet line also includes other receivables.
- **Effect:** Dec-25 receivables 23,784 (balance-sheet line 35,782). CIQ's accounts-receivable figure equals the note 5 net figure in all five years.

### 9. Other current liabilities include tax and interest accruals (chart rule)
- **What:** other_current_liabilities = other payables and accruals (note 14) + related-party payables + income tax payable + PTU + current derivatives + other short-term liabilities. The chart rule is "everything except debt and leases".
- **Effect:** Dec-25 31,788. It includes other taxes payable (3,650), tax contributions (1,085) and accrued interest and bank charges (2,517); the working-capital table removes these.
- **Note for the forecast:** other_cl_pct_revenue will carry derivatives and tax accruals unless the team later splits them out.

### 10. Trade payables only
- payables is "Cuentas por pagar a proveedores" (trade payables to suppliers): 39,074 at Dec-25. Related-party payables (1,154) sit in other_current_liabilities. CIQ's accounts payable is 954 higher in FY2025 and is not used.

### 11. Derivatives, collateral deposits and held-for-sale assets
- Derivative assets (current 60; non-current 657) and collateral deposits (459) go to other_current_assets and other_noncurrent_assets. Derivative liabilities go to other_current_liabilities (1,588) and other_noncurrent_liabilities (2,314). Held-for-sale assets (886 at Dec-25) go to other_current_assets. Balance-sheet totals tie in every year.

### 12. Shares
- shares_diluted is the weighted-average number of shares in millions (the filing gives thousands): 4,487.268; 4,448.693; 4,418.137; 4,357.250; 4,310.531. The filing reports one figure (basic), and no dilutive instruments are disclosed, so diluted equals basic.

### 13. Capex is PP&E plus intangibles, cash basis
- **What:** capex = purchases of PP&E + purchases of intangibles, from the cash-flow statement. ROU additions are non-cash and are excluded (see the lease section). The "increase in distribution rights in structured entities" line is not in capex, because the company's capex definition does not include it: (77) FY2021, +3 FY2022, (129) FY2023, (705) FY2024, (52) FY2025.
- **Judgement:** FY2024 includes a large distribution-rights outflow (705) that the model excludes. Open item.

### 14. Perpetual notes in equity (FY2021–FY2022)
- The USD perpetual subordinated notes (8,867 at Dec-21; 8,098 at Dec-22) are inside equity_parent, as reported. They were redeemed in 2023 and reclassified to debt (8,845 in the debt reconciliation, EEFF25 p.52). Treating them as debt would change Dec-21 and Dec-22 leverage.

### 15. Dividends paid to the parent
- **What:** dividends_paid is the amount decreed to owners of the parent in each year, from the statement of changes in equity: 4,502 (FY2021), 5,791, 3,458, 4,125 and 4,316 (FY2025). The non-controlling share is excluded (163, 94, 91, 109 and 135).
- **Check:** For FY2022–FY2025 the cash-flow "Dividendos pagados" (5,885; 3,549; 4,234; 4,451) equals the parent amount plus the non-controlling share. FY2021 cash paid is 4,636, which differs from the decreed 4,665 in total by 29 (timing).

### 16. Tags
- One value family is tagged calc: lease_principal_paid (payments less interest accrued; the cash split is not disclosed, see adjustment 6). It was tagged unverified until 2026-10-17. Every other value in the CSV is tagged sourced, because each ties to a PDF page. Derived lines (sums or differences of sourced lines) are tagged sourced, and their components are written in the note column.

### 17. Operating cash flow is before interest and lease payments
- Reported operating cash flow excludes interest and lease payments, both of which are financing cash flows. A historical CFO − capex − lease figure is therefore not a levered free cash flow.

## Adjusted EBITDA bridge (reported basis)

The model keeps EBIT and da on the reported basis (no normalisation). The company's Adjusted EBITDA adds back impairment and other non-cash items, mainly the multi-employer pension plan (MEPP) valuation. It does not add back restructuring.

| MXN m | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Operating income (EBIT), reported | 32,580 | 53,696 | 35,455 | 33,149 | 34,146 |
| Add: D&A, continuing (segment note) | 16,126 | 18,038 | 18,929 | 23,051 | 24,838 |
| Model EBITDA = EBIT + continuing D&A | 48,706 | 71,734 | 54,384 | 56,200 | 58,984 |
| Add: impairment of long-lived assets | 682 | 252 | 383 | 249 | 445 |
| Add: other non-cash items (mainly MEPP) | (2,016) | (18,540) | 175 | (976) | 27 |
| Company Adjusted EBITDA (result) | 47,372 | 53,446 | 54,942 | 55,473 | 59,456 |
| Gap: model minus company | 1,334 | 18,288 | (558) | 727 | (472) |
| of which company adds back impairment | (682) | (252) | (383) | (249) | (445) |
| of which company adds back other non-cash items | 2,016 | 18,540 | (175) | 976 | (27) |
| Memo: cash-flow D&A (includes discontinued) | 16,375 | 18,282 | 18,929 | 23,051 | 24,838 |
| Memo: cash-flow D&A less continuing D&A | 249 | 244 | 0 | 0 | 0 |

- **FY2025 target (59,456).** Model EBITDA = revenue − cogs − opex + da = 426,952 − 203,465 − 189,341 + 24,838 = 58,984. The 472 gap is impairment (445) plus other non-cash items (27).
- **FY2022.** The gap of 18,288 is almost entirely the MEPP non-cash gain (18,540) inside EBIT, less the impairment of 252. Operating income of 53,696 is not a run-rate figure.
- **Restructuring** is not added back. It was 2,059 (FY2021), 1,657, 2,959, 6,293 and 3,908 (FY2025), verified on RA23 p.354 and EEFF25 p.82.

## Lease history (IFRS 16) — kept out of the CSV

Source: note 9 roll-forwards — RA23 pp.299–301 (FY2021–FY2023) and EEFF25 pp.41–43 (FY2023–FY2025).

| MXN m | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Lease liability, opening | 29,089 | 31,149 | 29,185 | 26,815 | 35,801 |
| Add: new leases (ROU additions, non-cash) | 3,967 | 3,439 | 3,751 | 6,197 | 5,293 |
| Add: acquired with businesses | 753 | 50 | 276 | 33 | 236 |
| Add: modifications and remeasurements | 1,362 | 1,437 | 687 | 2,483 | 1,746 |
| Add: interest accrued (in interest expense) | 1,255 | 1,329 | 1,476 | 1,751 | 2,137 |
| Less: payments (cash-flow financing line) | (5,372) | (6,385) | (6,278) | (7,072) | (8,060) |
| Less: early termination and COVID rent concessions | (522) | (302) | (211) | (149) | (311) |
| Less: discontinued operation (Ricolino) | 0 | (372) | 0 | 0 | 0 |
| FX and translation | 617 | (1,160) | (2,071) | 5,743 | (2,052) |
| Lease liability, closing (result) | 31,149 | 29,185 | 26,815 | 35,801 | 34,790 |
| Memo: ROU depreciation (in da) | 4,904 | 5,143 | 4,860 | 5,417 | 6,142 |
| Memo: principal (payments less interest accrued; the CSV value) | 4,117 | 5,056 | 4,802 | 5,321 | 5,923 |
| Memo: new leases + acquired + modified (ROU basis) | 6,148 | 5,178 | 5,221 | 9,668 | 7,933 |

Every column reconciles: opening + movements = closing (checked in the build). Closing lease liabilities equal the current + non-current lease liabilities on the balance sheet in all five years.

**Capex excludes non-cash ROU additions — confirmed.** Capex is the cash purchase of PP&E (22,530 in FY2025) plus intangibles (311). ROU additions (5,293) are recognised against the lease liability with no cash movement; they do not appear in investing or financing cash flows.

**Test of the proxy "new leases = principal repaid".** The engine's DCF deducts new leases as "lease principal repaid", which implies a flat lease liability. Over FY2021–FY2025 the liability rose 5,701: 1,077 from FX and translation and 4,624 excluding FX. So the proxy slightly understates lease growth.
- Five-year totals: new leases plus acquired and modified (ROU basis) 34,148; cash lease payments 33,167 (ratio 1.03x); principal-only 25,219 (ratio 1.35x).
- Year by year, the ratio of new leases (incl. acquired and modified) to principal ranges from 1.02x (FY2022) to 1.82x (FY2024). Against cash payments the range is 0.81x to 1.37x.
- Matching new leases to total payments does not on its own decide the line. The choice rests on the FCF and DCF definitions in adjustment 6.

## Cash taxes paid vs income-tax expense

| MXN m | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Income-tax expense (income statement, continuing) | 8,726 | 14,381 | 8,386 | 6,797 | 7,197 |
| Income taxes paid (cash flow) | 7,578 | 11,824 | 13,831 | 6,472 | 8,955 |
| Paid ÷ expense | 0.87x | 0.82x | 1.65x | 0.95x | 1.24x |

Cash taxes are consolidated (FY2021–FY2022 include Ricolino), while expense is continuing, so FY2021–FY2022 are not like-for-like. The statements reviewed do not explain the timing differences in other years.

## Balance-sheet bridge candidates (Dec-2025)

| Item | Dec-25 | Where it sits in the model | Source |
|---|---|---|---|
| Employee benefits (non-current) | 6,507 | other_noncurrent_liabilities | EEFF25 p.12 |
| MEPP exit liabilities (inside other long-term liabilities) | 985 (Dec-24 1,205; Dec-23 2,033) | other_noncurrent_liabilities | EEFF25 p.79, note 19 |
| Derivative assets (current 60 + non-current 657) | 717 | other_current_assets, other_noncurrent_assets | EEFF25 p.12 |
| Derivative liabilities (current 1,588 + non-current 2,314) | 3,902 | other_current_liabilities, other_noncurrent_liabilities | EEFF25 p.12 |
| Collateral deposits on derivatives (restricted-type, not cash) | 459 | other_current_assets | EEFF25 p.12 |
| Investments in associates | 7,018 | other_noncurrent_assets; results in other_financial_net | EEFF25 p.12, note 10 p.43 |
| Non-controlling interests (book value) | 743 | nci_equity | EEFF25 p.12 |
| Restricted cash | None on the balance sheet | The only restricted-type balance identified is the 459 of collateral deposits above | EEFF25 p.12 |
| Lease liabilities | 34,790 | lease_liabilities | EEFF25 p.12, p.43 |
| Financial debt (current 12,635 + long-term 141,028) | 153,663 | debt_short, debt_long | EEFF25 p.12 |

## Operating working capital (excludes financing and tax items)

Excluded: cash; all derivatives and collateral deposits; held-for-sale assets; income-tax balances; short-term debt; current lease liabilities; and accruals of other taxes, tax contributions and accrued interest and bank charges (note 14). Note 14 has no dividends-payable line.

| MXN m | Dec-21 | Dec-22 | Dec-23 | Dec-24 | Dec-25 |
|---|---|---|---|---|---|
| Trade receivables, net (note 5) | 19,184 | 21,600 | 21,268 | 23,555 | 23,784 |
| Other receivables (balance-sheet line less trade) | 7,986 | 10,585 | 12,001 | 13,104 | 11,998 |
| Inventories | 13,710 | 16,989 | 16,120 | 18,832 | 17,151 |
| Prepayments | 2,296 | 928 | 1,378 | 1,371 | 1,798 |
| **Operating assets** | 43,176 | 50,102 | 50,767 | 56,862 | 54,731 |
| Trade payables | 35,752 | 44,058 | 40,409 | 40,815 | 39,074 |
| Related-party payables | 1,527 | 1,240 | 1,412 | 1,260 | 1,154 |
| Employee profit sharing (PTU) payable | 1,692 | 1,811 | 1,787 | 1,752 | 1,592 |
| Operating accruals (other payables less tax and interest) | 19,065 | 18,346 | 15,758 | 19,314 | 19,143 |
| **Operating liabilities** | 58,036 | 65,455 | 59,366 | 63,141 | 60,963 |
| **Operating working capital** | (14,860) | (15,353) | (8,599) | (6,279) | (6,232) |
| Increase in operating working capital (balance sheet; use of cash) | n/a | (493) | 6,754 | 2,320 | 47 |
| Cash-flow working-capital lines, total (use of cash) | (5,451) | 2,737 | 6,542 | 7,733 | 655 |

Notes on the year-on-year changes:
- **FY2022** cash-flow lines include Ricolino until its sale and the balance sheet does not, so the two are not comparable.
- **FY2023** balance-sheet change (6,754) and cash-flow lines (6,542) are close.
- **FY2024** and **FY2025** differ by 5,413 and 608. The balance-sheet change is net of acquired balances and translation, which the cash-flow lines exclude. The cash-flow lines also include items outside this definition (taxes, interest accruals, collateral deposits).
- **FY2025 acquisitions.** Cash paid for business acquisitions was 11,294 (EEFF25 p.16). The deals named in the wiki are Karamolegos (Romania), Don Don (Balkans), Stone House Bread (US) and Wickbold (Brazil); these names were not re-checked against the PDF. The wiki gives Wickbold's acquisition date as 6 October 2025 (4Q25 release); not re-checked. The statements do not split the acquired working capital.
- **FY2025 FX.** Translation moved the balance sheet: the cumulative translation reserve went from (868) to (10,377) (EEFF25 p.12), and lease balances moved by (2,052) on conversion (note 9). Individual working-capital lines are not split for FX.
- **Receivables.** Trade receivables rose by 229 on the balance sheet (23,555 to 23,784). Total receivables fell by 877 (36,659 to 35,782), while the cash-flow receivables line shows an inflow of 601. The 276 difference reflects acquired balances and translation, which the filings do not split.

## One-off items (kept in the numbers, flagged for the forecast)

| Year | Item | Amount | Line |
|---|---|---|---|
| FY2021 | MEPP non-cash benefit (cash-flow line) | 2,247 | Operating expenses / other long-term liabilities |
| FY2022 | Ricolino disposal, pre-tax gain (cash flow) | 22,038 | Discontinued operations (after tax, in other_financial_net) |
| FY2022 | MEPP non-cash gain (cash flow) | 19,010 | Inside operating income |
| FY2022 | Other (income) expenses, net, as reported | (15,309) | Operating expenses |
| FY2023 | Impairment of long-lived assets | 383 | Operating expenses |
| FY2024 | MEPP non-cash gain (cash flow) | (982) | Operating expenses |
| FY2024 | Restructuring (11 bakeries closed) | 6,293 | Operating expenses (EEFF25 p.82) |
| FY2025 | Impairment of long-lived assets | 445 | Operating expenses |
| FY2025 | Integration expenses | 541 | Operating expenses |
| FY2025 | Restructuring | 3,908 | Operating expenses (EEFF25 p.82) |

Restructuring for FY2021–FY2023 (2,059; 1,657; 2,959) is in the numbers as reported (RA23 p.354).

## Open items

1. **Lease principal is derived (calc; closed 2026-10-17).** The cash split of lease interest is not disclosed in EEFF25, RA23 or the BMV XBRL (adjustment 6 lists where we looked). Values (FY2021–FY2025): 4,117; 5,056; 4,802; 5,321; 5,923. The reported financing line (8,060 in FY2025) is in the lease table as the cash total.
2. **Distribution-rights purchases.** FY2024 (705) and FY2025 (52) are excluded from capex. Decide whether they belong in capex for the forecast.
3. **Dividend timing.** FY2021 cash dividends (4,636) differ from the amount decreed (4,665) by 29; treated as timing.
4. **Shares.** Only the basic weighted average is reported. Confirm with the team that no dilutive instrument is outstanding.
5. **Capital IQ export.** It has quarters only and no FY2024 Q4 for the income statement and cash flow. A re-export with annual rows would simplify cross-checks. CIQ's accounts-payable (+954 in FY2025) and D&A (−790 in FY2025) differences are unexplained and not used.
6. **Other receivables.** Composition (11,998 at Dec-25) was not extracted; it may include tax receivables. Operating working capital includes it as presented.
7. **Acquisitions.** Wickbold's acquisition date and the acquired balance sheet were not extracted (EEFF25 note 1). FY2025 working-capital changes are not split between acquisitions and translation.
8. **Log and memory entries (closed 2026-10-17).** The history decision is in `docs/context/memory.md` (FY2021-FY2025, MXN millions, IFRS) and the extraction is logged in `docs/context/ai-use-log.md`.

## Three questions a judge may ask about our numbers

1. **Q:** Why is FY2022 net income 48.5bn when FY2023 is 16.9bn?
   **A:** FY2022 includes the Ricolino disposal (discontinued after-tax result 16,988; the pre-tax gain on sale was 22,038) and a non-cash MEPP gain of 19,010 in the cash flow (18,540 inside the company's Adjusted EBITDA). Both are one-off; the model keeps them, flagged.
2. **Q:** Why is our FY2025 EBITDA 58,984 when the company reports Adjusted EBITDA of 59,456?
   **A:** We keep reported EBIT (34,146) and continuing D&A (24,838) unadjusted. The company adds back impairment (445) and other non-cash items (27), which together are the 472 difference.
3. **Q:** Why are lease payments 8.1bn when lease depreciation is 6.1bn?
   **A:** The cash line includes lease interest. Under IFRS 16 the lease cost in the income statement is depreciation (6,142) plus interest (2,137), which is 8,279, close to the cash payments of 8,060. Principal alone is about 5.9bn: payments less the 2,137 of interest accrued, because the company does not split the cash.

## Engine check and target reconciliation

Engine (run from the project root, check mode, no files written), 2026-10-17 validation pass:

```
[ok] inputs are valid (check only, no files written)
checks: 123 OK, 0 ERROR, 0 WARN
status: ALL CHECKS OK
```

The earlier warnings are gone: lease_principal_paid is tagged calc (adjustment 6), and `model/drivers.yaml` and `valuation/valuation.yaml` now exist. The 123 checks include the balance sheet balancing in every year, total assets and net income tying to the reported figures for FY2021-FY2025, and revenue segments adding up to revenue.

Targets:
- **FY2025 revenue 426,952:** matches the income statement (EEFF25 p.13) and the four regions plus eliminations (EEFF25 pp.85–86).
- **FY2025 Adjusted EBITDA 59,456:** EBIT 34,146 + D&A 24,838 + impairment 445 + other non-cash 27 (segment note, EEFF25 p.85). The model's EBITDA is 58,984; the 472 gap is explained in the bridge.
- **Net debt ex-IFRS 16 at Dec-25:** total financial debt 153,663 (12,635 + 141,028) less cash 8,535 = 145,128, matching the target of about 145.1bn. Lease liabilities of 34,790 sit on top, giving 179,918 including leases.

## Validation pass (2026-10-17)

- No new fiscal year and no restatement since FY2025, so `data/financials.csv` is unchanged: 180 rows, FY2021-FY2025, 175 `sourced` and 5 `calc` (lease principal, adjustment 6), no `unverified` figure.
- The Capital IQ data integrated on 2026-10-16/17 (peer data, rates, Bimbo market data) does not touch the history; it feeds `valuation/` only.
- Interim 1H26 figures stay outside the annual history; they are used in `valuation/inputs/spg_inputs.yaml` (dated bridge, Dated_Check) with their own sources.
- Contradictions checked against this history: the 2026 dividend is MXN 1.075 per share (AGM notice 13-Apr-2026; the 1.75 in the BMV Jun-26 filing is a typo) and does not enter FY2021-FY2025; the 249 plants of RA25 p.14 equal the 248 included in the country-risk table plus Venezuela (deconsolidated). Still open: FY2022 buybacks 2,556 vs 2,568 (not a line in this chart, so it does not move the history).
- Provenance of the first pass (kept from the earlier note): tie-outs were checked by script against the PDF pages and by the engine, and an independent review of the mapping was applied; no Codex cross-check of the mapping itself.
