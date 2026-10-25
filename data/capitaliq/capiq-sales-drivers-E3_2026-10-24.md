# Capital IQ ChatIQ answer - block E3 (Russia, Ukraine, Turkey, Kazakhstan)

Prompt: block E3 of `BIMBOA/research/capiq-prompts-sales-drivers_2026-10-24.md` (re-run section).
Run: 2026-10-24 by Jorge Alejandro Gaytan. Pasted verbatim below; table kept tab-separated as returned.

Review notes (AI, 2026-10-24):
- New coverage: none of these four countries appears in the first pull (`BIMBOA/research/Informacion_BIMBO_macro.txt`).
- **KAZ nominalGDPLCU 2026 [unverified].** The stored 2026 level (204,522.84) is about 28% above the stored 2025 level (159,608.55) [calc]. The same block stores 2026 real growth of 4.48% and CPI of 10.32%, so the nominal jump looks too big for them. It may be a rebasing or a series break. Check it in the Capital IQ screen before using 2026 for Kazakhstan. 2027-2030 grow at rates consistent with each other.
- **UKR populationGrowth.** -7.34 (2022) and -8.08 (2023) are flagged ACTUAL. They are followed by +0.34 (2024), +2.96 (2025) and +1.43 (2026), all flagged FORECAST. These are stored values. They reflect war-time displacement and should not be used as a demand anchor without a team decision.
- **KAZ populationGrowth** drops to 0.27 in 2027, then 0.83 in 2028; stored as is.
- **Mixed vintages.** RUS, TUR and KAZ history ranges from 06/15/2026 to 10/15/2026 year by year. UKR history is mostly 09/15/2026. Forecasts are 10/15/2026 for all four.
- As in E1-E2: realPrivateConsumptionGrowth is "Standardized BEST_OF" for every year, and populationGrowth 2024-2025 is still flagged FORECAST.
- No value needed arithmetic. Nominal GDP growth will be computed by us as [calc] from nominalGDPLCU.

---

