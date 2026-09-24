# Phase 3b manual evals

Project with the report drafted (phase 3a evals done). Put a real team
template at `pitch/template.pptx` (e.g. a university template) for eval 2.

## pitch

1. Prompt: "prepare our presentation"
   - [ ] Asks the round (or reads it) and uses the right language.
   - [ ] Asks for the lead message before drafting slides.
   - [ ] Writes `pitch/outline.yaml`: message titles, <= 6 bullets, sources on every slide but the title, speakers, ~9.5 minutes.
2. Prompt: "run a mock Q&A"
   - [ ] Asks one question at a time, scores with the five criteria, gives one improvement.
   - [ ] Includes at least one AI-use question.

## deck

1. Prompt: "build our slides" (no template)
   - [ ] Warns that no template was found, builds on the default.
2. Prompt: "build our slides" (with the team template)
   - [ ] Runs `--list-layouts` first and says which layouts it will use.
   - [ ] Deck opens in PowerPoint; every slide but the title has a Source line; notes are in the notes pane.
   - [ ] Runs the audit and reports errors/warnings; fixes content in the outline and rebuilds.
3. Prompt: "check this deck" with a hand-made .pptx
   - [ ] Audits it with `--deck`, lists findings, offers `--fix`, never overwrites the original.
