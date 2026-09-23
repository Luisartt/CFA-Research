# Phase 1 — Plugin Foundation + Coaching Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship an installable `research-challenge` Claude Code plugin containing `init-skills` (team project setup), `thesis` (thesis coaching), `industry` (industry analysis) and the `/wrap-up` command.

**Architecture:** This repo is both the plugin and its own marketplace. Every skill is a folder under `skills/` with a `SKILL.md` (max 150 lines, fixed sections) plus on-demand `references/`. `init-skills` owns the project templates in `skills/init-skills/templates/` so skills only ever reference files inside their own directory (works when installed from the plugin cache on Windows and macOS). A stdlib+pytest structural test suite enforces the anatomy, manifests, and template-token consistency.

**Tech Stack:** Claude Code plugin format (`.claude-plugin/plugin.json`, `marketplace.json`), Markdown skills, Python 3.10+ with pytest and mypy for structural tests only (no runtime Python in phase 1).

**Spec:** `docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md`

**Deviations from spec (to be recorded in Task 10):**
- Templates live in `skills/init-skills/templates/`, not repo-root `templates/` (resolves spec §15 item 3: a skill can only rely on its own base directory).
- `/wrap-up` is built in phase 1, not phase 3, because the `AGENTS.md` template references it.

---

## File map

| File | Responsibility |
|---|---|
| `.gitattributes` | Force LF line endings (mixed Windows/Mac teams) |
| `pyproject.toml` | Dev deps + pytest/mypy config |
| `tests/test_plugin_structure.py` | Structural tests: manifests, skill anatomy, templates, command |
| `.claude-plugin/plugin.json` | Plugin manifest |
| `.claude-plugin/marketplace.json` | Marketplace manifest (repo = marketplace) |
| `skills/init-skills/SKILL.md` | Audit -> env check -> interview -> create -> verify |
| `skills/init-skills/references/framework-inference.md` | Exchange -> framework/currency/city defaults, LatAm accounting notes |
| `skills/init-skills/templates/AGENTS.md` | Canonical project instructions: persona, who-decides, coaching rules, tags, skill map, context rules |
| `skills/init-skills/templates/CLAUDE.md` | `@AGENTS.md` import + Claude-only notes |
| `skills/init-skills/templates/company-profile.yaml` | Company/accounting/report/team facts every skill reads |
| `skills/init-skills/templates/docs/context/*.md` (6) | Memory file stubs |
| `skills/thesis/SKILL.md` | Graded Socratic thesis coaching + co-writing |
| `skills/thesis/references/question-bank.md` | L1/L2/L3 questions |
| `skills/thesis/references/synthesis-template.md` | `research/thesis.md` layout |
| `skills/industry/SKILL.md` | 7-section industry analysis with coach moments |
| `skills/industry/references/industry-report-template.md` | `research/industry.md` layout + LatAm lens |
| `commands/wrap-up.md` | End-of-session context update |
| `evals/phase1.md` | Manual eval prompts + expected behaviors |
| `README.md`, `LICENSE`, `NOTICE` | Docs, MIT license, attribution |

---

### Task 1: Repo tooling and manifest tests

**Files:**
- Create: `.gitattributes`
- Create: `pyproject.toml`
- Create: `tests/test_plugin_structure.py`

- [ ] **Step 1: Create `.gitattributes`**

```
* text=auto eol=lf
*.xlsx binary
*.docx binary
*.pdf binary
```

- [ ] **Step 2: Create `pyproject.toml`**

```toml
[project]
name = "research-challenge-plugin"
version = "0.1.0"
description = "Structural tests for the research-challenge Claude Code plugin"
requires-python = ">=3.10"

[project.optional-dependencies]
dev = ["pytest>=8", "mypy>=1.10"]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.mypy]
strict = true
python_version = "3.10"
```

- [ ] **Step 3: Write the failing manifest tests**

Create `tests/test_plugin_structure.py`:

```python
"""Structural checks for the research-challenge plugin (stdlib + pytest only)."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parent.parent
PLUGIN_NAME = "research-challenge"
MARKETPLACE_NAME = "cfa-research"


def load_json(path: Path) -> dict[str, Any]:
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    return data


def test_plugin_manifest_identity() -> None:
    manifest = load_json(ROOT / ".claude-plugin" / "plugin.json")
    assert manifest["name"] == PLUGIN_NAME
    assert re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]), manifest["version"]
    assert manifest["license"] == "MIT"
    assert manifest["description"].strip()


def test_marketplace_lists_plugin_at_repo_root() -> None:
    marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    assert marketplace["name"] == MARKETPLACE_NAME
    names = [p["name"] for p in marketplace["plugins"]]
    assert names == [PLUGIN_NAME]
    assert marketplace["plugins"][0]["source"] == "./"
```

- [ ] **Step 4: Run tests to verify they fail**

Run: `python -m pytest -q`
Expected: 2 failed, `FileNotFoundError` on `.claude-plugin/plugin.json`.

- [ ] **Step 5: Commit**

```bash
git add .gitattributes pyproject.toml tests/test_plugin_structure.py
git commit -m "test: add plugin manifest structure tests"
```

---

### Task 2: Plugin and marketplace manifests

**Files:**
- Create: `.claude-plugin/plugin.json`
- Create: `.claude-plugin/marketplace.json`

- [ ] **Step 1: Create `.claude-plugin/plugin.json`**

```json
{
  "name": "research-challenge",
  "version": "0.1.0",
  "description": "Coaching skills for CFA Research Challenge teams: project setup with a LatAm specialist analyst persona, thesis coaching, industry analysis. The assistant does the technical work; the team owns the story.",
  "author": {
    "name": "CFA-Research contributors"
  },
  "homepage": "https://github.com/Luisartt/CFA-Research",
  "license": "MIT",
  "keywords": ["cfa", "research-challenge", "equity-research", "latam", "ifrs", "us-gaap", "coaching"]
}
```

- [ ] **Step 2: Create `.claude-plugin/marketplace.json`**

```json
{
  "name": "cfa-research",
  "description": "Skills for university teams competing in the CFA Institute Research Challenge (LatAm).",
  "owner": {
    "name": "CFA-Research contributors"
  },
  "plugins": [
    {
      "name": "research-challenge",
      "displayName": "Research Challenge",
      "source": "./",
      "description": "From filings to report and pitch: setup, thesis coaching, industry analysis (phase 1). The assistant does the technical work; the team owns the story.",
      "keywords": ["cfa", "research-challenge", "equity-research", "latam"]
    }
  ]
}
```

