# research-challenge

Claude Code skills for university teams competing in the **CFA Institute
Research Challenge** (LatAm). The assistant acts as a senior sell-side analyst
specialized in your company's sector and country: it does the technical work
and coaches you on the decisions that are yours — the story, the thesis, the
recommendation.

## Install

In Claude Code:

```
/plugin marketplace add Luisartt/CFA-Research
/plugin install research-challenge@cfa-research
```

Then open your team's project folder and run once:

```
/research-challenge:init-skills
```

It interviews you (company, exchange, sector, accounting framework, report
language, roles, deadlines) and writes `AGENTS.md`, `CLAUDE.md`,
`company-profile.yaml`, the memory files in `docs/context/`, and the folders
`filings/ data/ research/ model/ valuation/ report/ pitch/`.

**Requirements:** Claude Code. The model skills need Python 3 with `openpyxl`
and `pyyaml`; `init-skills` checks and tells you the exact install command.

## Skills (v0.2)

| Skill | What it does | You decide |
|---|---|---|
| `/research-challenge:init-skills` | Sets up the project and the specialist persona | Interview answers |
| `thesis` | Stress-tests your investment story, then co-writes it | The pillars, your edge vs consensus, what would change your mind |
| `industry` | Market, five forces, competitors, moat, SWOT, peers | Where the company really competes, what protects it, the peer set |
| `financials` | Extracts the last 3-5 years from your filings, maps them and explains every adjustment | Nothing — but read `data/adjustments.md` before Q&A |
| `forecast` | Sets every driver from history; proposes the story drivers | The 3-5 assumptions that carry your thesis |
| `model` | Builds the Excel model (3 statements, schedules, ratios, checks, valuation) and explains it | Whether the model looks like the business |
| `valuation` | WACC, DCF, comps, sensitivity, football field | WACC calls, terminal value, target price, recommendation |
| `/research-challenge:wrap-up` | Updates the memory files at the end of a session | — |

Just ask in plain words ("roast our thesis", "analyze the industry") — the
right skill triggers (except `init-skills`, which you run by name). Every
skill works on its own, so team members can split roles.

Coming next: `risks-esg`, `report`, `pitch`.

Typical order: `init-skills` -> `thesis` + `industry` -> `financials` -> `forecast`
-> `model` -> `valuation`. Each skill also works on its own.

## Working as a team

- Share the project folder through git. The append-only logs (`ai-use-log`,
  `thesis-journal`, `session-log`) merge automatically thanks to the
  `.gitattributes` that `init-skills` installs; `todo.md` and `memory.md` may
  need a quick manual merge.
- Run `/research-challenge:wrap-up` before you stop working.
- Drop filings (annual and quarterly reports) into `filings/`.

## AI-use disclosure

Every time the assistant drafts, edits, computes or extracts something, it logs
one line in `docs/context/ai-use-log.md`. The report skill will turn it into
your disclosure appendix. Check your competition's current rules on AI use.

## Development

```
python -m pip install "openpyxl>=3.1" "pyyaml>=6" "pytest>=8" "mypy>=1.10" "hypothesis>=6" "formulas>=1.2"
python -m pytest -q
python -m mypy tests skills/model/engine
```

Test locally without publishing: `/plugin marketplace add <path-to-this-repo>`.

## Credits

See `NOTICE`. MIT licensed.
