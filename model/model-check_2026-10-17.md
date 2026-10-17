# MODEL CHECK — model/BIMBOA_model_v7.xlsx  [2026-10-17]

Run: `/research-analyst:model-check` (read-only; the Excel recalculation for S10 ran on a copy in the scratchpad). The model is **external** to the research-analyst plugin: it is built by the CFA research-challenge engine (`build_model.py`, never edited), so contract-specific checks are `n/a` and the format checks (F) audit it against a different house style.

```
Estructurales : [ok] S2 (0 external links), S3 (0 volatile functions), S7 (automatic calculation, full calc on load),
                S10 (Excel full rebuild on a copy: 1,492 formulas, 0 without a cached value, 0 errors; Checks 123/123 OK)
                [x]  S5 DCF!19-20: '=H18-C7' and '=1/(1+WACC!C21)^H19' do not anchor C7 / WACC!C21, so the formulas differ
                     in R1C1 across periods (values are correct: Excel = Python at build, 123/123 after recalculation)
                [aviso] S4 82 constants in formulas, all outside the calculation tabs: 33 sensitivity steps, 2 football
                     +/-1x, 47 check tolerances; none in IS/BS/CF/Schedules/DCF
                [aviso] S8 file name BIMBOA_model_v7.xlsx follows the CFA engine convention, not _YYYY-MM-DD_v#
                [n/a] S1, S6, S9 (research-analyst model-spec tabs and sections; the CFA engine uses IS/BS/CF/Schedules tabs)
Contables     : [ok] C1 balance sheet balances (15/15), C2 cash-flow closing cash = balance-sheet cash (10/10),
                C3 equity roll-forward (10/10), C4 PP&E linked to the schedule (Excel = Python total assets),
                C5 interest on opening balances (no circularity, F18), C9 history ties to data/financials.csv
                (total assets 5/5, net income 5/5), C10 opening balances drive interest (graph acyclic)
                [n/a] C6 (no DuPont tab), C7 (days held flat in drivers.yaml; no CCC schedule), C8 (annual model)
Contenido     : [ok] D1 every forecast line has a driver (revenue_growth is an engine default, unused because segments are set),
                D2 FY2027-30 revenue growth 4.4-4.5% vs Bimbo-mix market value growth 4.2% (within 10%),
                D3 peer data as of 16-Oct-2026 (BIMBOA_PeerAnalysis_v3), D6 macro-view updated 2026-10-17,
                D8 every driver tagged with rationale, D9 CFO/NI below 1 only in FY2022 (0.80, Ricolino gain), not two years
                in a row, D10 industry report 2026-10-17
                [aviso] D4 terminal cross-check: the published Gordon value implies 5.21x vs the 6.0x exit; the 6.0x exit
                implies g 5.08% vs 4.25% (valuation/valuation.md section 4)
                [aviso] D4b market-implied g 6.41% vs the 4.25% proposal: a required question for the team
                [aviso] (no number) every macro-view field is status: propuesto (not confirmed by the team)
                [n/a] D5 (no DDM/FCFE/RI), D7 (IFRS issuer; Mexico 3-year CPI 13.09% < 22%)
Formato (F)   : [ok] F1, F4, F6, F8, F9, F14 (n/a), F16, F18 (acyclic), F19 (n/a)
                [x]  F2 font Calibri (house style: Aptos Narrow)
                [x]  F3 font colours FF008000 / FF7F7F7F (green links and grey notes of the CFA engine)
                [x]  F5 number formats outside the whitelist (#,##0.0; 0.0"x"; ...)
                [x]  F7 no row outline grouping
                [x]  F11 / F12 Drivers rows 11 and 26 and DCF row 18 have no history columns (forecast-only by design)
                [x]  F13 the research-analyst ratio set (Spanish labels, DuPont) is not in the Ratios tab
                [x]  F15 CF rows 7-25: the historical cash-flow statement (FY2021-25) is not shown; history lives in
                     data/financials.csv
                [x]  F17 IS!26 and BS!35 are "as reported" tie-out rows (history only by design)
                [aviso] F10 no builder stamp (external model)
                (tools/xlsx_builder.py audit: 9 ok, 10 failures, exit 1)
Resumen: 27 ok · 10 fallas (S5 + 9 F) · 6 avisos · 8 n/a
Veredicto: FALLA
```

## Next action per failure

| Failure | What it means | Suggested action |
|---|---|---|
| S5 DCF!19-20 | Missing `$` anchors on two DCF rows; values are right | Report to the research-challenge plugin maintainer (the engine is not edited in this project). The published DCF (`valuation/BIMBOA_DCF_v3.xlsx`, own builder) is the basis the report quotes |
| F2, F3, F5, F7, F10, F13 | House-style differences between the two plugins | None for valuation integrity. Rebuilding in the research-analyst format would mean a second model; not recommended before the report |
| F11, F12, F17 | Forecast-only or history-only rows by design (DCF periods, driver inputs, reported tie-outs) | None; document in the report appendix if a judge asks |
| F15 | The historical cash-flow statement is not shown in the model | Optional: show FY2021-25 cash flow from `data/financials.csv` in the report appendix |

The accounting and calculation checks are green: the balance sheet balances, cash ties, the equity roll-forward closes, history ties to the filings, the formula graph has no cycle, and an Excel full recalculation reproduces every Python value.