- [ ] **Step 3: Run tests to verify they pass**

Run: `python -m pytest -q`
Expected: `2 passed`

- [ ] **Step 4: Commit**

```bash
git add .claude-plugin/
git commit -m "feat: add plugin and marketplace manifests"
```

---

### Task 3: Skill-anatomy and template tests

**Files:**
- Modify: `tests/test_plugin_structure.py` (append)

- [ ] **Step 1: Append the failing anatomy/template tests**

Append to `tests/test_plugin_structure.py`:

```python
SKILLS_DIR = ROOT / "skills"
PHASE1_SKILLS: tuple[str, ...] = ("init-skills", "thesis", "industry")
USER_INVOKED_ONLY: frozenset[str] = frozenset({"init-skills"})
REQUIRED_SECTIONS: tuple[str, ...] = (
    "## Purpose",
    "## Reads",
    "## Steps",
    "## Coach moments",
    "## Writes",
    "## Log",
)
MAX_SKILL_LINES = 150
MIN_DESCRIPTION_WORDS = 40
TEMPLATES_DIR = SKILLS_DIR / "init-skills" / "templates"
CONTEXT_FILES: tuple[str, ...] = (
    "memory.md",
    "thesis-journal.md",
    "todo.md",
    "lessons.md",
    "ai-use-log.md",
    "session-log.md",
)
AGENTS_REQUIRED_HEADINGS: tuple[str, ...] = (
    "## System Persona",
    "## Who decides what",
    "## Coaching rules",
    "## Data tags",
    "## Skills",
    "## Context files",
    "## AI-use log",
    "## Professional standards",
)
TOKEN_RE = re.compile(r"\{\{([A-Z_]+)\}\}")
LOCAL_REF_RE = re.compile(r"`((?:references|templates)/[\w./-]+)`")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_frontmatter(path: Path) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", read_text(path), re.DOTALL)
    if match is None:
        raise AssertionError(f"{path} has no frontmatter block")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and not line.startswith(" "):
            fields[key.strip()] = value.strip()
    return fields


def skill_md(name: str) -> Path:
    return SKILLS_DIR / name / "SKILL.md"


@pytest.mark.parametrize("name", PHASE1_SKILLS)
def test_skill_file_exists(name: str) -> None:
    assert skill_md(name).is_file(), f"missing {skill_md(name)}"


@pytest.mark.parametrize("name", PHASE1_SKILLS)
def test_frontmatter_name_matches_directory(name: str) -> None:
    assert read_frontmatter(skill_md(name))["name"] == name


@pytest.mark.parametrize("name", PHASE1_SKILLS)
def test_description_is_yaml_safe_and_rich(name: str) -> None:
    description = read_frontmatter(skill_md(name))["description"]
    assert ": " not in description, "unquoted ': ' breaks YAML frontmatter"
    assert len(description.split()) >= MIN_DESCRIPTION_WORDS
    if name in USER_INVOKED_ONLY:
        assert read_frontmatter(skill_md(name)).get("disable-model-invocation") == "true"
    else:
        assert "Use whenever" in description


@pytest.mark.parametrize("name", PHASE1_SKILLS)
def test_required_sections_in_order(name: str) -> None:
    text = read_text(skill_md(name))
    positions = [text.find(section) for section in REQUIRED_SECTIONS]
    assert all(p >= 0 for p in positions), dict(zip(REQUIRED_SECTIONS, positions))
    assert positions == sorted(positions), "sections out of order"


@pytest.mark.parametrize("name", PHASE1_SKILLS)
def test_skill_is_short(name: str) -> None:
    line_count = len(read_text(skill_md(name)).splitlines())
    assert line_count <= MAX_SKILL_LINES, f"{name}: {line_count} lines"


@pytest.mark.parametrize("name", PHASE1_SKILLS)
def test_referenced_local_files_exist(name: str) -> None:
    skill_dir = SKILLS_DIR / name
    for ref in LOCAL_REF_RE.findall(read_text(skill_md(name))):
        target = skill_dir / ref.rstrip("/")
        assert target.exists(), f"{name} references missing {ref}"


def test_context_templates_exist() -> None:
    for filename in CONTEXT_FILES:
        assert (TEMPLATES_DIR / "docs" / "context" / filename).is_file(), filename


def test_claude_template_imports_agents() -> None:
    lines = [ln for ln in read_text(TEMPLATES_DIR / "CLAUDE.md").splitlines() if ln.strip()]
    assert lines[0] == "@AGENTS.md"


def test_agents_template_has_required_headings() -> None:
    text = read_text(TEMPLATES_DIR / "AGENTS.md")
    missing = [h for h in AGENTS_REQUIRED_HEADINGS if h not in text]
    assert not missing, missing


def test_every_template_token_is_documented_in_init_skill() -> None:
    documented = set(TOKEN_RE.findall(read_text(skill_md("init-skills"))))
    used: set[str] = set()
    for path in TEMPLATES_DIR.rglob("*"):
        if path.is_file():
            used |= set(TOKEN_RE.findall(read_text(path)))
    assert used, "templates contain no tokens"
    assert used <= documented, f"undocumented tokens: {sorted(used - documented)}"


def test_wrap_up_command_has_description() -> None:
    fields = read_frontmatter(ROOT / "commands" / "wrap-up.md")
    assert fields.get("description"), "wrap-up needs a description"
    assert ": " not in fields["description"]
```

- [ ] **Step 2: Run tests to verify the new ones fail**

Run: `python -m pytest -q`
Expected: the 2 manifest tests pass; every new test fails (missing `skills/...`, `templates/...`, `commands/wrap-up.md`).

- [ ] **Step 3: Type-check the test file**

Run: `python -m mypy tests`
Expected: `Success: no issues found in 1 source file`

- [ ] **Step 4: Commit**

```bash
git add tests/test_plugin_structure.py
git commit -m "test: add skill anatomy, template and command structure tests"
```

---

### Task 4: Project templates (installed by `init-skills`)

