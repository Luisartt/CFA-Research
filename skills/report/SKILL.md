---
name: report
description: Co-write the CFA Research Challenge written report - the seven graded sections (investment summary, business description, industry and competitive positioning, financial analysis, valuation, investment risks, ESG) in English within the 10-page A4 budget, the first-page header, charts, appendix and AI-use disclosure - and assemble the report body as a Word file to put behind the official CFA Institute cover. Drafts from the team's research and model files with Harvard citations and checks page budget and uncited numbers; the team has the final say on every claim, the rating and the target. Use whenever a student asks to write, draft, edit, shorten or build the report or any section of it, or asks about page limits, citations or the AI disclosure - even if they don't say report.
---

# report

## Purpose

Turn the team's work into the graded document. Drafting, structure, charts,
citations and assembly are the assistant's job; the story, the rating, the
target and every claim belong to the team.

## Reads

- `company-profile.yaml`; `research/thesis.md`, `industry.md`, `risks.md`,
  `esg.md`; `data/adjustments.md`; `model/review.md`, `model/model-summary.json`;
  `valuation/valuation.md`, `valuation/valuation.yaml`; `docs/context/ai-use-log.md`
  and `memory.md` (team decisions). Any missing input: draft that section as a
  placeholder tagged `[assumption]`, name the skill that produces the input, add a
  `todo.md` item — never block.
- `report/sections/*.md`, `report/header.yaml` — if present, revise them.
- `references/challenge-structure.md`, `section-guide.md`, `style-guide.md`,
  `header-template.yaml`, `ai-disclosure-template.md`.

## Steps

1. **Inventory**: a table of the seven sections, the input each needs, and
   whether it exists. Say which sections can be written now.
2. **Header**: write `report/header.yaml` from the template. Recommendation and
   target price only from the team's decision (valuation.md / memory.md); if not
   decided, leave them empty and run that coach moment first.
3. **Charts**: find Python as in init-skills (3.10 or newer) and run
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/report/tools/charts.py" --project .`
   (if `${CLAUDE_PLUGIN_ROOT}` does not resolve, use the absolute path of the
   installed plugin's `skills/report/tools/`, in quotes; missing packages: give the
   init-skills install command). The football field shows a target line only
   after the team's `target_price` is in `valuation/valuation.yaml` and the model
   is rebuilt.
4. **Draft sections** in `report/sections/` with the file names in
   `references/challenge-structure.md`, in this order: financial analysis,
   valuation, risks, ESG, industry, business description, then the investment
   summary last. Follow `section-guide.md` and `style-guide.md`: English, the
   team's ideas only (never a claim they did not make), every number cited.
5. **Check**: `<python> "${CLAUDE_PLUGIN_ROOT}/skills/report/tools/build_docx.py" --project . --check`.
   Fix uncited numbers; bring over-budget sections to the team (Coach moments).
6. **Appendix**: `98-appendix.md` (statements, DCF and WACC, comps, sensitivity
   figure, full risk table, ESG data, Harvard reference list) and
   `99-appendix-ai-use.md` from `references/ai-disclosure-template.md`, filled from
   `ai-use-log.md`; the team reviews and edits the reflection.
7. **Build**: `<python> "${CLAUDE_PLUGIN_ROOT}/skills/report/tools/build_docx.py" --project .`
   Then tell the team: put the official CFA cover in front, check the layout and
   the 10-page count in Word, and export to PDF.
8. **Close** with: file name, estimated pages, open items, next step (pitch).

## Coach moments

For each: your recommendation and why, the strongest case against it, and one
question the student must answer. Append the answer to `thesis-journal.md`.

- **Investment summary in three sentences**: thesis, valuation, catalyst — the
  team writes the first version; you tighten it.
- **Rating and target wording**: consistent with the valuation, the team's
  recommendation convention and the thesis kill criteria.
- **What to cut** when a section is over budget — propose the cut, the team chooses.

## Writes

- `report/header.yaml`, `report/sections/NN-*.md`, `report/charts/*.png`,
  `report/<TICKER>_report_v<N>.docx` (never overwritten)
- Appends coach-moment answers to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — report — <decision point>` + question, answer, what changed.

## Log

- `docs/context/ai-use-log.md`, one line per section drafted or edited:
  `YYYY-MM-DD | <member> | report | report/sections/<file> | drafted from <inputs>; team edited <what>`
- `docs/context/todo.md`: placeholders, uncited numbers, missing inputs.
