# Capital IQ ChatIQ answer - block E2 (Slovenia, Croatia, Montenegro, North Macedonia)

Prompt: block E2 of `BIMBOA/research/capiq-prompts-sales-drivers_2026-10-24.md` (re-run section).
Run: 2026-10-24 by Jorge Alejandro Gaytan. Pasted verbatim below; table kept tab-separated as returned.

Review notes (AI, 2026-10-24):
- New coverage: none of these four countries appears in the first pull (`BIMBOA/research/Informacion_BIMBO_macro.txt`).
- **HRV unit label [unverified].** nominalGDPLCU is labelled "knB" (Croatian kuna billions), but Croatia replaced the kuna with the euro on 2023-01-01, and the stored levels (45.97 in 2015 to 121.25 in 2030) look like euro billions, not kuna. Confirm the unit in Capital IQ before using the level. The growth rate we compute ([calc]) is the same in either unit as long as the whole series uses one unit, but the label must be fixed before any value is cited.
- **SVN 2025 nominalGDPLCU.** ChatIQ says two of its own queries return different flags for this cell ("As reported ACTUAL" vs "Standardized ACTUAL") and promises footnotes for any differing values. No footnotes were returned. We keep 71.17 as shown; [unverified] until checked in the Capital IQ screen.
- **Vintages.** MNE and MKD are dated 08/25/2026 for every year, forecasts included. SVN and HRV history is dated 08/18/2026 and their forecasts 10/15/2026.
- **Population.** populationGrowth 2024-2025 is still flagged FORECAST for SVN, HRV and MKD, as in E1. MNE goes from +0.14 (2026) to -0.54 (2027); both are stored values.
- realPrivateConsumptionGrowth is flagged "Standardized BEST_OF" for every year (no actual/forecast split), as in E1.
- No value needed arithmetic. Nominal GDP growth will be computed by us as [calc] from nominalGDPLCU.

---