**Files:**
- Create: `skills/init-skills/templates/AGENTS.md`
- Create: `skills/init-skills/templates/CLAUDE.md`
- Create: `skills/init-skills/templates/company-profile.yaml`
- Create: `skills/init-skills/templates/docs/context/memory.md`
- Create: `skills/init-skills/templates/docs/context/thesis-journal.md`
- Create: `skills/init-skills/templates/docs/context/todo.md`
- Create: `skills/init-skills/templates/docs/context/lessons.md`
- Create: `skills/init-skills/templates/docs/context/ai-use-log.md`
- Create: `skills/init-skills/templates/docs/context/session-log.md`

- [ ] **Step 1: Create `skills/init-skills/templates/AGENTS.md`**

````markdown
# {{COMPANY_NAME}} ({{TICKER}}) — CFA Research Challenge project

This file is the single source of truth for how the AI assistant works in this
project. `CLAUDE.md` imports it. Edit here, not there.

## System Persona

{{SYSTEM_PERSONA}}

You are coaching a university team competing in the CFA Institute Research
Challenge. Team: {{TEAM}}. The report is written in {{REPORT_LANGUAGE}}; coach
in whatever language the student writes to you in.

## Who decides what

| The assistant does (do it well, do not ask permission) | The team decides (never decide for them) |
|---|---|
| Filing ingestion, statement extraction, every accounting adjustment | The investment thesis and its 2-3 pillars |
| Model construction, checks, valuation mechanics | How their view differs from consensus |
| Industry structure, peer data, risk matrix mechanics | The 3-5 assumptions that carry the story |
| Drafting and polishing prose from the team's ideas | Target price and recommendation |
| Explaining every technical choice in plain words | Which risks matter and why |

Technical work: just do it, then explain it in plain words so the team can
defend it in Q&A. Story decisions: recommend, argue the other side, ask — the
team chooses.

## Coaching rules

1. Restate the student's idea in their own terms before challenging it.
2. Ask at most 2-3 questions per turn. No compound questions.
3. On story decisions, flag weaknesses; do not silently rewrite their view.
4. At every decision point give: your recommendation and why, the strongest
   case against it, and one question the student must answer.
5. End every turn with exactly one clear next step.
6. If something is genuinely solid, say so plainly. False red flags burn trust.
7. Teach by showing: when you do technical work, say what you did and why in
   two or three sentences a first-year student understands.

## Data tags

Every number in research files, the model and the report carries one tag:

| Tag | Meaning |
|---|---|
| `[sourced]` | From a filing or public source — cite document and page/URL |
| `[guidance]` | Management said it (call, presentation, release) — cite it |
| `[assumption]` | Team judgment — one line of rationale |
| `[calc]` | Computed from other tagged numbers |
| `[unverified]` | Could not be tied to a source yet — must be resolved before the report |

Never invent a number. If you do not know it, say so and propose how to find it.

## Skills

Plugin `research-challenge`. Each skill works on its own; missing inputs become
`[assumption]` placeholders plus a `todo.md` item, never a blocker.

| Skill | Use it to | Writes |
|---|---|---|
| `/research-challenge:init-skills` | Set up or repair this project | this file, profile, context files |
| `thesis` | Shape and stress-test the investment story | `research/thesis.md` |
| `industry` | Industry structure, competition, peers | `research/industry.md` |
| `/research-challenge:wrap-up` | Close a work session | `docs/context/*` |

Skills also trigger from plain requests ("roast our thesis", "analyze the industry").

## Context files

Read ON DEMAND — grep for what you need, never bulk-read. Skip them for trivial
tasks. Caps are soft (approx. tokens = bytes / 4); when a file passes its cap,
`/research-challenge:wrap-up` proposes condensing the oldest entries.

| File | Holds | Write when | Soft cap |
|---|---|---|---|
| `docs/context/memory.md` | Decisions (`# decision: ...`) | A decision is locked | 8000 |
| `docs/context/thesis-journal.md` | Coaching answers, thesis evolution (append-only) | After every coach moment | 10000 |
| `docs/context/todo.md` | Open work by owner (`pending` / `in_progress` only) | Work starts, moves, or finishes (delete done items) | 2500 |
| `docs/context/lessons.md` | Corrections, one line each | The team corrects you | 5000 |
| `docs/context/ai-use-log.md` | What the AI did (append-only) | See below | none — never condense |
| `docs/context/session-log.md` | `[YYYY-MM-DD]: summary` | End of a work block | 4000 |

Before fixing something, grep `lessons.md` for a related lesson.

## AI-use log

After any work where you drafted, edited, computed or extracted content that
ends up in the report, model or pitch, append one line to
`docs/context/ai-use-log.md`:

`YYYY-MM-DD | member | skill | section or file | what the AI did`

Never skip this. The team's AI-use disclosure is built from it.

## Professional standards

- Public information only (CFA Standard II(A)). If a student mentions material
  non-public information, stop and flag it.
- Independence and objectivity: the recommendation follows the evidence, not
  management's charm or the team's hopes.
- Cite sources. Distinguish fact from opinion.
````

- [ ] **Step 2: Create `skills/init-skills/templates/CLAUDE.md`**

```markdown
@AGENTS.md

# Claude Code notes

- Plugin skills are namespaced: `/research-challenge:<skill>`. They also trigger
  from plain requests.
- Run `/research-challenge:wrap-up` at the end of every work session.
- To change the persona or rules, edit `AGENTS.md` — it is the single source of truth.
```

- [ ] **Step 3: Create `skills/init-skills/templates/company-profile.yaml`**

```yaml
# Written by /research-challenge:init-skills. Every skill reads this file.
# Edit by hand if something changes; keep the keys.
company:
  name: "{{COMPANY_NAME}}"
  ticker: "{{TICKER}}"
  exchange: "{{EXCHANGE}}"          # BMV | BIVA | B3 | BCS | BVC | BVL | BYMA | NYSE | NASDAQ
  country: "{{COUNTRY}}"
  sector: "{{SECTOR}}"
  issuer_type: "{{ISSUER_TYPE}}"    # non_financial | bank | insurer | reit
accounting:
  framework: "{{FRAMEWORK}}"        # ifrs | us_gaap | nif
  framework_confirmed_by_team: {{FRAMEWORK_CONFIRMED}}
  reporting_currency: "{{CURRENCY}}"
  fiscal_year_end: "{{FISCAL_YEAR_END}}"   # MM-DD
  units: "{{UNITS}}"                # millions | thousands
report:
  language: "{{REPORT_LANGUAGE}}"   # en | es | pt
  report_deadline: "{{REPORT_DEADLINE}}"      # YYYY-MM-DD
  presentation_date: "{{PRESENTATION_DATE}}"  # YYYY-MM-DD
team:
{{TEAM_YAML}}
compliance:
  public_information_only_confirmed: {{MNPI_CONFIRMED}}
created: "{{TODAY}}"
```

