# data/market

Public market series used for valuation inputs. Read 2026-10-17. Tag: `[sourced]`. Each series was checked against Capital IQ before use.

| File | What | Source | Check |
|---|---|---|---|
| `bimbo_ipc_monthly_2021-11_2026-10.csv` | Month-end closes of BIMBO A (MXN; close and dividend-adjusted close) and the S&P/BMV IPC, Nov-2021 to 16-Oct-2026 (last row is the 16-Oct-2026 close) | Yahoo Finance chart API (`BIMBOA.MX`, `^MXX`), monthly bars | BIMBO A equals the Capital IQ AI month-ends to the cent for Nov-2021 to Aug-2022 and is within 0.53 pesos to Sep-2023 (column `ciq_close_mxn_check`). The ten IPC month-ends of 2026 equal the Capital IQ chart values (`data/capitaliq/capiq-ai-model-gaps-1_2026-10-17.md`). The 16-Oct-2026 close of 58.60 equals the BMV official close |
| `usdmxn_daily_2026-09-15_2026-10-16.csv` | USD/MXN daily close. The bar stamps are UTC as returned (the 23:00 stamps are the start of the next local day) | Yahoo Finance (`MXN=X`) | The Capital IQ chart implies 18.49 on 16-Oct-2026 (BIMBO A MXN 58.60 / USD 3.17); Yahoo closes at 18.479 |

Use: Bimbo's 5-year monthly beta against the IPC (`valuation/build/beta_bimbo.py`), and the USD/MXN rate of the peer workbook. The Capital IQ AI assistant could not return betas, the IPC series or USD/MXN (`capiq-ai-model-gaps-1` and `-2`).
