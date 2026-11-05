# Open work

Only `pending` and `in_progress` items. Delete an item when it is done.
Format: `- [pending|in_progress] <task> — owner: <name> — due: <YYYY-MM-DD>`
Soft cap: see AGENTS.md > Context files.

## Milestones

- [in_progress] industry analysis (research/industry.md drafted 2026-10-17; market definition, moat and peers open) — owner: industry — due: 2026-10-21
- [in_progress] report v2 (report/BIMBOA_report_v2.docx, template = La Comer report, TP12m basis: HOLD, target Ps 64.18, price Ps 58.60) built 2026-10-28; team to confirm the three pillars, risks and ESG choices, and check the 10-page count in Word — owner: writer — due: 2026-10-30
- [pending] final report — owner: all — due: 2026-11-04
- [pending] presentation — owner: all — due: 2026-12-08

## Model and valuation (source: analisis-dcf-2026-10-26/precio-objetivo/..._TP12m.xlsx)

- [pending] fix the five workbook inconsistencies flagged in analisis-dcf-2026-10-26/notas/guion_proyecciones_V2_4T26_ES.md §7, in a copy: stale notes (Methodology C22/F22, row 13, row 15; Assumptions G298), FY2026E PP&E depreciation base (17,254 vs 16,591), FY2026E debt repayment 2,413 vs contractual 1,552 (possible FX translation counted as cash) — owner: Jorge Alejandro Gaytan — due: 2026-10-30
- [pending] decide whether to deduct 4Q26 and FY2027E buybacks from the share count (up to +Ps 0.92 on the target) — owner: valuation — due: 2026-10-30
- [pending] WACC D/E is provisional (current market 0.743, 2026-10-27): confirm or replace — owner: valuation — due: 2026-10-30
- [pending] statements opens: cost of debt 6.5% vs implied 7.47%, VPPA = 0, payable days trend, FY2027E margin vs FY2026E (wheat) — owner: Jorge Alejandro Gaytan — due: 2026-10-30
- [pending] text files still quote superseded figures (valuation/valuation.yaml g 0.0271, valuation/valuation.md, research/thesis.md, output/dcf-v3-conclusiones.md): left untouched in PR 4 by decision; update to the TP12m workbook or mark them superseded — owner: Jorge Alejandro Gaytan — due: 2026-11-01
- [in_progress] BIMBOA_WACC_v3.xlsx restored in valuation/ on 2026-10-28 (identical to the archived copy; the 11 cells cited by WACC_V2 and Assumptions match); commit it and open a pull request together with the context files — owner: Jorge Alejandro Gaytan — due: 2026-10-30
- [pending] the TP12m workbook has no build script in the repo (analisis-dcf-2026-10-26/build/ only rebuilds the auditfix and V1V3 copies): keep a backup and change it only in copies — owner: Jorge Alejandro Gaytan — due: 2026-10-30
- [pending] main checkout CFA-Research has 9 uncommitted changes (3 old Excel modified, 5 untracked files in raw/, mostly copies of files already on GitHub): sort them out before git pull — owner: Jorge Alejandro Gaytan — due: 2026-10-30
- [pending] optional: delete the merged remote branch tp12m-final-2026-10-28 — owner: Jorge Alejandro Gaytan — due: 2026-11-01
- [pending] valuation/SPG_* and valuation/team-models/ (the Bimbo_*_Alejandro models are Jorge's own; the SPG_* models are Diego's) were left in the repo for now (Jorge, 2026-10-28); revisit only if the team wants them out; Diego's Capital IQ debt/cash fix only matters if they stay — owner: all — due: 2026-11-01
- [pending] learn the business-vs-FX split of consolidated sales (regional FX factor and FX effect line) before Q&A prep — owner: Jorge Alejandro Gaytan — due: 2026-11-01

## Thesis, risks, industry

