"""Shared fixtures for the report tools: a project folder with a model summary, risks and sections."""

from __future__ import annotations

import json
import shutil
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import pytest
import yaml

TOOLS_DIR = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures"
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

RISKS: dict[str, Any] = {
    "risks": [
        {"id": "R1", "risk": "Wheat price spike", "category": "market", "pillar": "2",
         "probability": 3, "impact": 4, "mitigation": "Hedging 6-9 months", "priced_in": "partly"},
        {"id": "R2", "risk": "Peso depreciation", "category": "financial", "pillar": "1",
         "probability": 2, "impact": 3, "mitigation": "USD revenue from US unit", "priced_in": "yes"},
        {"id": "R3", "risk": "Front-of-pack labeling rules", "category": "regulatory", "pillar": "3",
         "probability": 4, "impact": 2, "mitigation": "Reformulation plan", "priced_in": "no"},
    ]
}

HEADER: dict[str, Any] = {
    "company": "Acme Alimentos",
    "exchange": "BMV",
    "ticker": "ACME",
    "sector": "Consumer Staples",
    "industry": "Packaged Foods",
    "recommendation": "BUY",
    "price": 25.0,
    "price_date": "2026-10-14",
    "currency": "MXN",
    "target_price": 31.0,
    "report_date": "2026-11-05",
}

SECTIONS: dict[str, str] = {
    "01-investment-summary.md": (
        "# Investment summary\n\n"
        "We rate Acme a **BUY** with a target of MXN 31.0 (Acme 2025, p. 12).\n\n"
        "- Pillar one: volume recovery\n- Pillar two: *margin* expansion\n\n"
        "![Revenue and EBITDA margin](../charts/revenue-margin.png)\n"
    ),
    "02-business-description.md": "# Business description\n\nAcme sells bread in Mexico and the US.\n",
    "05-valuation.md": (
        "# Valuation\n\n"
        "| Method | Value |\n|---|---|\n| DCF | 31.0 |\n| Comps | 29.5 |\n\n"
        "Our DCF gives 31 per share with a WACC of 12.5%.\n"
    ),
    "99-appendix.md": "# Appendix\n\nAI-use disclosure: we used an AI assistant to extract statements.\n",
}


def write_report_project(root: Path, summary: bool = True, risks: Mapping[str, Any] | None = RISKS,
                         header: Mapping[str, Any] | None = HEADER,
                         sections: Mapping[str, str] | None = SECTIONS) -> Path:
    for folder in ("model", "research", "report/sections", "report/charts"):
        (root / folder).mkdir(parents=True, exist_ok=True)
    if summary:
        shutil.copy(FIXTURES / "model-summary.json", root / "model" / "model-summary.json")
    if risks is not None:
        (root / "research" / "risks.yaml").write_text(yaml.safe_dump(dict(risks), sort_keys=False), encoding="utf-8")
    if header is not None:
        (root / "report" / "header.yaml").write_text(yaml.safe_dump(dict(header), sort_keys=False), encoding="utf-8")
    for name, text in (sections or {}).items():
        (root / "report" / "sections" / name).write_text(text, encoding="utf-8")
    return root


def load_fixture_summary() -> dict[str, Any]:
    data: dict[str, Any] = json.loads((FIXTURES / "model-summary.json").read_text(encoding="utf-8"))
    return data


@pytest.fixture
def report_project(tmp_path: Path) -> Path:
    return write_report_project(tmp_path)
