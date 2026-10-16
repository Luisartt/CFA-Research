---
Writer: AI-compiled (Claude)
Source:
  - filings/annual/INFORME ANUAL 2002_0.pdf
  - filings/bmv/Grupo_Bimbo_Reporte_Anual_CNBV_2009_25.06.10_ESP.pdf
  - filings/bmv/Reporte_Anual_2012_FINAL.pdf
  - filings/bmv/REPORTE ANUAL 2025 OFICIAL VF.pdf
  - filings/annual/IA25_GB_EEFF_V10.pdf
  - filings/bmv/Reporte_Definitivo_BMV_XBRL_Español_Jun_26.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%204T25.pdf
  - filings/quarterly/Grupo%20Bimbo%20Reporta%20Resultados%20del%202T26_VF.pdf
  - filings/refinitiv/Filings/Receipt Date - 2026-Jul-24 - BIMBOA.MX - Grupo Bimbo SAB de CV - Half Year Presentation - gb investor ppt 2q26 vf 0 pdf - cr22276039.pdf
  - filings/capitaliq/News, Events and filings/Recent Documents/Transcript & Presentation/Bimbo_2024-02-19_EP_Q4-2023-Earnings-Call/Bimbo_2024-02-19_EP_Q4-2023-Earnings-Call.pdf
  - filings/capitaliq/News, Events and filings/Recent Documents/Transcript & Presentation/Bimbo_2014-02-12_MACALL_M-A-Call-Canada-Bread-Grupo-Bimbo/Bimbo_2014-02-12_MACALL_M-A-Call-Canada-Bread-Grupo-Bimbo.pdf
  - filings/capitaliq/News, Events and filings/Recent Documents/Transcript & Presentation/Bimbo_2011-10-24_MACALL_M-A-Call-Sara-Lee/Bimbo_2011-10-24_MACALL_M-A-Call-Sara-Lee.pdf
tags: [Thesis, cross-source-connections]
---

# Cross-source connections for BIMBOA: 15 patterns, contradictions between sources, data gaps and kill criteria

Compiled 2026-10-14 from the wiki articles built on the 1998-2026 filings, the Capital IQ (CIQ) exports, the LSEG (Refinitiv) governance, credit and ESG exports, the call transcripts and decks, and the 2014-2020 broker notes. ==The purpose is to find what several independent sources say together, so that the team can use it or must confront it.== No rating is proposed; the weights in section 3 are `[assumption]` and belong to the team. Companion: [[bimbo-evidence-vs-mentor-tests]] (the five mentor tests and the build recipes).

**Mentor frame (Alan, 2026-10-13).** Reports are a crime scene: test each management claim against history. Every pattern below starts from a claim and keeps the evidence on both sides.

**Source classes (used for the "independent" count).** S1 = filings (annual, quarterly, BMV XBRL, audited statements). S2 = management calls and decks (CIQ transcripts and slides). S3 = sell-side notes (2014-2020) and CIQ consensus. S4 = CIQ data exports (multiples, ownership, ESG history, estimates). S5 = LSEG exports (credit, governance, ownership, ESG). S6 = rating-agency and company press releases. Two articles built on the same document count once.

**Confidence.** High = at least three independent classes agree and the arithmetic was reproduced. Medium = two classes, or a basis caveat. Low = one class or an inference.

**Tags.** `[sourced]` = printed in the cited document; `[calc]` = my arithmetic from sourced numbers; `[assumption]` = a rule or weight the team should overwrite; `[unverified]` = not checkable from the files. Citation style: `call yyyy-mm-dd p.N` and `deck yyyy-mm-dd p.N` are CIQ transcripts and slides as in [[bimbo-guidance-vs-delivery-2011-2026]]; `RAyy` = annual report to the BMV; `EEFF25` = audited FY25 statements; `4T25`, `2T26` = earnings releases. MXN millions unless stated; own-year pesos before 2008 (Mexican GAAP).

## 1. Ranking table

Ranked by decision relevance times confidence. "Touches" = which draft pillar of the team's thesis memo (`output/bimbo-tesis-3-pilares.md`: P1 North America margin, P2 capex/FCF/deleveraging, P3 valuation) the pattern bears on. This is not a vote.

| # | Pattern (one line) | Touches | Confidence |
|---|---|---|---|
| 1 | Every large deal lifted leverage by 0.9-1.6x and took 2-6 years to digest; claims about the target ran 5-28% above reality | P2, P3 | High |
| 2 | Deleveraging has come from disposals, FX, capex under-spend and a smaller buyback, not from operating cash alone; the metric moved four times | P2 | High |
| 3 | Price-first, elasticity-second: price-led growth reversed within 2-4 quarters in five episodes; no volume is disclosed after 2017 | P1 | High |
| 4 | Dividends and buybacks have run ahead of free cash flow (FY21-FY25 FCF proxy -5.7bn vs 36.5bn returned) and buybacks were bought at 62-86 | P2, P3 | High |
| 5 | Guidance hit rate is 36% overall, 16% for 2011-2016 targets, and regime-dependent: first-of-year guides were above outcome three years in a row, then FY26 flipped to a floor | P1, P2 | Medium-High |
| 6 | Brokers over-forecast EPS (median -18.7% in 2011-2020) and multi-year margin paths, not next-year EBITDA; consensus FY27-28 margin is flat at 14.6-14.7% | P3 | Medium-High |
| 7 | Margins "recover" on a COVID- and IFRS 16-inflated peak; on a pre-IFRS 16 basis group margin is about where it was in 2007 | P1, P3 | Medium |
| 8 | Credit: S&P outlook negative for 19 months, LSEG model BBB-, lease-adjusted leverage 2.8-3.0x vs 2.5-2.7x reported | P2 | Medium |
| 9 | Adjusted EBITDA excludes multi-employer pension (MEPP) cash of MXN 2.4-2.7bn a year; pensions were 48% of gross debt in 2012 and sit outside every leverage ratio | P2, P3 | Medium-High |
| 10 | Commodity relief and pain reach margins 6-12 months late; 2027 hedges were placed at higher cost and no pass-through is committed | P1, P2 | Medium |
| 11 | FX is the standing explanation for cuts but not the whole story; it moves revenue (6.7 pp in 2Q26) and debt (-12.3bn in 2025) together | P1, P2 | Medium |
| 12 | Governance is structurally weak and not improving; ESG instruments carry a trivial penalty (MXN 30m a year) | Risks | Medium-High on facts, Low on value impact |
| 13 | Leadership turnover and disclosure quality: two CEOs in 18 months, one constant CFO since 2017, irregular disclosure | P1 | Medium |
| 14 | Canada Bread legal tail: CAD 50m fine, two open class actions, a CAD 2bn+ claim against the seller; none is quantified | Risks | Medium |
| 15 | The market paid for acquisition narrative until 2016 (EV/EBITDA 11.3-13.3x) and de-rated since; today's 6.3x is an IFRS-era low, not an all-history low | P3 | Medium |

## 2. The patterns

### P1. M&A cycles: leverage up, margin down, 2-6 years to digest, claims about the target too generous

**Claim tested.** Management: acquisitions create value, "proven ability to delever" (deck 2018-04-27 p.17), "48 acquisitions in ten years" (INT-180524) `[sourced]`.