- [ ] **Step 4: Create the six context stubs**

`skills/init-skills/templates/docs/context/memory.md`:

```markdown
# Decisions

Format: `# decision: <one sentence>` (optional second line: why). Newest last.
Soft cap and rules: see AGENTS.md > Context files.

*(empty)*
```

`skills/init-skills/templates/docs/context/thesis-journal.md`:

```markdown
# Thesis journal

Append-only. One entry per coach moment:
`## YYYY-MM-DD — <skill> — <decision point>` then the question, the team's
answer, and what changed. Never edit past entries.

*(empty)*
```

`skills/init-skills/templates/docs/context/todo.md`:

```markdown
# Open work

Only `pending` and `in_progress` items. Delete an item when it is done.
Format: `- [pending|in_progress] <task> — owner: <name> — due: <YYYY-MM-DD>`

## Milestones

{{MILESTONES}}

## Tasks

*(empty)*
```

`skills/init-skills/templates/docs/context/lessons.md`:

```markdown
# Lessons

One line per correction from the team, so the mistake is not repeated.
Format: `- <rule> (YYYY-MM-DD)`

*(empty)*
```

`skills/init-skills/templates/docs/context/ai-use-log.md`:

```markdown
# AI-use log

Append-only evidence for the report's AI-use disclosure. Never condense or edit.
Format: `YYYY-MM-DD | member | skill | section or file | what the AI did`

```

`skills/init-skills/templates/docs/context/session-log.md`:

```markdown
# Session log

One line per work session: `[YYYY-MM-DD]: <what was done> — <who>`

*(empty)*
```

- [ ] **Step 5: Run the template tests**

Run: `python -m pytest -q -k "context_templates or claude_template or agents_template"`
Expected: `3 passed`

- [ ] **Step 6: Commit**

```bash
git add skills/init-skills/templates/
git commit -m "feat(init-skills): add project templates (AGENTS, CLAUDE, profile, context)"
```

---

### Task 5: `init-skills` skill

**Files:**
- Create: `skills/init-skills/SKILL.md`
- Create: `skills/init-skills/references/framework-inference.md`

- [ ] **Step 1: Create `skills/init-skills/references/framework-inference.md`**

```markdown
# Framework and defaults by exchange

Use to propose defaults in the interview. Always confirm against the accounting
policies note (usually Note 2 or 3) of the latest annual report.

| Exchange | Country | City | Currency | Default framework | Notes |
|---|---|---|---|---|---|
| BMV / BIVA | Mexico | Mexico City | MXN | IFRS (IASB) | Listed non-financial issuers report under IFRS. Banks use CNBV criteria — out of v1 model scope. |
| B3 | Brazil | Sao Paulo | BRL | IFRS (CPC-converged) | Banks also file regulatory COSIF statements; use the IFRS consolidated set. |
| Bolsa de Santiago (BCS) | Chile | Santiago | CLP (some USD functional) | IFRS | Check functional currency — miners and some exporters report in USD. |
| BVC | Colombia | Bogota | COP | IFRS-based (NCIF) | |
| BVL | Peru | Lima | PEN (some USD) | IFRS | Miners often report in USD. |
| BYMA | Argentina | Buenos Aires | ARS | IFRS | IAS 29 hyperinflation restatement applies — flag it early. |
| NYSE / NASDAQ, 10-K filer | USA | New York | USD | US GAAP | Domestic filer: 10-K / 10-Q. |
| NYSE / NASDAQ, 20-F filer (ADR) | home country | home city | home currency | IFRS as issued by IASB | Foreign private issuer. |

## Issuer types that change the work

| Issuer type | What changes |
|---|---|
| bank | Valuation by DDM or residual income, not DCF. Regulatory capital matters. v1 model does not build it. |
| insurer | Same as bank; IFRS 17 in IFRS jurisdictions. |
| reit (FIBRA in Mexico) | NAV and AFFO-based valuation alongside DCF. |

## Differences that move numbers (for the persona to watch)

- **Leases:** IFRS 16 puts nearly all leases on balance sheet and moves rent out
  of EBITDA; US GAAP ASC 842 keeps operating-lease cost inside operating
  expenses. Comparing IFRS and US GAAP peers on EBITDA needs an adjustment.
- **Hyperinflation:** IAS 29 restates Argentine figures to current purchasing power.
- **Inventory:** LIFO is not allowed under IFRS.
- **Cash-flow classification:** IFRS lets interest paid sit in operating or
  financing; check before comparing free cash flow.
- **PP&E revaluation:** allowed under IFRS, not under US GAAP.
- **Mexico PTU (employee profit sharing):** an operating cost; check where it is
  presented before computing margins.
```

- [ ] **Step 2: Create `skills/init-skills/SKILL.md`**

````markdown
---
name: init-skills
description: One-time setup for a CFA Research Challenge team project. Interviews the team (company, exchange, sector, accounting framework, report language, roles, deadlines), builds a LatAm sector-specialist analyst persona, and writes AGENTS.md, CLAUDE.md, company-profile.yaml, the docs/context memory files and the project folders. Idempotent - audits first, fills only gaps, never overwrites silently. Run it once per team folder before the other research-challenge skills, or again to repair a broken setup.
disable-model-invocation: true
---

# init-skills

## Purpose

Set up a team's project so every other skill has a persona, shared facts
(`company-profile.yaml`) and memory (`docs/context/`). A project that is already
set up must cost the team nothing: audit first, act only on gaps.

## Reads

- The current project folder (what already exists).
- `filings/` if present — infer company, exchange and currency from the files.
- `templates/` and `references/framework-inference.md` in this skill's base directory.

## Steps

### Step 1 — Audit (before touching anything)

Check each item and print a table `item | present | missing | non-conforming`:

1. `AGENTS.md` exists with a non-empty `## System Persona` and the headings
   `## Who decides what`, `## Coaching rules`, `## Data tags`, `## AI-use log`.
2. `CLAUDE.md` exists and its first non-empty line is `@AGENTS.md`.
3. `company-profile.yaml` exists and contains no `{{`.
4. The six files in `docs/context/` exist.
5. Folders exist: `filings/ data/ research/ model/ valuation/ report/ pitch/`.

