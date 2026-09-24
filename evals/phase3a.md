# Phase 3a manual evals

Project with a built model and valuation (phase 2 evals done).

## init-skills

1. New folder, `/research-challenge:init-skills`
   - [ ] Does not ask for a report language; asks the presentation language.
   - [ ] `company-profile.yaml` has `language: "en"` and `presentation_language`.

## risks-esg

1. Prompt: "what are our key risks?"
   - [ ] Proposes specific cause -> effect -> driver -> value risks tied to pillars.
   - [ ] Asks the team to pick 4-6 and to say mitigated / priced in.
   - [ ] Writes `research/risks.yaml` and draws `report/charts/risk-matrix.png`.
2. Prompt: "do the ESG section"
   - [ ] Picks 3-5 industry-material issues, runs the governance checklist, links to value.

## report

1. Prompt: "draft the report"
   - [ ] Shows the section inventory first; placeholders for missing inputs.
   - [ ] Leaves rating/target empty until the team decides.
   - [ ] Writes sections in English with Harvard citations.
   - [ ] Runs `--check`, reports pages per section, flags uncited numbers.
2. Prompt: "build the Word file"
   - [ ] Produces `report/<TICKER>_report_v<N>.docx`, A4, header block, figures with captions.
   - [ ] Tells the team to add the official CFA cover and check 10 pages in Word.
   - [ ] Appendix includes the AI-use disclosure drafted from the log.
