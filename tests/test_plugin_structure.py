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


SKILLS_DIR = ROOT / "skills"
SKILLS: tuple[str, ...] = (
    "init-skills", "thesis", "industry", "financials", "forecast", "model", "valuation",
    "risks-esg", "report", "pitch", "deck",
)
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
    text = read_text(path)
    if text.startswith("\ufeff"):
        raise AssertionError(f"{path} starts with a UTF-8 BOM; save it as UTF-8 without BOM")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
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


@pytest.mark.parametrize("name", SKILLS)
def test_skill_file_exists(name: str) -> None:
    assert skill_md(name).is_file(), f"missing {skill_md(name)}"


@pytest.mark.parametrize("name", SKILLS)
def test_frontmatter_name_matches_directory(name: str) -> None:
    assert read_frontmatter(skill_md(name))["name"] == name


@pytest.mark.parametrize("name", SKILLS)
def test_description_is_yaml_safe_and_rich(name: str) -> None:
    description = read_frontmatter(skill_md(name))["description"]
    assert ": " not in description, "unquoted ': ' breaks YAML frontmatter"
    assert len(description.split()) >= MIN_DESCRIPTION_WORDS
    if name in USER_INVOKED_ONLY:
        assert read_frontmatter(skill_md(name)).get("disable-model-invocation") == "true"
    else:
        assert "Use whenever" in description


@pytest.mark.parametrize("name", SKILLS)
def test_required_sections_in_order(name: str) -> None:
    text = read_text(skill_md(name))
    positions: list[int] = []
    for section in REQUIRED_SECTIONS:
        match = re.search(rf"^{re.escape(section)}[ \t]*$", text, re.MULTILINE)
        positions.append(match.start() if match else -1)
    assert all(p >= 0 for p in positions), dict(zip(REQUIRED_SECTIONS, positions))
    assert positions == sorted(positions), "sections out of order"


@pytest.mark.parametrize("name", SKILLS)
def test_skill_is_short(name: str) -> None:
    line_count = len(read_text(skill_md(name)).splitlines())
    assert line_count <= MAX_SKILL_LINES, f"{name}: {line_count} lines"


@pytest.mark.parametrize("name", SKILLS)
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


def test_gitattributes_template_uses_union_merge() -> None:
    path = TEMPLATES_DIR / "gitattributes"
    assert path.is_file(), path
    text = read_text(path)
    for filename in ("ai-use-log.md", "thesis-journal.md", "session-log.md"):
        assert f"docs/context/{filename} merge=union" in text, filename


def test_wrap_up_command_has_description() -> None:
    fields = read_frontmatter(ROOT / "commands" / "wrap-up.md")
    assert fields.get("description"), "wrap-up needs a description"
    assert ": " not in fields["description"]


ENGINE_SKILLS: tuple[str, ...] = ("financials", "forecast", "model", "valuation")
ENGINE_CALL = "${CLAUDE_PLUGIN_ROOT}/skills/model/engine/build_model.py"
ENGINE_DIR = SKILLS_DIR / "model" / "engine"


@pytest.mark.parametrize("name", ENGINE_SKILLS)
def test_engine_skills_call_the_engine_by_plugin_root(name: str) -> None:
    assert ENGINE_CALL in read_text(skill_md(name))
    assert (ENGINE_DIR / "build_model.py").is_file()


def _engine_chart() -> tuple[tuple[str, ...], tuple[str, ...]]:
    import sys

    if str(ENGINE_DIR) not in sys.path:
        sys.path.insert(0, str(ENGINE_DIR))
    from rcmodel.chart import CHART, DRIVER_KEYS

    return tuple(item.key for item in CHART), DRIVER_KEYS


def test_chart_reference_lists_every_engine_line_item() -> None:
    chart_keys, _ = _engine_chart()
    text = read_text(SKILLS_DIR / "financials" / "references" / "chart-of-accounts.md")
    missing = [key for key in chart_keys if f"`{key}`" not in text]
    assert not missing, missing


def test_drivers_guide_lists_every_engine_driver() -> None:
    _, driver_keys = _engine_chart()
    for path in (SKILLS_DIR / "forecast" / "references" / "drivers-guide.md",
                 SKILLS_DIR / "forecast" / "references" / "drivers-template.yaml"):
        text = read_text(path)
        missing = [key for key in driver_keys if key not in text]
        assert not missing, (path.name, missing)


def test_valuation_template_matches_the_loader() -> None:
    text = read_text(SKILLS_DIR / "valuation" / "references" / "valuation-template.yaml")
    for field in ("share_price", "price_52w_low", "price_52w_high", "years_since_fiscal_year_end",
                  "non_operating_assets", "debt_like_items", "risk_free", "equity_risk_premium",
                  "country_risk_premium", "beta_unlevered", "target_debt_to_equity", "pre_tax_cost_of_debt",
                  "tax_rate", "growth", "exit_ev_ebitda", "lt_nominal_gdp_growth", "peers", "target_price"):
        assert f"{field}:" in text, field


REPORT_TOOLS = SKILLS_DIR / "report" / "tools"
TOOL_CALLS: dict[str, tuple[str, ...]] = {
    "risks-esg": ("${CLAUDE_PLUGIN_ROOT}/skills/report/tools/charts.py",),
    "report": ("${CLAUDE_PLUGIN_ROOT}/skills/report/tools/charts.py",
               "${CLAUDE_PLUGIN_ROOT}/skills/report/tools/build_docx.py"),
    "deck": ("${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/build_pptx.py",
             "${CLAUDE_PLUGIN_ROOT}/skills/deck/tools/audit_pptx.py"),
}


@pytest.mark.parametrize("name", sorted(TOOL_CALLS))
def test_report_skills_call_the_tools_by_plugin_root(name: str) -> None:
    text = read_text(skill_md(name))
    for call in TOOL_CALLS[name]:
        assert call in text, call
        assert (ROOT / call.replace("${CLAUDE_PLUGIN_ROOT}/", "")).is_file(), call


def test_challenge_structure_matches_the_page_budget() -> None:
    import sys

    if str(REPORT_TOOLS) not in sys.path:
        sys.path.insert(0, str(REPORT_TOOLS))
    from build_docx import BUDGET_PAGES

    text = read_text(SKILLS_DIR / "report" / "references" / "challenge-structure.md")
    for slug, pages in BUDGET_PAGES.items():
        assert f"-{slug}.md`" in text, slug
        assert f"| {pages:.1f} |" in text, (slug, pages)


def test_risks_template_loads_in_the_chart_tool() -> None:
    import sys

    if str(REPORT_TOOLS) not in sys.path:
        sys.path.insert(0, str(REPORT_TOOLS))
    from charts import load_risks

    risks = load_risks(SKILLS_DIR / "risks-esg" / "references" / "risks-template.yaml")
    assert risks and risks[0]["id"] == "R1"


def test_outline_template_names_real_charts_and_fields() -> None:
    import sys

    if str(REPORT_TOOLS) not in sys.path:
        sys.path.insert(0, str(REPORT_TOOLS))
    from charts import CHARTS

    text = read_text(SKILLS_DIR / "pitch" / "references" / "outline-template.yaml")
    for chart in CHARTS:
        assert chart.name in text, chart.name
    for field in ("kind:", "title:", "subtitle:", "bullets:", "chart:", "sources:", "notes:", "speaker:", "minutes:"):
        assert field in text, field
