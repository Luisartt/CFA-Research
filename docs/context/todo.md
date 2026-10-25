# Open work

Only `pending` and `in_progress` items. Delete an item when it is done.
Format: `- [pending|in_progress] <task> — owner: <name> — due: <YYYY-MM-DD>`
Soft cap: see AGENTS.md > Context files.

## Milestones

- [in_progress] thesis v2 (three theses validated 2026-10-19, research/thesis.md v2; open: what the market misses per thesis, and the rating, which follows the exit multiple) — owner: all — due: 2026-10-24
- [in_progress] industry analysis (research/industry.md and BIMBOA/research/industry/industry-report_2026-10-17.md drafted; market definition, moat and peers open) — owner: industry — due: 2026-10-21
- [in_progress] valuation and target price (mechanics v3 done: route B base proposal, Gordon 33.55 / exit 45.72; team decisions open, valuation/valuation.md §11 and output/dcf-v3-conclusiones.md) — owner: valuation — due: 2026-10-14
- [in_progress] report draft (first draft PDF built 2026-10-19: report/BIMBOA_report_v1_draft.pdf, La Comer format, Bimbo palette, 9 body pages + 5 appendix; theses provisional, target TBD; on the consolidated cash flow only; copy in Drive Reporte Final) — owner: writer — due: 2026-10-25
- [pending] final report — owner: all — due: 2026-11-04
- [pending] presentation — owner: all — due: 2026-12-08

## Tasks

