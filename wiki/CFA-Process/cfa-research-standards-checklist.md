---
Writer: AI-compiled (Claude)
Source:
  - AGENTS.md
  - company-profile.yaml
tags: [CFA-Process, standards]
---

# CFA research standards checklist (team workflow)

Working standards for the BIMBOA team, drawn ==only from project files== (`AGENTS.md`, `company-profile.yaml`). It contains no external CFA Institute rubric weights, scores or section limits, because none are in the project files. If the team wants rubric points, add the official rules to `raw/` first. Related: [[cfa-challenge-timeline]], [[bimbo-filings-source-map]].

## 1. Project set-up facts

| Item | Value | Source |
|---|---|---|
| Company | Grupo Bimbo, S.A.B. de C.V. (BIMBOA, BMV) | `[sourced]` company-profile.yaml |
| Sector | Consumer Staples - Packaged Food & Bakery; non-financial issuer | `[sourced]` company-profile.yaml |
| Accounting | IFRS, MXN, millions, FYE 12-31 (framework confirmed by team) | `[sourced]` company-profile.yaml |
| Report language | English always (CFA Institute Official Rules 2.6c, as cited in the profile) | `[sourced]` company-profile.yaml |
| Presentation language | English (local round setting "en"; English from sub-regional up) | `[sourced]` company-profile.yaml; AGENTS.md |
| Report deadline | ==2026-11-04== | `[sourced]` company-profile.yaml |
| Presentation date | ==2026-12-08== | `[sourced]` company-profile.yaml |
| Public information only | Confirmed by team | `[sourced]` company-profile.yaml |

## 2. Roles

Team per `company-profile.yaml` `[sourced]`:

| Member | Role in profile |
|---|---|
| Luis Arturo Romo Alba | captain (all) |
| Diego Benavides Pro | not assigned yet |
| Alexa Garcia Saldivar | not assigned yet |
| Jorge Alejandro Gaytan | not assigned yet |
| Carolina del Rosario Benites | not assigned yet |

> [!question] Four of five members have no assigned role. Assigning owners (for example model, valuation, industry, risks/ESG) would help the team defend its sections in Q&A, but the team decides, not the assistant.

### Who decides what `[sourced]` AGENTS.md "Who decides what"

| The assistant does | The team decides |
|---|---|
| Filing ingestion, statement extraction, accounting adjustments | The investment thesis and its 2-3 pillars |
| Model construction, checks, valuation mechanics | How their view differs from consensus |
| Industry structure, peer data, risk matrix mechanics | The 3-5 assumptions that carry the story |
| Drafting and polishing prose from the team's ideas | Target price and recommendation |
| Explaining technical choices in plain words | Which risks matter and why |

- Technical work: do it, then explain it so the team can defend it in Q&A. Story decisions: recommend, argue the other side, ask. `[sourced]` AGENTS.md.
- Wiki articles carry no investment opinion, thesis or target price; the team's own thesis lives in `notes/` and `research/thesis.md` `[sourced]` WIKI.md.

## 3. Data-tag standard (every number)

| Tag | Meaning | Required support |
|---|---|---|
| `[sourced]` | From a filing or public source | Document and page/URL |
| `[guidance]` | Management said it (call, presentation, release) | Cite which one |
| `[assumption]` | Team judgment | One-line rationale |
| `[calc]` | Computed from other tagged numbers | Show inputs |
| `[unverified]` | Not yet tied to a source | ==Must be resolved before the report== |

Checklist:
- [ ] Each number in research files, the model and the report has exactly one tag `[sourced]` AGENTS.md.
- [ ] No invented numbers; unknowns are stated and a way to find them is proposed `[sourced]` AGENTS.md.
- [ ] Zero `[unverified]` tags left in the report before the 2026-11-04 deadline `[sourced]` AGENTS.md; company-profile.yaml.
- [ ] Time-bound figures carry their as-of date `[sourced]` WIKI.md.
- [ ] Restated periods: keep latest figure, note the earlier one `[sourced]` WIKI.md.

## 4. Public information only

- Use public information only (CFA Standard II(A), as cited in AGENTS.md) `[sourced]` AGENTS.md.
- If a member mentions material non-public information: ==stop and flag it== `[sourced]` AGENTS.md.
- Independence and objectivity: the recommendation follows the evidence, not management's charm or the team's hopes `[sourced]` AGENTS.md.
- Cite sources; distinguish fact from opinion `[sourced]` AGENTS.md.
- Checklist: [ ] every source in the report is public; [ ] each claim cites a document and page.