All conform -> say "Project already set up. Nothing changed." and stop.

### Step 2 — Environment check (warn, never block)

Run `python --version` (on Windows fall back to `py --version`) and
`python -c "import openpyxl"`. Phase-1 skills do not need Python; the model
skills will. If missing, print the exact command and offer to run it:

- Python missing -> Windows: `winget install Python.Python.3.12`; macOS: `brew install python`
- openpyxl missing -> Windows: `py -m pip install openpyxl python-docx`; macOS: `python3 -m pip install openpyxl python-docx`

### Step 3 — Interview (only for what the audit found missing)

One question at a time. Always offer a default the student can accept with
"ok". If `filings/` has documents, infer answers and ask to confirm instead.

1. Company, ticker and exchange.
2. Sector. Then propose the persona and ask accept/edit:
   "Senior equity research analyst with 15 years covering LatAm {sector} at a
   top-tier investment bank, based in {city}. Known for tying every forecast to
   how the business actually makes money. Has mentored dozens of junior
   analysts: demanding on the story, generous with technique."
3. Accounting framework, reporting currency, fiscal year end, units — propose
   from `references/framework-inference.md`, ask to confirm. Bank, insurer or
   REIT -> read the issuer-type table there and warn what changes.
4. Report language: en / es / pt.
5. Team members and roles (optional): model, industry, valuation, writer, all.
6. Report deadline and presentation date (YYYY-MM-DD).
7. "Is all the material you will use public information?" (CFA Standard II(A)).
   If not yes, explain the rule and do not record `true`.

### Step 4 — Create missing files

Copy from `templates/` in this skill's base directory; never edit the templates.
Replace every token:

| Token | Value |
|---|---|
| `{{COMPANY_NAME}}` `{{TICKER}}` `{{EXCHANGE}}` `{{COUNTRY}}` `{{SECTOR}}` | Q1-Q2 |
| `{{ISSUER_TYPE}}` | non_financial, bank, insurer or reit |
| `{{SYSTEM_PERSONA}}` | Persona text accepted in Q2 |
| `{{FRAMEWORK}}` `{{CURRENCY}}` `{{FISCAL_YEAR_END}}` `{{UNITS}}` | Q3 |
| `{{FRAMEWORK_CONFIRMED}}` | `true` if the team confirmed, else `false` |
| `{{REPORT_LANGUAGE}}` | Q4 |
| `{{TEAM}}` | One line, e.g. `Ana (model), Luis (industry)` or `not assigned yet` |
| `{{TEAM_YAML}}` | One `  - name: "..."` / `    role: "..."` pair per member, or `  []` |
| `{{REPORT_DEADLINE}}` `{{PRESENTATION_DATE}}` | Q6 |
| `{{MILESTONES}}` | See below |
| `{{MNPI_CONFIRMED}}` | `true` only on an explicit yes in Q7 |
| `{{TODAY}}` | Today, YYYY-MM-DD |

`{{MILESTONES}}`: count back from the report deadline D, one todo line each:
thesis v1 (D-42), industry analysis (D-35), model v1 (D-28), valuation and target
price (D-21), report draft (D-10), final report (D), presentation (presentation
date). Format: `- [pending] <milestone> — owner: <role or all> — due: <date>`.

Create the seven folders with an empty `.gitkeep` in each.

A file that exists but does not conform: show the difference and ask
`[k] keep / [o] overwrite / [m] merge` (default keep). Merge = add the missing
sections from the template, keep every existing line. Never overwrite silently.

### Step 5 — Verify and report

Re-run the Step 1 audit. Print `file | created / kept / merged`. Then give one
next step: "Next: `thesis` to shape your story, or `industry` to map the market.
Drop the latest annual report and quarterly reports into `filings/`."

## Coach moments

- **Persona (Q2):** the persona sets the bar for every later answer — invite the
  team to sharpen the sector focus rather than accept a generic one.
- **Framework (Q3):** ask the team to open the accounting policies note and
  confirm; one minute now avoids comparing IFRS and US GAAP numbers later.

## Writes

`AGENTS.md`, `CLAUDE.md`, `company-profile.yaml`, `docs/context/*.md` (6),
`filings/ data/ research/ model/ valuation/ report/ pitch/`.

## Log

- `docs/context/ai-use-log.md`: `YYYY-MM-DD | <member> | init-skills | project setup | created project files and persona`
- `docs/context/memory.md`: `# decision: framework = <framework> (confirmed by team: yes/no)` and `# decision: report language = <lang>`
- `docs/context/session-log.md`: `[YYYY-MM-DD]: project set up with init-skills — <member>`
````

- [ ] **Step 3: Run the init-skills tests**

Run: `python -m pytest -q -k "init-skills or token"`
Expected: all selected tests pass (skill file exists, name, description, sections, length ≤150, referenced files exist, tokens documented).

If `test_skill_is_short[init-skills]` fails, tighten prose in Step 3/Step 4 (do not move required content out of the file).

- [ ] **Step 4: Commit**

```bash
git add skills/init-skills/
git commit -m "feat(init-skills): add setup skill and framework inference reference"
```

---

### Task 6: `thesis` skill

**Files:**
- Create: `skills/thesis/SKILL.md`
- Create: `skills/thesis/references/question-bank.md`
- Create: `skills/thesis/references/synthesis-template.md`

- [ ] **Step 1: Create `skills/thesis/references/question-bank.md`**

