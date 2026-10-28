# Capital IQ ChatIQ answer - block E5 (South Africa, Morocco, Tunisia)

Prompt: block E5 of `BIMBOA/research/capiq-prompts-sales-drivers_2026-10-24.md` (re-run section).
Run: 2026-10-24 by Jorge Alejandro Gaytan. Pasted verbatim below; table kept tab-separated as returned.

Review notes (AI, 2026-10-24):
- New coverage: none of these three countries appears in the first pull (`BIMBOA/research/Informacion_BIMBO_macro.txt`).
- **2025-to-2026 nominal step** (the check opened after KAZ in E3 and KOR in E4) [calc]:
  - ZAF +5.7%, close to the stored real growth and CPI for 2026 (0.88%, 4.35%).
  - TUN +5.8%, below what 2026 real growth and CPI (2.21%, 5.33%) would suggest; no break visible.
  - **MAR +10.5%**, against stored 2026 real growth of 4.69% and CPI of 0.60%. CPI is not the GDP deflator, so a gap is possible, but this one is large and the vintage changes at the same point (history 06/15-07/15/2026, forecasts 10/15/2026). Smaller than KAZ or KOR, but check it in the Capital IQ screen before using Morocco's 2026 step.
- **Vintages.** TUN forecasts are dated 08/18/2026, older than the 10/15/2026 forecasts for ZAF and MAR.
- **TUN population.** Unlike the other countries, 2024 is flagged ACTUAL and only 2025 onward is FORECAST.
- The `currency` column shows the local currency on % rows. Formatting only.
- As in E1-E4: realPrivateConsumptionGrowth is "Standardized BEST_OF" for every year.
- No value needed arithmetic. Nominal GDP growth will be computed by us as [calc] from nominalGDPLCU.

---

