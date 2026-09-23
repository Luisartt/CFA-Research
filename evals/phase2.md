# Phase 2 manual evals

Run in a project set up with init-skills, with 3-5 annual reports of a real
BMV-listed company in `filings/`. Mark each expected behavior pass/fail.

## financials

1. Prompt: "pull the last five years of financials"
   - [ ] Lists the documents and years before extracting.
   - [ ] Writes `data/financials.csv` with a page for every sourced figure.
   - [ ] Runs the engine with `--check` and fixes input errors until `[ok]`.
   - [ ] Writes `data/adjustments.md` with three judge questions and answers.
2. Prompt (with `filings/` empty): "load the numbers"
   - [ ] Stops and lists which documents to download and where.

## forecast

1. Prompt: "set up the forecast"
   - [ ] Builds a baseline and reads historical drivers from `model-summary.json`.
   - [ ] Sets mechanical drivers itself with a rationale citing the years used.
   - [ ] Proposes the story drivers but asks the team to decide each one.
   - [ ] Writes `model/drivers.yaml` with tag, rationale and pillar for every driver.
2. Prompt: "is 12% growth reasonable?"
   - [ ] Compares with history, industry growth and guidance; asks what must be true.

## model

1. Prompt: "build the model"
   - [ ] Runs the engine, reports the file name and status.
   - [ ] Explains every failed check in plain words and names the fix.
   - [ ] Writes `model/review.md` with the ratio table and flags.
   - [ ] Asks whether the model looks like the business.
2. Prompt: "why is the model red?"
   - [ ] Reads the checks in `model-summary.json`, not the workbook.

## valuation

1. Prompt: "what's our WACC?"
   - [ ] Explains the currency route and proposes each input with a source and date.
   - [ ] Leaves the judgment calls (beta source, target D/E) to the team.
2. Prompt: "what's our target price?"
   - [ ] Shows DCF, comps and the football field; does not pick the target.
   - [ ] Writes the team's target into `valuation.yaml` and rebuilds.
   - [ ] Writes `valuation/valuation.md` with sources and the recommendation convention.
