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

**Requirements:** Claude Code. Python 3 with `openpyxl` will be needed by the
model skills in the next release; `init-skills` checks and tells you how to install it.

## Skills (v0.1)

| Skill | What it does | You decide |
|---|---|---|
| `init-skills` | Sets up the project and the specialist persona | Interview answers |
| `thesis` | Stress-tests your investment story, then co-writes it | The pillars, your edge vs consensus, what would change your mind |
| `industry` | Market, five forces, competitors, moat, SWOT, peers | Where the company really competes, what protects it, the peer set |
| `/research-challenge:wrap-up` | Updates the memory files at the end of a session | — |

Just ask in plain words ("roast our thesis", "analyze the industry") — the
right skill triggers. Every skill works on its own, so team members can split
roles.

Coming next: `financials`, `forecast`, `model`, `valuation` (institutional-grade
Excel model), then `risks-esg`, `report`, `pitch`.

## Working as a team

- Share the project folder through git. Shared memory files are append-only,
  so parallel work merges cleanly.
- Run `/research-challenge:wrap-up` before you stop working.
- Drop filings (annual and quarterly reports) into `filings/`.

## AI-use disclosure

Every time the assistant drafts, edits, computes or extracts something, it logs
one line in `docs/context/ai-use-log.md`. The report skill will turn it into
your disclosure appendix. Check your competition's current rules on AI use.

## Development

```
python -m pip install -e ".[dev]"
python -m pytest -q
python -m mypy tests
```

Test locally without publishing: `/plugin marketplace add <path-to-this-repo>`.

## Credits

See `NOTICE`. MIT licensed.
