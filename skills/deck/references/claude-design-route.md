# Claude Design route (Slides + Design System)

Claude's design features make a 16:9 deck in claude.ai that the team can
present from, co-edit (comments, live editing) and download as .pptx or PDF,
styled by a design system (the team's colors, typefaces and components).
Everything here is private to the team until they share it.

## 1. Is it available in this session?

It needs Claude's **Artifact tool** with the **Slides** type. Check with the
Artifact tool's `quickstart` action, intent `slides`. If the tool is not there,
the Slides type is not listed, or the call is refused: say "the Claude Design
route isn't available in this Claude session" and use the PowerPoint route.
Never try to recreate it another way.

## 2. Design system (the team's decision)

- List the design systems the team can open (Artifact `list`, type "Design System").
  One marked default: use it. Several: name them and let the team pick. None:
  ask whether they want one.
- To create one from their brand: start from the Design System type (Artifact
  `quickstart`, intent `other`) and fill it from what the team gives you — the
  colors and fonts of `pitch/template.pptx` (read its theme with python-pptx),
  the university's brand page, or a logo they upload. Ask before inventing a look.
- No design system wanted: a clean, restrained look; say which typefaces and colors you chose.

## 3. Build the deck from `pitch/outline.yaml`

Create a deck from the Slides type (quickstart gives its link; title = the
outline's `deck.title`) and follow that type's own instructions for the file
format. Map the outline without adding content:

| Outline | Slide |
|---|---|
| `kind: title` | Cover: `title`, `subtitle` (rating, target, upside) |
| `kind: section` | Section divider with `title` |
| `kind: content` | `title` as the heading (it is the message); `bullets` as one list, or as cards/big numbers when that reads better; `chart` beside or below |
| `kind: chart` | `title` + the chart, large |
| `sources` | A pinned source row at the bottom of every slide but the cover: "Source:" (en), "Fuente:" (es), "Fonte:" (pt) from `deck.language` — Challenge rule |
| `notes`, `speaker`, `minutes` | Speaker notes: `[speaker - minutes min] notes` |

- Charts: upload each `report/charts/<chart>.png` as an asset of the deck and use
  the returned link; never re-draw a chart or type its numbers by hand.
- Every number on a slide comes from the outline or the charts. Never invent a
  statistic, quote or logo.
- One idea per slide, at most 6 bullets; keep the title within about 60 characters.
- Give the team the link. Do not re-render or screenshot to check unless they ask.

## 4. Changes, download and audit

- Content changes go into `pitch/outline.yaml` first, then into the deck, so
  both stay the same. The team's visual edits in claude.ai are theirs; rebuild
  from the outline only if they agree to lose them.
- For judging, the team downloads the deck as .pptx into `pitch/` (or PDF to
  present). Audit that file:
  `<python> "${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/audit_pptx.py" --project . --deck "pitch/<file>.pptx"`
- Presenting: check with the local host whether they present from their own
  laptop, a PDF or PowerPoint; bring the downloaded file either way.