- [pending] decide WACC variant: route B (base proposal) or A, beta source, target D/E; alternatives in DCF v3 'Scenarios' — owner: valuation — due: 2026-10-21
- [pending] decide terminal assumptions: g, exit multiple, long-run return on new capital (capex path FY2031-35) — owner: valuation — due: 2026-10-21
- [pending] confirm the 3-5 story drivers (segment growth, gross margin, opex, capex) and the number each must hit — owner: all — due: 2026-10-21
- [pending] decide bridge judgements: NCI uplift (Ps 4.47/share at ke 12.94%), provisions incl. uncertain tax positions (Ps 2.66/share) — owner: valuation — due: 2026-10-21
- [pending] decide use of excess cash in the forecast (buybacks, debt paydown, M&A) — owner: model — due: 2026-10-21
- [pending] set target price, method weights and rating — owner: all — due: 2026-10-24
- [pending] decide how to weight country risk and the discount rate by region: one MXN WACC with weighted country premium (v3 base: route B by FY2025 Adj. EBITDA 2.05%; by sales 1.70%, 3-year weights 1.99% / 1.65%, ex-Argentina 2.02%) or a regional DCF using the company's own impairment-test rates (Mexico 10.00%, US 7.27%, Canada 6.50%, Spain 7.00%, Brazil 10.25%; RA25 p.265) — owner: valuation — due: 2026-10-21
- [pending] settle the terminal capex (peers' consensus 3.7-3.8% of sales, Bimbo consensus ~5.0%, model 6.0%; ±50 bp = ∓Ps 9.4): the company's impairment tests assume 3.3-4.3% of sales (maintenance-type, IAS 36), disclosed growth share of capex was 45% in 2021 and 36% in 2022; terminal capex below D&A excluding right-of-use (4.4%) is not sustainable with 4.25% growth — owner: model — due: 2026-10-24
- [pending] compile remaining Capital IQ material (1,921 PDFs, 115 docx, 66 mp3: news, filings, broker research, transcripts) — owner: all — due: 2026-10-14
- [pending] resolve the last flagged contradiction: FY22 buyback 2,556 vs 2,568 (resolved 2026-10-17: dividend 1.075 not 1.75, AGM notice; plants 249 = 248 + Venezuela; CIQ net debt 149,031 vs company 145,128 is a basis difference, wiki C4) — owner: model — due: 2026-10-21
- [pending] add callout in bimbo-valuation-data-gaps: consensus now exists in ciq-consensus-estimates; confirm FY26 guidance vs transcript — owner: valuation — due: 2026-10-14
- [pending] confirm macro/macro-view.yaml field by field (all status: propuesto; BIMBOA/journal/decisions.md 2026-10-17) and save a FRED key in macro/fred.key (keep it out of git) — owner: all — due: 2026-10-21
- [pending] peer data still open: Gruma BMV official close; Aryzta and Arca book NCI; Yamazaki operating leases (J-GAAP); Gruma consensus in its native currency — owner: valuation — due: 2026-10-21
- [pending] thesis: for each of the three validated theses, state what the market misses (variant perception vs consensus; research/thesis.md v2 [team] slots) — owner: all — due: 2026-10-24
- [pending] thesis evidence gaps: North America volume/price/mix and transformation programme size (capex, savings, end date), a Circana share series, the source of Mexico's share gain (about 0.3 points a year), Bimbo's 2027 wheat hedge coverage — owner: all — due: 2026-10-24
- [pending] risks-esg: choose the 4-6 key risks, their scores and what is priced in; choose 3-5 material ESG issues; re-score the governance rubric (research/risks.md §5, research/esg.md) — owner: all — due: 2026-10-24
- [pending] ESG data gaps: Sustainalytics second-party opinion, MSCI/DJSI ratings, assured Scope 1-3 series, water-stressed plant count (101 vs 89), renewable electricity 100% vs 99% — owner: all — due: 2026-10-24
- [pending] report charts: football-field.png and sensitivity.png in report/charts come from the engine basis (superseded in valuation-outputs.yaml); redraw them from the published basis before the report — owner: valuation — due: 2026-10-25
- [pending] forecast evidence: what supports an EBITDA margin above the clean historical best (14.4% FY21) from FY2028 (program-level savings), and the implied share path in North America (~0.8 pp a year) and Mexico (~0.3 pp a year) — owner: all — due: 2026-10-24
- [pending] industry [unverified] figures: Mexico competitor shares (Sabritas, Gamesa, Bokados), numeric shares in Brazil, Colombia, Argentina, Spain and the UK, a US share series by category (Circana) and Bimbo's US volume/price split; save sources in research/sources/ — owner: industry — due: 2026-10-24
- [pending] industry decisions: market definition, moat and peer set (research/industry.md coach moments) — owner: all — due: 2026-10-21
- [pending] SECURITY: rotate the Obsidian Local REST API key and its TLS certificate (they are committed in .obsidian/plugins/obsidian-local-rest-api/data.json in the public repo), then stop tracking that file; purging it from git history needs a force push (your decision) — owner: Luis Arturo Romo Alba — due: 2026-10-18
- [pending] optional: report the two unanchored DCF rows of the engine model (DCF!19-20, model-check S5) to the research-challenge plugin maintainer — owner: model — due: 2026-10-24
- [pending] decide the consolidation rules for the three DCFs: weights (50/50 input sets vs one third per model), Diego's exit-multiple basis (5.92x lease-consistent vs 6.2x raw), tax on EBIT (34% / 30% / 32%), horizon (5-year template vs v3 10 years); valuation/consolidated-valuation.md §11 — owner: all — due: 2026-10-21
- [pending] Diego's workbooks: replace the Capital IQ debt reconverted at 17.96 MXN/US$ (194,918, incl. 2,658 derivatives) and cash (17,023) with the company figures (187,021 / 16,563); confirm Gruma LTM EBITDA (company 1,108.9 vs CIQ 995.0) — owner: Diego Benavides Pro — due: 2026-10-21
- [pending] report: choose the exit multiple on evidence (base 5.92x; clean HOLD needs 6.16x-6.82x; price needs 6.95x), set target price and rating, then remove "provisional" and "TBD" from the header band, Executive Summary and Valuation — owner: all — due: 2026-10-24
- [pending] report: insert the official CFA cover and fill its fields; team confirms the AI-use disclosure (who checked the citations); spot-check the citations and page numbers against the PDFs — owner: writer — due: 2026-10-30
- [pending] report: refresh after the 3Q26 results (late October, date not announced): rerun valuation/build/consolidate_models.py, report/build/report_levers.py, report_charts.py, build_report_pdf.py, check_report.py — owner: model — due: 2026-10-30
- [pending] report: decide the final format and length (the PDF template is 9 body pages in two columns at 8.7 pt; the plugin's Word estimate is 12 pages at 500 words per page; the rule is 10 A4 pages) — owner: all — due: 2026-10-25
- [pending] report: keep the Spanish copy in sync after every English edit: update output/reporte-es/sections/*.md, then from report/build run `REPORT_LANG=es python report_charts.py` and `REPORT_LANG=es python build_report_pdf.py` (writes output/BIMBOA_reporte_v1_borrador_ES.pdf); the build lists any untranslated string — owner: writer — due: 2026-10-30

- [in_progress] Forecast statements FY2027E-FY2030E (FY2026E IS, BS, CF and equity done, Checks OK, 2026-10-23); NCI method B done (NCI held at 743); FY2027E sales: CAGR 1.71% still in the Excel but superseded 2026-10-24 (advisor feedback), to be replaced once the method is chosen; FY2027E cost of sales by nature linked (raw materials by elasticity 0.109, wheat 2026E 217.92; freight at FY2026E ratio, final; COGS depreciation from PP&E depreciation rate 10.54%; gross margin 51.99%); capex FY2027E US$1.30bn (2026 level + deferred projects) x 17.77 = 23,101; FY2027E opex by nature linked (integration 541; EBIT 35,395; Adj. EBITDA margin 14.08%); FY2027E below EBIT linked (interest 11,553; tax 37% proposed; EPS 3.054); open: 6.5% vs implied 7.47% rate, tax FY2027 37% and FY2028-30 32.7% (decided), PP&E/capex into BS-CF 2027, debt in MXN at 17.84 with FX through interest (decided), VPPA = 0 pending, tax rate levels FY2027 and FY2028-30, debt x rate interest, buybacks 0, dividend 1.117 — owner: Jorge Alejandro Gaytan — due: 2026-10-27
- [in_progress] Sales method (advisor feedback): Capital IQ data collected 2026-10-24 (blocks M1-M5, X1, E1-E5, F1-F2, S1-S2, P1-P2, I1 in data/capitaliq/); next: screen checks (KAZ/KOR/MAR 2026 step, HRV unit, SVN 2025, FX thousands unit), nominal GDP growth [calc], team picks variable, ratio per region and FX path, replace the FY2027E CAGR; see docs/context/handoff_sales-method_2026-10-24.md — owner: Jorge Alejandro Gaytan — due: 2026-10-26
- [pending] learn the business-vs-FX split of consolidated sales (regional FX factor and FX effect line) before Q&A prep — owner: Jorge Alejandro Gaytan — due: 2026-10-27
- [pending] finish FY2027E: cash-flow items held at 0 in FY2026E-FY2027E (employee benefits paid ~2,600/yr, current service cost, intangible purchases); interest income on cash (0 today) — owner: Jorge Alejandro Gaytan — due: 2026-10-27
