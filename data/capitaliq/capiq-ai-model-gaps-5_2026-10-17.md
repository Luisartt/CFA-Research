# Capital IQ AI output — model-gaps Prompt 5 (peer market data), pricing date 2026-10-16

_Raw source copy. Pasted by the team on 2026-10-17 from the Capital IQ AI assistant, response to Prompt 5 of `BIMBOA/research/capiq-prompts-model-gaps_2026-10-17.md`, plus the 5-year chart table pasted with it. Text and numbers are as received; tab-separated tables were converted to markdown. This file could not be written to `raw/` (write permission denied); move it there unchanged if you want it in the inbox._

_Use: the chart table gives month-end USD closes for the nine peers to 16-Oct-2026. The BMV:AC column in that table is Arca Continental's own series (USD 11.34 = MXN 209.66 / 18.479), not AON. Price changes over 1, 2, 3 and 5 years computed from it are month-end approximations (base dates 31-Oct-2025, 31-Oct-2024, 31-Oct-2023 and 29-Oct-2021); quarter-to-date and year-to-date use exact base dates (30-Sep-2026 and 31-Dec-2025)._

---

## Important Data Availability Notice

The pricing data retrieval for 10/16/2026 returned no close prices, 52-week high/low, or price change percentages for any of the nine companies. The latest_pricing call returned only market cap (USD), shares outstanding, and total enterprise value — all other pricing fields (close, high, low, all performance periods) came back null. The historical pricing queries (for 1-day, 1-year, 2-year, 3-year, and 5-year lookback dates) returned no data at all.

Additionally: The AC ticker resolved to AON (Aon plc) in the pricing module — not Arca Continental, S.A.B. de C.V. (BMV:AC). Per your instruction, the AON data is excluded; Arca Continental pricing is reported as N/A throughout.

Yamazaki Baking (TSE:2212) returned a NO_DATA error for all pricing fields including market cap and shares outstanding.

The dividend data and the market cap/shares/EV figures were successfully retrieved and are presented below.

## Market Data Table — Pricing Date: 10/16/2026

All price and performance columns are N/A — no pricing data was returned for any entity for this date. Market cap and shares outstanding are sourced from the latest available data in S&P Capital IQ. Dividend figures are in USD as returned by S&P Capital IQ Financials. Local trading currency applies where noted.

Entity note — Arca Continental: Ticker AC resolved to AON (Aon plc) in the pricing module; all Arca Continental pricing fields are N/A. Market cap and shares outstanding for Arca Continental are excluded from this table as the returned figures belong to AON.

| | Flowers Foods | Gruma | Yamazaki Baking | ARYZTA AG | J. M. Smucker | Campbell's | Mondelez | Arca Continental | PepsiCo |
|---|---|---|---|---|---|---|---|---|---|
| Ticker | NYSE:FLO | BMV:GRUMA B | TSE:2212 | SWX:ARYN | NYSE:SJM | NasdaqGS:CPB | NasdaqGS:MDLZ | BMV:AC | NasdaqGS:PEP |
| Close Price – 10/16/2026 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 52-Week High | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 52-Week Low | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 1-Day Price Chg % | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 1-Year Price Chg % | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 2-Year Price Chg % | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 3-Year Price Chg % | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 5-Year Price Chg % | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| Quarter-to-Date Chg % | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| Year-to-Date Chg % | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| DPS – Last 12 Months (USD) | $0.87 | $0.32 | $0.39 | N/A | $4.42 | $1.56 | $2.00 | $0.24 | $5.81 |
| DPS – FY2024 (USD) | $0.95 | $0.28 | $0.30 | N/A | $4.24 | $1.48 | $1.79 | $0.23 | $5.33 |
| DPS – FY2025 (USD) | $0.98 | $0.32 | $0.40 | N/A | $4.32 | $1.54 | $1.94 | $0.22 | $5.62 |
| Shares Outstanding (M) | 212.1 | 332.6 | N/A | 24.8 | 106.8 | 298.2 | 1,276.3 | N/A ¹ | 1,362.7 |
| Market Cap (USD M) | $1,295.7 | $4,355.1 | N/A | $1,218.8 | $13,612.5 | $5,925.9 | $81,568.8 | N/A ¹ | $179,186.8 |

