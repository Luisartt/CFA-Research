# Capital IQ ChatIQ answer - block X1 (same-basis history, Americas)

Prompt: block X1 of `BIMBOA/research/capiq-prompts-sales-drivers_2026-10-24.md` (re-run section).
Run: 2026-10-24 by Jorge Alejandro Gaytan. Pasted verbatim below; table kept tab-separated as returned.

Review notes (AI, 2026-10-24):
- Capital IQ stores no separate "Standardized" history for most country-years: the "As reported ACTUAL" value is the only stored actual. History (As reported) plus forecast (Standardized) is therefore the series as Capital IQ builds it, not a mix we can avoid.
- PRY nominalGDPLCU 2019 is 236.68 here; the first pull (`BIMBOA/research/Informacion_BIMBO_macro.txt`) shows 239.91 for both 2019 and 2020, a duplicated value. Use 236.68 from this block for 2019.
- All other overlapping values match the first pull and blocks M1-M5.

---

Below is the long table exactly as stored in S&P Capital IQ fields — no arithmetic applied. All values are reproduced at full decimal precision as returned. The value_type_flag_as_shown column carries the macroDataSource string exactly as stored. The as_of_date column reflects economicAsOfEOP (end-of-period as-of date for the economic data point).

Notes on flags:

Where macroDataSource = "As reported ACTUAL" for either field, that value is flagged accordingly — it is not the Standardized version. Per your instructions, it is included and flagged.
Where macroDataSource = "Standardized ACTUAL" or "Standardized FORECAST", the Standardized version was stored and is flagged accordingly.
The outer dataSourceType for all records is "BEST_OF" — this is the query-level selection method, not the field-level flag; the field-level flag is macroDataSource and is what appears in value_type_flag_as_shown.
VEN nominalGDPLCU 2015–2017 are flagged "As reported ACTUAL"; 2018–2025 are flagged "Standardized FORECAST" — reproduced exactly as stored.
URY nominalGDPLCU currency stored as "$B" (Uruguayan peso billions) — reproduced exactly as stored.
Source: S&P Capital IQ (S&P Global Market Intelligence), Economic & Demographic data, as-of dates per row.

