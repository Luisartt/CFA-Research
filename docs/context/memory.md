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
