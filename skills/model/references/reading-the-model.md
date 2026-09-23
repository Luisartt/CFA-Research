# Reading the model

## Never edit the workbook to change an assumption

Change `data/financials.csv`, `model/drivers.yaml` or `valuation/valuation.yaml`
and rebuild. Every build is a new file (`<TICKER>_model_v<N>.xlsx`); old versions
stay. If someone edits inputs in Excel, the parity checks turn to warnings
("stale — rebuild").

## Tabs

| Tab | What it shows |
|---|---|
| Cover | Status (live), how to read the model, engine warnings |
| Drivers | Every assumption: history (black) next to forecast inputs (blue on yellow), with tag, rationale, pillar |
| IS / BS / CF | Three statements; history in blue with the source in the cell comment |
| Schedules | Revenue build, PP&E and intangibles, working capital, debt and revolver, interest |
| Ratios | Margins, returns (ROE, ROIC), leverage, cash conversion cycle |
| WACC / DCF / Comps / Sensitivity / Football | Valuation (only when `valuation.yaml` exists) |
| Checks | Every integrity check by year; OK / ERROR / WARN |

Colors: blue = input or reported figure, black = formula, green = link to another tab.

## When a check is not met

| Check | Usually means | Fix | Where |
|---|---|---|---|
| Balance sheet balances (history) | A reported line was missed or double counted | Re-map the year; tie to reported totals | financials |
| Total assets / net income tie | Mapping differs from the reported total | Find the missing line | financials |
| Segments add up | Segments miss eliminations | Add `seg_eliminations` | financials |
| Balance sheet balances (forecast only) | Inherited from a history gap | Fix history first | financials |
| Cash at or above minimum / revolver not drawn | The plan burns cash: high payout, capex or working capital | Revisit story drivers or accept the borrowing and say so | forecast |
| PP&E stays at or above zero | D&A too high vs capex, or intangible amortization not split out | Set `amort_pct_revenue`, revisit capex/D&A | forecast |
| WACC above g, g below GDP, spread >= 2 pts | Terminal assumptions inconsistent | Lower g or revisit WACC inputs | valuation |
| Terminal value share, methods agree, positive values | Valuation depends on the terminal value or the two methods disagree | Revisit g, exit multiple, final-year margins | valuation |
| Excel matches Python (WARN) | Inputs were edited in Excel | Rebuild | model |