| Deal (year) | Price and multiple paid | Leverage before, peak, after | Group EBITDA margin around the deal | Claim vs outcome |
|---|---|---|---|---|
| Weston western US (2002) | US$610m on US$56m 2001 EBITDA = 10.9x `[calc]` (RA02 p.37) | Debt/EBITDA 1.07x (FY01), 2.64x (FY02), 1.48x (FY04), 1.08x (FY06) `[calc]` [[bimbo-history-1998-2007]] | 13.6% (FY01), 10.7% (FY02), 10.3% (FY03), 12.8% (FY05), 12.0% (FY07) `[calc]` | Pre-deal margin not regained in five years |
| Weston Foods (2009) | US$2,505m incl. financial assets, 8.7x (RA09 p.35) | Total debt/EBITDA 1.13x (FY08), 2.32x (FY09), 2.15x (FY10) [[bimbo-balance-sheet-and-debt-fy08-fy13]] | 11.9% (FY08), 13.6% (FY09), 13.2% (FY10) NIF; FY09 flattered by US intangible add-back | Net debt 3.8bn to 31.8bn in one year `[calc]` |
| Sara Lee NAFB (2011) | EV US$709m, 9.1x on US$78m (deck 2011-10-24 p.4-5) | 2.15x (FY10), 3.00x NIF / 3.12x IFRS (FY11), 2.33x (FY13) | 11.0% (FY11 IFRS), 8.1% (FY12), 9.8% (FY13), 11.6% (FY16) `[calc]` | Target EBITDA fell 28% between signing and close; synergy target US$150-200m by 2013 became US$150m by 2014 [[bimbo-major-deals-terms]] |
| Canada Bread (2014) | CAD 1,830m; 9.3x on CAD 185m "earnings capacity"; 9.8x on reported CAD 176m `[calc]` (EV 1,730 / 176) | 2.3x (Dec-13), 3.2x pro forma (Dec-14), 2.9x (Dec-15) (call 2015-02-27 p.5; call 2016-02-26 p.5) | 9.84% (FY13), 9.85% (FY14): flat `[calc]` | Pro forma margin claim met; efficiencies CAD 40-65m by 2018 never reported as a line [[bimbo-analyst-forecast-accuracy]] |
| East Balt / QSR (2017) | US$650m, 9.3x on ~US$70m (call 2017-07-26 p.5) | 2.5x (2Q17), 3.5x (Dec-17), 2.8x adjusted vs 3.1x unadjusted (Dec-18) (release 2018-02-24 p.8; deck 2019-02-21 p.15) | 11.6% (FY16), 10.2% (FY17): -140bp (release 2018-02-24 p.7) | "Immediately accretive to margin and EPS": net majority income -21.5% in FY17 |
| Ricolino sale (2022) | EV 27,000 = 2.66x sales; EBITDA not disclosed (PR 2022-04-24) | 2.0x (3Q22) to 1.5x (Dec-22), 2.1x (Dec-23), 2.9x (Dec-24) | 13.4% FY22 (-60bp) | Disposal worth ~0.4-0.5x of deleveraging (call 2022-10-27 p.9) |

`[sourced]` unless marked; ratios are as printed on each date and definitions changed four times ([[bimbo-leverage-and-deleveraging-commentary]]). Margins are first-reported EBITDA / net sales `[calc]` from [[bimbo-income-statement-fy98-fy07]], [[bimbo-income-statement-fy08-fy13]], [[bimbo-income-statement-fy14-fy20]].

**Independent confirmation (at least four classes).**
- S1: the ratio and margin series above come from audited statements; cumulative FY14-FY20 cash flow shows CFO 174.1bn funding capex 89.7bn, acquisitions 47.6bn, interest 35.3bn and distributions 16.7bn while net debt still rose 38.2bn `[sourced]` [[bimbo-cash-flow-and-capex-fy14-fy20]].
- S2: of 12 M&A targets scored, 3 were met (25%); integration cost, closing dates and synergy timing slipped in Sara Lee, Panrico, Canada ERP (CAD 40m vs US$10-15m said) and Donuts Iberia `[sourced]` [[bimbo-guidance-vs-delivery-2011-2026]].
- S3: the Jul-2015 broker path expected consolidated EBITDA margin 12.4% (FY16) and 14.8% (FY17) after the 2014-15 deals; actual 11.6% and 10.2% `[sourced]` INT-150710 vs [[bimbo-income-statement-fy14-fy20]].
- S4: CIQ multiples show the market paid 11.3x LTM EBITDA on average in 2012-2018 while ND/EBITDA ran 2.1-2.8x and ROE 4-10% `[sourced]` [[ciq-long-history-multiples-and-returns]].

**Implication.** (a) A deal is a leverage event first and a margin event 2-5 years later; the first full year after Weston (2002), Sara Lee (2012) and East Balt (2017) cut group margin by 1.4-3.0 pp, Canada Bread by 0 `[calc]`. (b) At 8-9.3x paid against a stock at 6.3x LTM EBITDA (CIQ), a bolt-on at 8x needs synergies of 27% of target EBITDA just to reach the group's own multiple (8.0 / 6.29 - 1) `[calc]`; Canada Bread at 9.3x needed 48%, against 22-35% promised (CAD 40-65m on CAD 185m) `[calc]`. (c) The 2021-2025 bolt-on programme (about US$480m a year, deck 2026-07-23 p.22) has no disclosed prices; accretion cannot be tested `[sourced]`. (d) The one measurable M&A success is slow: EAA EBITDA margin from -4.4% (2015) to 10.8% (2025) took ten years `[sourced]` [[bimbo-investor-presentations-2024-2026]].
**Forecast use.** Model any announced deal as +0.3-0.5x leverage per US$500m, no synergy in year one, and a 12-18 month closing delay `[assumption]`. **Confidence: High.**

### P2. Deleveraging came from disposals, FX, capex under-spend and a smaller buyback

**Claim tested.** "Deleveraging even with zero M&A", "slight deleverage by Dec-26 from 2.7x" (call 2026-02-25 p.15; call 2026-04-29 p.5) `[guidance]`.

| Episode | Stated cause | What the numbers say |
|---|---|---|
| 2022: 2.0x to 1.5x | Ricolino sale | Disposal effect ~0.4-0.5x (call 2022-10-27 p.9) `[sourced]` |
| 2024: 2.3x to 2.9x | Capex and M&A | Net debt +39.2bn (103,582 to 142,848) with a ~20% peso depreciation on USD debt `[sourced]` [[bimbo-balance-sheet-and-leverage]] |
| 2025: 2.9x to 2.7x | "Gradual deleveraging" | Net debt rose 2,280 (142,848 to 145,128); debt FX revaluation was -12,269, so underlying debt grew ~15,000 `[calc]` (EEFF25 p.52). On the ex-IFRS 16 basis the ratio fell from 2.85x to 2.72x entirely through EBITDA (+6.5%) `[calc]` (net debt / (Adj. EBITDA less right-of-use depreciation)) |
| 1H26: 2.7x to 2.5x | Capex and FCF | Net debt -8,031; company FCF 11.9bn less 5.3bn returned less 0.2bn acquisitions = 6.4bn; the remaining ~1.6bn is FX and other (debt reconciliation "other effects" -2,972) `[calc]` (deck 2026-07-23 p.15; BMV Jun-26 p.52) |

- The leverage scorecard looks better than it is: of six "Met" leverage rows, one is a definition change (net debt from Oct 2019), one is the Ricolino sale, one is the 2025 capex under-spend (US$1.2bn vs US$1.3-1.4bn guided) and FX `[calc]` from [[bimbo-guidance-vs-delivery-2011-2026]] rows 22, 34, 42, 47, 54, 58.
- The <2x target was on every 2014 deck and disappeared in Oct 2014; the ratio first held below 2x in Dec-2020 (1.9x, COVID cash flow) `[sourced]` [[bimbo-leverage-and-deleveraging-commentary]].
- Capex guidance is the least reliable line: 2 of 11 met; 2018, 2019, 2020, 2024 and 2025 came in below the first guide (2025: -24.1% vs first midpoint) `[sourced]` [[ciq-guidance-and-estimate-history]].
- 1H26 PP&E capex is 3.4% of sales against 4.0% implied by the company's own impairment-model capex ratios (Mexico 4.15%, US 3.96%, Canada 3.50%, Spain 3.31%, Brazil 4.32%; EEFF25 p.46) weighted by regional sales `[calc]` `[assumption]` (mapping cash-generating units to regions). A steady-state 4.0% instead of 3.4% would be about MXN 2.6bn a year of FCF `[calc]`. FY26 guidance of US$1.0-1.2bn implies a 2H26 PP&E spend of 10.6-14.1bn, 1.5-2.0x 1H26 `[calc]`.

