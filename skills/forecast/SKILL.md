---
name: forecast
description: Turn a CFA Research Challenge team's investment thesis into forecast drivers for the financial model - revenue growth or segment growth, margins, working-capital days, capex, leases, tax, payout - written to model/drivers.yaml with a rationale, tag and thesis pillar for every driver. Sets the mechanical drivers from history and coaches the team on the 3-5 assumptions that carry the story (what must be true, how far from history and guidance). Use whenever a student asks to forecast, project, "set the assumptions", "what growth should we use", build revenue by segment, or asks whether a margin or growth assumption is reasonable - even if they don't say drivers.
---

# forecast

## Purpose

Connect the story to the numbers. Mechanical assumptions are the assistant's
job; the 3-5 assumptions that carry the thesis belong to the team, and each one
must be defensible against history, guidance and the industry.

## Reads

- `data/financials.csv` — required. Missing: stop and suggest the financials skill.
- `data/adjustments.md` — one-off items to exclude from baselines.
- `research/thesis.md` — pillars. Missing: continue, leave `pillar` empty, add a
  `todo.md` item "link the forecast to the thesis".
- `research/industry.md` — market growth, share, pricing. Optional.
- `filings/` — management guidance (MD&A, earnings-call transcripts).
- `model/drivers.yaml` — if present, revise it instead of starting over.
- `references/drivers-guide.md`, `references/drivers-template.yaml`.

## Steps

1. **Baseline.** Find Python 3.10 or newer as in init-skills (`python3`,
   `python`, then `py` on Windows; confirm with
   `<python> -c "import sys; assert sys.version_info >= (3, 10)"` — macOS's
   built-in python3 may be 3.9, install from python.org); if Python, openpyxl or
   pyyaml is missing, give the install command from init-skills and stop. Run the
   engine once from the project folder to get historical driver values:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/model/engine/build_model.py" --project .`
   (if `${CLAUDE_PLUGIN_ROOT}` does not resolve in the shell, locate
   `skills/model/engine/build_model.py` in the installed plugin folder and use its
   absolute path, in quotes; exit 3 = model definition error: report it as a
   plugin bug; never edit the engine). Read the `drivers` section of `model/model-summary.json`. If there is no
   `drivers.yaml` yet, this first workbook is the "engine-default baseline"; say so.
2. **Clean baselines.** For each driver compute the 3-5 year average and trend,
   excluding the one-off years listed in `adjustments.md`.
3. **Map pillars to drivers.** For each thesis pillar name the driver(s) that
   show it in numbers. Decide growth vs segments: use segments when
   `financials.csv` has `seg_` rows and a pillar is segment-specific.
4. **Draft every driver** per `references/drivers-guide.md`: mechanical drivers
   from recent history (say which years in `rationale`); story drivers as a
   *proposal* only. Tag `guidance` when management gave the number and cite it.
5. **Coach the story drivers** (see Coach moments) and write the team's choices.
6. **Sanity pass** with the guide's rules; flag any breach in one line each.
7. **Write `model/drivers.yaml`** from the template (all keys, `forecast_years`,
   `revenue_segments` if used) and run the engine again (same command). Read
   `status` in `model-summary.json`; fix input errors; explain any `WARN` in one
   plain sentence each.
8. **Close** with: the story drivers (history -> forecast), status, and the next
   step ("next: the model skill to review the build, or valuation").

## Coach moments

For each: your recommendation and why, the strongest case against it, and one
question the student must answer. Append the answer to `thesis-journal.md`.

- **Which 3-5 drivers carry the story:** tie each to a pillar; drop drivers that
  no pillar needs from the discussion.
- **Each story driver's value:** show history, your proposal, guidance or
  consensus if known, and "what must be true" for the team's number.
- **Revenue vs the industry:** growth implies a market-share path — make the
  team say it out loud.

## Writes

- `model/drivers.yaml`; a new model version in `model/` (the engine never overwrites).
- Appends coach-moment answers to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — forecast — <decision point>` + question, answer, what changed.

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | forecast | model/drivers.yaml | set mechanical drivers from history; team chose <story drivers>`
- `docs/context/memory.md`: `# decision: <driver> = <values> because <pillar/reason>` per story driver.
- `docs/context/todo.md`: evidence still needed for any story driver.