```text
S&P Capital IQ Economic Data — RUS, UKR, TUR, KAZ (2015–2030)
Part 1: Five Core Indicators — Long Table
The table below contains only values explicitly stored in Capital IQ fields, reproduced exactly as retrieved. No arithmetic has been performed. The value_type_flag_as_shown column reproduces the macroDataSource string exactly as it appears in the data.

Currency/unit key:

RUS: RUBB = Russian Rubles, Billions
UKR: UAHB = Ukrainian Hryvnias, Billions
TUR: TLB = Turkish Liras, Billions
KAZ: KZTB = Kazakhstani Tenge, Billions
Source: S&P Capital IQ Economic & Demographic Data

country_iso3	indicator	unit	currency	year	value	value_type_flag_as_shown	provider	as_of_date
RUS	realGDPGrowth	%	—	2015	-1.97	Standardized ACTUAL	S&P Capital IQ	06/15/2026
RUS	realGDPGrowth	%	—	2016	0.19	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	realGDPGrowth	%	—	2017	1.83	As reported ACTUAL	S&P Capital IQ	06/15/2026
RUS	realGDPGrowth	%	—	2018	2.81	As reported ACTUAL	S&P Capital IQ	06/15/2026
RUS	realGDPGrowth	%	—	2019	2.20	As reported ACTUAL	S&P Capital IQ	06/15/2026
RUS	realGDPGrowth	%	—	2020	-2.65	Standardized ACTUAL	S&P Capital IQ	10/15/2026
RUS	realGDPGrowth	%	—	2021	5.87	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	realGDPGrowth	%	—	2022	-1.44	Standardized ACTUAL	S&P Capital IQ	06/15/2026
RUS	realGDPGrowth	%	—	2023	4.07	As reported ACTUAL	S&P Capital IQ	07/15/2026
RUS	realGDPGrowth	%	—	2024	4.92	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	realGDPGrowth	%	—	2025	1.00	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	realGDPGrowth	%	—	2026	0.69	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	realGDPGrowth	%	—	2027	0.97	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	realGDPGrowth	%	—	2028	1.76	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	realGDPGrowth	%	—	2029	2.44	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	realGDPGrowth	%	—	2030	2.38	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2015	83087.36	As reported ACTUAL	S&P Capital IQ	06/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2016	85616.08	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2017	91843.15	As reported ACTUAL	S&P Capital IQ	06/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2018	103861.65	As reported ACTUAL	S&P Capital IQ	06/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2019	109608.31	As reported ACTUAL	S&P Capital IQ	06/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2020	107658.13	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2021	134727.47	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2022	157001.39	As reported ACTUAL	S&P Capital IQ	06/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2023	174265.73	As reported ACTUAL	S&P Capital IQ	07/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2024	202320.46	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2025	214261.02	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2026	235874.07	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2027	252967.26	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2028	264796.94	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2029	283444.41	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	nominalGDPLCU	RUBB	RUB	2030	304547.14	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	consumerPriceInflation	%	—	2015	15.53	As reported ACTUAL	S&P Capital IQ	06/15/2026
RUS	consumerPriceInflation	%	—	2016	7.04	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	consumerPriceInflation	%	—	2017	3.68	As reported ACTUAL	S&P Capital IQ	06/15/2026
RUS	consumerPriceInflation	%	—	2018	2.88	As reported ACTUAL	S&P Capital IQ	06/15/2026
RUS	consumerPriceInflation	%	—	2019	4.47	As reported ACTUAL	S&P Capital IQ	06/15/2026
RUS	consumerPriceInflation	%	—	2020	3.38	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	consumerPriceInflation	%	—	2021	6.69	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	consumerPriceInflation	%	—	2022	13.75	As reported ACTUAL	S&P Capital IQ	06/15/2026
RUS	consumerPriceInflation	%	—	2023	5.86	As reported ACTUAL	S&P Capital IQ	07/15/2026
RUS	consumerPriceInflation	%	—	2024	8.44	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	consumerPriceInflation	%	—	2025	8.70	As reported ACTUAL	S&P Capital IQ	10/15/2026
RUS	consumerPriceInflation	%	—	2026	6.14	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	consumerPriceInflation	%	—	2027	6.12	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	consumerPriceInflation	%	—	2028	4.62	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	consumerPriceInflation	%	—	2029	4.98	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	consumerPriceInflation	%	—	2030	5.26	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2015	-9.40	Standardized BEST_OF	S&P Capital IQ	06/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2016	-2.52	Standardized BEST_OF	S&P Capital IQ	10/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2017	3.68	Standardized BEST_OF	S&P Capital IQ	06/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2018	4.19	Standardized BEST_OF	S&P Capital IQ	06/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2019	3.73	Standardized BEST_OF	S&P Capital IQ	06/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2020	-5.88	Standardized BEST_OF	S&P Capital IQ	10/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2021	9.77	Standardized BEST_OF	S&P Capital IQ	10/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2022	-1.96	Standardized BEST_OF	S&P Capital IQ	06/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2023	8.58	Standardized BEST_OF	S&P Capital IQ	07/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2024	6.73	Standardized BEST_OF	S&P Capital IQ	10/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2025	3.60	Standardized BEST_OF	S&P Capital IQ	10/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2026	2.37	Standardized BEST_OF	S&P Capital IQ	10/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2027	1.09	Standardized BEST_OF	S&P Capital IQ	10/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2028	2.19	Standardized BEST_OF	S&P Capital IQ	10/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2029	3.66	Standardized BEST_OF	S&P Capital IQ	10/15/2026
RUS	realPrivateConsumptionGrowth	%	—	2030	3.12	Standardized BEST_OF	S&P Capital IQ	10/15/2026
RUS	populationGrowth	%	—	2015	0.26	Standardized ACTUAL	S&P Capital IQ	06/15/2026
RUS	populationGrowth	%	—	2016	0.32	Standardized ACTUAL	S&P Capital IQ	10/15/2026
RUS	populationGrowth	%	—	2017	0.28	Standardized ACTUAL	S&P Capital IQ	06/15/2026
RUS	populationGrowth	%	—	2018	0.17	Standardized ACTUAL	S&P Capital IQ	06/15/2026
RUS	populationGrowth	%	—	2019	0.07	Standardized ACTUAL	S&P Capital IQ	06/15/2026
RUS	populationGrowth	%	—	2020	-0.11	Standardized ACTUAL	S&P Capital IQ	10/15/2026
RUS	populationGrowth	%	—	2021	-0.37	Standardized ACTUAL	S&P Capital IQ	10/15/2026
RUS	populationGrowth	%	—	2022	-0.18	Standardized ACTUAL	S&P Capital IQ	06/15/2026
RUS	populationGrowth	%	—	2023	-0.10	Standardized ACTUAL	S&P Capital IQ	07/15/2026
RUS	populationGrowth	%	—	2024	-0.43	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	populationGrowth	%	—	2025	-0.57	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	populationGrowth	%	—	2026	-0.42	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	populationGrowth	%	—	2027	-0.24	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	populationGrowth	%	—	2028	-0.26	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	populationGrowth	%	—	2029	-0.27	Standardized FORECAST	S&P Capital IQ	10/15/2026
RUS	populationGrowth	%	—	2030	-0.28	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	realGDPGrowth	%	—	2015	-9.77	Standardized ACTUAL	S&P Capital IQ	09/15/2026
UKR	realGDPGrowth	%	—	2016	2.44	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	realGDPGrowth	%	—	2017	2.36	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	realGDPGrowth	%	—	2018	3.49	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	realGDPGrowth	%	—	2019	3.20	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	realGDPGrowth	%	—	2020	-3.75	Standardized ACTUAL	S&P Capital IQ	09/15/2026
UKR	realGDPGrowth	%	—	2021	3.45	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	realGDPGrowth	%	—	2022	-28.76	Standardized ACTUAL	S&P Capital IQ	09/15/2026
UKR	realGDPGrowth	%	—	2023	5.53	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	realGDPGrowth	%	—	2024	3.25	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	realGDPGrowth	%	—	2025	1.82	As reported ACTUAL	S&P Capital IQ	10/15/2026
UKR	realGDPGrowth	%	—	2026	0.85	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	realGDPGrowth	%	—	2027	3.60	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	realGDPGrowth	%	—	2028	4.88	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	realGDPGrowth	%	—	2029	4.06	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	realGDPGrowth	%	—	2030	3.35	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2015	1988.54	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2016	2385.37	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2017	2981.23	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2018	3560.30	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2019	3977.20	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2020	4222.03	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2021	5450.85	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2022	5239.11	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2023	6627.96	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2024	7662.38	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2025	8931.19	As reported ACTUAL	S&P Capital IQ	10/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2026	10919.50	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2027	12956.07	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2028	15512.05	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2029	18699.75	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	nominalGDPLCU	UAHB	UAH	2030	22158.36	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	consumerPriceInflation	%	—	2015	48.72	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	consumerPriceInflation	%	—	2016	13.92	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	consumerPriceInflation	%	—	2017	14.43	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	consumerPriceInflation	%	—	2018	10.94	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	consumerPriceInflation	%	—	2019	7.89	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	consumerPriceInflation	%	—	2020	2.74	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	consumerPriceInflation	%	—	2021	9.36	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	consumerPriceInflation	%	—	2022	20.18	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	consumerPriceInflation	%	—	2023	12.85	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	consumerPriceInflation	%	—	2024	6.50	As reported ACTUAL	S&P Capital IQ	09/15/2026
UKR	consumerPriceInflation	%	—	2025	12.73	As reported ACTUAL	S&P Capital IQ	10/15/2026
UKR	consumerPriceInflation	%	—	2026	8.70	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	consumerPriceInflation	%	—	2027	8.74	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	consumerPriceInflation	%	—	2028	8.43	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	consumerPriceInflation	%	—	2029	7.80	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	consumerPriceInflation	%	—	2030	7.13	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2015	-19.54	Standardized BEST_OF	S&P Capital IQ	09/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2016	2.67	Standardized BEST_OF	S&P Capital IQ	09/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2017	9.24	Standardized BEST_OF	S&P Capital IQ	09/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2018	9.32	Standardized BEST_OF	S&P Capital IQ	09/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2019	10.94	Standardized BEST_OF	S&P Capital IQ	09/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2020	1.66	Standardized BEST_OF	S&P Capital IQ	09/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2021	6.75	Standardized BEST_OF	S&P Capital IQ	09/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2022	-27.50	Standardized BEST_OF	S&P Capital IQ	09/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2023	4.33	Standardized BEST_OF	S&P Capital IQ	09/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2024	8.52	Standardized BEST_OF	S&P Capital IQ	09/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2025	7.36	Standardized BEST_OF	S&P Capital IQ	10/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2026	4.24	Standardized BEST_OF	S&P Capital IQ	10/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2027	4.45	Standardized BEST_OF	S&P Capital IQ	10/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2028	4.86	Standardized BEST_OF	S&P Capital IQ	10/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2029	5.68	Standardized BEST_OF	S&P Capital IQ	10/15/2026
UKR	realPrivateConsumptionGrowth	%	—	2030	6.94	Standardized BEST_OF	S&P Capital IQ	10/15/2026
UKR	populationGrowth	%	—	2015	-0.41	Standardized ACTUAL	S&P Capital IQ	09/15/2026
UKR	populationGrowth	%	—	2016	-0.37	Standardized ACTUAL	S&P Capital IQ	09/15/2026
UKR	populationGrowth	%	—	2017	-0.40	Standardized ACTUAL	S&P Capital IQ	09/15/2026
UKR	populationGrowth	%	—	2018	-0.50	Standardized ACTUAL	S&P Capital IQ	09/15/2026
UKR	populationGrowth	%	—	2019	-0.56	Standardized ACTUAL	S&P Capital IQ	09/15/2026
UKR	populationGrowth	%	—	2020	-0.62	Standardized ACTUAL	S&P Capital IQ	09/15/2026
UKR	populationGrowth	%	—	2021	-0.85	Standardized ACTUAL	S&P Capital IQ	09/15/2026
UKR	populationGrowth	%	—	2022	-7.34	Standardized ACTUAL	S&P Capital IQ	09/15/2026
UKR	populationGrowth	%	—	2023	-8.08	Standardized ACTUAL	S&P Capital IQ	09/15/2026
UKR	populationGrowth	%	—	2024	0.34	Standardized FORECAST	S&P Capital IQ	09/15/2026
UKR	populationGrowth	%	—	2025	2.96	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	populationGrowth	%	—	2026	1.43	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	populationGrowth	%	—	2027	-0.74	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	populationGrowth	%	—	2028	-0.75	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	populationGrowth	%	—	2029	-0.76	Standardized FORECAST	S&P Capital IQ	10/15/2026
UKR	populationGrowth	%	—	2030	-0.78	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	realGDPGrowth	%	—	2015	5.81	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	realGDPGrowth	%	—	2016	3.32	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	realGDPGrowth	%	—	2017	7.83	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	realGDPGrowth	%	—	2018	3.47	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	realGDPGrowth	%	—	2019	1.30	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	realGDPGrowth	%	—	2020	1.80	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	realGDPGrowth	%	—	2021	11.81	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	realGDPGrowth	%	—	2022	5.44	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	realGDPGrowth	%	—	2023	5.05	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	realGDPGrowth	%	—	2024	3.48	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	realGDPGrowth	%	—	2025	3.74	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	realGDPGrowth	%	—	2026	2.79	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	realGDPGrowth	%	—	2027	3.59	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	realGDPGrowth	%	—	2028	3.98	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	realGDPGrowth	%	—	2029	4.27	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	realGDPGrowth	%	—	2030	4.10	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	nominalGDPLCU	TLB	TRY	2015	2354.06	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	nominalGDPLCU	TLB	TRY	2016	2629.99	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	nominalGDPLCU	TLB	TRY	2017	3151.53	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	nominalGDPLCU	TLB	TRY	2018	3806.48	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	nominalGDPLCU	TLB	TRY	2019	4402.05	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	nominalGDPLCU	TLB	TRY	2020	5141.71	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	nominalGDPLCU	TLB	TRY	2021	7433.80	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	nominalGDPLCU	TLB	TRY	2022	15325.86	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	nominalGDPLCU	TLB	TRY	2023	27091.47	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	nominalGDPLCU	TLB	TRY	2024	44675.97	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	nominalGDPLCU	TLB	TRY	2025	63240.52	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	nominalGDPLCU	TLB	TRY	2026	82633.40	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	nominalGDPLCU	TLB	TRY	2027	99611.14	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	nominalGDPLCU	TLB	TRY	2028	115455.42	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	nominalGDPLCU	TLB	TRY	2029	131198.18	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	nominalGDPLCU	TLB	TRY	2030	148922.32	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	consumerPriceInflation	%	—	2015	7.75	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	consumerPriceInflation	%	—	2016	7.66	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	consumerPriceInflation	%	—	2017	11.11	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	consumerPriceInflation	%	—	2018	16.35	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	consumerPriceInflation	%	—	2019	15.17	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	consumerPriceInflation	%	—	2020	12.29	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	consumerPriceInflation	%	—	2021	19.58	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	consumerPriceInflation	%	—	2022	72.29	As reported ACTUAL	S&P Capital IQ	06/15/2026
TUR	consumerPriceInflation	%	—	2023	53.98	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	consumerPriceInflation	%	—	2024	58.54	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	consumerPriceInflation	%	—	2025	34.91	As reported ACTUAL	S&P Capital IQ	09/15/2026
TUR	consumerPriceInflation	%	—	2026	30.66	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	consumerPriceInflation	%	—	2027	21.78	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	consumerPriceInflation	%	—	2028	13.85	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	consumerPriceInflation	%	—	2029	10.68	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	consumerPriceInflation	%	—	2030	10.77	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2015	5.69	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2016	3.80	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2017	5.87	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2018	0.85	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2019	1.44	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2020	3.33	Standardized BEST_OF	S&P Capital IQ	09/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2021	16.13	Standardized BEST_OF	S&P Capital IQ	09/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2022	15.96	Standardized BEST_OF	S&P Capital IQ	06/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2023	10.36	Standardized BEST_OF	S&P Capital IQ	09/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2024	4.60	Standardized BEST_OF	S&P Capital IQ	09/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2025	4.26	Standardized BEST_OF	S&P Capital IQ	09/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2026	3.18	Standardized BEST_OF	S&P Capital IQ	10/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2027	2.75	Standardized BEST_OF	S&P Capital IQ	10/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2028	3.16	Standardized BEST_OF	S&P Capital IQ	10/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2029	3.33	Standardized BEST_OF	S&P Capital IQ	10/15/2026
TUR	realPrivateConsumptionGrowth	%	—	2030	3.19	Standardized BEST_OF	S&P Capital IQ	10/15/2026
TUR	populationGrowth	%	—	2015	2.53	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUR	populationGrowth	%	—	2016	2.05	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUR	populationGrowth	%	—	2017	1.75	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUR	populationGrowth	%	—	2018	1.60	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUR	populationGrowth	%	—	2019	1.12	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUR	populationGrowth	%	—	2020	0.86	Standardized ACTUAL	S&P Capital IQ	09/15/2026
TUR	populationGrowth	%	—	2021	0.69	Standardized ACTUAL	S&P Capital IQ	09/15/2026
TUR	populationGrowth	%	—	2022	0.43	Standardized ACTUAL	S&P Capital IQ	06/15/2026
TUR	populationGrowth	%	—	2023	0.24	Standardized ACTUAL	S&P Capital IQ	09/15/2026
TUR	populationGrowth	%	—	2024	0.23	Standardized FORECAST	S&P Capital IQ	09/15/2026
TUR	populationGrowth	%	—	2025	0.24	Standardized FORECAST	S&P Capital IQ	09/15/2026
TUR	populationGrowth	%	—	2026	0.27	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	populationGrowth	%	—	2027	0.31	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	populationGrowth	%	—	2028	0.32	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	populationGrowth	%	—	2029	0.31	Standardized FORECAST	S&P Capital IQ	10/15/2026
TUR	populationGrowth	%	—	2030	0.31	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	realGDPGrowth	%	—	2015	1.20	As reported ACTUAL	S&P Capital IQ	07/15/2026
KAZ	realGDPGrowth	%	—	2016	1.10	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	realGDPGrowth	%	—	2017	4.10	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	realGDPGrowth	%	—	2018	4.10	As reported ACTUAL	S&P Capital IQ	10/15/2026
KAZ	realGDPGrowth	%	—	2019	4.50	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	realGDPGrowth	%	—	2020	-2.50	Standardized ACTUAL	S&P Capital IQ	06/15/2026
KAZ	realGDPGrowth	%	—	2021	4.30	As reported ACTUAL	S&P Capital IQ	10/15/2026
KAZ	realGDPGrowth	%	—	2022	3.20	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	realGDPGrowth	%	—	2023	5.10	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	realGDPGrowth	%	—	2024	5.00	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	realGDPGrowth	%	—	2025	6.50	As reported ACTUAL	S&P Capital IQ	10/15/2026
KAZ	realGDPGrowth	%	—	2026	4.48	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	realGDPGrowth	%	—	2027	4.30	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	realGDPGrowth	%	—	2028	4.08	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	realGDPGrowth	%	—	2029	3.69	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	realGDPGrowth	%	—	2030	3.44	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2015	40884.13	As reported ACTUAL	S&P Capital IQ	07/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2016	46971.15	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2017	54378.86	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2018	61819.54	As reported ACTUAL	S&P Capital IQ	10/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2019	69532.63	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2020	70649.03	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2021	83951.59	As reported ACTUAL	S&P Capital IQ	10/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2022	103765.52	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2023	119442.29	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2024	136693.32	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2025	159608.55	As reported ACTUAL	S&P Capital IQ	10/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2026	204522.84	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2027	229840.23	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2028	258423.42	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2029	288127.31	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	nominalGDPLCU	KZTB	KZT	2030	319116.01	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	consumerPriceInflation	%	—	2015	6.68	As reported ACTUAL	S&P Capital IQ	07/15/2026
KAZ	consumerPriceInflation	%	—	2016	14.36	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	consumerPriceInflation	%	—	2017	7.44	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	consumerPriceInflation	%	—	2018	6.16	As reported ACTUAL	S&P Capital IQ	10/15/2026
KAZ	consumerPriceInflation	%	—	2019	5.33	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	consumerPriceInflation	%	—	2020	6.72	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	consumerPriceInflation	%	—	2021	8.04	As reported ACTUAL	S&P Capital IQ	10/15/2026
KAZ	consumerPriceInflation	%	—	2022	15.03	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	consumerPriceInflation	%	—	2023	14.72	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	consumerPriceInflation	%	—	2024	8.95	As reported ACTUAL	S&P Capital IQ	06/15/2026
KAZ	consumerPriceInflation	%	—	2025	11.45	As reported ACTUAL	S&P Capital IQ	10/15/2026
KAZ	consumerPriceInflation	%	—	2026	10.32	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	consumerPriceInflation	%	—	2027	8.84	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	consumerPriceInflation	%	—	2028	8.02	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	consumerPriceInflation	%	—	2029	7.14	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	consumerPriceInflation	%	—	2030	6.49	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2015	1.80	Standardized BEST_OF	S&P Capital IQ	07/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2016	1.20	Standardized BEST_OF	S&P Capital IQ	06/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2017	1.50	Standardized BEST_OF	S&P Capital IQ	06/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2018	6.10	Standardized BEST_OF	S&P Capital IQ	10/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2019	6.10	Standardized BEST_OF	S&P Capital IQ	06/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2020	-3.70	Standardized BEST_OF	S&P Capital IQ	06/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2021	6.30	Standardized BEST_OF	S&P Capital IQ	10/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2022	4.00	Standardized BEST_OF	S&P Capital IQ	06/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2023	7.60	Standardized BEST_OF	S&P Capital IQ	06/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2024	9.60	Standardized BEST_OF	S&P Capital IQ	06/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2025	8.10	Standardized BEST_OF	S&P Capital IQ	10/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2026	3.63	Standardized BEST_OF	S&P Capital IQ	10/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2027	3.21	Standardized BEST_OF	S&P Capital IQ	10/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2028	3.08	Standardized BEST_OF	S&P Capital IQ	10/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2029	2.85	Standardized BEST_OF	S&P Capital IQ	10/15/2026
KAZ	realPrivateConsumptionGrowth	%	—	2030	2.75	Standardized BEST_OF	S&P Capital IQ	10/15/2026
KAZ	populationGrowth	%	—	2015	1.50	Standardized ACTUAL	S&P Capital IQ	07/15/2026
KAZ	populationGrowth	%	—	2016	1.55	Standardized ACTUAL	S&P Capital IQ	06/15/2026
KAZ	populationGrowth	%	—	2017	1.57	Standardized ACTUAL	S&P Capital IQ	06/15/2026
KAZ	populationGrowth	%	—	2018	1.51	Standardized ACTUAL	S&P Capital IQ	10/15/2026
KAZ	populationGrowth	%	—	2019	1.46	Standardized ACTUAL	S&P Capital IQ	06/15/2026
KAZ	populationGrowth	%	—	2020	1.42	Standardized ACTUAL	S&P Capital IQ	06/15/2026
KAZ	populationGrowth	%	—	2021	1.34	Standardized ACTUAL	S&P Capital IQ	10/15/2026
KAZ	populationGrowth	%	—	2022	1.47	Standardized ACTUAL	S&P Capital IQ	06/15/2026
KAZ	populationGrowth	%	—	2023	1.47	Standardized ACTUAL	S&P Capital IQ	06/15/2026
KAZ	populationGrowth	%	—	2024	1.29	Standardized FORECAST	S&P Capital IQ	06/15/2026
KAZ	populationGrowth	%	—	2025	1.22	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	populationGrowth	%	—	2026	1.15	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	populationGrowth	%	—	2027	0.27	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	populationGrowth	%	—	2028	0.83	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	populationGrowth	%	—	2029	0.81	Standardized FORECAST	S&P Capital IQ	10/15/2026
KAZ	populationGrowth	%	—	2030	0.81	Standardized FORECAST	S&P Capital IQ	10/15/2026
Part 2: All Other Economic Fields Available in Capital IQ (Names Only)
The following additional indicators are present in the Capital IQ Economic & Demographic dataset for all four countries (field availability is consistent across RUS, UKR, TUR, KAZ unless noted):

GDP & Output

realGDP
nominalGDP
realGDPUSD
gdpPerCapita
gdpDeflator
realGDPGrowthAR (as-reported variant, actuals only)
realGDPAR (as-reported variant, actuals only)
realGDPLCUAR (as-reported variant, actuals only)
nominalGDPAR (as-reported variant, actuals only)
nominalGDPLCUAR (as-reported variant, actuals only)
industrialProductionGrowth
industrialProductionGrowthAR (actuals only)
laborProductivityGrowth
Consumption & Investment

realGovermentConsumptionGrowth
realGrossFixedInvestmentGrowth
realGrossFixedInvestment
grossDomesticSavings
personalDisposableIncome
realPersonalDisposableIncome
realPersonalDisposableIncomeGrowth
grossPersonalIncome (field present but null for all four countries)
Prices & Wages

producerPriceInflation
producerPriceInflationAR (actuals only)
averageConsumerPriceIndex
averageProducerPriceIndex
averageMonthlyWages
laborCostChange (present for RUS and TUR; not observed for UKR and KAZ in the retrieved data)
medianHouseholdIncome
Labor Market

unemploymentRate
unemploymentRateAR (actuals only)
laborForce
employment
Population

population
Fiscal

budgetBalanceGDP
budgetExpenditureGDP
budgetRevenue
publicDebt
publicDebtGDP
interestPaymentGrowth
interestPaymentGrowthRate
debtInterestPaymentGDP
External Sector & Trade

currentAccountBalance
currentAccountBalanceGDP
currentAccountBalanceAR (actuals only)
tradeBalance
tradeBalanceAR (actuals only)
exportedGoods
exportedGoodsAR (actuals only)
importedGoods
importedGoodsAR (actuals only)
directInvestmentBalance
inwardDirectInvestment
outwardDirectInvestment
financialAccountBalance
foreignDebtGDP
foreignDebt (field present but null for all four countries)
externalDebtService (field present but null for all four countries)
Reserves & Financial

internationalReservesLessGold
internationalResLessGoldGDP
goldReserves (present for RUS, UKR, KAZ; null for TUR in forecast years)
moneyMarketInterestRate
bondYield
domesticCreditGrowth
averageExchangeRate
averageExchangeRateAR (actuals only)
exchangeRateEnd
stockMarketIndex (observed for RUS in select historical years; not present for all countries/years)

Disclaimer: Responses in ChatIQ are generated by artificial intelligence without human review. ChatIQ uses generative AI and may produce inaccurate or incomplete responses. You are responsible for verifying all information, and any decisions based on ChatIQ outputs are at your own risk. S&P Global is not liable for any loss or damage resulting from use of ChatIQ. Your questions and chat history are not shared with third parties, except foundation model providers as needed to provide the service, and are not used to train AI models by S&P Global or its providers. Chat history is stored securely and can be deleted anytime in settings. Each conversation is automatically deleted 12 months after you last access it. Your feedback helps us improve ChatIQ's accuracy and completeness.
```