- [pending] export a new Capital IQ consensus dated after 22-Oct-2026 (Estimates > Consensus, Estimate Highlights) into filings/capitaliq/Estimates/ and re-run the margin, EBITDA and EPS gaps of thesis 3 — owner: Jorge Alejandro Gaytan — due: 2026-10-30

- [pending] thesis v3: team confirms kill criteria and says why the MXN 64.18 target does not fall; refresh CIQ consensus and price after 22-Oct-2026 — owner: all — due: 2026-10-30

- [pending] single HOLD thesis v4 (BIMBOA_Entrega_CFA/02_Tesis/BIMBOA_Tesis_HOLD_unica_v4_EN.docx): resolve the [unverified] numbers; reconcile the North America share-gain ratio 0.17 with pillar 1 and the old Thesis 3 line; state what the market misses per pillar — owner: all — due: 2026-10-30
- [pending] thesis evidence gaps: North America volume/price/mix and transformation programme size, a Circana share series, the source of Mexico's share gain, Bimbo's 2027 wheat hedge coverage; Stone House inside 9M26 growth — owner: all — due: 2026-10-30
- [pending] risks-esg: choose the 4-6 key risks (draft v3 pillars 1 and 3 move here), their scores and what is priced in; choose 3-5 material ESG issues; re-score the governance rubric — owner: all — due: 2026-10-30
- [pending] ESG data gaps: Sustainalytics second-party opinion, MSCI/DJSI ratings, assured Scope 1-3 series, water-stressed plant count (101 vs 89), renewable electricity 100% vs 99% — owner: all — due: 2026-10-30
- [pending] industry [unverified] figures: Mexico competitor shares, numeric shares in Brazil, Colombia, Argentina, Spain and the UK, a US share series by category (Circana), Bimbo's US volume/price split; save sources in research/sources/ — owner: industry — due: 2026-10-30
- [pending] industry decisions: market definition, moat and peer set — owner: all — due: 2026-10-30
- [pending] confirm macro/macro-view.yaml field by field (all status: propuesto) and save a FRED key in macro/fred.key (keep it out of git) — owner: all — due: 2026-10-30
- [pending] peer data still open: Gruma BMV official close; Aryzta and Arca book NCI; Yamazaki operating leases (J-GAAP); Gruma consensus in its native currency — owner: valuation — due: 2026-10-30

## Report

- [pending] report v10 (team approved the figures; CFA La Comer layout, report/build/build_report_cfa.py): open in Word and check that the two-column rows and figures break well across pages, insert the official CFA cover, check the 10-page count (10 pages in LibreOffice, page 10 half full, 8.8 pt) — owner: all — due: 2026-10-30

- [pending] report: team gives the rubric weights of the other sections (summary, business, industry, risks, management, peers); v5 (four charts moved to Financial Analysis) has summary 1.5, financial analysis and forecast 1.9, valuation and peers 2.2, ESG 0.8, risks 0.9 and industry 0.8 pages; risks is the section furthest under its default share (1.5) — owner: all — due: 2026-10-30

- [pending] report: insert the official CFA cover and fill its fields; team confirms the AI-use disclosure (who checked the citations); spot-check citations and page numbers against the PDFs — owner: writer — due: 2026-10-30
- [pending] report: v2 body is 10 A4 pages in LibreOffice (9 pt Times, about 46 lines on page 10): open in Word, fix any overflow, then decide the final format (Word body behind the official CFA cover vs the old PDF template) — owner: all — due: 2026-10-30
- [pending] report: Spanish copy (output/reporte-es/) is still on the v1 basis; v1 sections moved to report/archive_v1_sections/ and the old PDF build (report/build/build_report_pdf.py) no longer finds its sections — rebuild or retire it — owner: writer — due: 2026-10-30
- [pending] report v3: verify the quarterly North America margins (4Q24 5.9%, 3Q25 10.4%; the 3Q26 figure differs between sources, 9.8% vs 10.8%), the Banxico 17.77 run and the 27-Oct close of MXN 64.85 (Yahoo Finance) against the releases and the market data; check the 10-page count in Word (v2 body is 10 pages in LibreOffice, six thesis charts) — owner: all — due: 2026-10-30
- [pending] report: pillar wording, what the market misses per pillar, risk scores R1-R6 and the third ESG/risk choices are assistant drafts — team confirms — owner: all — due: 2026-10-30

