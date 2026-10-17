# Capital IQ prompt: peer market data for the Financials & Peer Analysis template (2026-10-17)

> Superseded the same day by `capiq-prompts-model-gaps_2026-10-17.md`, which splits this prompt into prompts 5 and 6 (shorter prompts fail less often) and adds five more.

The fields below are blank (shaded "pending CIQ refresh") in `valuation/BIMBOA_PeerAnalysis_v2.xlsx` because the local data does not have them. Paste the prompt into the Capital IQ AI assistant (about 2,400 characters). Alternatively, refresh `valuation/SPG_FinancialsAndPeerAnalysis_VA_v1.xlsx` with the CIQ Excel plugin and send the result back.

In the last pull, BMV tickers did not resolve in the AI assistant: Bimbo came back as "Bmvb Immo", Gruma as "Bevgru Ab", and Arca as AON. For those three, the Excel plugin or a search by full company name is safer.

---

```
CFA Research Challenge - Grupo Bimbo peer set. Pricing date: 16-Oct-2026. Return values exactly as in S&P Capital IQ, with the field name, period, currency and as-of date for every number. Write N/A when a value is not available; never estimate.

Companies (resolve by full name if a ticker fails, and state the entity you used):
1 Grupo Bimbo, S.A.B. de C.V. (BMV:BIMBO A)
2 Flowers Foods, Inc. (NYSE:FLO)
3 Gruma, S.A.B. de C.V. (BMV:GRUMA B)
4 Yamazaki Baking Co., Ltd. (TSE:2212)
5 ARYZTA AG (SWX:ARYN)
6 The J. M. Smucker Company (NYSE:SJM)
7 The Campbell's Company (NasdaqGS:CPB)
8 Mondelez International, Inc. (NasdaqGS:MDLZ)
9 Arca Continental, S.A.B. de C.V. (BMV:AC)
10 PepsiCo, Inc. (NasdaqGS:PEP)

TASK A - Market data (local trading currency), one row per company:
close price 16-Oct-2026; 52-week high; 52-week low; price change % for 1 day, 1 year, 2 years, 3 years, 5 years, quarter-to-date and year-to-date (all ending 16-Oct-2026); dividends per share for the last 12 months, FY2024 and FY2025; shares outstanding; market cap (USD m).

TASK B - Gross profit (USD m, CIQ standardized): FY2024, FY2025 and LTM (state the LTM end date). If available, consensus mean gross profit for FY1, FY2 and FY3, with the fiscal year each one refers to.

TASK C - Free cash flow (USD m): levered free cash flow FY2024, FY2025 and LTM (CIQ definition); consensus mean free cash flow for FY1, FY2 and FY3 (state the fiscal year).

Output: three markdown tables (Task A, B, C). Columns: company, ticker, field, period, value, currency, as-of date, source. After the tables, list anything that could not be retrieved.
```
