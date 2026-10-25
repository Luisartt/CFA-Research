# Lessons

One line per correction from the team, so the mistake is not repeated.
Format: `- <rule> (YYYY-MM-DD)`
Soft cap: see AGENTS.md > Context files.

- The report uses only the consolidated cash flow (DCF): never describe comparing, averaging or weighting the team's models in report text (2026-10-19)
- A DCF table or sheet must show the last actual year (FY2025A) next to the forecast, with reported figures and any pro forma line marked (2026-10-19)
- Tag a line [sourced] only when it is read from a filing; anything derived from statement lines is [calc], and growth rates are rounded, not truncated (2026-10-19)

- 2026-10-23: say "CAGR", not "TACC", with the team; and separate clearly "we project acquisitions" (never) from "the historical CAGR already contains acquired sales".
- AI asked Capital IQ (block S1) for Bimbo regional sales FY2018-FY2020 that were already in data/capitaliq/segments.csv and filings/; check local files before writing any data-request prompt (2026-10-24)
- S1 and S2 asked Capital IQ for data already in filings/quarterly (1T18-3T26) and filings/annual; and S2 asked for an organic split the team already knew Bimbo refuses to give. Before any data prompt: list filings/ and data/, and ask the team what is known not to exist (2026-10-24)
- Computed data goes in Excel with live formulas linked to the source cells, never as pasted values or a CSV with a "calc" label; the team must see where every number came from (2026-10-24)
- A historical ratio (yearly or compound) is evidence, not the forward ratio: applying it mechanically carries the past forward, the same flaw as a sales CAGR; the team sets the ratio with history, recent quarters and its thesis (2026-10-25)
- 2026-10-25: Do not extend a team rule to a new year without asking. "No new borrowing" was Jorge's rule for 4Q26 only (repay the US$87m maturity, 2026-10-23); the AI carried it into FY2027E on its own and logged it as a team decision.