```markdown
# Thesis question bank

Pick 2-3 per turn. Move to the next level only when the current one is answered
cleanly. Adapt wording to the student's own terms and company.

## L1 — Frame (is there a story?)

1. In one sentence: what do you recommend, and why will the market agree with you within 12 months?
2. What does this company actually sell, to whom, and why do they pay?
3. What is the one number that best captures how this business makes money?
4. If you had to pick one reason to own (or avoid) this stock, which is it?
5. What does the market currently believe about this company? Where did you see that?
6. Why this company, of all the ones you could have picked? What drew you?
7. Is your story about growth, margins, capital allocation, or valuation re-rating?
8. What happened to the stock over the last year, and what explains it?

## L2 — Probe (is each pillar real?)

1. What evidence supports this pillar? Which of it is `[sourced]` and which is `[assumption]`?
2. Which line of the model would show this pillar if you are right?
3. What does consensus (sell-side, market pricing) assume for that line? How far are you from it?
4. Why is the market wrong here — what does it miss, misread, or overweight?
5. Has management said anything that supports or contradicts this? Quote it.
6. Is this pillar already in the price? How would you know?
7. What would a competitor say about this claim?
8. Is this pillar independent of the others, or do they all depend on one assumption?
9. What happened the last time this company promised something similar?
10. Which peer proves or disproves your point?
11. How big is the effect in numbers: how many points of margin or growth, how much per share?
12. What is the time frame — when does the market see it?

## L3 — Stress (does it survive attack?)

1. Argue the opposite recommendation as convincingly as you can. What is its best point?
2. What single fact, if it came out tomorrow, would make you change the recommendation?
3. Which assumption, if 20% worse, flips your call?
4. What catalyst forces the market to see what you see, and when?
5. If the catalyst does not happen, what is the stock worth?
6. Which macro variable (FX, rates, commodity, election) hurts the thesis most?
7. What governance or controlling-shareholder risk could override the fundamentals?
8. If a judge says "this is already priced in", what is your answer in 20 seconds?
9. What did you drop from the thesis, and why was it weaker?
10. What would you need to see in the next quarterly report to feel more confident?
```

- [ ] **Step 2: Create `skills/thesis/references/synthesis-template.md`**

```markdown
# Investment thesis — <Company> (<TICKER>)

_Version <N> — <YYYY-MM-DD> — status: draft | locked_

## One-line thesis

We rate <Company> a <BUY/HOLD/SELL — provisional until valuation> because
<pillar 1>, <pillar 2>, <pillar 3>, which the market misses because <reason>.

## Pillars

### Pillar 1 — <title>

- **Claim:**
- **Evidence:** (every number tagged)
- **Consensus view:**
- **Why the market is wrong:**
- **Model link:** <driver in model/drivers.yaml, or "to be built">

(Repeat for pillars 2-3.)

## Catalysts (next 12 months)

| Catalyst | Expected timing | Pillar | How we will know |
|---|---|---|---|

## Kill criteria — what would change our mind

-

## Red flags still open

-

## Next moves

1.

## History

- v<N> <YYYY-MM-DD>: <what changed and why>
```

- [ ] **Step 3: Create `skills/thesis/SKILL.md`**

```markdown
---
name: thesis
description: Coach a CFA Research Challenge team to a sharp, defensible investment thesis - 2-3 pillars, variant perception versus consensus, catalysts and kill criteria. Stress-tests the story Socratically in graded levels (Frame, Probe, Stress), then co-writes research/thesis.md once the team owns the ideas. Use whenever a student is choosing or shaping the story, asks "is our thesis good", "why buy or sell", "what is our angle", "roast our thesis", wants a buy/sell/hold argument challenged, or is about to lock the recommendation - even if they don't explicitly ask for coaching.
---

# thesis

## Purpose

The thesis is the one thing the team must own. Help them find it, test it until
it holds, then write it up well. Challenge ideas; never supply the pillars.

## Reads

- `company-profile.yaml` — missing: ask company and sector in one line and
  suggest `/research-challenge:init-skills`; continue anyway.
- `research/thesis.md` — if present, resume from the latest version.
- `docs/context/thesis-journal.md` — grep the last entries for open questions.
- Optional evidence: `research/industry.md`, `data/financials.csv`,
  `model/model-summary.json`. Use what exists; never block on what does not.
- `references/question-bank.md` and `references/synthesis-template.md`.

## Steps

1. **Load state.** If `research/thesis.md` exists, summarize the current
   one-line thesis, pillars and open red flags in five lines. Ask what changed.
2. **Frame (L1).** Ask for the thesis in one sentence. Restate it in the
   student's own words and ask "is that right?". Do not move on until confirmed.
   No thesis yet: use L1 questions to help them find one — ask, do not propose.
3. **Probe (L2).** Pillar by pillar: evidence, model line, consensus view, why
   the market is wrong, size of the effect. 2-3 questions per turn from the bank.
   When a student cites a number, check its tag; untagged numbers get flagged.
4. **Stress (L3).** Opposite case, kill criteria, catalysts and timing,
   "already priced in". Escalate only after L2 is answered cleanly.
5. **Stop** when answers stop producing new information, or when the student
   asks. If the thesis is genuinely solid, say so plainly.
6. **Synthesize.** Write `research/thesis.md` from
   `references/synthesis-template.md`. Co-write the prose from the team's
   answers — polish wording, never add a pillar they did not argue. Tag every
   number. New version: bump `Version`, add a `History` line, keep the old
   pillars in History if they changed.
7. **Close** with one next step (usually: the evidence gap that matters most).

## Coach moments

For each: your recommendation and why, the strongest case against it, and one
question the student must answer. Append the answer to `thesis-journal.md`.

- **Pillar selection:** which 2-3 survive. Push to cut the weakest one.
- **Variant perception:** what exactly the market misses. "Good company" is not
  a thesis; a gap versus consensus is.
- **Kill criteria:** the fact that would change their mind.
- **Direction:** Buy/Hold/Sell stays provisional until valuation — say so.

## Writes

- `research/thesis.md` (versioned in-file; history kept).
- Appends to `docs/context/thesis-journal.md`:
  `## YYYY-MM-DD — thesis — <decision point>` + question, answer, what changed.

## Log

- `docs/context/ai-use-log.md`: one line per session, e.g.
  `YYYY-MM-DD | <member> | thesis | research/thesis.md | coached pillars; co-wrote prose from team answers`
- `docs/context/memory.md`: `# decision: pillar <n> = <title>` when a pillar is locked.
- `docs/context/todo.md`: one item per evidence gap, with owner if known.
```

- [ ] **Step 4: Run the thesis tests**

Run: `python -m pytest -q -k thesis`
Expected: all selected tests pass.

- [ ] **Step 5: Commit**

```bash
git add skills/thesis/
git commit -m "feat(thesis): add graded thesis coaching skill with question bank"
```

---

### Task 7: `industry` skill

**Files:**
- Create: `skills/industry/SKILL.md`
- Create: `skills/industry/references/industry-report-template.md`

- [ ] **Step 1: Create `skills/industry/references/industry-report-template.md`**

```markdown
# Industry analysis — <Company> (<TICKER>)

_Updated <YYYY-MM-DD>. Every number tagged; sources listed at the end._

## 1. Market definition, size and life cycle