**Implication.** Read FY26 deleveraging as likely (1H26 already 2.5x) but of lower quality than "FCF-led"; the sustainable part is the capex run-rate and EBITDA growth. **Confidence: High** on the sources, Medium on the capex steady-state.

### P3. Price first, elasticity second; volume is never disclosed

**Claim tested.** "Pricing power", "inelastic demand", "price/mix positive" (calls 2025-2026).

| Episode | Price action | What followed | Source |
|---|---|---|---|
| Mexico 2013-14 | 2012-13 price rises; IEPS pass-through | Volume -3% (4Q13), -6% (1Q14), -3% (2Q14), FY14 -4%; "mid-single-digit return" target missed | call 2013-04-26 p.12; call 2014-04-30 p.3; call 2015-02-27 p.4 |
| US 2015 | Bread price +5% vs category flat | Share loss, bread category -2-3%, private label tonnage -6-8% | call 2015-07-22 p.6; call 2015-04-24 p.5 |
| US 2018-19 | Priced ahead of category | Mainstream volume loss; ~16% of branded SKUs eliminated | call 2019-07-23 p.7; call 2020-02-21 p.4 |
| US 2022 | Three rises by 8-Jul-2022 | First branded elasticity in 3Q22; private label and down-trading; no 2023 price | call 2022-10-27 p.4, p.10 |
| Mexico 2022-23 | Price "pushing the envelope" | Volume soft in 2H23 | call 2023-10-26 p.10 |

All `[sourced]` [[bimbo-call-themes-by-year]], [[bimbo-volume-and-price-disclosures]].

- Management never published group or regional volume as a series; Mexico volume stops in 2017; the company declined the price/volume split in 2021, 2022 and 2025 (call 2021-07-28 p.11; call 2022-02-22 p.8; call 2025-04-29 p.8) `[sourced]`.
- North America: ex-FX sales fell eight straight quarters (1Q24-4Q25, -2.9% to -5.7%), +0.7% and +1.3% in 1H26; the CFO said US volumes were still declining in 2025 (call 2026-02-25 p.13); 2Q26 growth is price/mix and a smaller World Cup effect `[sourced]` [[bimbo-north-america-turnaround-evidence]].
- Third-party cross-check (S6/press, `[unverified]` per the team memo): NielsenIQ volume -5.8% and price +5.6% (Merca2, 8-Oct-2026); Circana 52 weeks to 19-Apr-2026 Bimbo box bread -2.8%; Flowers volume -5.8% `[unverified]`. Company-selected Circana windows (4 and 12 weeks) show Bimbo mainstream bread -0.2% vs industry -1.1% (deck 2026-07-23 p.12) `[sourced]`.
- Mexico is the counter-evidence: ex-FX sales +4.5% (1Q26) and +4.7% (2Q26) against ANTAD total sales 3.6% and 2.3% and F&B industry +3.0% (deck 2026-06-10 p.13; 2Q26 p.13) `[sourced]`; margin 20.4% in FY25, a record `[sourced]`.

**Implication.** A volume x price model has to treat volume as a residual: ex-FX sales growth by region less an assumed price/mix. The residual for North America is about zero to slightly negative in 1H26 if price/mix is +1-2% `[assumption]`. Recipes and bounds are in [[bimbo-evidence-vs-mentor-tests]]. **Confidence: High** that price-led growth reverses; Low on today's elasticity because no number exists.

### P4. Distributions ahead of free cash flow; buybacks at the top

**Claim tested.** "Dividends and buybacks to the same extent as before" (call 2026-07-23 p.8); "no payout ratio" (call 2022-10-27 p.8).

| MXN m | FY21 | FY22 | FY23 | FY24 | FY25 | FY21-25 |
|---|---|---|---|---|---|---|
| FCF proxy B (CFO - capex - leases - net interest) | 12,703 | (2,668) | (17,166) | (4,791) | 6,216 | (5,706) |
| Dividends paid | 4,636 | 5,885 | 3,549 | 4,234 | 4,451 | 22,755 |
| Buybacks | 1,901 | 2,568 | 3,586 | 4,433 | 1,253 | 13,741 |
| Acquisitions (incl. 1,468 NCI in FY25) | 10,637 | 6,520 | 6,548 | 5,988 | 12,762 | 42,455 |
| Net borrowing | 5,389 | (3,872) | 26,791 | 22,616 | 13,790 | 64,714 |

`[sourced]` EEFF25 p.16 and RA23 p.11 via [[bimbo-cash-flow-and-fcf]]; sums `[calc]`. Net debt rose 61.0bn from Dec-21 to Dec-25 (84,107 to 145,128) `[calc]`, equal to the FY21-25 shortfall after returns and M&A of 60.9bn (proxy C) `[calc]`.

- Same pattern in FY14-FY20: FCF after interest and leases 41.5bn vs acquisitions plus distributions 64.3bn `[calc]` [[bimbo-cash-flow-and-capex-fy14-fy20]].
- Buybacks ran through every leverage rise: 2018 (3.2x), 2020 (cash is king), 2024 (2.3x to 2.8x) `[sourced]` [[bimbo-leverage-and-deleveraging-commentary]]. The 2023-24 programme bought 106.2m shares for MXN 8,019m, an average of ~75.5, against 55.41 on 6-Oct-2026: a mark-to-market loss of about MXN 2.1bn (-26.6%) `[calc]` ([[bimbo-agm-dividends-and-buybacks]]; price from the team memo, CIQ).
- S&P's 20-Mar-2025 outlook cut cited capex, dividends, buybacks and acquisitions outrunning cash flow; the buyback fell 72% in 2025 (4,433 to 1,253) `[sourced]` [[bimbo-agm-dividends-and-buybacks]]. In 2025 dividends plus buybacks were 92% of proxy B (5,704 / 6,216) and in 1H26 59% (5,281 / 8,986) `[calc]`.
- The 2026 dividend is MXN 1.075 a share (+7.5%), not 1.75 (see C3).

**Implication.** The dividend is covered only on the post-capex-cut run-rate; a return to US$1.4-2.0bn capex with the same distributions would reopen external funding `[calc]`. **Confidence: High.**

### P5. Guidance: 36% hit rate, regime-dependent, and FY26 flipped to a floor

- 61 resolved targets: 22 met, 9 mixed, 30 missed (36% met; 42% excluding mixed). By era of target: 2011-2016 16% (4 of 25), 2017-2019 30%, 2020-2022 62%, 2023-2025 56% `[sourced]`/`[calc]` [[bimbo-guidance-vs-delivery-2011-2026]]. By type: capex 18%, M&A 25%, segment 22%, leverage 60%, growth 67%.
- Independent cross-check on the full-year guides in CIQ: first EBITDA guide above outcome three years running (FY23 -4.8%, FY24 -2.4%, FY25 -10.0% vs the floor), last guide missed in FY22-FY24 and beaten in FY25 (+3.6% vs midpoint); FY26 reversed: first guide only a floor equal to FY25 (>=59,456), then 60,051-64,043 (29-Apr) and 60,465-64,470 (23-Jul) `[sourced]` [[ciq-guidance-and-estimate-history]]. Decks confirm margin +60-110bp then +70-120bp and capex US$1.2-1.4bn then US$1.0-1.2bn `[sourced]` [[bimbo-investor-presentations-2024-2026]].
- The 2020-22 beats came during COVID and inflation-led pricing (guidance raised in each year); the 2023-25 cuts blamed FX. The beats were not forecasting skill `[sourced]`.
- Implied 2H26: 1H26 EBITDA 29,149 `[calc]` (14,036 + 15,113) means the floor needs 2H26 31,316 (-1.4% vs 2H25 31,770), the midpoint 33,319 (+4.9%), consensus 62,117 needs 32,968 (+3.8%) `[calc]`.

