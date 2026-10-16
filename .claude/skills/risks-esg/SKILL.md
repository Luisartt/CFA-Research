---
name: risks-esg
description: Investment risks and ESG analysis for a CFA Research Challenge company - specific risks tied to the thesis pillars with probability x impact and a risk-matrix chart, plus industry-based ESG materiality with a LatAm governance checklist (controlling shareholder, board independence, related parties) and the link from ESG to value. Researches filings and sustainability reports and structures everything; coaches the team on which risks and ESG issues really matter and whether they are priced in. Use whenever a student asks about risks, downside, risk matrix, what could go wrong, ESG, sustainability, governance, controlling shareholders or materiality - even if they don't say risks-esg.
---

# risks-esg

## Purpose

Risks and ESG are 30 of 100 report points. Research and structure are the
assistant's job; the team decides which risks matter, how they are mitigated or
priced, which ESG issues are material and how they affect value.

## Reads

- `research/thesis.md` — pillars and kill criteria. Missing: continue, mark every
  risk's pillar as empty, add a `todo.md` item.
- `research/industry.md`, `data/adjustments.md`, `model/model-summary.json`
  (drivers and sensitivity, to size impacts). Optional.
- `filings/` — risk factors, governance section, related-parties note,
  sustainability or integrated report. Missing sustainability report: say so and
  add a `todo.md` item to download it.
- `company-profile.yaml` — sector, country.
- `research/risks.yaml`, `research/risks.md`, `research/esg.md` — if present, update them.
- `references/risk-framework.md`, `references/risks-template.yaml`,
  `references/esg-materiality-latam.md`, `references/esg-template.md`.

## Steps

1. **Collect candidate risks** from risk factors, the industry analysis, the
   thesis kill criteria, macro (FX, rates, commodities) and regulation. Write each
   as cause -> effect -> driver -> value (`references/risk-framework.md`).
2. **Size them**: probability and impact scores 1-5; use the model's drivers and
   sensitivity grid to estimate impact on value where possible. Propose, don't decide.
3. **ESG materiality**: pick 3-5 material issues for the industry from
   `references/esg-materiality-latam.md`; gather the company's data and trend for
   each; run the governance checklist.
4. **Run the coach moments** below and record the team's choices.
5. **Write** `research/risks.yaml` (template), `research/risks.md` (key-risks
   table, mitigation, priced in, downside scenario, appendix list) and
   `research/esg.md` (template). Cite every figure.
6. **Draw the risk matrix.** Find Python as in init-skills (3.10 or newer; install
   command there if matplotlib is missing) and run from the project folder:
   `<python> "${CLAUDE_PLUGIN_ROOT}/skills/report/tools/charts.py" --project .`
   (if `${CLAUDE_PLUGIN_ROOT}` does not resolve in the shell, use the absolute
   path of `skills/report/tools/charts.py` in the installed plugin, in quotes).
7. **Downside scenario** (`references/risk-framework.md`): copy the project
   folder, change the scenario's drivers in the copy's `model/drivers.yaml`, run
   `build_model.py --project "<copy>"` (same engine call as the model skill) and
   record the value per share from the copy's `model/model-summary.json` in
   `research/risks.md`. Never edit the team's base `drivers.yaml` for a scenario.
   **Close** with the key risks, the material ESG issues, the downside value and
   one next step.

## Coach moments

For each: your recommendation and why, the strongest case against it, and one
question the student must answer. Append the answer to `thesis-journal.md`.

- **Which 4-6 risks** truly threaten the thesis — cut the generic ones.
- **Mitigated, priced in, or neither** — for each key risk.
- **Material ESG issues** — why these 3-5 affect value for this industry.
- **Governance and value** — does the ownership structure justify a discount?

## Writes

- `research/risks.yaml`, `research/risks.md`, `research/esg.md`
- `report/charts/risk-matrix.png` (and any other chart the tool can draw)
- Appends to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — risks-esg — <decision point>` + question, answer, what changed.

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | risks-esg | research/risks.md, research/esg.md | researched risks and ESG; team chose key risks and material issues`
- `docs/context/memory.md`: `# decision: key risks = <ids>; material ESG = <issues>`.
- `docs/context/todo.md`: missing sustainability data, risks to quantify.