- Where the company competes (product x geography x customer). Say what is
  *out* of the market too.
- Market size and growth, history and outlook `[sourced]` / `[assumption]`.
- Life-cycle stage (emerging, growth, mature, decline) and why.

## 2. Five forces

| Force | Intensity (low/med/high) | Evidence |
|---|---|---|
| Rivalry | | |
| Threat of entrants | | |
| Supplier power | | |
| Buyer power | | |
| Substitutes | | |

One paragraph: what the forces imply for long-run margins.

## 3. Competitive landscape and share

| Competitor | Share | Trend | Listed? (ticker) | Note |
|---|---|---|---|---|

## 4. Positioning and moat

- What protects the company (scale, brand, network, switching costs,
  regulation/concessions, cost position) — with evidence, not adjectives.
- How durable, and what would erode it.

## 5. SWOT

| Strengths | Weaknesses |
|---|---|
| | |

| Opportunities | Threats |
|---|---|
| | |

## 6. Peer universe (for comps)

| Peer | Ticker | Why comparable | Framework | Caveat |
|---|---|---|---|---|

Aim for 5-8: local listed peers, regional LatAm peers, one or two global
benchmarks. Flag IFRS vs US GAAP peers (lease treatment moves EBITDA).

## 7. Implications for the forecast and thesis

- Industry assumptions the forecast must respect (market growth, pricing, share).
- Which thesis pillar this analysis supports or weakens.

## LatAm lens (check each)

- Regulation, concessions and tariff reviews.
- FX exposure: revenue vs cost currency.
- Informal market and data gaps in market-share figures.
- Family groups and controlling shareholders among competitors.
- Cross-border players (US, Brazilian, Chilean, Mexican) entering the market.

## Sources

- <document or URL> — <what it supports>
```

- [ ] **Step 2: Create `skills/industry/SKILL.md`**

```markdown
---
name: industry
description: Industry and competitive analysis for a CFA Research Challenge company - market definition and size, five forces, competitive landscape and market share, positioning and moat, SWOT, peer universe for comps, and what it all implies for the forecast and thesis, with a LatAm lens (regulation, FX, informal markets, family groups). Does the research and structure; coaches the team on where the company really competes and what protects it. Use whenever a student asks to analyze the industry or sector, map competitors, pick comparables, build a SWOT or five forces, assess a moat or market share - even if they don't explicitly ask for an industry report.
---

# industry

## Purpose

Give the team a rigorous, sourced picture of the market their company competes
in, fast. The research and structure are the assistant's job; two judgments
belong to the team: where the company really competes, and what protects it.

## Reads

- `company-profile.yaml` — missing: ask company, country and sector in one line
  and continue.
- `filings/` — annual report business and MD&A sections, risk factors.
- `research/sources/` — any reports or links the team saved.
- `research/thesis.md` — optional; used for section 7.
- `research/industry.md` — if present, update it instead of starting over.
- `references/industry-report-template.md`.

## Steps

1. **Gather.** Read the business description and MD&A in `filings/`, the team's
   `research/sources/`, and use web search if available. Record every source.
2. **Draft sections 1-6** of `references/industry-report-template.md`. Tag every
   number. Market share you cannot source: `[unverified]` plus a todo item —
   never estimate it silently.
3. **Apply the LatAm lens** checklist at the end of the template; add what
   applies to the relevant section.
4. **Run the coach moments** below before finalizing sections 1, 4 and 6.
5. **Write section 7** linking the findings to the forecast and, if
   `research/thesis.md` exists, to each pillar (supports / weakens / neutral).
6. **Save** `research/industry.md` (update the date line). Close with one next
   step — usually the pillar the analysis weakens most, or the data gap to close.

## Coach moments

For each: your recommendation and why, the strongest case against it, and one
question the student must answer. Append the answer to `thesis-journal.md`.

- **Market definition (section 1):** the most common trap. A company that looks
  dominant in a narrow market may be small in the one that sets its prices. Ask
  which market the customer actually chooses within.
- **Moat (section 4):** ask for the evidence that the advantage shows up in
  numbers (margins above peers, stable share, pricing power).
- **Peer set (section 6):** ask them to defend each peer in one sentence; a
  judge will ask why a peer was included or left out.

## Writes

- `research/industry.md`
- Appends coach-moment answers to `docs/context/thesis-journal.md`.

## Log

- `docs/context/ai-use-log.md`:
  `YYYY-MM-DD | <member> | industry | research/industry.md | researched and drafted sections 1-7; team decided market definition, moat, peers`
- `docs/context/todo.md`: one item per `[unverified]` figure.
- `docs/context/memory.md`: `# decision: peer set = <tickers>` once agreed.
```

- [ ] **Step 3: Run the industry tests**

Run: `python -m pytest -q -k industry`
Expected: all selected tests pass.

- [ ] **Step 4: Commit**

```bash
git add skills/industry/
git commit -m "feat(industry): add industry analysis skill with LatAm lens"
```

---

### Task 8: `/wrap-up` command

**Files:**
- Create: `commands/wrap-up.md`

- [ ] **Step 1: Create `commands/wrap-up.md`**

```markdown
---
description: End-of-session wrap-up for a CFA Research Challenge project - updates todo, session log, lessons, decisions and the AI-use log from this session's work, and flags context files over their soft cap. Run at the end of every work session.
---

Wrap up this work session. Follow the Context files and AI-use log rules in
`AGENTS.md` (read those two sections only).

1. Review this session: what was done, decided, corrected, and left open.
2. `docs/context/todo.md`: delete finished items, update status of moved items,
   add new open items with owner and due date if known.
3. `docs/context/memory.md`: add `# decision: ...` for each decision locked this session.
4. `docs/context/lessons.md`: add one line per correction the team made to your work.
5. `docs/context/ai-use-log.md`: check every piece of AI work this session has
   a line; add the missing ones. Never edit existing lines.
6. `docs/context/session-log.md`: add `[YYYY-MM-DD]: <summary> — <who>`.
7. Size check: for each context file with a soft cap, estimate tokens as
   bytes / 4. Over cap -> propose condensing the oldest entries into a short
   summary and ask before changing anything. Never condense `ai-use-log.md`.
8. Report in five lines or fewer: what was updated, anything over cap, and the
   one next step for the next session.