```text
S&P Capital IQ Economic Data — SVN, HRV, MNE, MKD (2015–2030)
Part 1 — Long Table: Five Requested Indicators
Notes on flags: The value_type_flag_as_shown column reproduces the macroDataSource string exactly as stored. For realPrivateConsumptionGrowth, the flag is always "Standardized BEST_OF" across all countries and years — this is how Capital IQ stores it, regardless of whether the underlying period is an actual or forecast year. The nominalGDPLCU flag for SVN 2025 is shown as stored in the specific_mnemonics_data query ("As reported ACTUAL"); note the all_indicators_data query returns "Standardized ACTUAL" for the same cell — both values are present in the context; the "As reported ACTUAL" version (71.17 €B) is used below as it matches the primary five-indicator pull. Where two queries return slightly different values for the same cell, both are noted in footnotes.

Source: S&P Capital IQ Currency (nominalGDPLCU): local currency as stored — €B for SVN and MNE; knB (Croatian kuna billions) for HRV; MKDB (Macedonian denar billions) for MKD. Provider: S&P Global Market Intelligence As-of dates: per economicAsOfEOP field shown in column.

country_iso3	indicator	unit	currency	year	value	value_type_flag_as_shown	as_of_date
SVN	realGDPGrowth	%	N/A	2015	2.39	As reported ACTUAL	08/18/2026
SVN	realGDPGrowth	%	N/A	2016	3.03	As reported ACTUAL	08/18/2026
SVN	realGDPGrowth	%	N/A	2017	5.17	As reported ACTUAL	08/18/2026
SVN	realGDPGrowth	%	N/A	2018	4.38	As reported ACTUAL	08/18/2026
SVN	realGDPGrowth	%	N/A	2019	3.51	As reported ACTUAL	08/18/2026
SVN	realGDPGrowth	%	N/A	2020	-4.43	Standardized ACTUAL	08/18/2026
SVN	realGDPGrowth	%	N/A	2021	8.42	As reported ACTUAL	08/18/2026
SVN	realGDPGrowth	%	N/A	2022	2.63	As reported ACTUAL	08/18/2026
SVN	realGDPGrowth	%	N/A	2023	2.63	As reported ACTUAL	08/18/2026
SVN	realGDPGrowth	%	N/A	2024	2.03	As reported ACTUAL	08/18/2026
SVN	realGDPGrowth	%	N/A	2025	1.54	As reported ACTUAL	08/18/2026
SVN	realGDPGrowth	%	N/A	2026	2.82	Standardized FORECAST	10/15/2026
SVN	realGDPGrowth	%	N/A	2027	2.18	Standardized FORECAST	10/15/2026
SVN	realGDPGrowth	%	N/A	2028	2.21	Standardized FORECAST	10/15/2026
SVN	realGDPGrowth	%	N/A	2029	2.18	Standardized FORECAST	10/15/2026
SVN	realGDPGrowth	%	N/A	2030	2.29	Standardized FORECAST	10/15/2026
SVN	nominalGDPLCU	€B	EUR	2015	38.49	As reported ACTUAL	08/18/2026
SVN	nominalGDPLCU	€B	EUR	2016	40.01	As reported ACTUAL	08/18/2026
SVN	nominalGDPLCU	€B	EUR	2017	42.63	As reported ACTUAL	08/18/2026
SVN	nominalGDPLCU	€B	EUR	2018	45.46	As reported ACTUAL	08/18/2026
SVN	nominalGDPLCU	€B	EUR	2019	48.16	As reported ACTUAL	08/18/2026
SVN	nominalGDPLCU	€B	EUR	2020	46.74	As reported ACTUAL	08/18/2026
SVN	nominalGDPLCU	€B	EUR	2021	52.03	As reported ACTUAL	08/18/2026
SVN	nominalGDPLCU	€B	EUR	2022	56.90	As reported ACTUAL	08/18/2026
SVN	nominalGDPLCU	€B	EUR	2023	64.12	As reported ACTUAL	08/18/2026
SVN	nominalGDPLCU	€B	EUR	2024	67.48	As reported ACTUAL	08/18/2026
SVN	nominalGDPLCU	€B	EUR	2025	71.17	As reported ACTUAL	08/18/2026
SVN	nominalGDPLCU	€B	EUR	2026	74.76	Standardized FORECAST	10/15/2026
SVN	nominalGDPLCU	€B	EUR	2027	79.67	Standardized FORECAST	10/15/2026
SVN	nominalGDPLCU	€B	EUR	2028	83.82	Standardized FORECAST	10/15/2026
SVN	nominalGDPLCU	€B	EUR	2029	88.13	Standardized FORECAST	10/15/2026
SVN	nominalGDPLCU	€B	EUR	2030	92.64	Standardized FORECAST	10/15/2026
SVN	consumerPriceInflation	%	N/A	2015	-0.76	Standardized ACTUAL	08/18/2026
SVN	consumerPriceInflation	%	N/A	2016	-0.16	Standardized ACTUAL	08/18/2026
SVN	consumerPriceInflation	%	N/A	2017	1.56	As reported ACTUAL	08/18/2026
SVN	consumerPriceInflation	%	N/A	2018	1.93	As reported ACTUAL	08/18/2026
SVN	consumerPriceInflation	%	N/A	2019	1.69	As reported ACTUAL	08/18/2026
SVN	consumerPriceInflation	%	N/A	2020	-0.27	Standardized ACTUAL	08/18/2026
SVN	consumerPriceInflation	%	N/A	2021	2.05	As reported ACTUAL	08/18/2026
SVN	consumerPriceInflation	%	N/A	2022	9.32	As reported ACTUAL	08/18/2026
SVN	consumerPriceInflation	%	N/A	2023	7.22	As reported ACTUAL	08/18/2026
SVN	consumerPriceInflation	%	N/A	2024	1.99	As reported ACTUAL	08/18/2026
SVN	consumerPriceInflation	%	N/A	2025	2.48	As reported ACTUAL	08/18/2026
SVN	consumerPriceInflation	%	N/A	2026	3.48	Standardized FORECAST	10/15/2026
SVN	consumerPriceInflation	%	N/A	2027	3.18	Standardized FORECAST	10/15/2026
SVN	consumerPriceInflation	%	N/A	2028	2.43	Standardized FORECAST	10/15/2026
SVN	consumerPriceInflation	%	N/A	2029	2.39	Standardized FORECAST	10/15/2026
SVN	consumerPriceInflation	%	N/A	2030	2.14	Standardized FORECAST	10/15/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2015	2.24	Standardized BEST_OF	08/18/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2016	4.00	Standardized BEST_OF	08/18/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2017	2.70	Standardized BEST_OF	08/18/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2018	3.39	Standardized BEST_OF	08/18/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2019	5.07	Standardized BEST_OF	08/18/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2020	-5.96	Standardized BEST_OF	08/18/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2021	10.96	Standardized BEST_OF	08/18/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2022	4.06	Standardized BEST_OF	08/18/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2023	0.17	Standardized BEST_OF	08/18/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2024	3.44	Standardized BEST_OF	08/18/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2025	1.70	Standardized BEST_OF	08/18/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2026	2.40	Standardized BEST_OF	10/15/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2027	2.32	Standardized BEST_OF	10/15/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2028	2.66	Standardized BEST_OF	10/15/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2029	2.90	Standardized BEST_OF	10/15/2026
SVN	realPrivateConsumptionGrowth	%	N/A	2030	2.80	Standardized BEST_OF	10/15/2026
SVN	populationGrowth	%	N/A	2015	0.29	Standardized ACTUAL	08/18/2026
SVN	populationGrowth	%	N/A	2016	0.44	Standardized ACTUAL	08/18/2026
SVN	populationGrowth	%	N/A	2017	0.40	Standardized ACTUAL	08/18/2026
SVN	populationGrowth	%	N/A	2018	0.36	Standardized ACTUAL	08/18/2026
SVN	populationGrowth	%	N/A	2019	0.33	Standardized ACTUAL	08/18/2026
SVN	populationGrowth	%	N/A	2020	0.22	Standardized ACTUAL	08/18/2026
SVN	populationGrowth	%	N/A	2021	0.08	Standardized ACTUAL	08/18/2026
SVN	populationGrowth	%	N/A	2022	0.02	Standardized ACTUAL	08/18/2026
SVN	populationGrowth	%	N/A	2023	-0.01	Standardized ACTUAL	08/18/2026
SVN	populationGrowth	%	N/A	2024	-0.03	Standardized FORECAST	08/18/2026
SVN	populationGrowth	%	N/A	2025	-0.06	Standardized FORECAST	08/18/2026
SVN	populationGrowth	%	N/A	2026	-0.08	Standardized FORECAST	10/15/2026
SVN	populationGrowth	%	N/A	2027	-0.10	Standardized FORECAST	10/15/2026
SVN	populationGrowth	%	N/A	2028	-0.11	Standardized FORECAST	10/15/2026
SVN	populationGrowth	%	N/A	2029	-0.13	Standardized FORECAST	10/15/2026
SVN	populationGrowth	%	N/A	2030	-0.14	Standardized FORECAST	10/15/2026
HRV	realGDPGrowth	%	N/A	2015	2.32	As reported ACTUAL	08/18/2026
HRV	realGDPGrowth	%	N/A	2016	3.47	As reported ACTUAL	08/18/2026
HRV	realGDPGrowth	%	N/A	2017	3.28	As reported ACTUAL	08/18/2026
HRV	realGDPGrowth	%	N/A	2018	2.91	As reported ACTUAL	08/18/2026
HRV	realGDPGrowth	%	N/A	2019	3.10	As reported ACTUAL	08/18/2026
HRV	realGDPGrowth	%	N/A	2020	-8.31	Standardized ACTUAL	08/18/2026
HRV	realGDPGrowth	%	N/A	2021	12.63	As reported ACTUAL	08/18/2026
HRV	realGDPGrowth	%	N/A	2022	7.29	As reported ACTUAL	08/18/2026
HRV	realGDPGrowth	%	N/A	2023	3.76	As reported ACTUAL	08/18/2026
HRV	realGDPGrowth	%	N/A	2024	3.83	As reported ACTUAL	08/18/2026
HRV	realGDPGrowth	%	N/A	2025	3.40	As reported ACTUAL	08/18/2026
HRV	realGDPGrowth	%	N/A	2026	2.34	Standardized FORECAST	10/15/2026
HRV	realGDPGrowth	%	N/A	2027	2.46	Standardized FORECAST	10/15/2026
HRV	realGDPGrowth	%	N/A	2028	2.59	Standardized FORECAST	10/15/2026
HRV	realGDPGrowth	%	N/A	2029	2.82	Standardized FORECAST	10/15/2026
HRV	realGDPGrowth	%	N/A	2030	2.81	Standardized FORECAST	10/15/2026
HRV	nominalGDPLCU	knB	HRK	2015	45.97	As reported ACTUAL	08/18/2026
HRV	nominalGDPLCU	knB	HRK	2016	47.57	As reported ACTUAL	08/18/2026
HRV	nominalGDPLCU	knB	HRK	2017	49.73	As reported ACTUAL	08/18/2026
HRV	nominalGDPLCU	knB	HRK	2018	52.22	As reported ACTUAL	08/18/2026
HRV	nominalGDPLCU	knB	HRK	2019	54.91	As reported ACTUAL	08/18/2026
HRV	nominalGDPLCU	knB	HRK	2020	50.74	As reported ACTUAL	08/18/2026
HRV	nominalGDPLCU	knB	HRK	2021	58.34	As reported ACTUAL	08/18/2026
HRV	nominalGDPLCU	knB	HRK	2022	67.61	As reported ACTUAL	08/18/2026
HRV	nominalGDPLCU	knB	HRK	2023	79.19	As reported ACTUAL	08/18/2026
HRV	nominalGDPLCU	knB	HRK	2024	85.91	As reported ACTUAL	08/18/2026
HRV	nominalGDPLCU	knB	HRK	2025	92.98	As reported ACTUAL	08/18/2026
HRV	nominalGDPLCU	knB	HRK	2026	99.07	Standardized FORECAST	10/15/2026
HRV	nominalGDPLCU	knB	HRK	2027	104.63	Standardized FORECAST	10/15/2026
HRV	nominalGDPLCU	knB	HRK	2028	110.00	Standardized FORECAST	10/15/2026
HRV	nominalGDPLCU	knB	HRK	2029	115.71	Standardized FORECAST	10/15/2026
HRV	nominalGDPLCU	knB	HRK	2030	121.25	Standardized FORECAST	10/15/2026
HRV	consumerPriceInflation	%	N/A	2015	-0.26	Standardized ACTUAL	08/18/2026
HRV	consumerPriceInflation	%	N/A	2016	-0.63	Standardized ACTUAL	08/18/2026
HRV	consumerPriceInflation	%	N/A	2017	1.30	As reported ACTUAL	08/18/2026
HRV	consumerPriceInflation	%	N/A	2018	1.56	As reported ACTUAL	08/18/2026
HRV	consumerPriceInflation	%	N/A	2019	0.79	As reported ACTUAL	08/18/2026
HRV	consumerPriceInflation	%	N/A	2020	0.02	As reported ACTUAL	08/18/2026
HRV	consumerPriceInflation	%	N/A	2021	2.68	As reported ACTUAL	08/18/2026
HRV	consumerPriceInflation	%	N/A	2022	10.66	As reported ACTUAL	08/18/2026
HRV	consumerPriceInflation	%	N/A	2023	8.40	As reported ACTUAL	08/18/2026
HRV	consumerPriceInflation	%	N/A	2024	4.02	As reported ACTUAL	08/18/2026
HRV	consumerPriceInflation	%	N/A	2025	4.38	As reported ACTUAL	08/18/2026
HRV	consumerPriceInflation	%	N/A	2026	4.13	Standardized FORECAST	10/15/2026
HRV	consumerPriceInflation	%	N/A	2027	2.96	Standardized FORECAST	10/15/2026
HRV	consumerPriceInflation	%	N/A	2028	2.39	Standardized FORECAST	10/15/2026
HRV	consumerPriceInflation	%	N/A	2029	2.25	Standardized FORECAST	10/15/2026
HRV	consumerPriceInflation	%	N/A	2030	2.01	Standardized FORECAST	10/15/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2015	0.18	Standardized BEST_OF	08/18/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2016	3.09	Standardized BEST_OF	08/18/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2017	3.21	Standardized BEST_OF	08/18/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2018	3.32	Standardized BEST_OF	08/18/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2019	3.97	Standardized BEST_OF	08/18/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2020	-5.19	Standardized BEST_OF	08/18/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2021	10.86	Standardized BEST_OF	08/18/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2022	6.93	Standardized BEST_OF	08/18/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2023	3.22	Standardized BEST_OF	08/18/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2024	5.91	Standardized BEST_OF	08/18/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2025	2.51	Standardized BEST_OF	08/18/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2026	1.75	Standardized BEST_OF	10/15/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2027	2.41	Standardized BEST_OF	10/15/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2028	2.38	Standardized BEST_OF	10/15/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2029	2.32	Standardized BEST_OF	10/15/2026
HRV	realPrivateConsumptionGrowth	%	N/A	2030	2.40	Standardized BEST_OF	10/15/2026
HRV	populationGrowth	%	N/A	2015	-0.68	Standardized ACTUAL	08/18/2026
HRV	populationGrowth	%	N/A	2016	-0.73	Standardized ACTUAL	08/18/2026
HRV	populationGrowth	%	N/A	2017	-0.74	Standardized ACTUAL	08/18/2026
HRV	populationGrowth	%	N/A	2018	-0.76	Standardized ACTUAL	08/18/2026
HRV	populationGrowth	%	N/A	2019	-0.74	Standardized ACTUAL	08/18/2026
HRV	populationGrowth	%	N/A	2020	-0.80	Standardized ACTUAL	08/18/2026
HRV	populationGrowth	%	N/A	2021	-0.90	Standardized ACTUAL	08/18/2026
HRV	populationGrowth	%	N/A	2022	-0.73	Standardized ACTUAL	08/18/2026
HRV	populationGrowth	%	N/A	2023	-0.54	Standardized ACTUAL	08/18/2026
HRV	populationGrowth	%	N/A	2024	-0.55	Standardized FORECAST	08/18/2026
HRV	populationGrowth	%	N/A	2025	-0.56	Standardized FORECAST	08/18/2026
HRV	populationGrowth	%	N/A	2026	-0.57	Standardized FORECAST	10/15/2026
HRV	populationGrowth	%	N/A	2027	-0.57	Standardized FORECAST	10/15/2026
HRV	populationGrowth	%	N/A	2028	-0.58	Standardized FORECAST	10/15/2026
HRV	populationGrowth	%	N/A	2029	-0.59	Standardized FORECAST	10/15/2026
HRV	populationGrowth	%	N/A	2030	-0.60	Standardized FORECAST	10/15/2026
MNE	realGDPGrowth	%	N/A	2015	2.52	As reported ACTUAL	08/25/2026
MNE	realGDPGrowth	%	N/A	2016	3.44	As reported ACTUAL	08/25/2026
MNE	realGDPGrowth	%	N/A	2017	3.22	As reported ACTUAL	08/25/2026
MNE	realGDPGrowth	%	N/A	2018	4.73	As reported ACTUAL	08/25/2026
MNE	realGDPGrowth	%	N/A	2019	4.39	As reported ACTUAL	08/25/2026
MNE	realGDPGrowth	%	N/A	2020	-14.99	Standardized ACTUAL	08/25/2026
MNE	realGDPGrowth	%	N/A	2021	13.05	As reported ACTUAL	08/25/2026
MNE	realGDPGrowth	%	N/A	2022	7.74	As reported ACTUAL	08/25/2026
MNE	realGDPGrowth	%	N/A	2023	6.48	As reported ACTUAL	08/25/2026
MNE	realGDPGrowth	%	N/A	2024	3.16	As reported ACTUAL	08/25/2026
MNE	realGDPGrowth	%	N/A	2025	2.74	As reported ACTUAL	08/25/2026
MNE	realGDPGrowth	%	N/A	2026	2.80	Standardized FORECAST	08/25/2026
MNE	realGDPGrowth	%	N/A	2027	3.00	Standardized FORECAST	08/25/2026
MNE	realGDPGrowth	%	N/A	2028	3.10	Standardized FORECAST	08/25/2026
MNE	realGDPGrowth	%	N/A	2029	3.20	Standardized FORECAST	08/25/2026
MNE	realGDPGrowth	%	N/A	2030	3.10	Standardized FORECAST	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2015	3.61	As reported ACTUAL	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2016	3.94	As reported ACTUAL	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2017	4.25	As reported ACTUAL	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2018	4.60	As reported ACTUAL	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2019	4.90	As reported ACTUAL	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2020	4.14	As reported ACTUAL	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2021	4.92	As reported ACTUAL	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2022	5.94	As reported ACTUAL	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2023	7.07	As reported ACTUAL	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2024	7.64	As reported ACTUAL	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2025	8.27	As reported ACTUAL	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2026	8.72	Standardized FORECAST	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2027	9.28	Standardized FORECAST	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2028	9.85	Standardized FORECAST	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2029	10.44	Standardized FORECAST	08/25/2026
MNE	nominalGDPLCU	€B	EUR	2030	11.05	Standardized FORECAST	08/25/2026
MNE	consumerPriceInflation	%	N/A	2015	1.55	As reported ACTUAL	08/25/2026
MNE	consumerPriceInflation	%	N/A	2016	-0.27	Standardized ACTUAL	08/25/2026
MNE	consumerPriceInflation	%	N/A	2017	2.37	As reported ACTUAL	08/25/2026
MNE	consumerPriceInflation	%	N/A	2018	2.61	As reported ACTUAL	08/25/2026
MNE	consumerPriceInflation	%	N/A	2019	0.36	As reported ACTUAL	08/25/2026
MNE	consumerPriceInflation	%	N/A	2020	-0.25	Standardized ACTUAL	08/25/2026
MNE	consumerPriceInflation	%	N/A	2021	2.41	As reported ACTUAL	08/25/2026
MNE	consumerPriceInflation	%	N/A	2022	13.04	As reported ACTUAL	08/25/2026
MNE	consumerPriceInflation	%	N/A	2023	8.58	As reported ACTUAL	08/25/2026
MNE	consumerPriceInflation	%	N/A	2024	3.34	As reported ACTUAL	08/25/2026
MNE	consumerPriceInflation	%	N/A	2025	3.90	As reported ACTUAL	08/25/2026
MNE	consumerPriceInflation	%	N/A	2026	3.80	Standardized FORECAST	08/25/2026
MNE	consumerPriceInflation	%	N/A	2027	3.20	Standardized FORECAST	08/25/2026
MNE	consumerPriceInflation	%	N/A	2028	2.90	Standardized FORECAST	08/25/2026
MNE	consumerPriceInflation	%	N/A	2029	2.72	Standardized FORECAST	08/25/2026
MNE	consumerPriceInflation	%	N/A	2030	2.64	Standardized FORECAST	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2015	0.76	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2016	7.28	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2017	3.98	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2018	3.10	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2019	4.14	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2020	-4.63	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2021	5.45	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2022	13.46	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2023	7.11	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2024	10.35	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2025	5.22	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2026	2.60	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2027	2.40	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2028	3.01	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2029	3.04	Standardized BEST_OF	08/25/2026
MNE	realPrivateConsumptionGrowth	%	N/A	2030	2.94	Standardized BEST_OF	08/25/2026
MNE	populationGrowth	%	N/A	2015	0.15	Standardized ACTUAL	08/25/2026
MNE	populationGrowth	%	N/A	2016	0.11	Standardized ACTUAL	08/25/2026
MNE	populationGrowth	%	N/A	2017	0.10	Standardized ACTUAL	08/25/2026
MNE	populationGrowth	%	N/A	2018	0.07	Standardized ACTUAL	08/25/2026
MNE	populationGrowth	%	N/A	2019	0.05	Standardized ACTUAL	08/25/2026
MNE	populationGrowth	%	N/A	2020	-0.03	Standardized ACTUAL	08/25/2026
MNE	populationGrowth	%	N/A	2021	-0.25	Standardized ACTUAL	08/25/2026
MNE	populationGrowth	%	N/A	2022	-0.23	Standardized ACTUAL	08/25/2026
MNE	populationGrowth	%	N/A	2023	-0.01	Standardized ACTUAL	08/25/2026
MNE	populationGrowth	%	N/A	2024	0.00	Standardized ACTUAL	08/25/2026
MNE	populationGrowth	%	N/A	2025	-0.07	Standardized ACTUAL	08/25/2026
MNE	populationGrowth	%	N/A	2026	0.14	Standardized FORECAST	08/25/2026
MNE	populationGrowth	%	N/A	2027	-0.54	Standardized FORECAST	08/25/2026
MNE	populationGrowth	%	N/A	2028	-0.54	Standardized FORECAST	08/25/2026
MNE	populationGrowth	%	N/A	2029	-0.56	Standardized FORECAST	08/25/2026
MNE	populationGrowth	%	N/A	2030	-0.57	Standardized FORECAST	08/25/2026
MKD	realGDPGrowth	%	N/A	2015	3.86	As reported ACTUAL	08/25/2026
MKD	realGDPGrowth	%	N/A	2016	2.85	As reported ACTUAL	08/25/2026
MKD	realGDPGrowth	%	N/A	2017	1.08	As reported ACTUAL	08/25/2026
MKD	realGDPGrowth	%	N/A	2018	2.88	As reported ACTUAL	08/25/2026
MKD	realGDPGrowth	%	N/A	2019	3.91	As reported ACTUAL	08/25/2026
MKD	realGDPGrowth	%	N/A	2020	-4.69	Standardized ACTUAL	08/25/2026
MKD	realGDPGrowth	%	N/A	2021	4.51	As reported ACTUAL	08/25/2026
MKD	realGDPGrowth	%	N/A	2022	2.76	As reported ACTUAL	08/25/2026
MKD	realGDPGrowth	%	N/A	2023	2.56	As reported ACTUAL	08/25/2026
MKD	realGDPGrowth	%	N/A	2024	2.99	As reported ACTUAL	08/25/2026
MKD	realGDPGrowth	%	N/A	2025	3.49	As reported ACTUAL	08/25/2026
MKD	realGDPGrowth	%	N/A	2026	3.04	Standardized FORECAST	08/25/2026
MKD	realGDPGrowth	%	N/A	2027	3.18	Standardized FORECAST	08/25/2026
MKD	realGDPGrowth	%	N/A	2028	3.04	Standardized FORECAST	08/25/2026
MKD	realGDPGrowth	%	N/A	2029	2.93	Standardized FORECAST	08/25/2026
MKD	realGDPGrowth	%	N/A	2030	3.02	Standardized FORECAST	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2015	558.95	As reported ACTUAL	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2016	594.79	As reported ACTUAL	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2017	618.11	As reported ACTUAL	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2018	660.88	As reported ACTUAL	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2019	692.68	As reported ACTUAL	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2020	669.28	As reported ACTUAL	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2021	729.44	As reported ACTUAL	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2022	816.08	As reported ACTUAL	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2023	902.91	As reported ACTUAL	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2024	964.09	As reported ACTUAL	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2025	1,043.88	As reported ACTUAL	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2026	1,119.63	Standardized FORECAST	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2027	1,197.48	Standardized FORECAST	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2028	1,263.51	Standardized FORECAST	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2029	1,331.58	Standardized FORECAST	08/25/2026
MKD	nominalGDPLCU	MKDB	MKD	2030	1,400.05	Standardized FORECAST	08/25/2026
MKD	consumerPriceInflation	%	N/A	2015	0.13	Standardized ACTUAL	08/25/2026
MKD	consumerPriceInflation	%	N/A	2016	0.24	Standardized ACTUAL	08/25/2026
MKD	consumerPriceInflation	%	N/A	2017	1.36	As reported ACTUAL	08/25/2026
MKD	consumerPriceInflation	%	N/A	2018	1.45	As reported ACTUAL	08/25/2026
MKD	consumerPriceInflation	%	N/A	2019	0.76	As reported ACTUAL	08/25/2026
MKD	consumerPriceInflation	%	N/A	2020	1.20	As reported ACTUAL	08/25/2026
MKD	consumerPriceInflation	%	N/A	2021	3.22	As reported ACTUAL	08/25/2026
MKD	consumerPriceInflation	%	N/A	2022	14.20	As reported ACTUAL	08/25/2026
MKD	consumerPriceInflation	%	N/A	2023	9.36	As reported ACTUAL	08/25/2026
MKD	consumerPriceInflation	%	N/A	2024	3.49	As reported ACTUAL	08/25/2026
MKD	consumerPriceInflation	%	N/A	2025	4.07	As reported ACTUAL	08/25/2026
MKD	consumerPriceInflation	%	N/A	2026	4.10	Standardized FORECAST	08/25/2026
MKD	consumerPriceInflation	%	N/A	2027	3.66	Standardized FORECAST	08/25/2026
MKD	consumerPriceInflation	%	N/A	2028	2.67	Standardized FORECAST	08/25/2026
MKD	consumerPriceInflation	%	N/A	2029	2.65	Standardized FORECAST	08/25/2026
MKD	consumerPriceInflation	%	N/A	2030	2.29	Standardized FORECAST	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2015	4.43	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2016	3.88	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2017	2.09	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2018	3.68	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2019	3.74	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2020	-3.56	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2021	8.58	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2022	5.51	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2023	1.65	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2024	2.14	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2025	2.12	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2026	2.26	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2027	2.50	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2028	2.85	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2029	2.73	Standardized BEST_OF	08/25/2026
MKD	realPrivateConsumptionGrowth	%	N/A	2030	2.55	Standardized BEST_OF	08/25/2026
MKD	populationGrowth	%	N/A	2015	-0.87	Standardized ACTUAL	08/25/2026
MKD	populationGrowth	%	N/A	2016	-0.96	Standardized ACTUAL	08/25/2026
MKD	populationGrowth	%	N/A	2017	-1.04	Standardized ACTUAL	08/25/2026
MKD	populationGrowth	%	N/A	2018	-1.09	Standardized ACTUAL	08/25/2026
MKD	populationGrowth	%	N/A	2019	-1.15	Standardized ACTUAL	08/25/2026
MKD	populationGrowth	%	N/A	2020	-1.35	Standardized ACTUAL	08/25/2026
MKD	populationGrowth	%	N/A	2021	-1.12	Standardized ACTUAL	08/25/2026
MKD	populationGrowth	%	N/A	2022	-0.59	Standardized ACTUAL	08/25/2026
MKD	populationGrowth	%	N/A	2023	-0.46	Standardized ACTUAL	08/25/2026
MKD	populationGrowth	%	N/A	2024	-0.48	Standardized FORECAST	08/25/2026
MKD	populationGrowth	%	N/A	2025	-0.51	Standardized FORECAST	08/25/2026
MKD	populationGrowth	%	N/A	2026	-0.54	Standardized FORECAST	08/25/2026
MKD	populationGrowth	%	N/A	2027	-0.55	Standardized FORECAST	08/25/2026
MKD	populationGrowth	%	N/A	2028	-0.56	Standardized FORECAST	08/25/2026
MKD	populationGrowth	%	N/A	2029	-0.59	Standardized FORECAST	08/25/2026
MKD	populationGrowth	%	N/A	2030	-0.62	Standardized FORECAST	08/25/2026
Part 2 — All Other Economic Fields Held by Capital IQ for Each Country
The following field names are present in the Capital IQ data for all four countries (SVN, HRV, MNE, MKD) unless noted. These are the indicator names as returned; availability of individual years may vary.

Present for all four countries:

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
currentAccountBalanceGDP
importedGoods
directInvestmentBalance
inwardDirectInvestment
outwardDirectInvestment
tradeBalance
realGrossFixedInvestment
moneyMarketInterestRate
domesticCreditGrowth
internationalReservesLessGold
interestPaymentGrowthRate
laborForce
laborProductivityGrowth
averageExchangeRate
exchangeRateEnd
employment
financialAccountBalance
internationalResLessGoldGDP
realGDPUSD
goldReserves (present for SVN and HRV actuals; not populated for MNE and MKD in the data returned)
Present for SVN and HRV only (not returned for MNE/MKD in this dataset):

personalDisposableIncome
realPersonalDisposableIncome
realPersonalDisposableIncomeGrowth
bondYield
laborCostChange
medianHouseholdIncome
Present for SVN and HRV actuals only (As reported / Standardized parallel series):

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
Present for SVN and HRV actuals only (stock market):

stockMarketIndex
Note on MNE: bondYield, laborCostChange, medianHouseholdIncome, personalDisposableIncome, realPersonalDisposableIncome, and realPersonalDisposableIncomeGrowth are returned as null for Montenegro in the dataset. The AR (as-reported parallel) series and stockMarketIndex are also not present in the MNE/MKD data returned.

Source: S&P Global Market Intelligence — Capital IQ Economic & Demographic data. As-of dates vary by country and period as shown in the table above.


Disclaimer: Responses in ChatIQ are generated by artificial intelligence without human review. ChatIQ uses generative AI and may produce inaccurate or incomplete responses. You are responsible for verifying all information, and any decisions based on ChatIQ outputs are at your own risk. S&P Global is not liable for any loss or damage resulting from use of ChatIQ. Your questions and chat history are not shared with third parties, except foundation model providers as needed to provide the service, and are not used to train AI models by S&P Global or its providers. Chat history is stored securely and can be deleted anytime in settings. Each conversation is automatically deleted 12 months after you last access it. Your feedback helps us improve ChatIQ's accuracy and completeness.
```
