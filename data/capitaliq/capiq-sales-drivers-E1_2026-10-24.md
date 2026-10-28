# Capital IQ ChatIQ answer - block E1 (United Kingdom, Switzerland, Romania, Serbia)

Prompt: block E1 of `BIMBOA/research/capiq-prompts-sales-drivers_2026-10-24.md` (re-run section).
Run: 2026-10-24 by Jorge Alejandro Gaytan. Pasted verbatim below; table kept tab-separated as returned.

Review notes (AI, 2026-10-24):
- Fills a gap: the first pull (`BIMBOA/research/Informacion_BIMBO_macro.txt`, line 996 on) had only GBR realGDPGrowth, cut off at 2024; CHE, ROU and SRB were missing. GBR realGDPGrowth 2015-2024 matches the first pull.
- The ChatIQ preamble says the table "uses the Standardized series", but most 2015-2025 rows are flagged "As reported ACTUAL". The row-level flag governs, consistent with block X1: history is As reported, forecasts are Standardized.
- realPrivateConsumptionGrowth is flagged "Standardized BEST_OF" for every year, so the field does not say which years are actual and which are forecast. Treat 2026-2030 as forecast by date only; note this when citing.
- populationGrowth 2024-2025 is flagged FORECAST for GBR, CHE and ROU (SRB shows 2024-2025 as ACTUAL). Stored as is; these are completed years still carried as forecasts.
- ROU 2026: realGDPGrowth -0.71 and realPrivateConsumptionGrowth -3.95, both stored Standardized FORECAST. Large but stored values, not errors.
- ROU and SRB nominalGDPLCU use thousand separators ("1,053.19"); the other countries do not. Formatting only.
- The `currency` column on % rows shows the local currency here (N/A in X1). Formatting only.
- No value needed arithmetic; ChatIQ correctly returned N/A for nominal GDP growth. We compute it ourselves as [calc] from nominalGDPLCU.

---

