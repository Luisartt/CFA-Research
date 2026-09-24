---
name: pitch
description: Prepare the CFA Research Challenge presentation - a 10-minute slide-by-slide outline (pitch/outline.yaml) with speaker notes, timing and speaker assignments built from the team's report and model, and a judge Q&A drill of about 30 questions generated from the team's own files, run as scored mock rounds (including questions about how the team used AI). The team decides the lead message, who presents what, and answers in their own words. Use whenever a student asks about the presentation, pitch, slides outline, speaker notes, timing, rehearsal, mock Q&A or likely judge questions - even if they don't say pitch.
---

# pitch

## Purpose

Turn the report into a 10-minute talk the judges remember and prepare every
member for Q&A. Structure, notes, timing and questions are the assistant's job;
the lead message, the speakers and the answers belong to the team.

## Reads

- `report/sections/*.md` and `report/header.yaml` (preferred source); if missing,
  `research/thesis.md`, `valuation/valuation.md`, `model/model-summary.json`,
  `research/risks.md`, `research/esg.md`, `data/adjustments.md` — say which
  inputs are missing and continue with placeholders tagged `[assumption]`.
- `report/charts/*.png` — the charts slides can use.
- `company-profile.yaml` — `presentation_language`; `docs/context/ai-use-log.md`
  for the AI-use questions; `docs/context/memory.md` for team decisions.
- `pitch/outline.yaml`, `pitch/qa-drill.md` — if present, revise them.
- `references/pitch-structure.md`, `references/outline-template.yaml`,
  `references/qa-bank.md`.

## Steps

1. **Round and language**: ask which round this is for (local final, recorded
   sub-regional, regional, global) unless `todo.md` or `memory.md` says; take
   the language from the table in `pitch-structure.md` (local: the profile's
   `presentation_language`).
2. **Lead message** (Coach moments) before any slide.
3. **Draft `pitch/outline.yaml`** from the template and the suggested flow: each
   slide's title = the message in at most about 10 words / 60 characters; at
   most 6 bullets of at most 20 words; a chart from `report/charts/` where one
   exists; `sources` on every slide but the title (Challenge rule); notes written as spoken sentences in the presentation
   language; speaker and minutes per slide, total about 9.5.
4. **Speakers and cuts** (Coach moments), then update the outline.
5. **Q&A drill**: write `pitch/qa-drill.md` with about 30 questions from
   `references/qa-bank.md`, each with a pointer to the file and number that
   answers it (not a scripted answer). For the recorded sub-regional round there
   is no Q&A; keep the drill for the regional semifinal.
6. **Mock rounds** when asked: one question at a time, the student answers,
   score with the bank's five criteria, give one improvement, re-ask weak ones
   later. Include AI-use questions every round.
7. **Close**: slide count, planned minutes, weakest Q&A area, next step
   ("next: the deck skill builds the slides from this outline").

## Coach moments

For each: your recommendation and why, the strongest case against it, and one
question the student must answer. Append the answer to `thesis-journal.md`.

- **Lead message**: the one sentence the judges should remember.
- **Who presents what**: every member speaks (team involvement is scored).
- **What to cut** to fit 10 minutes.

## Writes

- `pitch/outline.yaml`, `pitch/qa-drill.md`
- Appends to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — pitch — <decision point>` + question, answer, what changed.

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | pitch | pitch/outline.yaml, pitch/qa-drill.md | drafted outline, notes and Q&A drill; team chose message and speakers`
- `docs/context/todo.md`: rehearsal dates, weak Q&A areas.