¹ Arca Continental: ticker AC resolved to Aon plc (AON) in the pricing module; figures excluded per your instruction.

### LTM Dividend Period-End Dates

For reference, the LTM dividend per share figures use the following period-end dates (as reported by S&P Capital IQ):

| Company | LTM Period End |
|---|---|
| Flowers Foods | 07/18/2026 |
| J. M. Smucker | 07/31/2026 |
| Campbell's | 08/02/2026 |
| PepsiCo | 09/05/2026 |
| Gruma, Yamazaki, ARYZTA, Arca Continental, Mondelez | 06/30/2026 |

## Items Not Retrieved

- Close price on 10/16/2026 — Returned null for all nine companies. No pricing data was available for the requested date.
- 52-week high and 52-week low — Returned null for all companies.
- All price change percentages (1-day, 1-year, 2-year, 3-year, 5-year, QTD, YTD) — Returned null for all companies; historical pricing queries also returned no data.
- Yamazaki Baking (TSE:2212) — all market data — Returned a NO_DATA error; shares outstanding and market cap also unavailable.
- Arca Continental (BMV:AC) — pricing module — Ticker AC resolved to Aon plc (AON), not Arca Continental. All pricing, shares outstanding, and market cap figures for Arca Continental are excluded.
- ARYZTA AG — dividends per share — Returned N/A for LTM, FY2024, and FY2025 (ARYZTA does not pay a dividend per S&P Capital IQ data).
- FY2026 DPS — Not yet complete for most companies (fiscal years still open); shown as N/A in the annual dividend data and therefore excluded from the table. Exception: J. M. Smucker (FY ending April 2026) shows $4.40 and Campbell's (FY ending August 2026) shows $1.56 — these are captured in the FY2025 column above as the most recently completed fiscal year per each company's fiscal calendar.

A 5-year share price chart for all nine companies is shown below.

## Chart table pasted with the output (Symbol: FLO; month-end share prices in USD)