```text
Below is the long table exactly as stored in S&P Capital IQ — no arithmetic applied, all decimals preserved, units and value-type flags exactly as shown. The as_of_date column reflects economicAsOfEOP (end-of-period as-of date) for each row.

Currency notes:

ZAF (South Africa): Nominal GDP LCU unit = RB (Rand Billions)
MAR (Morocco): Nominal GDP LCU unit = د.م.B (Moroccan Dirham Billions)
TUN (Tunisia): Nominal GDP LCU unit = د.تB (Tunisian Dinar Billions)
All growth/inflation indicators unit = %
Source: S&P Capital IQ

country_iso3	indicator	ciq_field_name	unit	currency	year	value	value_type_flag_as_shown	provider	as_of_date
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2015	1.32	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2016	0.66	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2017	1.16	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2018	1.56	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2019	0.26	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2020	-6.17	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2021	4.86	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2022	2.06	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2023	0.81	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2024	0.53	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2025	1.11	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2026	0.88	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2027	1.17	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2028	1.93	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2029	2.5	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Real GDP Growth	realGDPGrowth	%	ZAR	2030	2.88	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2015	4,420.79	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2016	4,759.55	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2017	5,078.19	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2018	5,363.19	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2019	5,625.21	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2020	5,562.76	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2021	6,206.84	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2022	6,666.58	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2023	7,037.67	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2024	7,352.45	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2025	7,641.79	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2026	8,078.77	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2027	8,503.4	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2028	8,985.63	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2029	9,568.1	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Nominal GDP (LCU)	nominalGDPLCU	RB	ZAR	2030	10,219.44	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2015	4.59	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2016	6.32	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2017	5.29	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2018	4.6	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2019	4.12	As reported ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2020	3.29	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2021	4.55	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2022	6.86	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2023	5.9	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2024	4.43	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2025	3.22	As reported ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2026	4.35	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2027	4.37	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2028	3.24	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2029	3.02	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Consumer Price Inflation	consumerPriceInflation	%	ZAR	2030	3.08	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2015	2.16	Standardized BEST_OF	S&P Capital IQ	08/18/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2016	0.68	Standardized BEST_OF	S&P Capital IQ	08/18/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2017	1.71	Standardized BEST_OF	S&P Capital IQ	08/18/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2018	3.16	Standardized BEST_OF	S&P Capital IQ	08/18/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2019	1.28	Standardized BEST_OF	S&P Capital IQ	08/18/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2020	-6.12	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2021	6	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2022	2.64	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2023	0.23	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2024	0.98	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2025	3.56	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2026	2.04	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2027	1.54	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2028	1.96	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2029	2.58	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ZAF	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	ZAR	2030	3	Standardized BEST_OF	S&P Capital IQ	10/15/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2015	2.03	Standardized ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2016	0.94	Standardized ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2017	0.66	Standardized ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2018	1.7	Standardized ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2019	1.66	Standardized ACTUAL	S&P Capital IQ	08/18/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2020	1.64	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2021	1.55	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2022	1.42	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2023	1.34	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2024	1.26	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2025	1.16	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2026	1.09	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2027	1.05	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2028	1.04	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2029	1.01	Standardized FORECAST	S&P Capital IQ	10/15/2026
ZAF	Population Growth	populationGrowth	%	ZAR	2030	0.97	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2015	4.34	As reported ACTUAL	S&P Capital IQ	06/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2016	0.52	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2017	5.06	As reported ACTUAL	S&P Capital IQ	06/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2018	3.07	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2019	2.89	As reported ACTUAL	S&P Capital IQ	06/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2020	-7.18	Standardized ACTUAL	S&P Capital IQ	07/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2021	8.15	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2022	1.81	As reported ACTUAL	S&P Capital IQ	06/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2023	3.79	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2024	4.36	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2025	4.86	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2026	4.69	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2027	4.51	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2028	4.81	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2029	4.6	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Real GDP Growth	realGDPGrowth	%	MAD	2030	5.43	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2015	1,078.12	As reported ACTUAL	S&P Capital IQ	06/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2016	1,094.25	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2017	1,148.9	As reported ACTUAL	S&P Capital IQ	06/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2018	1,195.24	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2019	1,239.84	As reported ACTUAL	S&P Capital IQ	06/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2020	1,152.48	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2021	1,276.56	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2022	1,333.54	As reported ACTUAL	S&P Capital IQ	06/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2023	1,485.64	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2024	1,614.57	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2025	1,720.2	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2026	1,901.43	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2027	1,992.36	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2028	2,096.66	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2029	2,208.83	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Nominal GDP (LCU)	nominalGDPLCU	د.م.B	MAD	2030	2,372.32	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2015	1.56	As reported ACTUAL	S&P Capital IQ	06/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2016	1.64	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2017	0.75	As reported ACTUAL	S&P Capital IQ	06/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2018	1.79	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2019	0.31	As reported ACTUAL	S&P Capital IQ	06/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2020	0.4	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2021	1.34	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2022	6.66	As reported ACTUAL	S&P Capital IQ	06/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2023	6.09	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2024	0.99	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2025	0.7	As reported ACTUAL	S&P Capital IQ	07/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2026	0.6	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2027	1.2	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2028	1.98	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2029	1.67	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Consumer Price Inflation	consumerPriceInflation	%	MAD	2030	1.67	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2015	2.43	Standardized BEST_OF	S&P Capital IQ	06/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2016	1.89	Standardized BEST_OF	S&P Capital IQ	07/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2017	3.71	Standardized BEST_OF	S&P Capital IQ	06/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2018	2.52	Standardized BEST_OF	S&P Capital IQ	07/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2019	2.18	Standardized BEST_OF	S&P Capital IQ	06/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2020	-5.6	Standardized BEST_OF	S&P Capital IQ	07/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2021	6.96	Standardized BEST_OF	S&P Capital IQ	07/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2022	0.15	Standardized BEST_OF	S&P Capital IQ	06/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2023	4.85	Standardized BEST_OF	S&P Capital IQ	07/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2024	2.92	Standardized BEST_OF	S&P Capital IQ	07/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2025	1.16	Standardized BEST_OF	S&P Capital IQ	07/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2026	4.66	Standardized BEST_OF	S&P Capital IQ	10/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2027	4.06	Standardized BEST_OF	S&P Capital IQ	10/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2028	4.08	Standardized BEST_OF	S&P Capital IQ	10/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2029	4.76	Standardized BEST_OF	S&P Capital IQ	10/15/2026
MAR	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	MAD	2030	4.06	Standardized BEST_OF	S&P Capital IQ	10/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2015	1.18	Standardized ACTUAL	S&P Capital IQ	06/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2016	1.2	Standardized ACTUAL	S&P Capital IQ	07/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2017	1.21	Standardized ACTUAL	S&P Capital IQ	06/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2018	1.11	Standardized ACTUAL	S&P Capital IQ	07/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2019	1.04	Standardized ACTUAL	S&P Capital IQ	06/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2020	1.03	Standardized ACTUAL	S&P Capital IQ	07/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2021	1.01	Standardized ACTUAL	S&P Capital IQ	07/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2022	1.01	Standardized ACTUAL	S&P Capital IQ	06/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2023	1.03	Standardized ACTUAL	S&P Capital IQ	07/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2024	0.98	Standardized FORECAST	S&P Capital IQ	07/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2025	0.92	Standardized FORECAST	S&P Capital IQ	07/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2026	0.86	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2027	0.82	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2028	0.78	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2029	0.74	Standardized FORECAST	S&P Capital IQ	10/15/2026
MAR	Population Growth	populationGrowth	%	MAD	2030	0.7	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2015	0.89	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2016	1.12	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2017	2.25	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2018	2.61	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2019	1.55	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2020	-8.98	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2021	4.74	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2022	2.75	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2023	0.28	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2024	1.73	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2025	2.73	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2026	2.21	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2027	2.82	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2028	2.93	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2029	3.38	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Real GDP Growth	realGDPGrowth	%	TND	2030	3.46	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2015	89.8	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2016	95.29	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2017	102.01	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2018	112.99	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2019	122.97	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2020	119.5	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2021	131.54	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2022	139.44	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2023	149.79	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2024	159.85	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2025	171.64	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2026	181.53	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2027	198.23	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2028	214.54	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2029	228.84	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Nominal GDP (LCU)	nominalGDPLCU	د.تB	TND	2030	240.03	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2015	4.85	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2016	3.63	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2017	5.31	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2018	7.31	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2019	6.72	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2020	5.63	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2021	5.71	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2022	8.31	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2023	9.32	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2024	7.01	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2025	5.35	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2026	5.33	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2027	4.61	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2028	4.04	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2029	3.53	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Consumer Price Inflation	consumerPriceInflation	%	TND	2030	2.78	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2015	4.52	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2016	3.15	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2017	2.63	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2018	2.6	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2019	2.41	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2020	-5.14	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2021	3.25	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2022	1.86	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2023	0.91	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2024	4.08	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2025	2.74	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2026	2.64	Standardized BEST_OF	S&P Capital IQ	08/18/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2027	2.8	Standardized BEST_OF	S&P Capital IQ	08/18/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2028	3.37	Standardized BEST_OF	S&P Capital IQ	08/18/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2029	3.39	Standardized BEST_OF	S&P Capital IQ	08/18/2026
TUN	Real Private Consumption Growth	realPrivateConsumptionGrowth	%	TND	2030	3.44	Standardized BEST_OF	S&P Capital IQ	08/18/2026
TUN	Population Growth	populationGrowth	%	TND	2015	1.14	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUN	Population Growth	populationGrowth	%	TND	2016	1.11	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUN	Population Growth	populationGrowth	%	TND	2017	1.06	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUN	Population Growth	populationGrowth	%	TND	2018	0.99	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUN	Population Growth	populationGrowth	%	TND	2019	0.93	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUN	Population Growth	populationGrowth	%	TND	2020	0.83	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUN	Population Growth	populationGrowth	%	TND	2021	0.62	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUN	Population Growth	populationGrowth	%	TND	2022	0.59	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUN	Population Growth	populationGrowth	%	TND	2023	0.67	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUN	Population Growth	populationGrowth	%	TND	2024	0.63	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUN	Population Growth	populationGrowth	%	TND	2025	0.58	Standardized FORECAST	S&P Capital IQ	06/15/2026
TUN	Population Growth	populationGrowth	%	TND	2026	0.54	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Population Growth	populationGrowth	%	TND	2027	0.49	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Population Growth	populationGrowth	%	TND	2028	0.45	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Population Growth	populationGrowth	%	TND	2029	0.4	Standardized FORECAST	S&P Capital IQ	08/18/2026
TUN	Population Growth	populationGrowth	%	TND	2030	0.36	Standardized FORECAST	S&P Capital IQ	08/18/2026
Additional Economic Fields Held in S&P Capital IQ for Each Country
The following field names are stored in Capital IQ for all three countries (ZAF, MAR, TUN) beyond the five requested indicators. These are field names only, as requested.

Present across all three countries:

economicAsOf
population
averageMonthlyWages (ZAF and TUN only; null for MAR)
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
personalDisposableIncome
realPersonalDisposableIncome
realPersonalDisposableIncomeGrowth
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
laborCostChange (ZAF and TUN only; not present in MAR data)
averageExchangeRate
exchangeRateEnd
medianHouseholdIncome
employment
financialAccountBalance
internationalResLessGoldGDP
realGDPUSD
Null / not populated in the available data (present as fields but no value stored):

foreignDebt (null for all three)
externalDebtService (null for all three)
goldReserves (null for all three)
grossPersonalIncome (null for all three)

Disclaimer: Responses in ChatIQ are generated by artificial intelligence without human review. ChatIQ uses generative AI and may produce inaccurate or incomplete responses. You are responsible for verifying all information, and any decisions based on ChatIQ outputs are at your own risk. S&P Global is not liable for any loss or damage resulting from use of ChatIQ. Your questions and chat history are not shared with third parties, except foundation model providers as needed to provide the service, and are not used to train AI models by S&P Global or its providers. Chat history is stored securely and can be deleted anytime in settings. Each conversation is automatically deleted 12 months after you last access it. Your feedback helps us improve ChatIQ's accuracy and completeness.
```
