---
name: deck
description: Build the CFA Research Challenge pitch deck as a PowerPoint file from pitch/outline.yaml on the team's own template - layouts chosen from the template, charts from the report, a Sources line on every slide (Challenge rule) and speaker notes in the notes field - and audit any deck (slide count for 10 minutes, sources, notes, leftover placeholders, fonts, overflow, numbers that no longer match the model), fixing mechanical problems and flagging the rest. The team owns the design and final polish. Use whenever a student asks to make, build, generate, format, clean up, check or audit the slides, the deck or the PowerPoint - even if they don't say deck.
---

# deck

## Purpose

Save the team hours of slide formatting and catch rule breaks before judges
do. Building and checking are the assistant's job; the design (their template)
and the final visual polish belong to the team.

## Reads

- `pitch/outline.yaml` — required to build. Missing: suggest the pitch skill (an
  audit of an existing deck still works without it).
- `pitch/template.pptx` — the team's template. Missing: build on a plain default
  and recommend adding their template, then rebuild.
- `report/charts/*.png` — missing charts: run the report skill's `charts.py`.
- `model/model-summary.json`, `report/header.yaml` — for the stale-number check.
- `references/deck-design.md`.

## Steps

Find Python as in init-skills (3.10 or newer; python-pptx missing -> the
init-skills install command). Tools live in `${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/`
(if `${CLAUDE_PLUGIN_ROOT}` does not resolve, use the installed plugin's absolute
path, in quotes).

1. **Inspect the template**:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/build_pptx.py" --project . --list-layouts`
   Tell the team which layouts will be used and anything missing.
2. **Build**:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/build_pptx.py" --project .`
   Exit 2: fix the outline (sources, charts) and rerun. Exit 4: close the file in
   PowerPoint.
3. **Audit**:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/audit_pptx.py" --project .`
   Add `--fix` for mechanical fixes (new version). Fix content findings (dense
   slides, stale numbers, missing sources) in `pitch/outline.yaml` and rebuild —
   never edit numbers inside the deck.
4. **Existing deck**: to check a deck the team made by hand, run the audit with
   `--deck "<file>"` (and `--fix` if they agree).
5. **Visual check** per `references/deck-design.md` (LibreOffice render if
   available; otherwise list the slides for the team to check in PowerPoint).
6. **Close**: file name, slide count, errors and warnings left, and the checkpoint.

## Coach moments

No story decisions. One review checkpoint: the team opens the deck in
PowerPoint and confirms the layout and design are theirs to present; their
changes to wording go back into `pitch/outline.yaml` so the next build keeps them.

## Writes

- `pitch/<TICKER>_deck_v<N>.pptx` (never overwritten), `pitch/deck-audit.md`

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | deck | pitch/<file> | built deck from outline on team template; audit <n> errors, <m> warnings`
- `docs/context/todo.md`: remaining audit findings and slides to check visually.