**Implication.** Treat management's FY26 range as a conservative post-reset guide (two raises) rather than as evidence of forecasting skill; the structural record (36%) still argues for a haircut on any target beyond one year, especially capex, integration and segment targets. The Gaxiola constant (CFO since Oct 2017 delivered every revision 2018-2026) means the change in posture is not a CFO change `[sourced]` [[bimbo-ceo-and-management-changes]]. **Confidence: Medium-High.**

### P6. Broker bias: EPS and multi-year margin paths, not next-year EBITDA

- Final-consensus accuracy FY2000-FY2025: revenue MAE 1.1%, EBITDA MAE 2.9% (median +0.8%), EPS MAE 12.8%; in 2011-2020 the median EPS surprise was -18.7% (analysts expected more EPS in 6 of 10 years by 16-47%) `[sourced]` [[ciq-guidance-and-estimate-history]]. EBITDA beat in 52 of 79 quarters since 2004 (median +3.4%) while GAAP net income missed in 41 of 71 `[calc]`.
- 2014-2018 broker notes: net income over-forecast in 8 of 9 annual vintages (median miss ~-30%), EBITDA under-forecast in 7 of 9 (peso translation); in the nine quarterly previews the mean absolute error was 2.2% for sales, 4.9% for EBITDA and 34.2% for net income `[sourced]` [[bimbo-analyst-forecast-accuracy]].
- Two independent sources agree the error is below EBITDA (D&A, interest, tax, minorities, FX). The long-range error is margin: 14.8% expected for FY17 vs 10.2% reported `[sourced]`.
- Today: consensus FY26-FY28 EBITDA margin is 14.6%, 14.6%, 14.7% (no ramp) `[calc]` from [[ciq-consensus-estimates]]. Over 18 months FY26 EBITDA was cut 6.4%, EPS 21.3% and net debt raised 24.6% (117,862 to 146,914) `[sourced]` [[ciq-estimate-revisions-and-surprises]]. The last ten quarters repeat the old pattern: normalized EPS missed 8 of 10 (thesis memo, CIQ surprises) `[sourced]`.
- Soft spots in the current consensus `[calc]`: D&A FY26 22,933 (3 analysts) is 7.7% below FY25 24,838 while EBIT is up 9.7%; FY26 revenue 426,275 at the top of the 414,143-426,952 range needs 2H26 +2.2% on a 1H26 of -2.6% (205,308 vs 210,836); capex 21,979 is above the 21,024 top of guidance (stale) and net debt 146,911 is above the 137,097 already reported at Jun-26 on a basis that is 3,903 higher `[sourced]` [[ciq-consensus-estimates]].

**Implication.** A team forecast above consensus on EBITDA is not by itself a variant view (consensus EBITDA is conservative by construction); the exposure is EPS conversion. A margin ramp beyond FY26 would be a contrarian assumption against the broker record, not a consensus one. **Confidence: Medium-High.**

### P7. The margin story rests on a COVID- and IFRS 16-inflated peak