## Wiki and housekeeping

- [pending] compile remaining Capital IQ material (1,921 PDFs, 115 docx, 66 mp3) — owner: all — due: 2026-11-04
- [pending] add callout in bimbo-valuation-data-gaps: consensus now exists in ciq-consensus-estimates; confirm FY26 guidance vs transcript — owner: valuation — due: 2026-11-04
- [pending] SECURITY: rotate the Obsidian Local REST API key and TLS certificate committed in .obsidian/plugins/obsidian-local-rest-api/data.json (public repo), then stop tracking that file; purging history needs a force push (your decision) — owner: Luis Arturo Romo Alba — due: 2026-10-18
- [pending] optional: report the two unanchored DCF rows of the engine model (DCF!19-20, model-check S5) to the plugin maintainer — owner: model — due: 2026-11-04

- [pending] review the two arguments that assumed the share trades above the target (thesis 1 'against the price', thesis 3 'already paid') now that the TP12m_v2 target is MXN 66.13 and the 27-Oct close MXN 64.85 is 1.9% below it; also confirm what 'on its own' means in the central thesis — owner: all — due: 2026-11-04
- [pending] open report v12 in Word, check the 10-page body (10 pages in LibreOffice at FIG_W 2.3), insert the official CFA cover — owner: all — due: 2026-11-04
- [pending] cover of report v12: complete [TEAM UNIVERSITY] and the host society if it is not CFA Society Mexico, confirm the two declarations ("does not hold", "does not know" — highlighted in yellow) with every member, then remove the highlight; confirm that the official cover of this season is the same as the La Comer one — owner: all — due: 2026-11-04
- [pending] report v12 body is 10 pages in LibreOffice at 8.4 pt text and 1.8 in figures; check in Word, and decide whether to fill the 14% empty zone at the end of the ESG section with a chart — owner: all — due: 2026-11-04
- [pending] mentor (Alan, 2026-11-02): write the "what has to change" table for the BUY (below MXN 51.84) and SELL (above MXN 69.68) lines as a pessimistic and an optimistic case, with the Wickbold/leverage trigger Jorge described, using only the workbook's sensitivities — owner: Jorge Alejandro Gaytan — due: 2026-11-04
- [pending] mentor: size the hedge risk after 1H27 (roll-over at higher prices) and be ready to say in two sentences what is positive and what is negative; align the organic growth figure (about 3% in the report, 1.3% quoted in the meeting) — owner: all — due: 2026-11-04
- [pending] AI-use disclosure: write the reflection; make two cover versions (with and without the university name) — owner: Luis Arturo Romo Alba — due: 2026-11-04
- [pending] decide the 9M26 growth figure: 4.7% (workbook regional average) or 4.3% (consolidated quarterly: 4.8%, 4.5%, 3.6%); the second makes organic growth about 3.1% and the translation effect 6.4 points, and needs the growth_fx chart updated — owner: all — due: 2026-11-04
- [pending] attach a price file for 16-27 October 2026 (close MXN 64.85, +10.7%) or tag the figure [unverified]; source of the 6.3x-9.5x EV/EBITDA range (Ve por Mas note not in the repo); fix the Valuacion_12m H48 note in the workbook (it says buybacks are not subtracted); source of the 11.5 bp La Moderna one-off (1Q26 call, not the 3Q26 deck); IEPS 8% page reference; debt profile of 3Q26 (9.4 years, 91% long term) — owner: Diego Benavides Pro — due: 2026-11-04
- [Assistant] Quantify review points 5 (NOPAT tax 30% vs effective 37.0%/32.7%) and 6 (NCI growth-consistent) in the Python replica; report MXN/share impact. pending
- [Assistant] Check in filings whether "other expenses, net" and integration costs sit inside Bimbo's adjusted EBITDA (double-count risk, review point 3). pending
- [Team] Decide price date: does the competition fix 16-Oct (58.60) or may we update to 64.85? Decide whether ke flexes with WACC in the rating rule. pending
- [Team] Fill the three "[Team to confirm]" in 99-appendix-ai-use.md; check "as the advisor asked" against CFA advisor rules; choose 4.7% vs 4.3% ex-FX growth. pending
- [Team] attach a price file for 27-Oct-2026 (MXN 64.85, Yahoo Finance); the repo has none, so the figure is cited but not on file. pending
- [Assistant] 9M-multiples at 64.85 (20.4x, 16.2x, about 7.5x EV/EBITDA) were scaled from the earlier figures [calc]; recompute them in the model replica. pending
- [Team] verify in the filings the pillar 2 and Table 6 figures not rechecked (RA23 note 21, LatAm 9.1%/14.1%, 0.76%, +28 bp). pending
- [Team] decide whether to adopt the tax (32.7%) and NCI-with-growth corrections: together they give a target of MXN 59.83 and, at 64.85, the rule says SELL (optimistic return 10.2% < ke 12.26%); today the report discloses them but keeps the model. pending
- [Team] R1 is scored I4 (10-20% of the target); at 14.75 (22%) it would be I5 on the report's own scale; rescore or keep. pending
- [Assistant] compare the subagent's workbook run (B391 = B277*1.35) with the 14.75 and 11.51 figures and fix R1 if it differs. in_progress
- [Team] rating after the corrections: SELL by the team's own rule (target MXN 58.54, -9.7% against 64.85; SELL line 62.41 is 3.8% below the price) or an explicit HOLD override? Decides how the pillars and the central sentence are rewritten. pending
- [Assistant] after the rating decision: point the pipeline at the v3 workbook, refresh data, charts and tables, and rewrite every number tied to the target (66.13, 60.18, band 51.84-69.68, bridge, sensitivities, Table 6 lines) in EN and ES; redo the wheat stress case on v3. pending
- [pending] get the initial 2026 margin guide (4Q25 release, BIMBOA_report 2026b) and compare it with the three raises, to size the chance that the February 2027 guide clears +46 bp — owner: Luis Arturo Romo Alba — due: 2026-11-04
## Report v33 (Alan's feedback; source: docs/context/handoff_luisart_v33_2026-11-04.md on branch tp12m-final-2026-10-28)