```text
country_iso3	ciq_field_name	unit	currency	year	value	value_type_flag_as_shown	provider	as_of_date
MEX	nominalGDPLCU	Mex$B	MXN	2015	19228.61	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	nominalGDPLCU	Mex$B	MXN	2016	20758.79	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	nominalGDPLCU	Mex$B	MXN	2017	22536.21	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	nominalGDPLCU	Mex$B	MXN	2018	24176.67	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	nominalGDPLCU	Mex$B	MXN	2019	25121.82	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	nominalGDPLCU	Mex$B	MXN	2020	24086.76	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	nominalGDPLCU	Mex$B	MXN	2021	26690.03	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	nominalGDPLCU	Mex$B	MXN	2022	29525.51	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	nominalGDPLCU	Mex$B	MXN	2023	31871.09	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	nominalGDPLCU	Mex$B	MXN	2024	33582.9	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	nominalGDPLCU	Mex$B	MXN	2025	35301.59	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	consumerPriceInflation	%	N/A	2015	2.72	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	consumerPriceInflation	%	N/A	2016	2.82	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	consumerPriceInflation	%	N/A	2017	6.04	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	consumerPriceInflation	%	N/A	2018	4.9	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	consumerPriceInflation	%	N/A	2019	3.64	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	consumerPriceInflation	%	N/A	2020	3.4	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	consumerPriceInflation	%	N/A	2021	5.69	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	consumerPriceInflation	%	N/A	2022	7.9	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	consumerPriceInflation	%	N/A	2023	5.53	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	consumerPriceInflation	%	N/A	2024	4.72	As reported ACTUAL	S&P Capital IQ	10/15/2026
MEX	consumerPriceInflation	%	N/A	2025	3.81	As reported ACTUAL	S&P Capital IQ	10/15/2026
USA	nominalGDPLCU	$B	USD	2015	18295.02	As reported ACTUAL	S&P Capital IQ	10/07/2026
USA	nominalGDPLCU	$B	USD	2016	18804.91	As reported ACTUAL	S&P Capital IQ	10/07/2026
USA	nominalGDPLCU	$B	USD	2017	19612.1	As reported ACTUAL	S&P Capital IQ	10/07/2026
USA	nominalGDPLCU	$B	USD	2018	20656.52	As reported ACTUAL	S&P Capital IQ	10/07/2026
USA	nominalGDPLCU	$B	USD	2019	21539.98	As reported ACTUAL	S&P Capital IQ	10/07/2026
USA	nominalGDPLCU	$B	USD	2020	21375.28	As reported ACTUAL	S&P Capital IQ	10/15/2026
USA	nominalGDPLCU	$B	USD	2021	23745.85	As reported ACTUAL	S&P Capital IQ	10/15/2026
USA	nominalGDPLCU	$B	USD	2022	26059.71	As reported ACTUAL	S&P Capital IQ	10/15/2026
USA	nominalGDPLCU	$B	USD	2023	27825.89	As reported ACTUAL	S&P Capital IQ	10/15/2026
USA	nominalGDPLCU	$B	USD	2024	29380.99	As reported ACTUAL	S&P Capital IQ	10/15/2026
USA	nominalGDPLCU	$B	USD	2025	30861.29	As reported ACTUAL	S&P Capital IQ	10/15/2026
USA	consumerPriceInflation	%	N/A	2015	0.12	As reported ACTUAL	S&P Capital IQ	10/07/2026
USA	consumerPriceInflation	%	N/A	2016	1.26	As reported ACTUAL	S&P Capital IQ	10/07/2026
USA	consumerPriceInflation	%	N/A	2017	2.13	As reported ACTUAL	S&P Capital IQ	10/07/2026
USA	consumerPriceInflation	%	N/A	2018	2.44	As reported ACTUAL	S&P Capital IQ	10/07/2026
USA	consumerPriceInflation	%	N/A	2019	1.81	As reported ACTUAL	S&P Capital IQ	10/07/2026
USA	consumerPriceInflation	%	N/A	2020	1.23	As reported ACTUAL	S&P Capital IQ	10/15/2026
USA	consumerPriceInflation	%	N/A	2021	4.7	As reported ACTUAL	S&P Capital IQ	10/15/2026
USA	consumerPriceInflation	%	N/A	2022	8	As reported ACTUAL	S&P Capital IQ	10/15/2026
USA	consumerPriceInflation	%	N/A	2023	4.12	As reported ACTUAL	S&P Capital IQ	10/15/2026
USA	consumerPriceInflation	%	N/A	2024	2.95	As reported ACTUAL	S&P Capital IQ	10/15/2026
USA	consumerPriceInflation	%	N/A	2025	2.71	Standardized ACTUAL	S&P Capital IQ	10/15/2026
CAN	nominalGDPLCU	C$B	CAD	2015	1990.44	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	nominalGDPLCU	C$B	CAD	2016	2025.54	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	nominalGDPLCU	C$B	CAD	2017	2140.64	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	nominalGDPLCU	C$B	CAD	2018	2235.68	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	nominalGDPLCU	C$B	CAD	2019	2313.56	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	nominalGDPLCU	C$B	CAD	2020	2220.53	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	nominalGDPLCU	C$B	CAD	2021	2535.82	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	nominalGDPLCU	C$B	CAD	2022	2864.16	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	nominalGDPLCU	C$B	CAD	2023	2965.2	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	nominalGDPLCU	C$B	CAD	2024	3108.55	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	nominalGDPLCU	C$B	CAD	2025	3245.26	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	consumerPriceInflation	%	N/A	2015	1.13	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	consumerPriceInflation	%	N/A	2016	1.43	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	consumerPriceInflation	%	N/A	2017	1.6	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	consumerPriceInflation	%	N/A	2018	2.27	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	consumerPriceInflation	%	N/A	2019	1.95	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	consumerPriceInflation	%	N/A	2020	0.72	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	consumerPriceInflation	%	N/A	2021	3.4	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	consumerPriceInflation	%	N/A	2022	6.8	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	consumerPriceInflation	%	N/A	2023	3.88	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	consumerPriceInflation	%	N/A	2024	2.38	As reported ACTUAL	S&P Capital IQ	07/15/2026
CAN	consumerPriceInflation	%	N/A	2025	2.07	As reported ACTUAL	S&P Capital IQ	07/15/2026
ARG	nominalGDPLCU	AR$B	ARS	2015	5954.51	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	nominalGDPLCU	AR$B	ARS	2016	8228.16	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	nominalGDPLCU	AR$B	ARS	2017	10660.23	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	nominalGDPLCU	AR$B	ARS	2018	14744.81	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	nominalGDPLCU	AR$B	ARS	2019	21558.44	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	nominalGDPLCU	AR$B	ARS	2020	27209.81	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	nominalGDPLCU	AR$B	ARS	2021	46219.08	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	nominalGDPLCU	AR$B	ARS	2022	82810.05	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	nominalGDPLCU	AR$B	ARS	2023	193946.18	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	nominalGDPLCU	AR$B	ARS	2024	584377.01	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	nominalGDPLCU	AR$B	ARS	2025	850239.8	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	consumerPriceInflation	%	N/A	2015	16.36	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	consumerPriceInflation	%	N/A	2016	37.52	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	consumerPriceInflation	%	N/A	2017	25.28	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	consumerPriceInflation	%	N/A	2018	34.28	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	consumerPriceInflation	%	N/A	2019	53.55	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	consumerPriceInflation	%	N/A	2020	42.02	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	consumerPriceInflation	%	N/A	2021	48.41	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	consumerPriceInflation	%	N/A	2022	72.43	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	consumerPriceInflation	%	N/A	2023	133.49	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	consumerPriceInflation	%	N/A	2024	219.88	As reported ACTUAL	S&P Capital IQ	10/15/2026
ARG	consumerPriceInflation	%	N/A	2025	41.92	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	nominalGDPLCU	R$B	BRL	2015	5995.79	As reported ACTUAL	S&P Capital IQ	06/15/2026
BRA	nominalGDPLCU	R$B	BRL	2016	6269.33	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	nominalGDPLCU	R$B	BRL	2017	6585.48	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	nominalGDPLCU	R$B	BRL	2018	7004.14	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	nominalGDPLCU	R$B	BRL	2019	7389.13	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	nominalGDPLCU	R$B	BRL	2020	7609.6	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	nominalGDPLCU	R$B	BRL	2021	9012.14	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	nominalGDPLCU	R$B	BRL	2022	10079.68	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	nominalGDPLCU	R$B	BRL	2023	10943.34	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	nominalGDPLCU	R$B	BRL	2024	11779.25	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	nominalGDPLCU	R$B	BRL	2025	12738.57	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	consumerPriceInflation	%	N/A	2015	9.03	As reported ACTUAL	S&P Capital IQ	06/15/2026
BRA	consumerPriceInflation	%	N/A	2016	8.74	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	consumerPriceInflation	%	N/A	2017	3.45	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	consumerPriceInflation	%	N/A	2018	3.66	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	consumerPriceInflation	%	N/A	2019	3.73	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	consumerPriceInflation	%	N/A	2020	3.21	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	consumerPriceInflation	%	N/A	2021	8.3	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	consumerPriceInflation	%	N/A	2022	9.28	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	consumerPriceInflation	%	N/A	2023	4.59	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	consumerPriceInflation	%	N/A	2024	4.37	As reported ACTUAL	S&P Capital IQ	10/15/2026
BRA	consumerPriceInflation	%	N/A	2025	5.02	As reported ACTUAL	S&P Capital IQ	10/15/2026
CHL	nominalGDPLCU	CL$T	CLP	2015	158.62	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	nominalGDPLCU	CL$T	CLP	2016	168.76	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	nominalGDPLCU	CL$T	CLP	2017	179.31	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	nominalGDPLCU	CL$T	CLP	2018	189.43	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	nominalGDPLCU	CL$T	CLP	2019	195.55	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	nominalGDPLCU	CL$T	CLP	2020	201.31	As reported ACTUAL	S&P Capital IQ	09/15/2026
CHL	nominalGDPLCU	CL$T	CLP	2021	239.56	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	nominalGDPLCU	CL$T	CLP	2022	262.95	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	nominalGDPLCU	CL$T	CLP	2023	282.1	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	nominalGDPLCU	CL$T	CLP	2024	310.68	As reported ACTUAL	S&P Capital IQ	09/15/2026
CHL	nominalGDPLCU	CL$T	CLP	2025	339.98	As reported ACTUAL	S&P Capital IQ	09/15/2026
CHL	consumerPriceInflation	%	N/A	2015	4.35	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	consumerPriceInflation	%	N/A	2016	3.78	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	consumerPriceInflation	%	N/A	2017	2.18	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	consumerPriceInflation	%	N/A	2018	2.44	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	consumerPriceInflation	%	N/A	2019	2.56	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	consumerPriceInflation	%	N/A	2020	3.05	As reported ACTUAL	S&P Capital IQ	09/15/2026
CHL	consumerPriceInflation	%	N/A	2021	4.52	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	consumerPriceInflation	%	N/A	2022	11.64	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	consumerPriceInflation	%	N/A	2023	7.58	As reported ACTUAL	S&P Capital IQ	06/15/2026
CHL	consumerPriceInflation	%	N/A	2024	4.27	As reported ACTUAL	S&P Capital IQ	09/15/2026
CHL	consumerPriceInflation	%	N/A	2025	4.21	As reported ACTUAL	S&P Capital IQ	09/15/2026
COL	nominalGDPLCU	Col$T	COP	2015	804.69	As reported ACTUAL	S&P Capital IQ	10/15/2026
COL	nominalGDPLCU	Col$T	COP	2016	863.78	As reported ACTUAL	S&P Capital IQ	10/15/2026
COL	nominalGDPLCU	Col$T	COP	2017	920.47	As reported ACTUAL	S&P Capital IQ	10/15/2026
COL	nominalGDPLCU	Col$T	COP	2018	987.79	As reported ACTUAL	S&P Capital IQ	10/15/2026
COL	nominalGDPLCU	Col$T	COP	2019	1060.07	As reported ACTUAL	S&P Capital IQ	10/15/2026
COL	nominalGDPLCU	Col$T	COP	2020	998.47	As reported ACTUAL	S&P Capital IQ	09/15/2026
COL	nominalGDPLCU	Col$T	COP	2021	1192.63	As reported ACTUAL	S&P Capital IQ	08/18/2026
COL	nominalGDPLCU	Col$T	COP	2022	1471.08	As reported ACTUAL	S&P Capital IQ	08/18/2026
COL	nominalGDPLCU	Col$T	COP	2023	1587.2	As reported ACTUAL	S&P Capital IQ	09/15/2026
COL	nominalGDPLCU	Col$T	COP	2024	1713.32	As reported ACTUAL	S&P Capital IQ	09/15/2026
COL	nominalGDPLCU	Col$T	COP	2025	1852.67	As reported ACTUAL	S&P Capital IQ	09/15/2026
COL	consumerPriceInflation	%	N/A	2015	4.99	As reported ACTUAL	S&P Capital IQ	10/15/2026
COL	consumerPriceInflation	%	N/A	2016	7.51	As reported ACTUAL	S&P Capital IQ	10/15/2026
COL	consumerPriceInflation	%	N/A	2017	4.32	As reported ACTUAL	S&P Capital IQ	10/15/2026
COL	consumerPriceInflation	%	N/A	2018	3.24	As reported ACTUAL	S&P Capital IQ	10/15/2026
COL	consumerPriceInflation	%	N/A	2019	3.52	As reported ACTUAL	S&P Capital IQ	10/15/2026
COL	consumerPriceInflation	%	N/A	2020	2.53	As reported ACTUAL	S&P Capital IQ	09/15/2026
COL	consumerPriceInflation	%	N/A	2021	3.5	As reported ACTUAL	S&P Capital IQ	08/18/2026
COL	consumerPriceInflation	%	N/A	2022	10.18	As reported ACTUAL	S&P Capital IQ	08/18/2026
COL	consumerPriceInflation	%	N/A	2023	11.74	As reported ACTUAL	S&P Capital IQ	09/15/2026
COL	consumerPriceInflation	%	N/A	2024	6.61	As reported ACTUAL	S&P Capital IQ	09/15/2026
COL	consumerPriceInflation	%	N/A	2025	5.14	As reported ACTUAL	S&P Capital IQ	09/15/2026
CRI	nominalGDPLCU	¢B	CRC	2015	30171.92	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	nominalGDPLCU	¢B	CRC	2016	32056.29	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	nominalGDPLCU	¢B	CRC	2017	34343.65	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	nominalGDPLCU	¢B	CRC	2018	36099.88	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	nominalGDPLCU	¢B	CRC	2019	38029.38	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	nominalGDPLCU	¢B	CRC	2020	36735.63	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	nominalGDPLCU	¢B	CRC	2021	40716.61	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	nominalGDPLCU	¢B	CRC	2022	45947.44	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	nominalGDPLCU	¢B	CRC	2023	47611.32	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	nominalGDPLCU	¢B	CRC	2024	49819.17	As reported ACTUAL	S&P Capital IQ	06/15/2026
CRI	nominalGDPLCU	¢B	CRC	2025	51812.3	As reported ACTUAL	S&P Capital IQ	10/15/2026
CRI	consumerPriceInflation	%	N/A	2015	0.8	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	consumerPriceInflation	%	N/A	2016	-0.02	Standardized ACTUAL	S&P Capital IQ	03/17/2026
CRI	consumerPriceInflation	%	N/A	2017	1.63	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	consumerPriceInflation	%	N/A	2018	2.22	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	consumerPriceInflation	%	N/A	2019	2.1	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	consumerPriceInflation	%	N/A	2020	0.72	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	consumerPriceInflation	%	N/A	2021	1.73	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	consumerPriceInflation	%	N/A	2022	8.27	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	consumerPriceInflation	%	N/A	2023	0.53	As reported ACTUAL	S&P Capital IQ	03/17/2026
CRI	consumerPriceInflation	%	N/A	2024	-0.41	Standardized ACTUAL	S&P Capital IQ	06/15/2026
CRI	consumerPriceInflation	%	N/A	2025	-0.07	Standardized ACTUAL	S&P Capital IQ	10/15/2026
ECU	nominalGDPLCU	$B	USD	2015	97.21	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	nominalGDPLCU	$B	USD	2016	97.67	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	nominalGDPLCU	$B	USD	2017	104.47	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	nominalGDPLCU	$B	USD	2018	107.48	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	nominalGDPLCU	$B	USD	2019	107.6	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	nominalGDPLCU	$B	USD	2020	95.87	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	nominalGDPLCU	$B	USD	2021	107.18	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	nominalGDPLCU	$B	USD	2022	116.13	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	nominalGDPLCU	$B	USD	2023	120.79	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	nominalGDPLCU	$B	USD	2024	123.8	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	nominalGDPLCU	$B	USD	2025	130.32	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	consumerPriceInflation	%	N/A	2015	3.97	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	consumerPriceInflation	%	N/A	2016	1.73	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	consumerPriceInflation	%	N/A	2017	0.42	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	consumerPriceInflation	%	N/A	2018	-0.22	Standardized ACTUAL	S&P Capital IQ	06/15/2026
ECU	consumerPriceInflation	%	N/A	2019	0.27	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	consumerPriceInflation	%	N/A	2020	-0.34	Standardized ACTUAL	S&P Capital IQ	06/15/2026
ECU	consumerPriceInflation	%	N/A	2021	0.13	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	consumerPriceInflation	%	N/A	2022	3.47	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	consumerPriceInflation	%	N/A	2023	2.22	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	consumerPriceInflation	%	N/A	2024	1.55	As reported ACTUAL	S&P Capital IQ	06/15/2026
ECU	consumerPriceInflation	%	N/A	2025	0.71	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	nominalGDPLCU	$B	USD	2015	23.44	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	nominalGDPLCU	$B	USD	2016	24.19	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	nominalGDPLCU	$B	USD	2017	24.98	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	nominalGDPLCU	$B	USD	2018	26.02	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	nominalGDPLCU	$B	USD	2019	26.88	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	nominalGDPLCU	$B	USD	2020	24.92	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	nominalGDPLCU	$B	USD	2021	29.04	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	nominalGDPLCU	$B	USD	2022	31.87	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	nominalGDPLCU	$B	USD	2023	33.57	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	nominalGDPLCU	$B	USD	2024	34.88	As reported ACTUAL	S&P Capital IQ	08/25/2026
SLV	nominalGDPLCU	$B	USD	2025	36.71	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	consumerPriceInflation	%	N/A	2015	-0.73	Standardized ACTUAL	S&P Capital IQ	06/15/2026
SLV	consumerPriceInflation	%	N/A	2016	0.6	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	consumerPriceInflation	%	N/A	2017	1.01	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	consumerPriceInflation	%	N/A	2018	1.09	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	consumerPriceInflation	%	N/A	2019	0.07	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	consumerPriceInflation	%	N/A	2020	-0.37	Standardized ACTUAL	S&P Capital IQ	06/15/2026
SLV	consumerPriceInflation	%	N/A	2021	3.47	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	consumerPriceInflation	%	N/A	2022	7.2	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	consumerPriceInflation	%	N/A	2023	4.05	As reported ACTUAL	S&P Capital IQ	06/15/2026
SLV	consumerPriceInflation	%	N/A	2024	0.85	As reported ACTUAL	S&P Capital IQ	08/25/2026
SLV	consumerPriceInflation	%	N/A	2025	0.26	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	nominalGDPLCU	Q.B	GTQ	2015	476.02	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	nominalGDPLCU	Q.B	GTQ	2016	502	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	nominalGDPLCU	Q.B	GTQ	2017	526.51	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	nominalGDPLCU	Q.B	GTQ	2018	551.37	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	nominalGDPLCU	Q.B	GTQ	2019	593.97	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	nominalGDPLCU	Q.B	GTQ	2020	600.12	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	nominalGDPLCU	Q.B	GTQ	2021	668.68	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	nominalGDPLCU	Q.B	GTQ	2022	740.81	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	nominalGDPLCU	Q.B	GTQ	2023	816.86	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	nominalGDPLCU	Q.B	GTQ	2024	878.39	As reported ACTUAL	S&P Capital IQ	08/18/2026
GTM	nominalGDPLCU	Q.B	GTQ	2025	947.01	As reported ACTUAL	S&P Capital IQ	10/15/2026
GTM	consumerPriceInflation	%	N/A	2015	2.39	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	consumerPriceInflation	%	N/A	2016	4.45	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	consumerPriceInflation	%	N/A	2017	4.42	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	consumerPriceInflation	%	N/A	2018	3.75	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	consumerPriceInflation	%	N/A	2019	3.7	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	consumerPriceInflation	%	N/A	2020	3.21	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	consumerPriceInflation	%	N/A	2021	4.26	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	consumerPriceInflation	%	N/A	2022	6.89	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	consumerPriceInflation	%	N/A	2023	6.21	As reported ACTUAL	S&P Capital IQ	06/15/2026
GTM	consumerPriceInflation	%	N/A	2024	2.87	As reported ACTUAL	S&P Capital IQ	08/18/2026
GTM	consumerPriceInflation	%	N/A	2025	1.58	As reported ACTUAL	S&P Capital IQ	10/15/2026
HND	nominalGDPLCU	L.B	HNL	2015	460.41	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	nominalGDPLCU	L.B	HNL	2016	495.92	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	nominalGDPLCU	L.B	HNL	2017	543.4	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	nominalGDPLCU	L.B	HNL	2018	575.28	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	nominalGDPLCU	L.B	HNL	2019	609.83	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	nominalGDPLCU	L.B	HNL	2020	574.04	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	nominalGDPLCU	L.B	HNL	2021	675.93	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	nominalGDPLCU	L.B	HNL	2022	769.49	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	nominalGDPLCU	L.B	HNL	2023	845.21	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	nominalGDPLCU	L.B	HNL	2024	917.08	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	nominalGDPLCU	L.B	HNL	2025	1027.76	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	consumerPriceInflation	%	N/A	2015	3.16	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	consumerPriceInflation	%	N/A	2016	2.72	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	consumerPriceInflation	%	N/A	2017	3.93	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	consumerPriceInflation	%	N/A	2018	4.35	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	consumerPriceInflation	%	N/A	2019	4.37	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	consumerPriceInflation	%	N/A	2020	3.47	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	consumerPriceInflation	%	N/A	2021	4.48	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	consumerPriceInflation	%	N/A	2022	9.09	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	consumerPriceInflation	%	N/A	2023	6.66	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	consumerPriceInflation	%	N/A	2024	4.61	As reported ACTUAL	S&P Capital IQ	06/15/2026
HND	consumerPriceInflation	%	N/A	2025	4.6	As reported ACTUAL	S&P Capital IQ	06/15/2026
NIC	nominalGDPLCU	C$B	NIO	2015	347.71	As reported ACTUAL	S&P Capital IQ	03/17/2026
NIC	nominalGDPLCU	C$B	NIO	2016	380.26	As reported ACTUAL	S&P Capital IQ	03/17/2026
NIC	nominalGDPLCU	C$B	NIO	2017	414.28	As reported ACTUAL	S&P Capital IQ	03/17/2026
NIC	nominalGDPLCU	C$B	NIO	2018	410.99	As reported ACTUAL	S&P Capital IQ	03/17/2026
NIC	nominalGDPLCU	C$B	NIO	2019	420.61	As reported ACTUAL	S&P Capital IQ	03/17/2026
NIC	nominalGDPLCU	C$B	NIO	2020	437.05	As reported ACTUAL	S&P Capital IQ	03/17/2026
NIC	nominalGDPLCU	C$B	NIO	2021	499.75	As reported ACTUAL	S&P Capital IQ	05/15/2026
NIC	nominalGDPLCU	C$B	NIO	2022	560.88	As reported ACTUAL	S&P Capital IQ	05/15/2026
NIC	nominalGDPLCU	C$B	NIO	2023	648.87	As reported ACTUAL	S&P Capital IQ	05/15/2026
NIC	nominalGDPLCU	C$B	NIO	2024	721.36	As reported ACTUAL	S&P Capital IQ	05/15/2026
NIC	nominalGDPLCU	C$B	NIO	2025	814.42	As reported ACTUAL	S&P Capital IQ	05/15/2026
NIC	consumerPriceInflation	%	N/A	2015	4	As reported ACTUAL	S&P Capital IQ	03/17/2026
NIC	consumerPriceInflation	%	N/A	2016	3.52	As reported ACTUAL	S&P Capital IQ	03/17/2026
NIC	consumerPriceInflation	%	N/A	2017	3.85	As reported ACTUAL	S&P Capital IQ	03/17/2026
NIC	consumerPriceInflation	%	N/A	2018	4.95	As reported ACTUAL	S&P Capital IQ	03/17/2026
NIC	consumerPriceInflation	%	N/A	2019	5.38	As reported ACTUAL	S&P Capital IQ	03/17/2026
NIC	consumerPriceInflation	%	N/A	2020	3.68	As reported ACTUAL	S&P Capital IQ	03/17/2026
NIC	consumerPriceInflation	%	N/A	2021	4.93	As reported ACTUAL	S&P Capital IQ	05/15/2026
NIC	consumerPriceInflation	%	N/A	2022	10.47	As reported ACTUAL	S&P Capital IQ	05/15/2026
NIC	consumerPriceInflation	%	N/A	2023	8.39	As reported ACTUAL	S&P Capital IQ	05/15/2026
NIC	consumerPriceInflation	%	N/A	2024	4.63	As reported ACTUAL	S&P Capital IQ	05/15/2026
NIC	consumerPriceInflation	%	N/A	2025	2.08	As reported ACTUAL	S&P Capital IQ	05/15/2026
PAN	nominalGDPLCU	BB	PAB	2015	54.09	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	nominalGDPLCU	BB	PAB	2016	57.91	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	nominalGDPLCU	BB	PAB	2017	62.2	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	nominalGDPLCU	BB	PAB	2018	67.32	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	nominalGDPLCU	BB	PAB	2019	69.78	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	nominalGDPLCU	BB	PAB	2020	57.06	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	nominalGDPLCU	BB	PAB	2021	67.4	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	nominalGDPLCU	BB	PAB	2022	76.48	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	nominalGDPLCU	BB	PAB	2023	83.82	As reported ACTUAL	S&P Capital IQ	10/15/2026
PAN	nominalGDPLCU	BB	PAB	2024	86.56	As reported ACTUAL	S&P Capital IQ	10/15/2026
PAN	nominalGDPLCU	BB	PAB	2025	90.7	As reported ACTUAL	S&P Capital IQ	10/15/2026
PAN	consumerPriceInflation	%	N/A	2015	0.14	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	consumerPriceInflation	%	N/A	2016	0.74	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	consumerPriceInflation	%	N/A	2017	0.88	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	consumerPriceInflation	%	N/A	2018	0.76	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	consumerPriceInflation	%	N/A	2019	-0.36	Standardized ACTUAL	S&P Capital IQ	03/17/2026
PAN	consumerPriceInflation	%	N/A	2020	-1.55	Standardized ACTUAL	S&P Capital IQ	03/17/2026
PAN	consumerPriceInflation	%	N/A	2021	1.63	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	consumerPriceInflation	%	N/A	2022	2.86	As reported ACTUAL	S&P Capital IQ	03/17/2026
PAN	consumerPriceInflation	%	N/A	2023	1.49	As reported ACTUAL	S&P Capital IQ	10/15/2026
PAN	consumerPriceInflation	%	N/A	2024	0.69	As reported ACTUAL	S&P Capital IQ	10/15/2026
PAN	consumerPriceInflation	%	N/A	2025	-0.21	Standardized ACTUAL	S&P Capital IQ	10/15/2026
PRY	nominalGDPLCU	₲T	PYG	2015	188.48	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	nominalGDPLCU	₲T	PYG	2016	204.65	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	nominalGDPLCU	₲T	PYG	2017	219.12	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	nominalGDPLCU	₲T	PYG	2018	230.58	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	nominalGDPLCU	₲T	PYG	2019	236.68	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	nominalGDPLCU	₲T	PYG	2020	239.91	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	nominalGDPLCU	₲T	PYG	2021	270.54	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	nominalGDPLCU	₲T	PYG	2022	292.17	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	nominalGDPLCU	₲T	PYG	2023	314.45	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	nominalGDPLCU	₲T	PYG	2024	338.24	As reported ACTUAL	S&P Capital IQ	07/15/2026
PRY	nominalGDPLCU	₲T	PYG	2025	371.83	As reported ACTUAL	S&P Capital IQ	07/15/2026
PRY	consumerPriceInflation	%	N/A	2015	3.13	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	consumerPriceInflation	%	N/A	2016	4.09	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	consumerPriceInflation	%	N/A	2017	3.6	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	consumerPriceInflation	%	N/A	2018	3.98	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	consumerPriceInflation	%	N/A	2019	2.76	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	consumerPriceInflation	%	N/A	2020	1.77	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	consumerPriceInflation	%	N/A	2021	4.79	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	consumerPriceInflation	%	N/A	2022	9.77	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	consumerPriceInflation	%	N/A	2023	4.63	As reported ACTUAL	S&P Capital IQ	06/15/2026
PRY	consumerPriceInflation	%	N/A	2024	3.84	As reported ACTUAL	S&P Capital IQ	07/15/2026
PRY	consumerPriceInflation	%	N/A	2025	4.04	As reported ACTUAL	S&P Capital IQ	07/15/2026
PER	nominalGDPLCU	S/.B	PEN	2015	619.29	As reported ACTUAL	S&P Capital IQ	08/18/2026
PER	nominalGDPLCU	S/.B	PEN	2016	671.56	As reported ACTUAL	S&P Capital IQ	09/15/2026
PER	nominalGDPLCU	S/.B	PEN	2017	715.87	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	S/.B	PEN	2018	755.47	As reported ACTUAL	S&P Capital IQ	09/15/2026
PER	nominalGDPLCU	S/.B	PEN	2019	788.91	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	S/.B	PEN	2020	733.98	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	S/.B	PEN	2021	892.25	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	S/.B	PEN	2022	952.4	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	S/.B	PEN	2023	1018.13	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	S/.B	PEN	2024	1109.22	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	nominalGDPLCU	S/.B	PEN	2025	1213.9	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	%	N/A	2015	3.55	As reported ACTUAL	S&P Capital IQ	08/18/2026
PER	consumerPriceInflation	%	N/A	2016	3.59	As reported ACTUAL	S&P Capital IQ	09/15/2026
PER	consumerPriceInflation	%	N/A	2017	2.8	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	%	N/A	2018	1.32	As reported ACTUAL	S&P Capital IQ	09/15/2026
PER	consumerPriceInflation	%	N/A	2019	2.14	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	%	N/A	2020	1.83	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	%	N/A	2021	3.98	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	%	N/A	2022	7.88	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	%	N/A	2023	6.26	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	%	N/A	2024	2.35	As reported ACTUAL	S&P Capital IQ	10/15/2026
PER	consumerPriceInflation	%	N/A	2025	1.5	As reported ACTUAL	S&P Capital IQ	10/15/2026
URY	nominalGDPLCU	$B	UYU	2015	1620.07	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	nominalGDPLCU	$B	UYU	2016	1733.77	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	nominalGDPLCU	$B	UYU	2017	1864.14	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	nominalGDPLCU	$B	UYU	2018	2007.73	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	nominalGDPLCU	$B	UYU	2019	2193.67	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	nominalGDPLCU	$B	UYU	2020	2250.2	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	nominalGDPLCU	$B	UYU	2021	2645.46	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	nominalGDPLCU	$B	UYU	2022	2933.06	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	nominalGDPLCU	$B	UYU	2023	3075.19	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	nominalGDPLCU	$B	UYU	2024	3310.43	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	nominalGDPLCU	$B	UYU	2025	3515.52	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	consumerPriceInflation	%	N/A	2015	8.67	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	consumerPriceInflation	%	N/A	2016	9.64	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	consumerPriceInflation	%	N/A	2017	6.22	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	consumerPriceInflation	%	N/A	2018	7.61	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	consumerPriceInflation	%	N/A	2019	7.88	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	consumerPriceInflation	%	N/A	2020	9.76	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	consumerPriceInflation	%	N/A	2021	7.75	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	consumerPriceInflation	%	N/A	2022	9.1	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	consumerPriceInflation	%	N/A	2023	5.87	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	consumerPriceInflation	%	N/A	2024	4.85	As reported ACTUAL	S&P Capital IQ	06/15/2026
URY	consumerPriceInflation	%	N/A	2025	4.65	As reported ACTUAL	S&P Capital IQ	06/15/2026
VEN	nominalGDPLCU	Bs. SB	VES	2015	0.08	As reported ACTUAL	S&P Capital IQ	06/15/2026
VEN	nominalGDPLCU	Bs. SB	VES	2016	0.28	As reported ACTUAL	S&P Capital IQ	06/15/2026
VEN	nominalGDPLCU	Bs. SB	VES	2017	2.01	As reported ACTUAL	S&P Capital IQ	06/15/2026
VEN	nominalGDPLCU	Bs. SB	VES	2018	0	Standardized FORECAST	S&P Capital IQ	03/17/2026
VEN	nominalGDPLCU	Bs. SB	VES	2019	0.31	Standardized FORECAST	S&P Capital IQ	05/22/2026
VEN	nominalGDPLCU	Bs. SB	VES	2020	12.97	Standardized FORECAST	S&P Capital IQ	05/22/2026
VEN	nominalGDPLCU	Bs. SB	VES	2021	213.28	Standardized FORECAST	S&P Capital IQ	06/15/2026
VEN	nominalGDPLCU	Bs. SB	VES	2022	733.24	Standardized FORECAST	S&P Capital IQ	06/15/2026
VEN	nominalGDPLCU	Bs. SB	VES	2023	2172.21	Standardized FORECAST	S&P Capital IQ	06/15/2026
VEN	nominalGDPLCU	Bs. SB	VES	2024	4376.58	Standardized FORECAST	S&P Capital IQ	05/22/2026
VEN	nominalGDPLCU	Bs. SB	VES	2025	16671.53	Standardized FORECAST	S&P Capital IQ	06/15/2026
VEN	consumerPriceInflation	%	N/A	2015	121.89	As reported ACTUAL	S&P Capital IQ	06/15/2026
VEN	consumerPriceInflation	%	N/A	2016	254.82	As reported ACTUAL	S&P Capital IQ	06/15/2026
VEN	consumerPriceInflation	%	N/A	2017	438.12	As reported ACTUAL	S&P Capital IQ	06/15/2026
VEN	consumerPriceInflation	%	N/A	2018	65374.08	As reported ACTUAL	S&P Capital IQ	03/17/2026
VEN	consumerPriceInflation	%	N/A	2019	19906.29	As reported ACTUAL	S&P Capital IQ	05/22/2026
VEN	consumerPriceInflation	%	N/A	2020	2354.79	As reported ACTUAL	S&P Capital IQ	05/22/2026
VEN	consumerPriceInflation	%	N/A	2021	1589.52	As reported ACTUAL	S&P Capital IQ	06/15/2026
VEN	consumerPriceInflation	%	N/A	2022	186.65	As reported ACTUAL	S&P Capital IQ	06/15/2026
VEN	consumerPriceInflation	%	N/A	2023	337.46	As reported ACTUAL	S&P Capital IQ	06/15/2026
VEN	consumerPriceInflation	%	N/A	2024	49.39	As reported ACTUAL	S&P Capital IQ	05/22/2026
VEN	consumerPriceInflation	%	N/A	2025	252.08	As reported ACTUAL	S&P Capital IQ	06/15/2026
```

Key observations on the Standardized flag requirement:

- Rows where the Standardized version IS stored (flag = "Standardized ACTUAL"): USA CPI 2025; CRI CPI 2016, 2024, 2025; ECU CPI 2018, 2020; SLV CPI 2015, 2020; PAN CPI 2019, 2020, 2025.
- VEN nominalGDPLCU 2018–2025: stored as "Standardized FORECAST" — the only forecast-flagged values in the dataset.
- All remaining rows: stored as "As reported ACTUAL" — the Standardized version was not separately stored for those country-year combinations; the as-reported value is what Capital IQ holds and is flagged accordingly per your instructions.
- URY nominalGDPLCU unit is stored as "$B" in Capital IQ (Uruguayan peso billions); reproduced exactly as stored.
- NIC nominalGDPLCU currency is Nicaraguan córdoba (NIO); unit stored as "C$B."
- PAN nominalGDPLCU unit stored as "BB" (Balboa billions).

Disclaimer (ChatIQ, abridged): responses are generated by AI without human review and may be inaccurate or incomplete; the user must verify all information.