- Group Adjusted EBITDA margin FY25 13.9% includes IFRS 16 (from 2019). Removing right-of-use depreciation (6,142, the term that reproduces the company's ex-IFRS 16 ratios) gives 12.5%; removing 2025 lease payments (8,060) gives 12.0% `[calc]` (EEFF25 p.41-42; [[bimbo-balance-sheet-and-leverage]]). Comparable first-reported margins: 11.6% (FY16), 10.2% (FY17), 11.0% (FY18), 12.0% (FY07) `[calc]` ([[bimbo-income-statement-fy98-fy07]], [[bimbo-income-statement-fy14-fy20]]). Across FY14-FY25 the group spent MXN 220.5bn of PP&E capex and about 90.0bn on acquisitions (84,434 + 136,026; 47,587 + 42,455) `[calc]` ([[bimbo-cash-flow-and-capex-fy14-fy20]], [[bimbo-cash-flow-and-fcf]]); group margin moved from ~12.0% (FY07) to 12.0-12.5% (FY25) `[calc]` `[assumption]` (comparability of NIF and IFRS definitions).
- North America: the "11.3% in 2019, 12.9% in 2020, 8.4% in 2024" series in the guidance article mixes pre-IFRS 16 (to 2018) and IFRS 16 (from 2019) margins; FY20 is the COVID pantry-loading year with a 9bn working-capital inflow `[sourced]` [[bimbo-covid-2020-impact]]. The scenario of a return from 9.6% to 12.2% in the team memo uses FY21 as the target `[sourced]`.
- Flowers (10.2%) reports under US GAAP, where operating lease cost stays above EBITDA. Bimbo NA 9.0% (FY25) on an IFRS 16 basis is therefore not like-for-like with 10.2%: NA's share of right-of-use depreciation is not disclosed `[unverified]`; if NA bears 40-45% of 6,142 its ex-IFRS 16 margin is about 7.5-7.7% `[assumption]`.
- NA margin targets have been reset: ~10% "over time" (2015), "gradual improvement 2H25, 3-4 years" (Apr 2025), "2-3 more years" (Apr 2026) `[sourced]` [[bimbo-call-themes-by-year]]. 1Q26 group margin included a ~50bp one-off gain on a stake in an associate; the 1Q26 margin change was misquoted on the call (+260bp said, +160bp on the deck) `[sourced]` [[bimbo-ceo-and-management-changes]].

**Implication.** The four-quarter NA margin recovery (5.9% in 4Q24 to 10.0% in 2Q26) is real but is a recovery from a trough, mostly cost (record productivity, raw materials, lower restructuring) with sales volume still negative `[sourced]` [[bimbo-north-america-turnaround-evidence]]. A target of 12% needs a comparable-basis reference the files do not give (gap G2). **Confidence: Medium** (rests on the ROU proxy).

### P8. Credit: the agencies, LSEG and the bond market do not say the same thing

| Source | Reading | Tag |
|---|---|---|
| S&P | BBB+, outlook negative since 20-Mar-2025 (19 months old at 10-Oct-2026); expects ND/EBITDA above 3x in 2025 and below 3x in 2026 on its basis; national mxAAA | `[sourced]` [[bimbo-credit-risk-lseg]]; PR 2025-03-20 |
| Fitch / Moody's | BBB+ stable (affirmed 29-Jul-2026); Baa1 stable (15-Nov-2024); Fitch expects gross leverage ~3.0x easing to ~2.6x | `[sourced]` [[bimbo-credit-risk-lseg]] |
| LSEG combined model | Score 16/100, implied BBB-, PD 0.16%: SmartRatios 9 (leverage 7, liquidity 9), structural 53 (A-), text mining 70 | `[sourced]` [[bimbo-credit-risk-lseg]] |
| Bonds | USD OAS 85 bp (2029) to 107 bp (2036, 2051); yields 5.7-6.7%; MXN fixed 9.22% (2035), 10.06% (2032), 9.24% (2033) | `[sourced]` [[bimbo-credit-risk-lseg]], [[bimbo-bond-prospectus-terms]] |
| Company | 2.5x (ex-IFRS 16), cost 6.5%, tenor 9.5 years, 82% fixed, revolver US$2.35bn undrawn | `[sourced]` 2T26 p.6; deck 2026-07-23 p.17 |
| Our arithmetic | (Net debt + leases) / Adjusted EBITDA 3.03x (Dec-25), 2.80x (Jun-26) | `[calc]` [[bimbo-balance-sheet-and-leverage]] |

- The S&P statement and the 3.03x agree: S&P's "above 3x in 2025" is a lease-adjusted metric, while the company's 2.7x is ex-IFRS 16. The rating hinge is below 3.0x on the lease-adjusted basis, reached on 2.80x at Jun-26 `[calc]` `[assumption]` (S&P's definition is not in the files).
- Interest cover: EBITDA/interest 4.1x (FY25) from 6.6x (FY22) `[calc]`; the loan covenant on "Conformed EBITDA" was met in 2023-2025 and to Jun-26; the threshold is not disclosed `[sourced]` [[bimbo-balance-sheet-and-leverage]]. About 300 bp of fall in the floating coupon (BIMBO 25-2, TIIE funding + 0.34%: 9.86% in Mar-2025 to 6.83% in Jul-2026) is a cost tailwind on the 18% floating share `[sourced]` [[bimbo-bond-prospectus-terms]].
- LSEG's debt table is not model-grade (issue-size amounts; Tranche B maturity 19-Aug-2028 vs 15-Mar-2028 in the filing) `[sourced]`; use filings for the debt stack.

**Implication.** A BBB+ to BBB step (more probable if 3Q26 and 4Q26 slip) raises the spread on 2027 refinancing; a revision to stable is plausible if lease-adjusted leverage holds below 3.0x `[assumption]`. **Confidence: Medium.**

### P9. Adjusted EBITDA and net debt leave out pension cash

- Company Adjusted EBITDA is before "multi-employer pension plan items" (2T26 p.2 note 2) `[sourced]`. MEPP cash contributions were 2,430 (2023), 2,609 (2024), 2,700 (2025) and 2,406 expected in 2026 `[sourced]` [[bimbo-risk-factors]]; 2,700 is 4.5% of FY25 Adjusted EBITDA `[calc]`.
- Net debt excludes leases (34,790) and any pension liability; in FY2012 the employee-benefit line was 20.2bn, 48% of gross debt and 54% of net debt `[calc]` [[bimbo-balance-sheet-and-debt-fy08-fy13]]. The 2022 reversal of the MEPP provision (US$934m, non-cash) cut the balance-sheet benefits line from 30.7bn to 9.4bn `[sourced]` [[bimbo-balance-sheet-and-leverage]]; contingent exposure was US$1.6bn (2013), US$1.0-1.3bn (2015-2018), a bit over US$100m after the 2022 American Rescue Plan `[sourced]` [[bimbo-leverage-and-deleveraging-commentary]].
- DB plans are 94.8% funded, deficit 1,524 at Dec-25 `[sourced]` [[ciq-pension-obligations]].
- Company FCF vs our proxy: 1H26 company FCF 11.9bn uses working capital +2.6bn; the cash-flow statement lines sum to -582, a 3.2bn difference that is about the whole gap to proxy B (8,986) `[calc]` ([[bimbo-investor-presentations-2024-2026]]; [[bimbo-cash-flow-and-fcf]]). MEPP cash is not in the company FCF formula as printed `[unverified]`.

**Implication.** Treat MEPP cash as a debt-like or operating cash cost in the FCFF and show EV with and without it; reconcile the company FCF before quoting "FCF of ~12bn". **Confidence: Medium-High.**

### P10. Commodities and hedging: relief and pain are lagged, and 2027 is already priced at higher cost

- Hedge window: ~6 months (2011), 4-12 months (2015), 12-18 months lag (2020), 4-18 months (2022); 85% of 2022 needs hedged at 1Q22 and 100% by 2Q22, yet FY22 EBITDA margin fell 60bp to 13.4% `[sourced]` [[bimbo-call-themes-by-year]], [[bimbo-volume-and-price-disclosures]].
- Relief: wheat ~US$8 vs 13-14 a year earlier reached margin in 4Q23 (call 2023-10-26 p.13); raw materials -4.7% in FY24 lifted gross margin +120bp `[sourced]` [[bimbo-input-costs]]. Pain: 2011 basket +20%, flour +30%, flat-margin promise missed (-1.4pp operating margin in 4Q11) `[sourced]`.
- Size: raw materials are 30.4% of sales (FY25); wheat flour was ~9-10% of sales (2012) and under a quarter of raw materials (2013), sugar under 3% of cost of sales (2023) `[sourced]`. A 5-8% basket rise costs 150-240bp of gross margin before hedges, price and productivity (30.4% x 5-8%) `[calc]`.
- 2026-27: Iran-conflict inflation US$70-90m in 2026 (about 35-45bp), 2027 hedges at higher cost, "no pricing commitment" (call 2026-07-23 p.5-9) `[sourced]`. Wheat CBOT Dec-26 US$6.865 and Dec-27 US$7.235 a bushel (+5.4%) and continuous series +34.9% a year `[unverified]` (team memo, 7-Oct-2026). Commodity hedge charges to cost of sales fell from 1,767 (2023) to 1,053 to 647 (2025) `[sourced]` (EEFF25 p.73). Hedge coverage is not disclosed; the strategy references a five-year average price (EEFF25 p.9).
- No El Niño or weather-risk analysis appears in any file; RA25 p.22 lists weather and climate generically.

**Implication.** Lag of 6-12 months means 2027 gross margin is set by hedges placed in 2026, not by spot; a 2027 margin ramp needs either price (elasticity risk, P3) or productivity. **Confidence: Medium** (hedge coverage unknown).

### P11. FX: the standing explanation, only partly true

- FX was the stated cause of the 2023, 2024 and 2025 cuts; the CFO said 2025 was "100% FX" (call 2025-07-24 p.9) `[sourced]`. The May-2025 deck cited both the peso (20.5 vs 21.0, about 2 pp) and "softer North America consumption"; the July deck put FX at 250bp of sales and 160bp of EBITDA growth `[sourced]` [[bimbo-investor-presentations-2024-2026]]. The FY25 sales guide went from at least +10% to +4.6% actual: FX explains about 4.5 pp, the rest is other `[calc]`.
- FX moves both numerators and denominators: 2Q26 sales -2.2% in MXN vs +4.5% ex-FX (6.7 pp); 44% of debt was USD at Dec-25 and 42% at Jun-26 `[sourced]` [[bimbo-fx-exposure]]. Leverage ratios are partly hedged by translation; but cash taxes and MXN interest are not.
- Management quantifies FX in points of sales growth (2.0-2.5 pp per 0.5-0.75 MXN, call 2025-04-29 p.5; 2026 guide drag above 500-600bp) `[sourced]`.

**Implication.** Model in ex-FX local currency by region and translate with an explicit FX path; treat the "FX" label as necessary but not sufficient. **Confidence: Medium.**

### P12. Governance and ESG: structural, not improving, and not priced into the instruments

| Indicator | Reading | Source class |
|---|---|---|
| Independent directors | 7 of 18 = 38.9% `[calc]` (LSEG FY2024 38.10%; decks 39%) vs 25% legal floor; no independent chair; 7 Servitje-surname directors | S5, S2 [[bimbo-board-and-officers-lseg]] |
| Control | Six holding vehicles 72.03% (RA25) / 72.37% (LSEG); free float 27.63%; a 10% threshold = 36% of the free float | S1, S5 [[bimbo-ownership-lseg]] |
| LatAm governance checklist | 31/64 = 48%; takeover defences 1/10 (board veto over any >3% buyer); committees 6/8 | S5 `[assumption]` rubric [[bimbo-governance-checklist-latam]] |
| S&P ESG | 55 (Oct-2023), 61 (Aug-2024), 57-58 (2025); Governance CSA 45, 44, 41; percentile 90 to 74; Corporate Governance 28 vs industry 42; Information Security 0 | S4/S6 [[bimbo-sp-global-esg-score-history]] |
| CIQ ESG history | Governance & Economic 49 (2013) to 46 (2026); "Family Ownership" 0 vs industry 100 every year; Responsible AI 0 vs industry average 2 (best 65) | S4 [[ciq-esg-profile-history]] |
| LSEG ESG | 87.02 (FY2023) to 84.62 (FY2024), the whole drop in governance "Management" (-11.78); combined grade B (FY2023, controversies C) | S5 [[bimbo-esg-lseg-scores-and-policies]] |
| Related parties | MXN 9,295m in FY25 (2.2% of sales, 4.6% of cost of sales), growing 7.2% a year since 2018; Beta San Miguel 8%-owned supplier 2,500 | S1 [[bimbo-related-party-and-compensation-disclosures]] |
| Bond ESG step-up | 23L: +25 bp from Nov-2031 if Scope 3 target missed = MXN 30m a year (0.05% of FY25 EBITDA) `[calc]`; 23-2L missed -12.5% and costs MXN 6m | S1/S6 [[bimbo-bond-prospectus-terms]], [[bimbo-sustainable-financing]] |

**Implication.** All five governance sources point the same way (S&P, CIQ, LSEG pillar, checklist, bylaws), and no instrument or disclosed price signal links governance to the cost of capital. Use it as a risk, not as a catalyst; do not use ESG scores as a valuation driver. AI appears only as a gap (Responsible AI 0 vs industry average 2, CIQ) and as boilerplate in RA25 p.36-37; no evidence of AI-driven earnings exists `[sourced]`. **Confidence: Medium-High** on the facts, Low on value impact.

### P13. Leadership turnover and disclosure quality

- CEO changes: Servitje to Pamias (1-May-2024), Pamias to Rodriguez Bas (Nov-2025, reason not given on calls; press cites "personal and health matters" `[unverified]`); US head changes 2013, 2023, 2026; the Executive Chair remains `[sourced]` [[bimbo-ceo-and-management-changes]]. Each transition followed a weak stretch (Brazil 2012-13, US 2014-15, NA 2023-24).
- The new CEO's evidenced credential is Barcel (US salty snacks +9.0% vs industry +1.4% in a 4-week window to 16-May-2026, +8.9% vs +1.1% in 12 weeks to 5-Jul-2026; company-chosen windows; size not disclosed) `[sourced]`. The post-Nov-2025 improvements coincide with easy comps (NA 4Q24 margin 5.9%), a ~50bp one-off, FX and a programme led by the BBU president `[sourced]`/`[calc]`.
- Disclosure irregularities: eliminations line unexplained on the 2Q26 call, margin delta misquoted in 1Q26, 1Q26 transcript marked preliminary, no 4Q24 transcript, regional margin guidance refused every year since 2014 `[sourced]`.
- The stock reacted +9.1% on 30-Apr-2026 (IPC +1.1%) to the 1Q26 release that carried the ~50bp one-off `[sourced]` [[bimbo-event-study-inputs]].

**Implication.** The CEO is an unproven variable (mentor test 3) and the only constant in guidance is the CFO. **Confidence: Medium.**

### P14. Canada Bread: acquired in 2014, still producing legal outcomes in 2026

- Seller behaviour before sale: special dividend CAD 8.00 paid 6-Jan-2014, five weeks before signing; bakery closures in 2013; Bimbo's EBITDA base CAD 185m "earnings capacity" vs CAD 176m reported (5% gap) `[sourced]` [[bimbo-analyst-forecast-accuracy]], [[bimbo-major-deals-terms]].
- Outcomes: CAD 50m (US$38m) fine, 21-Jun-2023, for two bread price increases a decade earlier; two class actions with no provision and no exposure estimate (RA25 p.119); LSEG controversy grade fell to C (FY2023); Metro/Loblaw allegations (Dec-2023); Maple Leaf defamation suit (22-Nov-2024) and Bimbo's claim for more than CAD 2bn (29-Nov-2024, 1.09x the price) `[sourced]` [[bimbo-risk-factors]], [[bimbo-esg-lseg-scores-and-policies]].
- S&P scored it a minor controversy in 2023 (-0.46 on the CSA, -9.06 on Business Ethics) and removed it from 2024 reports while the actions stay open `[sourced]` [[bimbo-sp-global-esg-score-history]].

**Implication.** Exclude both the contingent liability and the CAD 2bn claim from the base case `[assumption]`; show them in risks with the unquantified tag. **Confidence: Medium** (court outcomes unknown).

### P15. Valuation regime: the market paid for M&A narrative until 2016 and de-rated since

- TEV/LTM EBITDA: 5.97-7.49x every year 2000-2006; 11.3x average in 2012-2018 (peak 14.22x, Sep-2013); 6.33-8.70x in 2019-2025; now 6.29x, 8th percentile of 2000-2026 and 5th of 2012-2026 `[sourced]` [[ciq-long-history-multiples-and-returns]]. P/E NTM 17.0x vs 18.97x mean since 2000, 13.35x in 2000-2008 `[sourced]`.
- The regime that makes the stock look cheap (2012-2018) coincided with the acquisition build-out, ND/EBITDA 2.1-2.8x and ROE 4-10%; using 2000-2008 (net cash, Mexico-centred) as normal flips the sign of the argument `[sourced]` same article.
- Return decomposition (price proxy): 2023 year-end 86.0 to 54.2 (-37%), while LTM EBITDA in US$ rose 10% from Dec-23 to Jun-26 (3.1 to 3.4bn) and market cap fell 37% (US$22.3bn to 14.1bn) `[calc]` ([[bimbo-investor-presentations-2024-2026]]).
- Versus peers: 6.29x (CIQ) or 6.68x (company EBITDA) against pure-play bakery median 6.45x (FLO 6.6x, GRUMAB 5.7x, 2212.T 6.3x, ARYN 7.2x), `[unverified]` (aggregator multiples in the team memo); the discount exists against Bimbo's own history and Mexican consumer names (AC 8.1x, PEP 10.8x), not against bakeries.
- Management said in Jul-2022 that Bimbo traded ~8-8.5x vs Flowers ~14x (call 2022-07-21 p.12) `[sourced]`; Flowers is now ~6.6x `[unverified]`: the peer de-rated more than Bimbo.

**Implication.** "Cheap versus history" depends on the chosen regime and on the IFRS 16 treatment (TEV includes 33,361 of leases; a pre-IFRS 16 equivalent is ~6.6x vs 6.29x reported `[calc]`). A sum-of-the-parts (Mexico 56% of EBITDA on 34% of sales, deck 2026-07-23 p.4) is more defensible than a single multiple. **Confidence: Medium.**

## 3. Evidence for buy, hold and sell, weighted `[assumption]`

Weights (1 = minor, 3 = major) are the compiler's `[assumption]`; the team should overwrite them. Direction is which rating the item supports if it is true. The totals are an arithmetic illustration of the item list, not a recommendation. The team decides rating and target.

| # | Evidence item | Pattern | Supports | Weight `[assumption]` |
|---|---|---|---|---|
| 1 | 6.29x LTM EBITDA is 8th percentile of 27 years and below every IFRS-era quarter on NTM EBITDA (0th percentile) | P15 | Buy | 2 |
| 2 | Consensus margin flat 14.6-14.7% FY26-28: no ramp embedded, so upside if NA recovery holds | P6 | Buy | 2 |
| 3 | NA EBITDA margin up YoY four quarters (+90, +330, +120, +100bp); capex down 23% in FY25 and 3.4% of sales in 1H26 | P2, P7 | Buy | 2 |
| 4 | FY26 guide raised twice from a floor start; 1H26 leverage 2.5x already below the Dec-26 goal | P2, P5 | Buy | 2 |
| 5 | Mexico: ex-FX growth above ANTAD and the F&B industry; margin 20.4% record; 55-56% of EBITDA | P3 | Buy | 2 |
| 6 | Consensus mean target 70.17 (+26.6% vs 55.41); 17 of 22 target changes up in 12 months | P6 | Buy | 1 |
| 7 | Valuation in line with pure-play bakery peers (6.3x vs 6.45x median); discount only versus own history | P15 | Hold | 2 |
| 8 | Consensus rating Hold (2.58); NA volumes still negative and share data mixed; 2Q26 growth +1.3% is price/mix | P3 | Hold | 2 |
| 9 | S&P negative outlook; lease-adjusted leverage 2.8-3.0x; BBB+ to BBB step possible | P8 | Hold | 2 |
| 10 | FCF depends on capex staying at US$1.0-1.2bn; distributions 59-92% of proxy FCF | P2, P4 | Hold | 2 |
| 11 | 2027 inputs hedged at higher cost; no pricing commitment; IEPS and labour (46 h) tails | P10 | Hold | 2 |
| 12 | 36% guidance hit rate; EPS over-forecast (median -18.7%, 8 of last 10 quarters missed) | P5, P6 | Sell | 2 |
| 13 | M&A cycle: each large deal added 0.9-1.6x of leverage; new deal risk with a stock at 6.3x | P1 | Sell | 2 |
| 14 | Governance (48% checklist, 1/10 takeover defences), two CEOs in 18 months, disclosure irregularities | P12, P13 | Sell | 1 |
| 15 | Price-led growth reversed in five episodes; GLP-1 and private label (35% of fresh packed bread units) | P3 | Sell | 2 |
| 16 | Canada Bread unquantified liabilities | P14 | Sell | 1 |

Weighted sums `[calc]` of the list above: Buy 11, Hold 10, Sell 8. The tallies are close because the items are not independent (items 3, 4 and 10 are one cash-flow story). Re-weight by the team's own view of volume and capex sustainability.

## 4. Mentor tests, in one line each

Full numbers in [[bimbo-evidence-vs-mentor-tests]].

| Mentor test | What the evidence says | Verdict |
|---|---|---|
| (1) M&A as thesis | 3 of 12 M&A targets met; leverage +0.9-1.6x per large deal; 9.1-9.3x paid vs 6.3x own multiple; pay-off in 3-10 years | Unsupported for a 12-month thesis |
| (2) Healthy-food trend in Europe | No call 2011-2Q26 discusses it; Europe is private label and bolt-ons; no market-growth number in the files | Unproven (no numbers) |
| (3) New CEO | Two CEOs in 18 months; Barcel credential is company-selected windows; improvements attributable to easy comps, one-off, FX, a prior programme | Unproven |
| (4) AI as a driver | No mention in any call, release or deck; Responsible AI score 0 vs industry average 2 | Unsupported (do not use) |
| (5) Inelastic demand | Mexico volume -6%/-3% (2014), US elasticity 2018-19 and 2022, NA volume negative 2024-25; Mexico resilient 2025-26 | Unsupported as stated; Mexico partly resilient |
| Commodities, hedging, pass-through | Lags 6-18 months; unsized pass-through; 2027 at higher cost | Partly supported (hedging delays, does not remove) |
| Deleveraging, how | Disposal, FX, capex under-spend, EBITDA growth; 1H26 FCF-led but with a WC gap | Supported for 2026, quality mixed |
| Volume x price | Volume never disclosed after 2017; residual method only | Unproven (needs assumptions) |

## 5. Contradictions between sources the team must resolve

| # | Topic | Source A | Source B | Why it matters | Suggested resolution |
|---|---|---|---|---|---|
| C1 | 2026 dividend per share | MXN 1.75 (BMV Jun-26 p.97; [[bimbo-cash-flow-and-fcf]]; [[bimbo-catalyst-calendar-facts]]) | MXN 1.075 (AGM notice CONV-2026 p.1; [[bimbo-agm-dividends-and-buybacks]]); 4,626.7 / 4,304.7m shares = 1.075 `[calc]` | Yield and payout (1.075 / 55.41 = 1.9%) | Use 1.075; BMV filing has a digit transposition; fix the team memo and three wiki articles |
| C2 | Control group | 81% / float 19% (deck 3Q22 p.2, filed to LSEG Nov-2024; [[bimbo-ceo-and-management-changes]]) | 72.03% six vehicles (RA25), 72.37% (LSEG), 72.5% (Apr-2022 register) | Free float for liquidity and governance scoring; an 8.5-pt gap | Take the register; ask IR what the 81% includes |
| C3 | EBITDA and multiple basis | CIQ implied LTM EBITDA 64,706, EV/EBITDA 6.29x | Company LTM 60,919, 6.68x; Yahoo 6.9x | Comps and valuation bridge | Use one basis per method and state it; do not mix with company net debt |
| C4 | Net debt basis and consensus | CIQ net debt FY25 149,031, FY24 +1,200; consensus FY26 146,911 | Company 145,128 (Dec-25), 137,097 (Jun-26); 2.5x | Consensus deleveraging (-2,120) is stale vs the -8,031 in 1H26 | Compare on company basis (consensus less 3,903) |
| C5 | Consensus capex and revenue | Capex 21,979; revenue 426,275 (top of range) | Guidance top 21,024 (US$1.2bn); 1H26 revenue -2.6%; 2H needs +2.2% | Stale consensus is the variant-view opening | Show forecast vs guidance, not vs consensus |
| C6 | Company FCF 1H26 | ~12.0bn (deck 2Q26 p.15; working capital +2.6bn) | Proxy B 8,986; cash-flow lines working capital -582 (BMV Jun-26 p.17-18) | Pillar 2 FCF and yield | Ask IR for the WC definition; use proxy B until reconciled |
| C7 | NA volume and share | "Share gains in all US categories, first since 2020" (2T26 p.3; Circana 12 weeks) | Bimbo box bread -2.8%, other center-store breads -8.6% (Circana 52 weeks to 19-Apr-2026, press); Global Data share 7.4% vs 8.1%; Barcel USA #5 to #6 (team memo) | Pillar 1 | Purchase Circana or ask IR for 52-week series; use sequential windows consistently |
| C8 | Group volume | "Positive global volume" 2024, 1Q25, 3Q25 (calls) | Tonnes of packaged product -7.8% in 2025 (5.83 to 5.38 Mt; deck 2026-07-24 p.21) | Volume forecast | Annex excludes plants in grace period; request like-for-like tonnes |
| C9 | FY25 cut cause | "100% FX" (CFO, call 2025-07-24 p.9) | May-2025 deck cites peso (~2 pp) and softer NA consumption; July FX 250bp | Quality of excuses | Attribute 4.5 of 5 pp to FX `[calc]`; track NA consumption |
| C10 | FY24 EBITDA growth | +2.3% (deck 2025-02-27 p.18) | +1.0% (1Q-3Q25 decks p.16; 55,474 / 54,942 = +0.97% `[calc]`) | Base for FY25 growth | Use reported 55,474 |
| C11 | NA margin history | 9.4% (3Q16), 11.3% (2019), 12.9% (2020), 8.4% (2024) as printed | Mixed IFRS 16 bases; Flowers 10.2% on US GAAP | Pillar 1 ceiling | Rebuild NA margin ex-IFRS 16 (gap G2) |
| C12 | Leverage in the same quarter | Dec-14: 3.2x pro forma (call 2015-02-27 p.5); 3.4x (net, [[bimbo-analyst-forecast-accuracy]]) | 3.7x net (INT-140918, Sep-14); 1Q20 2.8x (call 2020-04-27 p.6) vs INVEX 3.92x (INVX-200428) | Comparing leverage across eras | Use company ex-IFRS 16 from 2020; record each broker's definition |
| C13 | Credit quality | S&P BBB+, Fitch BBB+, Moody's Baa1; RA25 p.82 "best-rated among global peers" | LSEG combined BBB- (score 16); S&P outlook negative | Cost of debt, buyback capacity | Quote agencies for rating, LSEG for relative ranking only (Bimbo near the bottom with Sigma and Andina of seven peers) |
| C14 | Debt records | Revolver Tranche B to 15-Mar-2028 (RA25 p.140); USD 2049 notes 560, 2051 585.3 outstanding | LSEG 19-Aug-2028; 600 and 600 (issue size) | Maturity wall | Use the filing and CIQ stack |
| C15 | ESG measures | LSEG ESG 84.62 (A), governance A- 76.59; renewable energy use 22.02% | S&P ESG 57-58, Governance 41; company 97-100% renewable electricity; LSEG sustainability pay FALSE vs TPI sheet Yes | Credibility of ESG claims | Cite both; define electricity vs energy; avoid single-score claims |
| C16 | Pamias dates and Ricolino proceeds | Pamias COO "2022" ([[bimbo-governance-and-ownership]]); Ricolino EV 27,000 | Announced 22-Feb-2023 (call 2023-02-22 p.4-5); collected 25,797 (RA23 EEFF p.11), 4.5% gap `[calc]` | Timelines, net debt bridge | Use calls for dates; ask for the EV-to-cash bridge |
| C17 | Deal multiples (resolved in the wiki) | Sara Lee 6.9x; Canada Bread 9.9x; "no multiples disclosed" ([[bimbo-history-2008-2013]], [[bimbo-history-2014-2020]]) | 9.1x on US$78m; 9.3x EV/EBITDA, 1.2x sales (deck 2011-10-24 p.5; deck 2014-02-12 p.2) | Precedent multiples | Use the company decks |

## 6. The ten most valuable data gaps and where to get them

| # | Gap | Why it limits the model | Where to get it |
|---|---|---|---|
| G1 | Volume and price/mix by region and quarter (North America and Mexico above all) | Volume x price forecast and mentor test 5 are residual-only | Ask IR for the call Q&A basis; Circana 52-week series for BBU; NielsenIQ and ANTAD/Kantar for Mexico; INEGI; sustainability annex tonnes like-for-like |
| G2 | North America EBITDA margin ex-IFRS 16 and the transformation programme (capex envelope, savings, end date, closures) | Pillar 1 ceiling and Flowers comparison | IR; 4Q24 call transcript; Nov-2019 investor-day Q&A; Flowers 10-K (US GAAP) for the peer basis |
| G3 | Hedge coverage and 2027 cost; raw-materials split (flour, oils, sugar, eggs, packaging); El Niño exposure | Pillar 1-2 margin in 2027 | EEFF derivative notes (counts illegible), 2Q26 call Q&A (the team memo cites roic.ai), CBOT/ICE forwards, USDA, procurement disclosure by IR |
| G4 | Mexico demand and a Walmex comparable | Mentor test 5 (Mexico demand "weak"; Walmex "beaten down") | Walmex (BMV filings), ANTAD monthly, INEGI retail and CPI, Banxico remittances; none of Walmex is in the corpus |
| G5 | Prices and EBITDA of 2021-2026 bolt-ons; organic vs inorganic split in EAA | Mentor test 1; accretion cannot be tested | Purchase-price notes in quarterly BMV XBRL (2025 PPA net assets ~11.7bn); CADE (Brazil), Romanian competition council; IR |
| G6 | Reconciliation of company FCF (working capital +2.6bn vs -0.6bn; MEPP cash; 1Q26 gain) and FCF FY22-FY25 on the company definition | Pillar 2 FCF yield | IR; 2Q26 call; EEFF cash-flow detail |
| G7 | S&P rating rationale and triggers; covenant threshold and definition of Conformed EBITDA; CDS and bond spreads over time | Credit risk, buyback capacity, WACC | S&P report of 20-Mar-2025; Fitch 29-Jul-2026 and Moody's 25-Sep-2026 reviews; indentures (GEM listing documents, Dublin); TRACE; LSEG has no Bimbo CDS |
| G8 | Broker-level consensus: rating distribution (Buy/Hold/Sell counts), names, regional margin, EPS bridge | Variant perception and hit rates | CIQ entitlements; Bloomberg; brokers Actinver, GBM, Itaú BBA, Santander |
| G9 | Canada Bread litigation exposure and the Maple Leaf claim (pleadings, hearing dates) | Risk sizing | Ontario court records; Maple Leaf Foods filings (SEDAR+); Bimbo events reports; class-action counsel notices |
| G10 | Missing narrative: 4Q24 transcript, Nov-2019 Q&A, reason for the Nov-2025 CEO change, beneficial owners behind the 72% bloc and the 81% claim | Mentor test 3, governance | BMV evento relevante of 6-Nov-2025; Reuters and El Economista; CNBV; ask IR for the 81% definition |

## 7. What would change the view (kill criteria)

Each trigger is observable; the date or source is the next point at which it can be checked. Thresholds are `[assumption]` and should be re-set by the team to its own thesis.

| Direction | Trigger | Threshold | When |
|---|---|---|---|
| Against P1 | NA YoY EBITDA margin falls in 3Q26 or 4Q26 | Below 10.4% (3Q25) or 9.2% (4Q25) | 3Q26 release expected 22-Oct-2026 (CIQ); 4Q26 Feb-2027 |
| Against P1 | NA ex-FX sales negative again, or volume positive claimed without a number | < 0% in two quarters | 3Q26, 4Q26 |
| Against P2 | Leverage back to 2.7x or net debt above Dec-25 (145,128) | >= 2.7x ex-IFRS 16 | each release |
| Against P2 | 2H26 capex above US$0.8bn (FY above US$1.2bn) | PP&E capex 2H26 > ~14bn | 4Q26 |
| Against P2 | Distributions above proxy FCF for two consecutive halves | >100% | 2H26, 1H27 |
| Against | An acquisition above US$500m or at 8x+ without a funding plan; second S&P action | EV > US$500m; downgrade to BBB | any time; S&P decision due by about 2027 `[assumption]` |
| Against | FY26 EBITDA below the floor of the range | < 60,465 (2H26 < 31,316) | 4Q26 |
| Against | 2027 guide below consensus | EBITDA < 64.9bn or margin < +50bp | Feb-2027 |
| Against P3 | IEPS rate to 20% or NA category volume below -5% in 2027 | enacted | Congress ~Nov-2026; Circana |
| Against | USD/MXN above 19.8 for a quarter (pessimistic case in the team memo) | > 19.8 | monthly |
| For | NA ex-FX sales >= +2% with quantified positive volume and margin >= 10.4% in 3Q26 | both | 3Q26 |
| For | Lease-adjusted leverage below 2.8x and S&P outlook stable | both | 2027 |
| For | FY26 EBITDA at or above 64,470 (top of range) and 2027 guide above consensus | both | 4Q26 / Feb-2027 |
| For | Reconciled FCF (company definition and proxy within 10%) above 20bn LTM | LTM | 2Q27 |

## Key Takeaways

- ==Large deals have been a leverage event first and a margin event 2-5 years later (six deals, 1.07x to 2.64x after Weston 2002, 3.5x after East Balt 2017); the only sub-2x readings came from COVID cash flow and the Ricolino sale.==
- Deleveraging in 2025 was entirely denominator (EBITDA +6.5% ex-IFRS 16) with net debt +2.3bn; 1H26 is FCF-led (6.4bn net) but the company FCF carries a 3.2bn working-capital gap to the cash-flow statement.
- Distributions exceeded the FCF proxy over FY21-FY25 (36.5bn returned vs -5.7bn proxy), buybacks were made at 62-86, and S&P's negative outlook is 19 months old.
- Brokers are good on next-year EBITDA (MAE 2.9%) and bad on EPS (median -18.7% in 2011-2020) and multi-year margins; today's consensus has no margin ramp and stale capex, net debt and D&A lines.
- Management guidance (36% hit rate; 16% for 2011-2016 targets) reset to a floor in FY26 and was raised twice; the AI, European healthy-food and new-CEO claims have no numbers in the files and should be dropped or proved.
- Seventeen cross-source contradictions need a decision before the model is locked; the most expensive are the net debt and EBITDA bases (C3, C4), the company FCF (C6) and North America margin comparability (C11).
- The evidence is balanced across buy, hold and sell once overlapping items are removed; the deciding variables are NA volume, capex sustainability and 2027 input costs, none of which is quantified in the sources.