- [done in v34, delete after review] Figure 13: redraw the 9M26 bar as 3.4 organic / 1.1 acquisitions / -6.6 translation (unrounded 3.368 / 1.075 / -6.643), replace word/media/image15.png in the EN and ES docx — owner: Luis Arturo Romo Alba — due: 2026-11-05
- [in_progress, wording added in v34; team decides base case] Alan 9: state that the 40-hour week in Mexico (R4) and corporate governance are outside the base case, with their effect; the team decides whether either enters the base case — owner: team — due: 2026-11-05
- [pending] Alan 10: fill the three "[Team to confirm]" in the AI-use section, review "as the advisor asked" (use "excluding acquisitions"), say who verified the citations — owner: team — due: 2026-11-05
- [done in v34, team decides R5 impact] capex +50 bp: measured -3.31 (55.23); original note: measure with the Table 13 method (fixed share count); handoff says -3.26, report says -1.46 (same as the average-RONIC case, likely a copy error); then Table 13 row, R5 text and row, maybe R5 impact 2 -> 3 (team decides; moves Figure 31) — owner: Luis Arturo Romo Alba — due: 2026-11-05
- [done in v34] Figure 32 (tornado): RONIC labels 11.9% / 15.1% -> 11.4% / 14.6%; capex bar depends on the capex item — owner: Luis Arturo Romo Alba — due: 2026-11-05
- [done in v34] risks: Mexico 35% vs 38% (R4) and North America 39% vs 43% (R2): put the year on both figures or use one; delete the stray "##" on p.6 — owner: Luis Arturo Romo Alba — due: 2026-11-05
- [pending] last, once: cut the Spanish body from 11 to 10 pages (EN is exactly 10) — owner: Luis Arturo Romo Alba — due: 2026-11-05

