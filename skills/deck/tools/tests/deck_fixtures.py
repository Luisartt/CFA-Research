"""Fixtures for the deck tools (a plain module, not conftest.py: two conftest modules collide).

Import this module FIRST in test files: it puts skills/deck/tools on sys.path.
"""

from __future__ import annotations

import json
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import pytest
import yaml

TOOLS_DIR = Path(__file__).resolve().parent.parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from pptx import Presentation  # noqa: E402

OUTLINE: dict[str, Any] = {
    "deck": {"title": "Acme Alimentos (BMV: ACME) - BUY, target MXN 31.0", "language": "en", "minutes": 10},
    "slides": [
        {"kind": "title", "title": "Acme Alimentos (BMV: ACME)", "subtitle": "BUY - target MXN 31.0 (+24%)",
         "notes": "Open with the recommendation.", "speaker": "Ana", "minutes": 0.5},
        {"kind": "content", "title": "Investment thesis", "bullets": ["Volume recovery", "Margin expansion"],
         "sources": "Company filings; team model", "notes": "Three pillars.", "speaker": "Ana", "minutes": 1.5},
        {"kind": "content", "title": "Revenue and margins", "bullets": ["Revenue grows 6% a year", "EBITDA margin 19-20%"],
         "chart": "revenue-margin", "sources": "Team model", "notes": "Walk the chart.", "speaker": "Luis",
         "minutes": 1.5},
        {"kind": "chart", "title": "Valuation summary", "chart": "football-field",
         "sources": "Team model; market data (2026-10-14)", "notes": "DCF vs comps.", "speaker": "Luis",
         "minutes": 1.5},
        {"kind": "section", "title": "Risks and ESG", "sources": "Team analysis", "notes": "", "speaker": "Eva",
         "minutes": 0.2},
    ],
}

SUMMARY: dict[str, Any] = {"valuation": {"wacc": 0.1245, "price_gordon": 13.43, "upside_gordon": 0.24}}
HEADER: dict[str, Any] = {"ticker": "ACME", "target_price": 31.0, "price": 25.0, "currency": "MXN"}


def _chart(path: Path, wide: bool) -> None:
    fig, ax = plt.subplots(figsize=(6.3, 3.0) if wide else (3.2, 2.3))
    ax.plot([1, 2, 3], [1, 4, 9])
    fig.savefig(path, dpi=100)
    plt.close(fig)


def write_template(path: Path, example_slides: int = 1) -> Path:
    prs = Presentation()
    for _ in range(example_slides):
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        slide.shapes.title.text = "Example slide from the template"
    path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(path))
    return path


def write_deck_project(root: Path, outline: Mapping[str, Any] | None = OUTLINE, template: bool = True,
                       charts: bool = True) -> Path:
    for folder in ("pitch", "report/charts", "model", "report"):
        (root / folder).mkdir(parents=True, exist_ok=True)
    (root / "company-profile.yaml").write_text(
        yaml.safe_dump({"company": {"name": "Acme Alimentos", "ticker": "ACME"}}), encoding="utf-8")
    if outline is not None:
        (root / "pitch" / "outline.yaml").write_text(yaml.safe_dump(dict(outline), sort_keys=False), encoding="utf-8")
    if template:
        write_template(root / "pitch" / "template.pptx")
    if charts:
        _chart(root / "report" / "charts" / "revenue-margin.png", wide=False)
        _chart(root / "report" / "charts" / "football-field.png", wide=True)
    (root / "model" / "model-summary.json").write_text(json.dumps(SUMMARY), encoding="utf-8")
    (root / "report" / "header.yaml").write_text(yaml.safe_dump(HEADER), encoding="utf-8")
    return root


@pytest.fixture
def deck_project(tmp_path: Path) -> Path:
    return write_deck_project(tmp_path)