| Date | NYSE:FLO | NASDAQGS:CPB | NYSE:SJM | BMV:AC * | TSE:2212 | NASDAQGS:MDLZ | BMV:GRUMA B | NASDAQGS:PEP | SWX:ARYN |
|---|---|---|---|---|---|---|---|---|---|
| 10/16/2026 | $6.11 | $19.87 | $127.43 | $11.34 | $24.17 | $63.91 | $13.09 | $131.49 | $49.10 |
| 09/30/2026 | $5.55 | $19.83 | $118.91 | $10.74 | $22.95 | $57.82 | $13.03 | $126.72 | $45.49 |
| 08/31/2026 | $6.92 | $23.68 | $131.16 | $11.44 | $23.17 | $62.07 | $14.52 | $140.34 | $50.90 |
| 07/31/2026 | $7.02 | $21.98 | $119.26 | $11.45 | $21.08 | $62.31 | $14.89 | $139.56 | $65.50 |
| 06/30/2026 | $7.90 | $22.27 | $112.50 | $11.99 | $19.73 | $57.84 | $16.08 | $135.40 | $69.43 |
| 05/29/2026 | $7.64 | $21.11 | $103.20 | $12.98 | $19.68 | $61.17 | $16.76 | $144.19 | $78.04 |
| 04/30/2026 | $9.06 | $20.79 | $98.03 | $11.98 | $20.93 | $61.44 | $17.30 | $158.49 | $79.80 |
| 03/31/2026 | $8.15 | $22.27 | $96.44 | $11.47 | $22.30 | $57.64 | $18.23 | $155.29 | $77.36 |
| 02/27/2026 | $9.88 | $26.95 | $115.95 | $12.05 | $22.48 | $61.58 | $17.94 | $169.74 | $72.18 |
| 01/30/2026 | $11.43 | $27.98 | $104.86 | $11.36 | $21.15 | $58.47 | $18.15 | $153.63 | $70.88 |
| 12/31/2025 | $10.88 | $27.87 | $97.81 | $10.82 | $21.07 | $53.83 | $17.23 | $143.52 | $65.20 |
| 11/28/2025 | $10.73 | $30.48 | $104.18 | $10.20 | $20.98 | $57.57 | $17.68 | $148.74 | $62.70 |
| 10/31/2025 | $11.93 | $30.13 | $103.55 | $9.69 | $19.59 | $57.46 | $16.99 | $146.09 | $64.11 |
| 09/30/2025 | $13.05 | $31.58 | $108.60 | $10.47 | $22.24 | $62.47 | $18.54 | $140.44 | $81.39 |
| 08/29/2025 | $15.04 | $31.93 | $110.51 | $10.21 | $23.25 | $61.44 | $17.21 | $148.65 | $92.06 |
| 07/31/2025 | $15.85 | $31.92 | $107.34 | $10.46 | $21.58 | $64.69 | $17.34 | $137.92 | $94.42 |
| 06/30/2025 | $15.98 | $30.65 | $98.20 | $10.52 | $22.38 | $67.44 | $17.17 | $132.04 | $101.66 |
| 05/30/2025 | $16.90 | $34.04 | $112.61 | $11.00 | $22.57 | $67.49 | $18.85 | $131.45 | $103.13 |
| 04/30/2025 | $17.59 | $36.46 | $116.27 | $10.53 | $23.92 | $68.13 | $19.13 | $135.58 | $100.31 |
| 03/31/2025 | $19.01 | $39.92 | $118.41 | $10.47 | $19.23 | $67.85 | $18.08 | $149.94 | $88.74 |
| 02/28/2025 | $18.74 | $40.06 | $110.53 | $10.34 | $18.00 | $64.23 | $17.29 | $153.47 | $82.33 |
| 01/31/2025 | $19.55 | $38.77 | $106.89 | $9.17 | $18.07 | $57.99 | $17.39 | $150.69 | $79.53 |
| 12/31/2024 | $20.66 | $41.88 | $110.12 | $8.29 | $18.73 | $59.73 | $15.64 | $152.06 | $69.90 |
| 11/29/2024 | $22.62 | $46.20 | $117.79 | $8.47 | $18.73 | $64.95 | $16.99 | $163.45 | $69.49 |
| 10/31/2024 | $22.23 | $46.65 | $113.51 | $8.55 | $20.42 | $68.48 | $17.24 | $166.08 | $70.57 |
| 09/30/2024 | $23.07 | $48.92 | $121.10 | $9.40 | $19.86 | $73.67 | $18.67 | $170.05 | $76.76 |
| 08/30/2024 | $23.24 | $49.72 | $114.68 | $8.98 | $18.51 | $71.81 | $18.41 | $172.88 | $80.93 |
| 07/31/2024 | $22.52 | $46.86 | $117.95 | $9.85 | $24.72 | $68.35 | $18.71 | $172.67 | $76.59 |
| 06/28/2024 | $22.20 | $45.19 | $109.04 | $9.82 | $20.53 | $65.44 | $18.27 | $164.93 | $71.22 |
| 05/31/2024 | $23.22 | $44.38 | $111.64 | $10.16 | $21.99 | $68.53 | $19.32 | $172.90 | $79.86 |
| 04/30/2024 | $24.94 | $45.71 | $114.85 | $9.81 | $24.22 | $71.94 | $19.74 | $175.91 | $76.14 |
| 03/29/2024 | $23.75 | $44.45 | $125.87 | $10.98 | $25.92 | $70.00 | $18.80 | $175.01 | $72.70 |
| 02/29/2024 | $22.42 | $42.64 | $120.17 | $10.76 | $23.52 | $73.07 | $17.79 | $165.34 | $70.86 |
| 01/31/2024 | $22.80 | $44.63 | $131.55 | $11.39 | $23.89 | $75.27 | $18.77 | $168.53 | $72.34 |
| 12/29/2023 | $22.51 | $43.23 | $126.38 | $10.97 | $22.81 | $72.43 | $18.40 | $169.84 | $73.72 |
| 11/30/2023 | $20.81 | $40.18 | $109.73 | $10.22 | $21.89 | $71.06 | $18.54 | $168.29 | $73.89 |
| 10/31/2023 | $21.93 | $40.41 | $113.84 | $8.94 | $21.15 | $66.21 | $17.35 | $163.28 | $73.12 |
| 09/29/2023 | $22.18 | $41.08 | $122.91 | $9.09 | $18.40 | $69.40 | $17.14 | $169.44 | $68.58 |
| 08/31/2023 | $23.56 | $41.70 | $144.95 | $9.83 | $18.95 | $71.26 | $16.86 | $177.92 | $66.57 |
| 07/31/2023 | $24.71 | $45.82 | $150.65 | $10.03 | $14.44 | $74.13 | $17.96 | $187.46 | $68.62 |
| 06/30/2023 | $24.88 | $45.71 | $147.67 | $10.26 | $13.49 | $72.94 | $16.02 | $185.22 | $66.33 |
| 05/31/2023 | $24.98 | $50.55 | $146.59 | $10.08 | $14.37 | $73.41 | $15.33 | $182.35 | $63.69 |
| 04/28/2023 | $27.51 | $54.30 | $154.41 | $9.50 | $13.41 | $76.72 | $15.63 | $190.89 | $71.15 |
| 03/31/2023 | $27.41 | $54.98 | $157.37 | $9.07 | $12.07 | $69.72 | $14.74 | $182.30 | $67.94 |
| 02/28/2023 | $27.88 | $52.52 | $147.89 | $8.42 | $11.61 | $65.18 | $14.62 | $173.53 | $55.62 |
| 01/31/2023 | $27.69 | $51.93 | $152.80 | $8.85 | $11.69 | $65.44 | $14.57 | $171.02 | $54.36 |
| 12/30/2022 | $28.74 | $56.75 | $158.46 | $8.11 | $11.94 | $66.65 | $13.37 | $180.66 | $47.63 |
| 11/30/2022 | $30.05 | $53.67 | $154.01 | $8.30 | $11.35 | $67.61 | $12.42 | $185.51 | $48.55 |
| 10/31/2022 | $28.71 | $52.91 | $150.66 | $8.18 | $10.19 | $61.48 | $11.59 | $181.58 | $40.99 |
| 09/30/2022 | $24.69 | $47.12 | $137.41 | $7.22 | $11.49 | $54.83 | $9.60 | $163.26 | $40.65 |
| 08/31/2022 | $27.30 | $50.38 | $139.99 | $6.83 | $11.82 | $61.86 | $10.93 | $172.27 | $47.06 |
| 07/29/2022 | $28.41 | $49.35 | $132.32 | $6.94 | $12.05 | $64.04 | $12.46 | $174.96 | $45.54 |
| 06/30/2022 | $26.32 | $48.05 | $128.01 | $6.57 | $12.19 | $62.09 | $11.04 | $166.66 | $44.45 |
| 05/31/2022 | $27.60 | $47.91 | $125.37 | $6.78 | $11.65 | $63.56 | $11.85 | $167.75 | $43.38 |
| 04/29/2022 | $26.52 | $47.22 | $136.93 | $6.35 | $12.28 | $64.48 | $11.89 | $171.71 | $37.52 |
| 03/31/2022 | $25.71 | $44.57 | $135.41 | $6.79 | $12.34 | $62.78 | $12.55 | $167.38 | $41.26 |
| 02/28/2022 | $27.41 | $44.97 | $134.75 | $6.61 | $13.51 | $65.48 | $13.59 | $163.74 | $45.57 |
| 01/31/2022 | $28.13 | $44.12 | $140.58 | $5.91 | $14.24 | $67.03 | $13.06 | $173.52 | $45.32 |
| 12/31/2021 | $27.47 | $43.46 | $135.82 | $6.37 | $13.27 | $66.31 | $12.81 | $173.71 | $49.93 |
| 11/30/2021 | $25.82 | $40.33 | $126.47 | $6.10 | $13.01 | $58.94 | $12.12 | $159.78 | $46.64 |
| 10/29/2021 | $24.75 | $39.95 | $122.86 | $6.11 | $15.17 | $60.74 | $11.76 | $161.60 | $52.22 |
