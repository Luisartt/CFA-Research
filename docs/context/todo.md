# Open work

Only `pending` and `in_progress` items. Delete an item when it is done.
Format: `- [pending|in_progress] <task> — owner: <name> — due: <YYYY-MM-DD>`
Soft cap: see AGENTS.md > Context files.

## Milestones

- [in_progress] industry analysis (research/industry.md drafted 2026-10-17; market definition, moat and peers open) — owner: industry — due: 2026-10-21
- [in_progress] report draft (v1 PDF 2026-10-19 is on the old basis; must move to HOLD, target Ps 64.18 method B, reference Ps 58.60, figures from the TP12m workbook only) — owner: writer — due: 2026-10-30
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

- [pending] single HOLD thesis v4 (BIMBOA_Entrega_CFA/02_Tesis/BIMBOA_Tesis_HOLD_unica_v4_EN.docx): resolve the [unverified] numbers; reconcile the North America share-gain ratio 0.17 with pillar 1 and the old Thesis 3 line; state what the market misses per pillar — owner: all — due: 2026-10-30
- [pending] thesis evidence gaps: North America volume/price/mix and transformation programme size, a Circana share series, the source of Mexico's share gain, Bimbo's 2027 wheat hedge coverage; Stone House inside 9M26 growth — owner: all — due: 2026-10-30
- [pending] risks-esg: choose the 4-6 key risks (draft v3 pillars 1 and 3 move here), their scores and what is priced in; choose 3-5 material ESG issues; re-score the governance rubric — owner: all — due: 2026-10-30
- [pending] ESG data gaps: Sustainalytics second-party opinion, MSCI/DJSI ratings, assured Scope 1-3 series, water-stressed plant count (101 vs 89), renewable electricity 100% vs 99% — owner: all — due: 2026-10-30
- [pending] industry [unverified] figures: Mexico competitor shares, numeric shares in Brazil, Colombia, Argentina, Spain and the UK, a US share series by category (Circana), Bimbo's US volume/price split; save sources in research/sources/ — owner: industry — due: 2026-10-30
- [pending] industry decisions: market definition, moat and peer set — owner: all — due: 2026-10-30
- [pending] confirm macro/macro-view.yaml field by field (all status: propuesto) and save a FRED key in macro/fred.key (keep it out of git) — owner: all — due: 2026-10-30
- [pending] peer data still open: Gruma BMV official close; Aryzta and Arca book NCI; Yamazaki operating leases (J-GAAP); Gruma consensus in its native currency — owner: valuation — due: 2026-10-30

## Report

- [pending] report charts: redraw football-field.png and sensitivity.png from the TP12m workbook (current ones come from the engine basis) — owner: valuation — due: 2026-10-30
- [pending] report: insert the official CFA cover and fill its fields; team confirms the AI-use disclosure (who checked the citations); spot-check citations and page numbers against the PDFs — owner: writer — due: 2026-10-30
- [pending] report: rebuild on the TP12m figures and the 3Q26 results; the old build (valuation/build/consolidate_models.py, report_levers.py) reads the archived three-DCF basis, so do not rerun it without asking — owner: model — due: 2026-10-30
- [pending] report: decide the final format and length (PDF template 9 body pages at 8.7 pt; the rule is 10 A4 pages) — owner: all — due: 2026-10-30
- [pending] report: keep the Spanish copy in sync after every English edit (output/reporte-es/sections/*.md, REPORT_LANG=es builds) — owner: writer — due: 2026-10-30

## Wiki and housekeeping

- [pending] compile remaining Capital IQ material (1,921 PDFs, 115 docx, 66 mp3) — owner: all — due: 2026-11-04
- [pending] add callout in bimbo-valuation-data-gaps: consensus now exists in ciq-consensus-estimates; confirm FY26 guidance vs transcript — owner: valuation — due: 2026-11-04
- [pending] SECURITY: rotate the Obsidian Local REST API key and TLS certificate committed in .obsidian/plugins/obsidian-local-rest-api/data.json (public repo), then stop tracking that file; purging history needs a force push (your decision) — owner: Luis Arturo Romo Alba — due: 2026-10-18
- [pending] optional: report the two unanchored DCF rows of the engine model (DCF!19-20, model-check S5) to the plugin maintainer — owner: model — due: 2026-11-04