- [pending] 20-second answer to "why is the 14.0% historical margin not SELL if pillar 2 says costs are absorbed?" and to "why is the Street target above ours with a lower margin?" — owner: team — due: 2026-11-04

## Report v35 (SELL; advisor's six points; source: pasted feedback 2026-11-04)
- [done in v35] Rating switched to SELL in EN and ES; reverse DCF (Table 19), model against consensus (Table 20), IFRS 16 note on the multiple history, upside risks with P and I (Table 7), price-date statement. Owner: Luis
- [pending] Team to confirm the five P values of Table 7 and the "[Team to confirm]" on the cut-off date rule and on who verified the citations. Owner: team
- [pending] Source for the 27% annualized volatility (point 5, Q&A only); prepare the answer in pitch/qa-drill.md. Owner: Luis
- [pending] EN: the bullet "The record" (61 targets, Figure 19) has no text in the EN docx; ES has it. Owner: Luis
- [pending] ES body is still 12 pages (appendix p.13); trim to the budget after the placeholders are filled. Owner: Luis
- [pending] Open v35 in Word and check pagination (PDFs are LibreOffice exports). Owner: Luis
- [done in v36] Reference price moved to the 4 November close, MXN 67.27; figures 1, 23, 35 redrawn; Table 4 rule column, Table 7 thresholds and the reverse DCF recomputed. Owner: Luis
- [done 2026-11-04] Price-date rule confirmed by the captain: close at the report cut-off date (4 November 2026). Still open: check that the local round does not fix the price date. Owner: team
- [pending] Page limit (10 pages incl. appendix, cover excluded): the report needs 15 pages today; team must choose option A (keep 8 pt, drop optional appendix, trim ~0.9 page of body) or B (9 pt and 1.5 cm margins, ~5 body pages to cut). Details in report/v36/auditoria_formato_v36.md. Owner: team
- [done in v37] English report in ASD-STE100 style, 10 content pages, detail tables in report/v37/BIMBOA_report_v37_supplement. Owner: Luis
- [pending] Audit of v36 by Jorge (2026-11-04): E5 (price 67.27 in the Excel, three cells), E6 (placeholders), reasoning points 3.1-3.6 need team decisions; 3.1 needs the Capital IQ LTM EV/EBITDA at 4-Nov. Owner: team
- [pending] Verify rule 2.6b against the official Rules PDF of 2026-07-16 (not in raw/). Owner: Luis
- [pending] Decide how to use the 1.2 free report pages: ESG has 0.4 page for 15 rubric points, Financial analysis 1.4 pages for 20 points. Owner: team
- [pending] Spanish v39 body is 10.4 pages (English 10.0): trim or accept, the English report is the one that is submitted. Owner: Luis
- [pending] Update from Capital IQ: consensus after the 3Q26 call, peer prices and the M-Bono yield on 4 November; then rerun the workbook (WACC, peers, consensus table) so all market data share one date. Owner: Luis

## Report v42
- [pending] The four "[Team to confirm]" marks are gone from the text (v42). The team still has to confirm who verified the citations and the cut-off date rule, because the text now states them as fact. Owner: team
- [pending] Environmental subhead in ESG ("climate and input costs matter most") now has only the KPMG sentence under it; keep, retitle or merge with the Table 9 text. Owner: team
- [pending] Spanish body is 10.4 pages (English 10.0), appendix inside; trim or accept. Owner: Luis