```text
S&P Capital IQ Economic Data — GBR, CHE, ROU, SRB (2015–2030)
Source: S&P Capital IQ (S&P Global Market Intelligence) Data as of: 10/15/2026 (EOP); some periods finalized through 10/21/2026 Note on flags: Values carry the macroDataSource flag exactly as stored. Where a field shows "As reported ACTUAL" and "Standardized ACTUAL" for the same period/indicator, both are stored separately in Capital IQ (the "As reported" variant uses the *AR field suffix). The primary table below uses the Standardized series (which is what the five requested indicators draw from in the primary_indicators dataset); "As reported" variants are noted in the supplemental field list.

Part 1 — Primary Indicators Long Table
Units key: % = percent; £B = GBP billions; SFr.B = CHF billions; LB = Romanian Leu billions; RSDB = Serbian Dinar billions

country_iso3	indicator	unit	currency	year	value	value_type_flag_as_shown	provider	as_of_date
GBR	realGDPGrowth	%	GBP	2015	2.17	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2016	2.22	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2017	3.31	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2018	1.64	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2019	1.39	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2020	-10.05	Standardized ACTUAL	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2021	8.52	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2022	5.02	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2023	0.44	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2024	1.11	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2025	1.21	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2026	1.29	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2027	1.06	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2028	1.54	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2029	1.52	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	realGDPGrowth	%	GBP	2030	1.44	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2015	1928.92	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2016	2005.53	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2017	2102.41	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2018	2178.10	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2019	2263.43	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2020	2131.73	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2021	2332.85	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2022	2590.76	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2023	2766.45	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2024	2904.95	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2025	3044.59	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2026	3163.80	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2027	3274.70	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2028	3403.83	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2029	3543.98	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	nominalGDPLCU	£B	GBP	2030	3688.44	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2015	0.04	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2016	0.66	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2017	2.68	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2018	2.48	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2019	1.79	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2020	0.85	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2021	2.59	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2022	9.07	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2023	7.30	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2024	2.53	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2025	3.37	As reported ACTUAL	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2026	3.11	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2027	3.30	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2028	2.30	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2029	2.31	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	consumerPriceInflation	%	GBP	2030	2.13	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2015	3.07	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2016	3.44	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2017	2.50	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2018	2.11	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2019	1.38	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2020	-12.73	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2021	7.19	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2022	7.57	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2023	-0.67	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2024	0.26	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2025	0.99	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2026	1.14	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2027	0.78	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2028	1.21	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2029	1.48	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	realPrivateConsumptionGrowth	%	GBP	2030	1.46	Standardized BEST_OF	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2015	0.80	Standardized ACTUAL	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2016	0.78	Standardized ACTUAL	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2017	0.70	Standardized ACTUAL	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2018	0.60	Standardized ACTUAL	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2019	0.54	Standardized ACTUAL	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2020	0.36	Standardized ACTUAL	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2021	0.47	Standardized ACTUAL	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2022	0.75	Standardized ACTUAL	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2023	0.74	Standardized ACTUAL	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2024	0.66	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2025	0.60	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2026	0.55	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2027	0.52	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2028	0.50	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2029	0.46	Standardized FORECAST	S&P Capital IQ	10/15/2026
GBR	populationGrowth	%	GBP	2030	0.44	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2015	1.45	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2016	1.91	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2017	1.42	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2018	3.33	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2019	1.12	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2020	-2.33	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2021	6.18	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2022	3.53	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2023	1.00	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2024	1.52	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2025	1.61	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2026	1.82	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2027	1.30	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2028	1.35	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2029	1.42	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	realGDPGrowth	%	CHF	2030	1.15	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2015	679.63	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2016	688.40	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2017	695.84	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2018	724.38	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2019	731.80	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2020	709.85	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2021	768.28	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2022	819.70	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2023	837.16	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2024	860.93	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2025	881.57	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2026	898.56	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2027	921.85	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2028	947.21	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2029	971.37	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	nominalGDPLCU	SFr.B	CHF	2030	991.86	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2015	-1.14	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2016	-0.43	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2017	0.53	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2018	0.94	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2019	0.36	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2020	-0.73	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2021	0.58	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2022	2.84	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2023	2.14	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2024	1.06	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2025	0.15	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2026	0.68	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2027	0.86	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2028	1.04	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2029	0.80	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	consumerPriceInflation	%	CHF	2030	0.75	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2015	2.37	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2016	1.32	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2017	1.45	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2018	0.08	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2019	1.42	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2020	-3.76	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2021	2.17	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2022	4.87	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2023	1.28	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2024	2.06	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2025	1.67	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2026	1.19	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2027	1.46	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2028	1.47	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2029	1.24	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	realPrivateConsumptionGrowth	%	CHF	2030	1.02	Standardized BEST_OF	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2015	1.14	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2016	1.10	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2017	0.94	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2018	0.74	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2019	0.72	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2020	0.74	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2021	0.77	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2022	0.98	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2023	0.89	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2024	0.58	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2025	0.51	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2026	0.45	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2027	0.40	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2028	0.36	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2029	0.31	Standardized FORECAST	S&P Capital IQ	10/15/2026
CHE	populationGrowth	%	CHF	2030	0.28	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2015	3.16	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2016	2.86	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2017	8.20	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2018	5.30	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2019	4.41	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2020	-3.60	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2021	5.94	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2022	4.93	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2023	2.48	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2024	0.53	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2025	0.76	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2026	-0.71	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2027	1.77	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2028	3.04	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2029	3.17	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	realGDPGrowth	%	RON	2030	3.03	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2015	712.55	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2016	752.13	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2017	851.62	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2018	952.39	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2019	1,053.19	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2020	1,056.30	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2021	1,179.83	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2022	1,378.46	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2023	1,587.96	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2024	1,767.52	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2025	1,929.93	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2026	2,096.65	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2027	2,255.59	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2028	2,384.19	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2029	2,560.14	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	nominalGDPLCU	LB	RON	2030	2,743.74	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2015	-0.41	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2016	-1.07	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2017	1.09	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2018	4.07	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2019	3.91	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2020	2.33	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2021	4.11	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2022	12.02	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2023	9.74	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2024	5.85	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2025	6.77	As reported ACTUAL	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2026	7.99	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2027	5.00	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2028	3.40	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2029	3.22	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	consumerPriceInflation	%	RON	2030	2.98	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2015	5.91	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2016	6.04	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2017	11.57	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2018	9.37	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2019	3.13	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2020	-3.62	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2021	6.97	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2022	5.44	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2023	2.52	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2024	5.71	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2025	0.52	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2026	-3.95	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2027	0.85	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2028	2.93	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2029	3.35	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	realPrivateConsumptionGrowth	%	RON	2030	3.01	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2015	-0.49	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2016	-0.47	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2017	-0.44	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2018	-0.46	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2019	-0.49	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2020	-0.56	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2021	-0.74	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2022	-0.42	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2023	-0.25	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2024	-0.54	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2025	-0.56	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2026	-0.57	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2027	-0.58	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2028	-0.59	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2029	-0.60	Standardized FORECAST	S&P Capital IQ	10/15/2026
ROU	populationGrowth	%	RON	2030	-0.60	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2015	1.30	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2016	2.98	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2017	2.36	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2018	4.65	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2019	4.75	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2020	-0.95	Standardized ACTUAL	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2021	7.95	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2022	2.70	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2023	3.75	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2024	3.95	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2025	2.03	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2026	3.38	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2027	3.48	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2028	3.93	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2029	3.65	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	realGDPGrowth	%	RSD	2030	3.64	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2015	4,493.63	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2016	4,698.76	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2017	4,953.98	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2018	5,287.99	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2019	5,669.24	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2020	5,764.15	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2021	6,576.02	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2022	7,460.14	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2023	8,817.91	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2024	9,748.26	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2025	10,392.69	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2026	11,179.15	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2027	11,738.74	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2028	12,379.97	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2029	12,987.74	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	nominalGDPLCU	RSDB	RSD	2030	13,433.30	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2015	1.38	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2016	1.12	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2017	3.17	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2018	1.96	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2019	1.87	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2020	1.54	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2021	4.09	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2022	11.97	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2023	12.36	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2024	4.68	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2025	3.90	As reported ACTUAL	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2026	2.99	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2027	3.20	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2028	3.11	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2029	3.07	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	consumerPriceInflation	%	RSD	2030	2.96	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2015	-0.35	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2016	1.90	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2017	2.15	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2018	2.81	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2019	3.68	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2020	-2.05	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2021	7.72	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2022	3.47	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2023	0.49	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2024	5.19	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2025	3.12	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2026	3.02	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2027	3.31	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2028	3.81	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2029	3.43	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	realPrivateConsumptionGrowth	%	RSD	2030	3.40	Standardized BEST_OF	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2015	-0.51	Standardized ACTUAL	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2016	-0.52	Standardized ACTUAL	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2017	-0.53	Standardized ACTUAL	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2018	-0.54	Standardized ACTUAL	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2019	-0.54	Standardized ACTUAL	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2020	-0.66	Standardized ACTUAL	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2021	-0.94	Standardized ACTUAL	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2022	-2.49	Standardized ACTUAL	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2023	-0.62	Standardized ACTUAL	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2024	-0.55	Standardized ACTUAL	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2025	-0.56	Standardized ACTUAL	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2026	-0.70	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2027	-0.67	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2028	-0.68	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2029	-0.69	Standardized FORECAST	S&P Capital IQ	10/15/2026
SRB	populationGrowth	%	RSD	2030	-0.70	Standardized FORECAST	S&P Capital IQ	10/15/2026
Part 2 — All Other Economic Fields Stored in Capital IQ (Names Only)
The following additional fields are present in the Capital IQ dataset for each of the four countries. Availability varies by country and year; ROU and SRB have somewhat narrower coverage on certain income/household fields.

Standardized series fields:

population
averageMonthlyWages
budgetBalanceGDP
exportedGoods
realGDP
nominalGDP
gdpPerCapita
unemploymentRate
realGovermentConsumptionGrowth
realGrossFixedInvestmentGrowth
currentAccountBalance
averageConsumerPriceIndex
producerPriceInflation
averageProducerPriceIndex
gdpDeflator
publicDebtGDP
interestPaymentGrowth
publicDebt
debtInterestPaymentGDP
foreignDebtGDP
grossDomesticSavings
industrialProductionGrowth
budgetExpenditureGDP
budgetRevenue
personalDisposableIncome (GBR, CHE; null for ROU)
realPersonalDisposableIncome (GBR, CHE; null for ROU)
realPersonalDisposableIncomeGrowth (GBR, CHE; null for ROU)
currentAccountBalanceGDP
importedGoods
directInvestmentBalance
inwardDirectInvestment
outwardDirectInvestment
tradeBalance
realGrossFixedInvestment
moneyMarketInterestRate
bondYield
domesticCreditGrowth
internationalReservesLessGold
interestPaymentGrowthRate
laborForce
laborProductivityGrowth
laborCostChange
averageExchangeRate
exchangeRateEnd
medianHouseholdIncome (GBR, CHE; not present for ROU/SRB in retrieved data)
employment
financialAccountBalance
internationalResLessGoldGDP
realGDPUSD
goldReserves (present for GBR and CHE actuals; null for forecast years and for ROU/SRB)
stockMarketIndex (present for GBR and CHE; not retrieved for ROU/SRB)
foreignDebt (field present but null across all four countries in retrieved data)
externalDebtService (field present but null across all four countries)
grossPersonalIncome (field present but null across all four countries)
economicAsOf
"As reported" variant fields (suffixed AR; available for actual years only where Capital IQ holds a separate as-reported series alongside the standardized series):

realGDPGrowthAR
realGDPAR
realGDPLCUAR
nominalGDPAR
nominalGDPLCUAR
consumerPriceInflationAR
producerPriceInflationAR
industrialProductionGrowthAR
unemploymentRateAR
currentAccountBalanceAR
importedGoodsAR
exportedGoodsAR
tradeBalanceAR
averageExchangeRateAR
Note on nominalGDPGrowth: A nominal GDP growth rate is not a stored field in Capital IQ for these countries — it would require arithmetic derivation from the nominalGDPLCU level series. Per your instruction, N/A — not a stored field.


Disclaimer: Responses in ChatIQ are generated by artificial intelligence without human review. ChatIQ uses generative AI and may produce inaccurate or incomplete responses. You are responsible for verifying all information, and any decisions based on ChatIQ outputs are at your own risk. S&P Global is not liable for any loss or damage resulting from use of ChatIQ. Your questions and chat history are not shared with third parties, except foundation model providers as needed to provide the service, and are not used to train AI models by S&P Global or its providers. Chat history is stored securely and can be deleted anytime in settings. Each conversation is automatically deleted 12 months after you last access it. Your feedback helps us improve ChatIQ's accuracy and completeness.
```
