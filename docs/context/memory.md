# Decisions

Format: `# decision: <one sentence>` (optional second line: why). Newest last.
Soft cap and rules: see AGENTS.md > Context files.

# decision: framework = IFRS (confirmed by team: yes)
# decision: presentation language = en (report always English)
# decision: wiki domains = Company, Industry, Financials, Valuation, Macro, Risks-ESG, Thesis, CFA-Process (strict 2 tags; raw/ + filings/ are read-only inboxes)
# decision: model history = FY2021-FY2025, MXN millions, IFRS (financials and model skills)
# decision: thesis pillars = climate change (input costs), new CEO (execution), debt management with a "hold" stance measured against all comparables, US and Mexican (team, 2026-10-16)
# decision: valuation published basis v2 = engine mechanics + lease liability grows with revenue + exit on peer-EV claims (technical choice; Codex audit PASS 2026-10-17)
why: the engine proxy keeps leases flat while revenue grows, and peer EVs exclude pensions, provisions and derivatives

# decision: peer claim basis v3 = debt + leases + NCI at book - cash with IFRS 16-equivalent EBITDA at the pricing-date FX (USD/MXN 18.479); a peer enters the medians only with a reconciled lease basis and verified NCI (technical, 2026-10-17)
why: one basis for every company; 102/102 results equal the independent calculation (valuation/BIMBOA_PeerAnalysis_v3.xlsx)
# decision: publication gate v3 = build -> translate -> recalculate in Excel -> scan -> checks, recorded with SHA-256 hashes in valuation/verification-v3.json by valuation/build/write_outputs.py (technical, 2026-10-17)
why: Codex found workbooks without cached results in round 1 of the v3 plan review
# decision: each thesis is one sentence in the format "Problema — a raíz de [causa]" (in English files: "Problem — due to [cause]"); candidate set for the HOLD = two sell theses and one buy thesis (team, 2026-10-19; wording of the three theses still open)
why: the team captain asked for this format when shaping the pillars; the pillars chosen on 2026-10-16 are not yet written this way
# decision: the report follows last year's La Comer report as a template (cover, header band, two-column body with figures on the right, appendix) in Bimbo's colour palette; the draft shows HOLD (provisional) and target price TBD (team, 2026-10-19)
why: the team captain attached the La Comer report and asked to replicate its format and charts for Bimbo with Bimbo's colours
# decision: the report rests only on the consolidated cash flow (DCF) for valuation and forecast; no model comparison in the report text; statements shown are the audited FY2021-FY2025 history (team, 2026-10-19)
why: the team captain corrected the first draft, which described averaging two input sets and a separate three-statement forecast
# decision: the report the team submits is the English one (CFA rule 2.6c); a Spanish copy is kept for internal use and is rebuilt from the English text after every edit (team request, 2026-10-19)
why: the team captain asked for the draft in Spanish; the Spanish sections live in output/reporte-es/sections and are built with REPORT_LANG=es
# decision: thesis 1 (upside) = "North America's margin problem is being corrected — due to cost restructuring and better price/mix, with capex normalised and Mexico funding the turnaround" (team, 2026-10-19; validated as written in report draft v1)
# decision: thesis 2 (downside) = "2027 margins are at risk — due to wheat, with futures up 35% year on year and hedges placed at 2025 prices rolling off" (team, 2026-10-19)
# decision: thesis 3 (downside) = "Organic growth falls short of the model — due to record private label, a shrinking US bread category and a Mexico that slowed to +2.4% in 2025" (team, 2026-10-19)
why: the team captain validated the three theses "tal como están en el borrador" and made them the base to continue; they replace the pillars of 2026-10-16 (climate and input costs, new CEO execution, debt hold); the drafted "what would change our view" triggers go with them; rating (HOLD, provisional) and target price stay open until the team chooses the exit multiple (research/thesis.md v2)
