---
name: deck
description: Build the CFA Research Challenge pitch deck from pitch/outline.yaml by one of two routes the team picks - a PowerPoint file on the team's own .pptx template (layouts chosen from the template, charts from the report, a Sources line on every slide, speaker notes in the notes field), or a Claude Design deck (Claude's Slides and Design System features) styled with the team's design system, co-edited in claude.ai and downloaded as .pptx or PDF - and audit any deck (slide count for 10 minutes, sources, notes, leftover placeholders, fonts, overflow, numbers that no longer match the model), fixing mechanical problems and flagging the rest. The team owns the design and final polish. Use whenever a student asks to make, build, design, generate, format, clean up, check or audit the slides, the deck or the PowerPoint - even if they don't say deck.
---

# deck

## Purpose

Save the team hours of slide work and catch rule breaks before judges do.
Building and checking are the assistant's job; the design (their template or
design system) and the final visual polish belong to the team.

## Reads

- `pitch/outline.yaml` — required to build. Missing: suggest the pitch skill (an
  audit of an existing deck still works without it).
- `pitch/template.pptx` — the team's template (PowerPoint route). Missing: build
  on a plain default and recommend adding their template, then rebuild.
- `report/charts/*.png` — missing charts: run the report skill's `charts.py`.
- `model/model-summary.json`, `report/header.yaml` — for the stale-number check.
- `references/deck-design.md`; `references/claude-design-route.md` (Claude Design route).

## Steps

Find Python as in init-skills (3.10 or newer; python-pptx missing -> the
init-skills install command). Tools live in `${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/`
(if `${CLAUDE_PLUGIN_ROOT}` does not resolve, use the installed plugin's absolute
path, in quotes).

0. **Pick the route** (Coach moments). The Claude Design route exists only when
   this session has Claude's Artifact tool with the Slides type (see
   `references/claude-design-route.md` for the check); otherwise say so and use
   PowerPoint. A university that requires its own .pptx template means PowerPoint.

**PowerPoint route**

1. **Inspect the template**:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/build_pptx.py" --project . --list-layouts`
   Tell the team which layouts will be used and anything missing.
2. **Build**:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/build_pptx.py" --project .`
   Exit 2: fix the outline (sources, charts) and rerun. Exit 4: close the file in
   PowerPoint.

**Claude Design route**

1. **Design system**: follow `references/claude-design-route.md` — use the team's
   design system, or create one from their template or brand if they want one.
2. **Build the Slides deck** from `pitch/outline.yaml` exactly as that reference
   says (one slide per entry, charts uploaded, a source line on every slide but the
   title, notes in the notes). Give the team the link; they present or co-edit there.
3. **Download**: the team downloads the deck as .pptx into `pitch/` (or PDF for
   presenting); audit the .pptx with `--deck` below.

**Both routes**

3. **Audit**:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/audit_pptx.py" --project .`
   (Claude Design route or a hand-made deck: add `--deck "<file>"`.) Add `--fix`
   for mechanical fixes (new version). Fix content findings (dense slides, stale
   numbers, missing sources) in `pitch/outline.yaml` and rebuild — never change a
   number only in the deck.
4. **Visual check** per `references/deck-design.md` (PowerPoint export or
   LibreOffice render; otherwise list the slides for the team to check).
5. **Close**: route, file or link, slide count, errors and warnings left, and the checkpoint.

## Coach moments

No story decisions. Two design calls belong to the team:

- **Route**: PowerPoint (their .pptx template, offline, what most judges' rooms
  expect) or Claude Design (design system, co-editing in claude.ai, download
  later). Give your recommendation for their situation and the case against it.
- **Review checkpoint**: the team opens the deck and confirms the layout and
  design are theirs to present; wording changes go back into
  `pitch/outline.yaml` so the next build keeps them.

Polish last. Every build starts again from the template or outline, so finish the
content in `pitch/outline.yaml` first. After the team polishes the deck by hand,
check it with `audit_pptx.py --deck "<file>"` instead of rebuilding. If a number
changes late, change it in the model, the outline and the polished deck, then
rerun the audit.

## Writes

- PowerPoint route: `pitch/<TICKER>_deck_v<N>.pptx` (never overwritten)
- Claude Design route: a private Slides deck (link) and, when the team downloads
  it, a `.pptx` in `pitch/`; a team design system if they asked for one
- `pitch/deck-audit.md`

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | deck | pitch/<file or deck link> | built deck (<route>) from outline; audit <n> errors, <m> warnings`
- `docs/context/memory.md`: `# decision: deck route = <PowerPoint | Claude Design>`
- `docs/context/todo.md`: remaining audit findings and slides to check visually.