```

- [ ] **Step 2: Run the command test**

Run: `python -m pytest -q -k wrap_up`
Expected: `1 passed`

- [ ] **Step 3: Run the full suite and type check**

Run: `python -m pytest -q; python -m mypy tests`
Expected: all tests pass; mypy `Success: no issues found in 1 source file`.

- [ ] **Step 4: Commit**

```bash
git add commands/wrap-up.md
git commit -m "feat: add /wrap-up command for end-of-session context updates"
```

---

### Task 9: README, LICENSE, NOTICE, evals

**Files:**
- Create: `README.md`
- Create: `LICENSE`
- Create: `NOTICE`
- Create: `evals/phase1.md`

- [ ] **Step 1: Create `LICENSE`**

```
MIT License

Copyright (c) 2026 CFA-Research contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

- [ ] **Step 2: Create `NOTICE`**

```
research-challenge plugin
Copyright (c) 2026 CFA-Research contributors

This project adapts material from research_analyst
  https://github.com/cfamexico/research_analyst
  Copyright (c) 2026 CFA Society Mexico - AI for Finance
  Licensed under the MIT License.
Adapted so far: data tags ([sourced]/[guidance]/[assumption]/[calc]), the
public-information (MNPI) confirmation, the industry report structure, the
issuer profile fields, and the IFRS / US GAAP / NIF framework notes.

It also adapts coaching and setup patterns (roast-me, scaffold) from
battle_tested_skills
  https://github.com/alanvaa06/battle_tested_skills
```

- [ ] **Step 3: Create `README.md`**

````markdown
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
````

- [ ] **Step 4: Create `evals/phase1.md`**

```markdown
# Phase 1 manual evals

Run in a fresh empty folder after installing the plugin from a local path
(`/plugin marketplace add <repo path>`, `/plugin install research-challenge@cfa-research`).
Mark each expected behavior pass/fail.

## init-skills

1. Prompt: `/research-challenge:init-skills` in an empty folder.
   - [ ] Prints the audit table before asking anything.
   - [ ] Asks one question at a time, each with a default.
   - [ ] Proposes IFRS + MXN + Mexico City for a BMV company and asks to confirm.
   - [ ] Creates all files and 7 folders; `company-profile.yaml` has no `{{`.
   - [ ] `todo.md` milestones are dated backwards from the deadline.
   - [ ] Appends a line to `ai-use-log.md`.
2. Prompt: `/research-challenge:init-skills` again in the same folder.
   - [ ] Says "Project already set up. Nothing changed." and asks nothing.
3. Setup: delete `docs/context/lessons.md`, edit `CLAUDE.md` to remove `@AGENTS.md`. Run again.
   - [ ] Recreates only `lessons.md`; asks `[k]/[o]/[m]` for `CLAUDE.md`; no interview.

## thesis

1. Prompt: "We think Cemex is a buy because infrastructure spending is going up."
   - [ ] Restates the idea and asks to confirm before challenging.
   - [ ] Asks at most 3 questions; ends with one next step.
   - [ ] Does not propose pillars the student did not raise.
2. Prompt: "roast our thesis" with an existing `research/thesis.md`.
   - [ ] Summarizes the current version first; uses L2/L3 questions.
3. Prompt: "ok, write it up" after a full session.
   - [ ] Writes `research/thesis.md` in template layout; every number tagged; History line added.
   - [ ] Appends to `thesis-journal.md` and `ai-use-log.md`.

## industry

1. Prompt: "analyze the industry for our company" (profile present, one annual report in `filings/`).
   - [ ] Drafts sections 1-6 with sources; unsourced market share tagged `[unverified]` + todo.
   - [ ] Stops for the market-definition coach moment before finalizing.
2. Prompt: "who should be our comparables?"
   - [ ] Proposes 5-8 peers mixing local/regional/global, flags IFRS vs US GAAP.
   - [ ] Asks the team to defend each peer.

## wrap-up

1. Prompt: `/research-challenge:wrap-up` after a thesis session.
   - [ ] Updates todo/session-log; ai-use-log has lines for the session's work.
   - [ ] Reports in five lines or fewer with one next step.
```

- [ ] **Step 5: Commit**

```bash
git add README.md LICENSE NOTICE evals/phase1.md
git commit -m "docs: add README, MIT license, attribution notice and phase 1 evals"
```

---

### Task 10: Record spec deviations and smoke-test the install

**Files:**
- Modify: `docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md` (§11, §14, §15)

- [ ] **Step 1: Update spec §11 repo layout**

Replace the line
`templates/              AGENTS.md, CLAUDE.md, docs/context/*, company-profile.yaml`
with
`skills/init-skills/templates/   AGENTS.md, CLAUDE.md, docs/context/*, company-profile.yaml`
and replace
`Skills locate \`engine/\` and \`templates/\` relative to their own base directory.`
with
`Skills reference only files inside their own directory (the plugin cache path differs per machine). Shared code for phase 2 lives inside the skill that owns it.`

- [ ] **Step 2: Update spec §14 build order**

Change item 1 to: `1. \`init-skills\`, \`thesis\`, \`industry\`, \`/wrap-up\` + templates + plugin manifests`
and item 3 to: `3. \`risks-esg\`, \`report\`, \`pitch\``

- [ ] **Step 3: Update spec §15**

Replace the three bullets' last one (plugin skills referencing sibling directories) with:
`- Resolved: skills reference only their own directory; marketplace name is \`cfa-research\`.`
and remove the marketplace-name bullet.

- [ ] **Step 4: Run the full suite**

Run: `python -m pytest -q; python -m mypy tests`
Expected: all pass.

- [ ] **Step 5: Validate the plugin with Claude Code (if the CLI supports it)**

Run: `claude plugin validate .`
Expected: no errors. If the subcommand does not exist in the installed version, skip and rely on Step 6.

- [ ] **Step 6: Local install smoke test (manual, by the user)**

In a new empty folder, in Claude Code:
```
/plugin marketplace add C:\Proyectos\CFA-Research
/plugin install research-challenge@cfa-research
```
Expected: `/research-challenge:init-skills` and `/research-challenge:wrap-up`
appear in the slash menu; "roast our thesis" triggers `thesis`. Then run the
evals in `evals/phase1.md`.

- [ ] **Step 7: Commit**

```bash
git add docs/superpowers/specs/2026-09-22-research-challenge-plugin-design.md
git commit -m "docs: record phase 1 deviations in spec (template location, wrap-up)"
```
