# FX, Interest Rates and Cost of Capital for Valuing Grupo Bimbo (BIMBOA), as of 8-Oct-2026

Research date: 2026-10-08. All quotes are dated. "ECB-derived" means USD crosses computed from European Central Bank reference rates (about 14:15 CET each business day), retrieved via the frankfurter.app API. These are not Banxico FIX rates, but they match Bimbo's reported quarterly averages to within 0.03 MXN (see Q2), so they are a usable proxy. Calculations are labelled [calc]. Assumptions I made, rather than sourced, are labelled [assumption].

## Q1. USD/MXN: spot, 2026 range, averages, forwards, forecasts and drivers

### Takeaway
After trading as strong as about 16.9 in late August and early September 2026, the peso weakened about 6% in September after the Fed hiked. In early October it trades around 17.9–18.2 per USD. The 2026 average so far (about 17.42) is about 10.6% stronger than the same period of 2025 (about 19.48). Consensus now sees about 18.0 at end-2026 and 18.0–18.5 at end-2027. The Banxico–Fed policy gap has narrowed to about 250bp, a record low, which weakens the carry case for the peso.

### Cited Findings
**Spot (early October 2026). Quotes differ by source and time of day:**
- ECB-derived USD/MXN was 18.0127 on 8-Oct-2026, 18.0943 on 7-Oct, 17.9448 on 6-Oct and 18.3350 on 2-Oct. 2-Oct is the 2026 high on this series. — [Frankfurter API (ECB reference rates)](https://api.frankfurter.app/latest?from=USD&to=MXN,CAD,EUR,BRL)
- 8-Oct-2026 close: 18.19 per USD. The peso fell 1.2%, the worst performer in a basket of major currencies, with an intraday high of 18.23. The trigger was Banxico minutes that opened the door to cuts. — [Milenio, 8-Oct-2026](https://www.milenio.com/negocios/cierre-del-dolar-cotizacion-peso-mexicano-hoy-dia-mes-2026)
- 6-Oct-2026 close: 17.92 (Banxico), with the peso up 0.93% on the day. The same article puts the US 10y at 5.25% and the Mexico 10y at 9.54%. — [El Financiero, 6-Oct-2026](https://www.elfinanciero.com.mx/mercados/2026/10/06/peso-dolar-precio-hoy-6-de-octubre-de-2026/). Milenio gave 17.96 for the same close. — [Milenio, 6-Oct-2026](https://www.milenio.com/negocios/precio-del-dolar-hoy-6-octubre-2026-a-cuanto-cotiza-en-vivo-atm)
- The DOF official rate (FIX) is 17.9670 published 7-Oct and 17.9780 published 8-Oct-2026. — [DOF indicadores](https://dof.gob.mx/indicadores.php)
- Early-October peak: about 18.43–18.44 intraday on 1-Oct-2026, described as the weakest level since November 2025. — [Milenio, 6-Oct-2026](https://www.milenio.com/negocios/precio-del-dolar-hoy-6-octubre-2026-a-cuanto-cotiza-en-vivo-atm); [Investing.com USD/MXN historical](https://es.investing.com/currencies/usd-mxn-historical-data)
- **Uncertainty flag:** the 8-Oct values run from 17.98 (FIX published that day, which is the previous day's fix) to 18.01 (ECB, midday Europe) to 18.19 (Milenio close). Use the close for "current spot" and the ECB/FIX series for averages.

**2026 range and averages:**
- 2026 strongest peso: 16.89 on 4-Sep-2026 (El Financiero) and 16.8855 on 5-Sep (Wise). The ECB-derived low is 16.898 on 21-Aug-2026. — [El Financiero Encuesta Citi note, 6-Oct-2026](https://www.elfinanciero.com.mx/mercados/2026/10/06/encuesta-citi-en-cuanto-cerrara-el-tipo-de-cambio-en-2026/); [Wise history](https://wise.com/es/currency-converter/usd-to-mxn-rate/history); [Frankfurter/ECB time series](https://api.frankfurter.app/2025-01-01..2026-10-08?from=USD&to=MXN,CAD,EUR,BRL)
- The peso lost about 6% in September 2026. It was the worst performer against the USD that month and had its worst month since June 2024. — [El Financiero, 6-Oct-2026](https://www.elfinanciero.com.mx/mercados/2026/10/06/encuesta-citi-en-cuanto-cerrara-el-tipo-de-cambio-en-2026/). The daily retail-aggregator series shows 17.00 on 1-Sep and 18.06 on 30-Sep (+6.3%). — [CambioDólar, Sept-2026](https://www.cambiodolar.com.mx/valor-dolar-septiembre-2026.html)
- ECB-derived quarterly average USD/MXN [calc from ECB series]:

| Period | Avg USD/MXN | Bimbo-reported avg (team data) |
|---|---|---|
| 1Q25 | 20.433 | – |
| 2Q25 | 19.510 | 19.54 |
| 3Q25 | 18.640 | 18.65 |
| 4Q25 | 18.314 | 18.31 |
| FY2025 | 19.213 (range 17.90 on 24-Dec to 20.97 on 9-Apr) | – |
| 1Q26 | 17.562 | – |
| 2Q26 | 17.371 | 17.40 |
| 3Q26 | 17.265 | (not yet reported) |
| 4Q26 to date (1–8 Oct) | 18.117 | – |
| 2026 YTD (to 8-Oct) | 17.419 | – |
| Same period 2025 (1-Jan to 8-Oct) | 19.479 | – |

  Source: [Frankfurter/ECB time series](https://api.frankfurter.app/2025-01-01..2026-10-08?from=USD&to=MXN,CAD,EUR,BRL). End-2025 ECB-derived rate: 17.97 (31-Dec-2025).
- Cross-check: the retail-aggregator monthly averages for 2026 are Mar 17.81, Apr 17.46, May 17.32, Jun 17.39, Jul 17.47, Aug 17.07 and Sep 17.23. On that series 2Q26 is 17.39 and 3Q26 is 17.26 [calc, calendar days including weekends]. — [CambioDólar monthly pages, e.g. Sept-2026](https://www.cambiodolar.com.mx/valor-dolar-septiembre-2026.html)
- 2025 average per CEFP (Banxico data): 19.2614 through 11-Dec-2025, against 18.2285 in the same span of 2024. — [CEFP, Dec-2025](https://www.cefp.gob.mx/ixDOCs/2017/261-251212.pdf)

**Forecasts:**
- Encuesta Citi (published 6-Oct-2026). End-2026 median is 18.00 (range 16.80–18.80), up 50 centavos from early September. End-2027 median is 18.50 (range 17.00–19.80), up from 18.00 two weeks earlier. — [El Financiero, 6-Oct-2026](https://www.elfinanciero.com.mx/mercados/2026/10/06/encuesta-citi-en-cuanto-cerrara-el-tipo-de-cambio-en-2026/)
- The previous Encuesta Citi (late Sept-2026) had end-2026 at 17.50 and end-2027 cut from 18.07 to 18.00. — [La Jornada, 22-Sep-2026](https://www.jornada.com.mx/noticia/2026/09/22/economia/encuesta-citi-mejora-la-proyeccion-de-crecimiento-para-este-ano-a-14)
- Banxico Encuesta de Especialistas, September 2026 (responses 15–28 Sep). End-2026: median 17.50, mean 17.57. End-2027: median 18.04, mean 18.11. — [Revista Fortuna, 6-Oct-2026](https://revistafortuna.com.mx/2026/10/06/corrigen-analistas-al-alza-estimacion-de-tipo-de-cambio-para-2026-y-2027-tasas-de-interes-permanecerian-en-6-50-sondeo/); [IDC Online, 6-Oct-2026](https://idconline.mx/finanzas/2026/10/06/expectativas-banxico-2026-2027-tasas-de-interes-tipo-de-cambio-e-inflacion-para-el-cierre-de-ano). Most responses predate the late-September sell-off.
- Banorte (24-Aug-2026 revision). End-2026 cut to 17.30 from 18.10, end-2027 to 17.45 from 18.50. Average 17.28 for 2026 and 17.08 for 2027. This is about 45 days old and predates the September sell-off. — [El Cronista](https://www.cronista.com/mexico/dolar-peso-mexicano/banorte-recalibra-sus-apuestas-preve-un-super-peso-aun-mas-fuerte-frente-al-dolar/); [Yahoo/El Universal](https://es-us.finanzas.yahoo.com/noticias/prev%C3%A9n-superpeso-fortaleza-2026-2027-060000994.html)
- BBVA Research: end-2026 at 17.80 (18-Jun-2026, updated 7-Jul-2026), from an aggregator rather than the primary source. — [exchangerate.dev](https://exchangerate.dev/forecast/usd-mxn-2026). Banamex, BBVA and Scotiabank earlier saw end-2026 below 18. — [El CEO](https://elceo.com/economia/banamex-bbva-scotiabank-dolar-cerrara-2026-debajo-18-pesos)
- Search snippets attribute Banamex 18.1 (2026) / 18.5 (2027) and Hacienda's Paquete Económico 17.8 (2026) / 18.0 (2027) to [Bloomberg Línea](https://www.bloomberglinea.com/latinoamerica/mexico/analistas-ajustan-al-alza-pronostico-para-el-dolar-en-mexico-y-ven-sin-cambios-tasa-de-interes/). I did not open that article, so these figures are unverified. Milenio separately says "Hacienda projects an average of 19.3 for 2026", which looks like the old Sept-2025 Paquete assumption. — [Milenio, 8-Oct-2026](https://www.milenio.com/negocios/cierre-del-dolar-cotizacion-peso-mexicano-hoy-dia-mes-2026)

**Forward points (not a market quote):** see Inferences.

**Drivers:**
- The Fed hiked on 16-Sep-2026 while Banxico held, leaving a policy-rate differential of about 250bp, a historical low. — [El Financiero, 6-Oct-2026](https://www.elfinanciero.com.mx/mercados/2026/10/06/encuesta-citi-en-cuanto-cerrara-el-tipo-de-cambio-en-2026/)
- XTB puts the 10y spread at about 9.5% (Mexico) against about 5.3% (US), roughly 4.2pp, down from about 4.6pp a year ago, which weakens carry. The DXY reached 102.5, its highest since April 2025. Banco Base cites a 0.81 correlation with the US 10y. — [XTB](https://www.xtb.com/lat/analisis-y-noticias/analisis-de-mercado/puede-el-peso-mexicano-enfrentar-nuevos-problemas-por-el-alza-de-los-rendimientos-globales)
- Banxico minutes (8-Oct-2026) opened the door to cuts if inflation eases, and the peso fell 1.2% that day. A technical analyst (Rankia) sees support at 17.90–18.00 and resistance at 18.23–18.46. — [Milenio, 8-Oct-2026](https://www.milenio.com/negocios/cierre-del-dolar-cotizacion-peso-mexicano-hoy-dia-mes-2026)
- Risk-off episodes are tied to the Iran war and oil, with Brent above or near $100. A weak US September payrolls report reduced Fed-hike bets on 6-Oct. — [El Financiero, 6-Oct-2026](https://www.elfinanciero.com.mx/mercados/2026/10/06/peso-dolar-precio-hoy-6-de-octubre-de-2026/)
- USMCA (T-MEC) review: USTR confirmed there will be no 16-year extension in 2026, so the treaty stays on annual reviews. The public-comment period runs 2-Oct-2026 to 12-Jan-2027. The 4th bilateral round was postponed to October, and rules of origin and labour issues were pushed to 2027. — [Proceso, 5-Oct-2026](https://www.proceso.com.mx/economia/2026/10/5/eu-cierra-la-puerta-a-extender-por-16-anos-mas-el-t-mec-en-2026-lleva-la-revision-a-2027-381260.html); [La Razón, 6-Oct-2026](https://www.razon.com.mx/negocios/2026/10/06/estados-unidos-lanza-convocatoria-para-revision-del-t-mec-2027/); [La Jornada, 24-Sep-2026](https://www.jornada.com.mx/2026/09/24/economia/018n1eco?partner=rss)
- Tariffs: Mexico says it is close to a deal to lower Section 232 tariffs on autos. The size of any cut to the 50% steel tariff is unknown. — [El Financiero, 1-Oct-2026](https://www.elfinanciero.com.mx/economia/2026/10/01/revision-del-t-mec-mexico-esta-cerca-de-acuerdo-con-eu-para-bajar-aranceles-a-autos-y-acero/)

### Inferences
- **Indicative 12-month forward** [calc, covered interest parity, not a dealer quote]: F = S × (1 + i_MXN) / (1 + i_USD). With S = 18.01 (ECB, 8-Oct), i_MXN ≈ 6.50–6.60% (Banxico target / TIIE de fondeo) and i_USD ≈ 3.88–3.90% (fed funds midpoint / SOFR), F ≈ **18.47–18.48**. That is forward points of about +0.45–0.47 MXN, or about 2.5%. The 2026 consensus end-2027 level (18.50) is essentially the forward, so consensus no longer predicts peso outperformance against carry.
- The 2026 range in daily reference rates is about 16.9–18.3, with intraday prints up to about 18.44.
- With Banxico leaning toward cuts and the Fed toward hikes, the carry cushion is thinning. Risks to the peso skew toward weakness (Citi's top-end 2027 forecast is 19.80). Upside comes from a USMCA/232 deal or lower oil.

### Gaps
- No market-quoted USD/MXN 12m forward points or NDF were found. The forward above is a CIP approximation.
- No current Goldman Sachs, JPMorgan or Bloomberg-consensus USD/MXN forecasts for 2026–2028 were found. No 2028 forecasts were found from any source.
- The official Banxico FIX quarterly averages were not retrieved directly from SIE; the ECB-derived series is used as a proxy.

## Q2. Translation impact on Bimbo's reported results (3Q26, 4Q26, 2027)

### Takeaway
FX translation was about a -6.7pp drag on sales growth in 2Q26. It should fall to about -4.5pp in 3Q26 (USD/MXN -7.4% YoY) and to about -1 to -2pp in 4Q26 at current spot. On the consensus path (Citi), translation turns into a +2–3pp tailwind in 2027. Bimbo's consolidated reported MXN growth should therefore converge toward organic growth over the next 2–3 quarters.

### Cited Findings
- Team data: Bimbo's quarterly average USD/MXN was 19.54 in 2Q25 and 17.40 in 2Q26 (-10.9%), 18.65 in 3Q25 and 18.31 in 4Q25. Reported 2Q26 sales were -2.2% against +4.5% excluding FX. The ECB-derived averages match: 2Q25 19.51, 2Q26 17.37, 3Q25 18.64, 4Q25 18.31. — [Frankfurter/ECB series](https://api.frankfurter.app/2025-01-01..2026-10-08?from=USD&to=MXN,CAD,EUR,BRL)
- ECB-derived quarterly average crosses (MXN per unit) [calc]:

| Cross | 2Q25 | 2Q26 | YoY | 3Q25 | 3Q26 | YoY | 4Q25 | Spot 8-Oct-26 | Spot vs 4Q25 |
|---|---|---|---|---|---|---|---|---|---|
| USD/MXN | 19.510 | 17.371 | -11.0% | 18.640 | 17.265 | **-7.4%** | 18.314 | 18.013 | **-1.6%** |
| CAD/MXN | 14.085 | 12.548 | -10.9% | 13.535 | 12.332 | -8.9% | 13.125 | 12.630 | -3.8% |
| EUR/MXN | 22.113 | 20.200 | -8.7% | 21.772 | 19.861 | -8.8% | 21.306 | 20.149 | -5.4% |
| BRL/MXN | 3.445 | 3.443 | -0.1% | 3.418 | 3.361 | -1.7% | 3.398 | 3.591 | +5.7% |

  Source: [Frankfurter/ECB series](https://api.frankfurter.app/2025-01-01..2026-10-08?from=USD&to=MXN,CAD,EUR,BRL). Current cross levels (ECB, 8-Oct-2026): CAD/MXN 12.63, EUR/MXN 20.15, BRL/MXN 3.59. — [Frankfurter latest](https://api.frankfurter.app/latest?from=USD&to=MXN,CAD,EUR,BRL)
- Full year: 2025 average USD/MXN was 19.21 and 2026 YTD is 17.42 (to 8-Oct). CAD/MXN averaged 13.74 in 2025 against 12.56 in 2026 YTD. EUR/MXN averaged 21.67 against 20.20. — [Frankfurter/ECB series](https://api.frankfurter.app/2025-01-01..2026-10-08?from=USD&to=MXN,CAD,EUR,BRL)
- Forecast inputs: Citi end-2026 18.00 and end-2027 18.50. Banxico survey 17.50 and 18.04. Banorte averages 17.28 (2026) and 17.08 (2027). — sources in Q1.

### Inferences
**Method** [calc, my approach]: translation effect on consolidated sales ≈ Σ (segment sales share × YoY change in that currency's average rate against MXN). Shares are North America 43% (USD/CAD), EAA 13% (EUR proxy), LatAm 11% and Mexico 34% (no translation). Two simplifications: North America is weighted to USD at 90% and CAD at 10% [assumption], and LatAm translation is proxied at half the BRL change plus a small negative for other LatAm currencies [assumption].

- **Back-test, 2Q26:** 0.43 × (0.9 × -11.0% + 0.1 × -10.9%) + 0.13 × -8.7% + 0.11 × (about -3%) = -4.73 - 1.13 - 0.33 ≈ **-6.2pp**. The actual gap was -6.7pp (-2.2% reported against +4.5% ex-FX). The method captures roughly 90%+ of the effect, so it is good enough for estimates.
- **3Q26 (actual averages):** USD -7.4%, CAD -8.9%, EUR -8.8%, BRL -1.7%.
  - 0.43 × (0.9 × -7.4 + 0.1 × -8.9) = 0.43 × -7.55 = -3.25pp
  - EAA: 0.13 × -8.8 = -1.14pp
  - LatAm: 0.11 × about -1.5 = -0.17pp
  - **Total ≈ -4.6pp.** If organic growth stays near +4.5%, reported 3Q26 sales would be about flat (≈ 0% YoY).
- **4Q26 scenarios** (4Q25 base 18.31; 1–8 Oct already averages 18.12):
  - Spot flat at about 18.0 → 4Q avg ≈ 18.02 → USD -1.6%. Crosses at spot: CAD -3.8%, EUR -5.4%, BRL +5.7%. Total ≈ 0.43 × -1.8 + 0.13 × -5.4 + 0.11 × +2 ≈ -0.77 - 0.70 + 0.22 ≈ **-1.3pp**.
  - Citi path (18.0 end-2026) ≈ same as spot → about -1.3pp.
  - Banxico-survey path (glide to 17.50 by December) → 4Q avg ≈ 17.8 → USD -2.8% → total ≈ **-2pp**.
  - Banorte (17.30) → 4Q avg ≈ 17.65 → USD -3.6% → total ≈ **-2.5pp**.
  - Bear case (Citi high 18.80) → 4Q avg ≈ 18.4 → USD +0.5% → total ≈ **0 to +0.3pp**.
- **FY2026 average:** Jan–Sep ECB average ≈ 17.40, plus 4Q ≈ 18.0, gives a FY2026 average ≈ **17.55**. Against 2025's 19.21 that is **-8.6%** for USD/MXN, or about -5.5pp on consolidated FY2026 sales growth (0.43 × 8.6 + 0.13 × about 7 + small LatAm).
- **2027 scenarios** (2026 avg ≈ 17.55):
  - Citi path (18.0 → 18.5) → 2027 avg ≈ 18.25 → USD **+4.0%** → about +2.6pp translation tailwind if crosses track the USD.
  - Banxico survey (17.5 → 18.04) → avg ≈ 17.8 → **+1.4%** → about +0.9pp.
  - Banorte avg 17.08 → **-2.7%** vs 17.55 (-1.2% vs Banorte's own 2026 avg of 17.28) → about -0.8 to -1.8pp.
  - CIP forward path (18.0 → 18.47) → avg ≈ 18.25 → **+4.0%**.
  - The consensus and forward-implied view is a modest MXN-translation tailwind in 2027, a reversal of the 2025–2026 headwind.
- The same percentages apply roughly to EBITDA and to USD-denominated debt and interest translation. North America's EBITDA weight is above its sales weight (not verified here), so EBITDA translation is likely somewhat larger in absolute terms. A weaker peso also raises MXN-reported net debt (about 38% of debt was USD at Dec-2023 per the team wiki).

### Gaps
- The exact USD/CAD split inside North America and the currency mix inside LatAm and EAA are not in my sources, so the weights are assumptions. Bimbo's own "ex-FX" disclosure also captures hyperinflation adjustments (e.g. Argentina) that this method ignores.
- 3Q26 results were not yet reported as of 8-Oct-2026, so the 3Q26 estimate cannot be checked against actuals.

## Q3. Fed and US rates: policy rate, 2026 decisions, SEP, market path, 10y, CPI

### Takeaway
The Fed (Chair Kevin Warsh) moved from three cuts in late 2025 to five holds in 2026 and then a 25bp hike on 16-Sep-2026, to 3.75–4.00%. The September SEP median sees 4.1% at end-2026 and end-2027 (one more hike), 3.9% in 2028 and 3.2% longer run. The US 10y is about 5.2–5.3%, its highest since 2002, and August CPI was 3.4%.

### Cited Findings
- 16-Sep-2026: the FOMC raised the target range 25bp to 3.75–4.00%. It was the first hike since July 2023 and was unanimous. — [CNBC, 16-Sep-2026](https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html) (headline accessed via search; the page returned 403); [Chase](https://www.chase.com/personal/investments/learning-and-insights/article/federal-reserve-raises-rates-officials-signal-one-more-hike-in-2026); [PNC](https://www.pnc.com/content/dam/pnc-com/pdf/aboutpnc/EconomicReports/EconomicUpdates/2026/PNC_Economics_Research_FOMC_Statement_16_September_2026.pdf)
- 2026 path: the Fed held at 3.50–3.75% for five straight meetings through 29-Jul-2026 (July vote 9-3, June 12-0). Before that, three consecutive cuts from Sep-2025 brought it to 3.50–3.75%. June 2026 was Warsh's first meeting as Chair. — [Advisor Perspectives, 29-Jul-2026](https://www.advisorperspectives.com/dshort/updates/2026/07/29/feds-interest-rate-decision-july-29-2026); [Advisor Perspectives, 17-Jun-2026](https://advisorperspectives.com/dshort/updates/2026/06/18/feds-interest-rate-decision-june-17-2026)
- **September 2026 SEP medians** (central tendency in parentheses):
  - Fed funds: 2026 4.1 (4.1–4.4); 2027 4.1 (3.6–4.4); 2028 3.9 (3.1–4.1); 2029 3.6; longer run 3.2.
  - PCE inflation: 2026 3.7; 2027 2.3; 2028 2.1. Core PCE: 2026 3.4; 2027 2.5.
  - GDP: 2.3 / 2.4 / 2.2. Unemployment: 4.1.
  - — [Federal Reserve SEP table, 16-Sep-2026](https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm)
- 16 of 18 participants expected another hike and two saw the cycle ending; the 2026 median rose to 4.10% from 3.80% in June. — [Raisin](https://www.raisin.com/en-us/news/fed-decision-dot-plot-breakdown-september-2026/); [KuCoin summary](https://www.kucoin.com/blog/september-2026-fomc-fed-hikes-25-bp-hawkish-dot-plot-is-this-a-new-hiking-cycle) (secondary sources).
- Market pricing (around 8-Oct-2026): about 18% odds of a hike at the 27–28 Oct FOMC and about 82% hold. — [Investing.com Fed Rate Monitor](https://www.investing.com/central-banks/fed-rate-monitor)
- Markets price one more 25bp hike in December. — [iShares Fed outlook](https://www.ishares.com/us/insights/portfolio-insights/fed-outlook-rates-kevin-warsh-fixed-income-2026)
- JPMorgan forecasts a December hike, with the next move around Sep-2027 and risks of an earlier one. — [J.P. Morgan](https://www.jpmorgan.com/insights/global-research/economy/fed-rate-cuts)
- A tracker cited in search results said futures price about 4.1% by Jan-2027 and about 4.7% by Oct-2027 (as of 7-Oct close). I could not confirm the source, so treat this as unverified. — [streetstats.finance](https://streetstats.finance/rates/fedfunds)
- September payrolls came in at just +29k, which reduced hike odds. — [Investing.com Fed Rate Monitor](https://www.investing.com/central-banks/fed-rate-monitor); [El Financiero, 6-Oct-2026](https://www.elfinanciero.com.mx/mercados/2026/10/06/peso-dolar-precio-hoy-6-de-octubre-de-2026/)
- **US 10y Treasury quotes:**
  - 5.229% on 8-Oct-2026 (morning, down more than 4bp) after its highest level since 2002 earlier that week. — [CNBC, 8-Oct-2026](https://www.cnbc.com/2026/10/08/us-treasury-yields-30-year-bond-auction.html); [FXStreet ES, 7-Oct-2026](https://www.fxstreet.es/analysis/el-rendimiento-del-bono-del-tesoro-estadounidense-a-10-anos-acaba-de-alcanzar-un-maximo-no-visto-desde-2002-le-dara-al-dolar-estadounidense-su-proximo-impulso-202610071925)
  - 5.28% on 7-Oct. — [Forbes](https://www.forbes.com/advisor/investing/treasury-rates/)
  - 5.25% on 6-Oct. — [El Financiero](https://www.elfinanciero.com.mx/mercados/2026/10/06/peso-dolar-precio-hoy-6-de-octubre-de-2026/)
  - Intraday vs close differences explain the 5.23–5.28% spread.
- 10y forecasts: the latest strategist benchmark found is a Reuters poll cited mid-August 2026, with medians of 4.50% in 3 months and 4.34% in 12 months and 82% seeing upside risk. Yields have since overshot it. One Seeking Alpha author argued for 6% by end-2026. — [Trading Economics](https://tradingeconomics.com/united-states/government-bond-yield/news/584057); [Seeking Alpha](https://seekingalpha.com/article/4906125-3-forces-to-push-10-year-treasury-rate-to-6-percent-in-2h-2026)
- US CPI August 2026 (released 11-Sep): headline 3.4% YoY, core 2.4%, +0.4% m/m driven by gasoline. — [PNC CPI note, 11-Sep-2026](https://www.pnc.com/content/dam/pnc-com/pdf/aboutpnc/EconomicReports/EconomicUpdates/2026/PNC_Economics_Research_CPI_11_September_2026.pdf); [macronest](https://macronest.online/indicators/us-cpi-inflation)
- September CPI is due 14-Oct-2026. The Cleveland Fed nowcast (7-Oct) is 3.60% headline and 2.39% core. — [Admiral Markets preview](https://admiralmarkets.com/analytics/traders-blog/us-cpi-preview-september-2026-forecasts-and-the-core-cpi-outlook)

### Inferences
- The USD risk-free rate for a USD WACC is about 5.2–5.3%, well above the 2025 average. The curve is steep: 10y about 5.25% against fed funds about 3.9%, roughly 135bp, which points to term premium and fiscal and oil-inflation risk rather than policy expectations alone.
- **Data inconsistency to flag:** the SEP shows 2026 core PCE at 3.4%, while reported core CPI is 2.4%. Core PCE normally runs below core CPI, so one of these figures (likely the secondary-source core CPI) may be misreported. Verify with BLS and BEA before use.

### Gaps
- No primary CME FedWatch snapshot or SOFR-futures strip was retrieved, so the 2027 market path is unverified.
- No current (October 2026) bank or consensus forecasts for the US 10y at end-2026, 2027 or 2028 were found.

## Q4. Banxico: policy rate, 2026 decisions, guidance, terminal rate, M-bono 10y, real rates

### Takeaway
Banxico cut to 6.50% on 7-May-2026 (3-2 vote) and called the end of the easing cycle that began in March 2024. It has held since, including unanimously on 24-Sep-2026, and said it will not mechanically follow the Fed. The 8-Oct minutes reveal a split that leans toward cuts. Consensus sees 6.50% through end-2027. The 10y M-bono is about 9.3–9.5% and the ex-ante real policy rate about 2.6–2.7%.

### Cited Findings
- 7-May-2026: Banxico cut 25bp to 6.50% (effective 8-May) by a 3-2 vote. Heath and Borja wanted to hold at 6.75%. The cut ended the cycle started in March 2024. Reasons given were the FX level, weak activity (1Q26 GDP contraction) and no demand pressure; the inflation balance of risks is still tilted up. — [Proceso, 7-May-2026](https://www.proceso.com.mx/economia/2026/5/7/con-dos-votos-en-contra-banxico-baja-la-tasa-650-concluye-ciclo-de-recortes-373610.html); [El Financiero, 8-May-2026](https://www.elfinanciero.com.mx/economia/2026/05/08/banxico-concluye-ciclo-de-recortes-a-la-tasa-de-referencia-queda-en-65-por-ciento/)
- 24-Sep-2026: Banxico held at 6.50% unanimously, saying policy "would not have to react mechanically" to Fed moves. Headline inflation went from 3.10% (1H-Jul) to 3.42% (1H-Sep); core went from 3.95% to 3.79%. USD/MXN rose about 1.2% to 17.72 after the decision. — [Infobae, 24-Sep-2026](https://www.infobae.com/america/agencias/2026/09/24/banxico-mantiene-tasa-de-interes-en-el-65-y-condiciona-futuras-decisiones-a-la-inflacion/); [El Financiero, 24-Sep-2026](https://www.elfinanciero.com.mx/economia/2026/09/24/tasa-del-banxico-hoy-24-de-septiembre-2026-en-cuanto-quedo/); [Yahoo/Investing](https://es-us.finanzas.yahoo.com/noticias/banxico-deja-tasa-inter%C3%A9s-6-193043710.html)
- Count discrepancy: Expansión calls this the fourth consecutive hold, while Investing/Rio Times say the third. — [Expansión](https://expansion.mx/economia/2026/09/24/banxico-tasa-de-interes-de-referencia-6-5-septiembre); [Rio Times](https://www.riotimesonline.com/banxico-holds-rates-6-5-percent-september-2026/)
- Minutes (8-Oct-2026): Milenio says 3 of 5 members considered possible future cuts. El Financiero describes a "schism", with two members ruling out a cut and two seeing room to evaluate one. — [Milenio](https://www.milenio.com/negocios/cierre-del-dolar-cotizacion-peso-mexicano-hoy-dia-mes-2026); [El Financiero, 8-Oct-2026](https://www.elfinanciero.com.mx/economia/2026/10/08/cisma-en-el-banxico-por-bajar-o-no-la-tasa-de-interes-debemos-estar-abiertos-a-la-discusion/)
- Expectations:
  - Banxico survey (Sep-2026): 6.50% at end-2026 and end-2027 (median). Inflation is expected at 3.87% for 2026 (median) and about 3.82% for 2027. GDP 2026 was raised to 1.40%. — [Pymenoticias](https://www.pymenoticias.com/post/encuesta-banxico-expectativas-pib-tasa-pymes); [FXStreet ES, 1-Oct-2026](https://www.fxstreet.es/news/la-encuesta-de-banxico-preve-una-menor-inflacion-un-crecimiento-mas-solido-y-mantener-la-tasa-en-el-650-202610011734)
  - Encuesta Citi (6-Oct): end-2027 median 6.50% (range 6.0–7.25%). Of 37 respondents, 25 see no change, 6 a 25bp hike and 5 a 25bp cut. — [El Financiero](https://www.elfinanciero.com.mx/mercados/2026/10/06/encuesta-citi-en-cuanto-cerrara-el-tipo-de-cambio-en-2026/)
  - Banamex and Banorte expect 6.50% through end-2027. — [Proceso](https://www.proceso.com.mx/economia/2026/5/7/con-dos-votos-en-contra-banxico-baja-la-tasa-650-concluye-ciclo-de-recortes-373610.html)
  - One forecast sees a possible 25bp hike at end-2027. — [El Financiero, 25-Sep-2026](https://www.elfinanciero.com.mx/economia/2026/09/25/banxico-se-desmarca-de-la-fed-y-mantiene-tasa-de-interes-en-65-por-ciento/)
- Mexico inflation: August 2026 headline 3.26%, core 3.88% (lowest since Mar-2025). July headline was 3.12%. — [México ¿cómo vamos?, Sep-2026](https://mexicocomovamos.mx/wp-content/uploads/2026/09/20260909_PublicacionMCV_inflacion_Ago26.pdf); [Zeta Tijuana](https://zetatijuana.com/2026/08/inflacion-anual-se-ubico-en-3-12-en-julio-de-2026-su-menor-nivel-en-el-ano/). September headline "accelerated, less than expected", with core still easing (Milenio, 8-Oct); the exact print was not found.
- **10y M-bono quotes:**
  - 9.32% on 8-Oct-2026 (-7bp); 20y at 9.76%. — [Milenio](https://www.milenio.com/negocios/cierre-del-dolar-cotizacion-peso-mexicano-hoy-dia-mes-2026)
  - 9.54% on 6-Oct. — [El Financiero](https://www.elfinanciero.com.mx/mercados/2026/10/06/peso-dolar-precio-hoy-6-de-octubre-de-2026/)
  - 9.51% on 2-Oct. — [Trading Economics](https://es.tradingeconomics.com/mexico/government-bond-yield)
  - 9.64% on 29-Sep, a 1-year high. — [Trading Economics](https://es.tradingeconomics.com/mexico/government-bond-yield)

### Inferences
- Ex-ante real policy rate ≈ 6.50% - 3.85% (2026 inflation expectations) ≈ **2.65%**, or 6.50% - 3.82% ≈ 2.7% against 2027 expectations [calc]. That is still restrictive, but only mildly against estimates of the neutral rate (not sourced here).
- Real 10y ≈ 9.32% - about 3.8% ≈ **5.5%** [calc, using short-horizon inflation expectations as a rough proxy; long-term expectations or the Udibono yield would be better]. This is a high real yield, which is why a 50–100bp compression is plausible if the Fed/US 10y stabilise.
- Mexico–US 10y spread ≈ 9.32% - 5.23% ≈ **4.1pp** (8-Oct) [calc].
- Terminal rate: 6.50% is the consensus terminal for this cycle. The internal debate is now about whether to cut further, which is FX-negative, against Fed-driven pressure to hold or hike.

### Gaps
- The full list of 2026 Banxico meeting dates and decisions (Feb, Mar, Jun, Aug) was not individually verified. The May cut to 6.50% from 6.75% implies a cut earlier in 2026 or late 2025 that was not checked.
- Udibono (real) 10y yield and Banxico's neutral-rate estimate were not found.
- The September 2026 INPC print (released around 8–9 Oct) was not found.

## Q5. Mexico country risk: CDS, EMBI, ratings, Pemex

### Takeaway
Mexico was downgraded by Moody's to Baa3 (stable) in May 2026, and S&P moved to a negative outlook. Fitch is at BBB- stable, so Mexico is one notch above high yield at two agencies. The 5y CDS nonetheless sits at about 80–100bp, near multi-year lows (around 120bp in Oct-2024), with a jump to about 98bp at the start of October. Pemex support is the key fiscal drag cited by the agencies.

### Cited Findings
- **5y CDS:**
  - 97.69bp on 1-Oct-2026 (+4.27% that day); 52-week range 77.55–113.79bp. — [Investing.com Mexico CDS 5Y](https://www.investing.com/rates-bonds/mexico-cds-5-years-usd-historical-data)
  - 82.32bp in week 37 of 2026 (mid-September). — [MacroMicro](https://en.macromicro.me/series/27134/mexico-5year-cds)
  - About 80bp in late August 2026, against about 120bp when President Sheinbaum took office in Oct-2024 (per Hacienda). BofA says Mexican debt yields 39bp more than similarly rated peers, i.e. bonds trade about 1.5 notches below the ratings. — [Bloomberg Línea](https://www.bloomberglinea.com/latinoamerica/mexico/mexico-destaca-mejora-de-cds-pese-a-que-sus-bonos-cotizan-como-basura/)
  - The 5-year high was about 310bp (2020), cited in an April 2025 note. — [Monex, 28-Apr-2025](https://www.monex.com.mx/portal/download/reportes/280425%20CDS%20Mexico.pdf)
- Mexico **10y** CDS was 1.59% on 30-Jun-2026 (1.46% net of the Swiss CDS). — [Damodaran ctrypremJuly26.xlsx](https://pages.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJuly26.xlsx)
- **Sovereign ratings:**
  - Moody's downgraded Mexico from Baa2 to Baa3 on 20-May-2026 and changed the outlook from negative to stable. It cited persistent fiscal weakening, a limited revenue base, rigid spending and continued Pemex support. — [Mundi](https://mundi.io/finanzas/calificacion-de-moodys-para-mexico-baa3-en-2026/); [Blackwood LCG](https://blackwoodlcg.com/Articulo-Calificacion-Moodys-Mexico-2026.html)
  - S&P moved Mexico's outlook from stable to negative in May 2026 (law-firm summary; verify with S&P). Damodaran's July-2026 sheet lists S&P BBB / BBB- for Mexico (columns likely FC/LC). — [Blackwood LCG](https://blackwoodlcg.com/Articulo-Calificacion-Moodys-Mexico-2026.html); [Damodaran workbook](https://pages.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJuly26.xlsx)
  - Fitch: BBB-, stable. — [Blackwood LCG](https://blackwoodlcg.com/Articulo-Calificacion-Moodys-Mexico-2026.html)
- **Pemex:**
  - Moody's affirmed B1 stable (May 2026) and expects about USD 14.9bn of annual financing needs over 2026–2028; it says "government support will remain determinant". — [El Financiero, 22-May-2026](https://www.elfinanciero.com.mx/economia/2026/05/22/pemex-se-salva-de-ser-reprobado-por-moodys-su-calificacion-queda-en-b1-con-perspectiva-estable/); [La Jornada](https://www.jornada.com.mx/2026/05/23/economia/014n1eco)
  - Fitch affirmed BB+ stable (Sep-2026), with leverage expected to average about 7.0x and a standalone profile of "ccc". — [Crónica, 25-Sep-2026](https://www.cronica.com.mx/nacional/2026/09/25/fitch-ratifica-calificacion-crediticia-de-pemex-en-bb-con-perspectiva-estable/)
  - Moody's warned that Pemex support raises sovereign debt. — [Energy Magazine, Feb-2026](https://energymagazine.mx/2026/02/moodys-advierte-que-apoyo-a-pemex-eleva-la-deuda-y-presiona-las-finanzas-de-mexico/)

### Inferences
- Market pricing (CDS about 80–100bp) is tighter than the Baa3/BBB- ratings would imply. That favours the CDS-based country risk premium (2.27%) over the rating-based one (2.72%) in Damodaran's framework, but the gap could close if S&P downgrades. That is a plausible 2027 event given the negative outlook.
- A downgrade to high yield by two agencies would hit index-eligibility flows and is the main tail risk for Mexican rates and the peso.

### Gaps
- No current JPMorgan EMBI Mexico spread was found.
- The S&P outlook change and its exact date were not confirmed from an S&P press release.

## Q6. Equity risk premium inputs and Mexican equity market

### Takeaway
Damodaran's July-2026 update gives a mature-market ERP of 4.20% (US 4.42%). For Mexico (Baa3) it gives a country risk premium of 2.72% (rating-based, total ERP 6.92%) or 2.27% (CDS-based, total ERP 6.47%), up from 2.46% / 6.69% in January 2026 after the Moody's downgrade. The S&P/BMV IPC is roughly flat YTD at about 65,000. Bimbo trades at about 6.3x EV/EBITDA and 17x NTM P/E, well below its 10-year means (7.8x and 21.0x).

### Cited Findings
- **Damodaran July 2026** (data date 1-Jul-2026; default spreads corrected 9-Jul-2026). — [ctrypremJuly26.xlsx](https://pages.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJuly26.xlsx); [Musings on Markets, 15-Jul-2026](https://aswathdamodaran.blogspot.com/2026/07/country-risk-drivers-measures-and.html)
  - Mature-market ERP is 4.20% (S&P 500 implied ERP of 4.42% on 1-Jul-2026, index 7,499.36, less the 0.22% US Aa1 default spread). The equity/bond volatility multiplier is 1.5545.
  - Mexico (Moody's Baa3): rating-based default spread 1.75%, CRP **2.72%**, total ERP **6.92%**. CDS-based: CDS net of Swiss 1.46%, CRP **2.27%**, total ERP **6.47%**.
  - Comparators (rating-based total ERP / CRP): US 4.42% / 0.22%; Canada 4.20% / 0%; Spain (A3) 5.68% / 1.48%; Brazil (Ba1) 7.30% / 3.10%.
- **Damodaran January 2026** (5-Jan-2026): Mexico Baa2, adjusted default spread 1.62%, CRP 2.46%, ERP 6.69%, mature ERP 4.23%. Other CRPs: Brazil 3.24%, Colombia 2.85%, Peru 2.07%, Chile 1.10%. — [Damodaran ctryprem.html](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html)
- **S&P/BMV IPC:**
  - 63,828.6 on 1-Oct-2026, -0.75% YTD (Actinver). — [Informador, 1-Oct-2026](https://www.informador.mx/economia/ipc-de-la-bolsa-mexicana-abre-octubre-con-baja-del-0.6--y-baja-a-63-mil-828.6-puntos-20261001-0210.html)
  - 64,975.08 on 5-Oct. — [El CEO, 5-Oct-2026](https://elceo.com/mercados/bmv-ipc-wall-street-hoy-5-de-octubre-de-2026-cierre/)
  - 64,986.91 on 8-Oct (+0.52%). — [Milenio](https://www.milenio.com/negocios/cierre-del-dolar-cotizacion-peso-mexicano-hoy-dia-mes-2026)
  - 52-week high 72,111.41. — [Investing.com IPC](https://mx.investing.com/indices/ipc-historical-data)
- **IPC valuation:**
  - P/E 16.3x in February 2026 against a 5-year average of about 16.6x ("the BMV looks expensive, but telecoms and consumer still have potential"). — [Expansión, 9-Feb-2026](https://expansion.mx/mercados/2026/02/09/la-bmv-luce-cara-pero-telecomunicaciones-y-consumo-aun-ven-potencial-en-2026)
  - BX+ (Dec-2025): P/E 14.4x against a 5-year average of 17.3x; 2026 target 69,693 on 14.0x and +15.5% EPS growth. — [BX+ Perspectiva IPC 2026](https://estrategia.vepormas.com/2025/12/18/flash-bx-perspectiva-ipc-2026/)
- **Bimbo multiples** (team wiki compiled from S&P Capital IQ, price MXN 54.20 on 18/19-Sep-2026): TEV 406,697m MXN, market cap 232,859m, total debt 189,679m (apparently including leases), cash 16,563m.

| Multiple | Close (18-Sep-2026) | 10y mean | 5y range | 10y low |
|---|---|---|---|---|
| TEV/LTM EBITDA | 6.29x | 7.78x | 6.62–8.99x | 6.03x |
| TEV/NTM EBITDA | 6.40x | 7.98x | – | – |
| NTM P/E | 17.02x | 21.04x | – | 15.69x (1Q25) |

  Year-end 4Q averages of TEV/LTM EBITDA: 8.85x (2023), 7.46x (2024), 7.03x (2025). — local file `wiki/Valuation/ciq-historical-multiples.md` (S&P Capital IQ Multiples, 19-Sep-2026)
- Bimbo's average cost of debt is 6.3% (Dec-25) and 6.5% (Jun-26). — local file `wiki/Valuation/bimbo-capital-structure-and-debt.md` (RA25 p.135; 2Q26 release p.6)

### Inferences
- The IPC's flat YTD performance, despite a peso that was much stronger for most of the year, means USD returns on Mexican equities were driven mainly by FX. With the peso now weakening, foreign investors' USD returns are under pressure.
- Bimbo's de-rating (EV/EBITDA from 8.85x in 4Q23 to 6.3x) happened while Mexico's CDS improved. That points to the de-rating being mostly company and sector specific (US bakery volumes, FX translation, leverage) rather than country risk. Lower Mexican rates alone may not re-rate it without an earnings or US-volume catalyst.

### Gaps
- No current (October 2026) IPC forward P/E, MSCI Mexico P/E or fund-flow data (EPFR/IIF) were found.
- Bimbo beta (vs IPC or MSCI) is not in the team sources; it is listed as a data gap in `wiki/Valuation/bimbo-valuation-data-gaps.md`. Damodaran's food-processing industry beta was not retrieved.

## Q7. WACC implications and re-rating potential

### Takeaway
On illustrative inputs (beta 0.8 [assumption]), Bimbo's MXN cost of equity is about 13–14% if built correctly (M-bono net of the default spread, plus beta × ERP, plus a CRP weighted to Mexico exposure). It is about 15.4% if the default risk is double-counted (M-bono + beta × ERP + full CRP). The USD cost of equity is about 9.9%. A 50–100bp fall in the Mexican 10y lowers an MXN WACC of about 10.5% by roughly 0.4–0.9pp. In a perpetuity framework that is worth about +8% to +17% on EV and +13% to +30% on equity, which would take EV/EBITDA back toward 6.8–7.4x, still below the 10-year mean.

### Cited Findings
- Inputs (all sourced above):
  - Mexico 10y M-bono: 9.32% (8-Oct-2026, Milenio).
  - US 10y: 5.23% (8-Oct-2026, CNBC).
  - Damodaran July-2026: mature ERP 4.20%, US ERP 4.42%; Mexico CRP 2.72% (rating) / 2.27% (CDS); Mexico rating default spread 1.75%; Brazil total ERP 7.30%; Spain 5.68%; volatility multiplier 1.5545. — [Damodaran workbook](https://pages.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJuly26.xlsx)
  - Inflation expectations: Mexico 2027 about 3.82% (Banxico survey, FXStreet); US 2027 PCE 2.3% (Fed SEP).
  - Bimbo market capital structure: equity 232,859m and total debt 189,679m (CIQ, 19-Sep-2026, team wiki), so E/V ≈ 55% and D/V ≈ 45% [calc]. Average cost of debt 6.5% (2Q26, team wiki).

### Inferences
All calculations are [calc]. Beta 0.8, tax rate 30% and terminal g are **[assumption]** and should be replaced by the team's own beta and regression.

**A. MXN cost of equity, three constructions:**
1. *Naive "Mexico 10y + β×ERP + CRP"*: 9.32 + 0.8 × 4.20 + 2.72 = **15.40%**. This double-counts country default risk, because the M-bono yield already includes the sovereign default spread.
2. *Damodaran-consistent, full CRP*: Rf_MXN = 9.32 - 1.75 = 7.57%. CoE = 7.57 + 0.8 × 4.20 + 2.72 = **13.65%** (13.20% with the CDS-based CRP of 2.27%).
3. *Revenue-weighted ERP* (better for Bimbo, with only 34% of sales in Mexico). Weighted ERP:
   - 0.43 × 4.42 (North America, US ERP) = 1.90
   - 0.34 × 6.92 (Mexico) = 2.35
   - 0.13 × 5.68 (EAA, Spain proxy [assumption]) = 0.74
   - 0.11 × 7.30 (LatAm, Brazil proxy [assumption]) = 0.80
   - Total ≈ **5.79%**
   - CoE_MXN = 7.57 + 0.8 × 5.79 = **12.20%**

**B. USD cost of equity:** 5.23 + 0.8 × 5.79 = **9.86%**. Converted to MXN with the inflation differential: (1.0986) × (1.0382 / 1.023) - 1 ≈ **11.5%**. This is close to construction 3, which supports the internal consistency.

**C. Indicative MXN WACC.** Marginal pre-tax Kd ≈ M-bono 9.32% + about 0.6% spread ≈ 9.9% [assumption]. That is above Bimbo's 6.5% average book cost, which reflects older fixed-rate USD notes. After tax (30%), Kd ≈ 6.9%.
- WACC (construction 2) ≈ 0.55 × 13.65 + 0.45 × 6.9 ≈ 7.5 + 3.1 = **10.6%**.
- WACC (construction 3) ≈ 0.55 × 12.2 + 0.45 × 6.9 ≈ **9.8%**.
- Using Bimbo's 6.5% book Kd instead: construction 2 gives ≈ 0.55 × 13.65 + 0.45 × 4.55 ≈ **9.6%**.

**D. Sensitivity to lower Mexican rates or CDS** (base WACC 10.5%):
- **-50bp M-bono, CDS unchanged:** CoE -0.50pp and Kd(after-tax) -0.35pp, so WACC ≈ -(0.55 × 0.50 + 0.45 × 0.35) = **-0.43pp**.
- **-100bp M-bono:** WACC ≈ **-0.87pp**.
- **-50bp CDS/default spread, M-bono unchanged:**
  - With a full CRP, the CRP falls by 0.5 × 1.55 = 0.78pp, but Rf_MXN rises by 0.5pp (less default spread to subtract), so the net CoE change is about -0.28pp.
  - In construction 3 the Mexico weight is 0.34, so the net CoE change is about -0.26 + 0.50 ≈ +0.24pp.
  - In practice CDS and M-bono yields move together, so the M-bono shock is the relevant one.
- **Valuation effect** (Gordon growth, illustrative MXN nominal terminal g = 4.5% [assumption]; spread WACC - g = 6.0pp):
  - -0.43pp → spread 5.57 → EV +7.7%. With net debt ≈ 189,679 + 722 - 16,563 = 173,838m and EV 406,697m, equity rises ≈ +31.3bn / 232.9bn ≈ **+13%**.
  - -0.87pp → spread 5.13 → EV +17.0% → equity ≈ **+30%**.
  - Implied TEV/LTM EBITDA would move from 6.29x to about **6.8x** (-50bp) or **7.4x** (-100bp), both still below the 7.78x 10-year mean.

**E. Re-rating discussion:**
- Rates: the Mexico 10y real yield is about 5.5% and the spread to USTs about 4.1pp. Compression needs a stable or falling US 10y. With the Fed hiking and the UST at 2002 highs, the near-term rate tailwind is uncertain.
- Bimbo's sensitivity to Mexican rates is diluted because about 66% of sales and a large share of debt are non-MXN. A USD-based WACC is driven more by the UST, which is currently a headwind.
- The strongest re-rating catalysts for Bimbo are more likely (i) translation turning positive in 2027 (+1 to +3pp to reported growth on consensus FX) and (ii) the multiple's distance from history (6.3x vs 7.8x), than a pure country-risk compression.
- Downside: an S&P cut to high yield, Banxico cuts that weaken the peso while USTs stay high (which would raise MXN-reported USD debt), or US 10y yields at or above 5.5%.

### Gaps
- Bimbo-specific inputs are missing: beta, marginal bond yields (USD 144A curve, MXN Cebures) and the target capital structure. All WACC figures here are illustrative.
- Peer consumer-staples (Mexico or LatAm) traded multiples vs history were not retrieved.
- Market-implied ERP for the IPC and Mexico-specific implied ERP were not found.