## 5. Language and file rules

- Write every file under `research/`, `report/` and `model/` in English `[sourced]` AGENTS.md.
- Files under `pitch/` use the presentation language (English per profile) `[sourced]` AGENTS.md; company-profile.yaml.
- Coaching language follows the student's language (Spanish or English) `[sourced]` AGENTS.md.
- Source filings are in Spanish; translate terms consistently and keep Spanish original in the citation. See [[bimbo-filings-source-map]].

## 6. Deliverable map `[sourced]` AGENTS.md "Skills"

| Deliverable | File(s) |
|---|---|
| Thesis | `research/thesis.md` |
| Industry | `research/industry.md` |
| Financials | `data/financials.csv`, `data/adjustments.md` |
| Drivers | `model/drivers.yaml` (team picks the 3-5 that carry the story) |
| Model | `model/<TICKER>_model_v<N>.xlsx`, `model/review.md` |
| Valuation | `valuation/valuation.yaml`, `valuation/valuation.md` |
| Risks and ESG | `research/risks.md`, `research/esg.md` |
| Report | `report/sections/` (seven sections), `report/<TICKER>_report_v<N>.docx` |
| Pitch | `pitch/outline.yaml`, `pitch/qa-drill.md` (10-minute outline per AGENTS.md) |
| Deck | `pitch/<TICKER>_deck_v<N>.pptx`, `pitch/deck-audit.md` |
| Session close | `docs/context/*` via `/research-challenge:wrap-up` |

- Missing inputs become `[assumption]` placeholders plus a `todo.md` item, never a blocker `[sourced]` AGENTS.md.
- The report is co-written in seven sections `[sourced]` AGENTS.md (the section titles are not listed in the project files; `[unverified]` until the official template is added).

## 7. Coaching rules the team can expect `[sourced]` AGENTS.md

1. The assistant restates the student's idea before challenging it.
2. At most 2-3 questions per turn, none compound.
3. Story weaknesses are flagged, never silently rewritten.
4. Each decision point gets: recommendation, strongest counter-case, one question to answer.
5. Each turn ends with exactly one next step.
6. Solid work is called solid; no false red flags.
7. Technical work comes with a plain-words explanation.

## 8. Logging and traceability

- AI-use log: after any work that ends up in the report, model or pitch, append `YYYY-MM-DD | member | skill | section or file | what the AI did` to `docs/context/ai-use-log.md`; never skip, never condense `[sourced]` AGENTS.md.
- `member` is the student working the session; if unknown, ask once, else write `team` `[sourced]` AGENTS.md.
- Wiki compile also logs to the AI-use log `[sourced]` WIKI.md.
- Context files are read on demand; locked decisions go to `docs/context/memory.md`, corrections to `lessons.md`, open work to `todo.md` `[sourced]` AGENTS.md.
- Grep `lessons.md` before fixing a repeat problem `[sourced]` AGENTS.md.
- Run `/research-challenge:wrap-up` at the end of every work session `[sourced]` CLAUDE.md.

## 9. Pre-submission checklist (derived from the rules above `[calc]`)

- [ ] Report in English; deck and pitch in English
- [ ] Every number tagged; no `[unverified]` left
- [ ] Thesis, pillars, key assumptions, target price and recommendation set by the team, not the assistant
- [ ] Sources public and cited with page numbers
- [ ] AI-use log complete for every contributed section
- [ ] Report submitted by 2026-11-04; presentation ready for 2026-12-08
- [ ] Each member can defend the technical choices in their area in Q&A

## Key Takeaways
- All standards here come from `AGENTS.md` and `company-profile.yaml`; no external CFA rubric numbers are included.
- Every number needs one of five tags; `[unverified]` must be cleared before the 2026-11-04 report deadline.
- Public information only; non-public information triggers a stop-and-flag.
- English is mandatory for report and files under `research/`, `report/`, `model/`; `pitch/` also English per profile.
- The team owns thesis, differentiation, key assumptions, target price and risk priorities; the assistant owns technical work.
- Four of five members have no role assigned yet.
