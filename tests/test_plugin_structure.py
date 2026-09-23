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
