---
name: model
description: Build, check and explain the CFA Research Challenge team's institutional-grade financial model - three statements, schedules, ratios, integrity checks and (when valuation inputs exist) the valuation tabs - by running the plugin's model engine on data/financials.csv, model/drivers.yaml and valuation/valuation.yaml. Reads model/model-summary.json, explains the status and every failed check in plain words, fixes mechanical problems, sends story problems back to the team, and writes a short model review. Use whenever a student asks to build, rebuild, run, update or check the model, asks what a tab or check means, asks why the model is red, or wants the Excel file - even if they don't say "model".
---

# model

## Purpose

Produce the workbook and make sure the team understands it. The engine does
the arithmetic; this skill runs it, reads the result, fixes what is mechanical
and explains the rest so any member can walk a judge through the model.

## Reads

- `data/financials.csv` — required. Missing: stop and suggest the financials skill.
- `model/drivers.yaml` — optional; without it every driver is held at its last
  actual value (say so and suggest the forecast skill).
- `valuation/valuation.yaml` — optional; without it no valuation tabs.
- `model/model-summary.json` — the result of each build.
- `references/reading-the-model.md`, `references/model-summary.md`.

## Steps

1. **Build.** Find Python as in init-skills (`python3`, `python`, then `py` on
   Windows); if Python, openpyxl or pyyaml is missing, give the install command
   from init-skills and stop. From the project folder run:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/model/engine/build_model.py" --project .`
   Exit code 2: fix the listed inputs (mapping problems yourself; story drivers
   go to the team) and rerun. Exit 4: ask the team to close the file, rerun.
2. **Read** `model/model-summary.json`: `status`, every check that is not OK,
   `warnings`, and the `ratios` and `lines` sections.
3. **Resolve failed checks** with `references/reading-the-model.md`: fix
   mechanical causes directly (a mapping gap, a missing lease line), rebuild, and
   list story causes for the team with the driver involved.
4. **Review the forecast against history** (from `ratios`): revenue growth,
   EBITDA margin, ROIC, net debt / EBITDA, FCF margin. Flag any forecast year that
   breaks the historical range and name the driver responsible.
5. **Write `model/review.md`**: status, the ratio table (last 3 actual years and
   all forecast years), flags, fixes made, open questions for the team.
6. **Explain** in five lines or fewer: which file to open, status, the two most
   important things the model says, and one next step.

## Coach moments

One review checkpoint, not a decision: **"Does the model look like the business?"**
Show the three ratio trends that move most between history and forecast; ask the
team to explain the biggest change in one sentence and which pillar causes it.
If they can't, that driver goes back to the forecast skill.

## Writes

- `model/<TICKER>_model_v<N>.xlsx` and `model/model-summary.json` (via the engine)
- `model/review.md`
- Appends the checkpoint answer to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — model — does the model look like the business` + question, answer.

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | model | model/<file>, model/review.md | built model v<N>; status <status>; <n> fixes`
- `docs/context/todo.md`: one item per open story issue, with the driver named.
