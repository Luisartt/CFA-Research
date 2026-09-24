# Deck design and checks

## The team's template is the design

Put the team's template at `pitch/template.pptx`. The builder keeps its theme,
fonts, colors and layouts, removes its example slides, and picks layouts by
where their placeholders actually sit (a title near the top, a body big enough
for bullets, room for a chart), so custom and Spanish-named layouts work. Run
`--list-layouts` first: it shows each layout and which one each slide kind
will use. `.potx` templates work too.

## Rules for every slide

- Title = the message, as a sentence.
- At most 6 bullets, at most 20 words each; charts over tables.
- A "Source:" line ("Fuente:" / "Fonte:" when the deck language is es / pt) at
  the bottom (Challenge rule) — the builder adds it as a shape named `Sources`.
- Speaker notes in the notes field, never on the slide.
- Numbers come from the model and the report through the outline; never type a
  number into the deck by hand.
- The template's fonts only; body text at least 10 pt (source lines 8 pt minimum).

## What the audit checks (structural, no rendering)

Slide count for 10 minutes (6-14), sources, notes, leftover placeholder text,
shapes off the slide, small fonts, more than two font families, likely text
overflow, dense slides (over 60 words), and target price or WACC that differ
from `report/header.yaml` / `model/model-summary.json`. It also warns when a
picture overlaps the title or the source line overlaps other shapes.

`--fix` saves a new version with mechanical fixes only: empty placeholders
removed, rare stray fonts on body text reset to the theme font (never the
theme's own fonts or the fonts used on titles); no new file when nothing needs
fixing. Everything else is a finding to fix in the outline (then rebuild) or by
the team.

## Visual check

The audit cannot see the slides. If LibreOffice is installed,
`soffice --headless --convert-to pdf <deck>` renders it; look at every page for
overflow, overlaps, the source line colliding with content, and contrast.
Otherwise the team opens the deck in PowerPoint and checks the slides the audit
listed.
