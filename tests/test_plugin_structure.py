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
    positions: list[int] = []
    for section in REQUIRED_SECTIONS:
        match = re.search(rf"^{re.escape(section)}[ \t]*$", text, re.MULTILINE)
        positions.append(match.start() if match else -1)
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
