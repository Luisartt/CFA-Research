from __future__ import annotations

import copy
from pathlib import Path

import matplotlib.image as mpimg
import pytest

from report_fixtures import RISKS, report_project, write_report_project  # noqa: F401
from charts import CHARTS, ChartError, load_risks, main

EXPECTED = {"revenue-margin", "free-cash-flow", "football-field", "sensitivity", "risk-matrix"}


def test_all_charts_are_drawn(report_project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--project", str(report_project)]) == 0
    written = {p.stem for p in (report_project / "report" / "charts").glob("*.png")}
    assert written == EXPECTED
    out = capsys.readouterr().out
    assert out.isascii() and "[ok] report/charts/football-field.png" in out


def test_chart_sizes_fit_the_page(report_project: Path) -> None:
    main(["--project", str(report_project)])
    for name in EXPECTED:
        height, width = mpimg.imread(report_project / "report" / "charts" / f"{name}.png").shape[:2]
        assert 500 <= width <= 1400, (name, width)
        assert height < width, name


def test_registry_names_match_files() -> None:
    assert {chart.name for chart in CHARTS} == EXPECTED


def test_missing_summary_still_draws_risks(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    project = write_report_project(tmp_path, summary=False)
    assert main(["--project", str(project)]) == 0
    written = {p.stem for p in (project / "report" / "charts").glob("*.png")}
    assert written == {"risk-matrix"}
    assert "[skip] revenue-margin" in capsys.readouterr().out


def test_nothing_to_draw_exits_2(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    project = write_report_project(tmp_path, summary=False, risks=None)
    assert main(["--project", str(project)]) == 2
    assert "model-summary.json" in capsys.readouterr().out


def test_invalid_risk_scores_are_rejected(tmp_path: Path) -> None:
    risks = copy.deepcopy(RISKS)
    risks["risks"][0]["probability"] = 7
    project = write_report_project(tmp_path, risks=risks)
    with pytest.raises(ChartError, match="R1"):
        load_risks(project / "research" / "risks.yaml")


def test_summary_without_valuation_skips_valuation_charts(report_project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    import json

    path = report_project / "model" / "model-summary.json"
    summary = json.loads(path.read_text(encoding="utf-8"))
    summary["football"], summary["sensitivity"], summary["valuation"] = [], None, {}
    path.write_text(json.dumps(summary), encoding="utf-8")
    assert main(["--project", str(report_project)]) == 0
    out = capsys.readouterr().out
    assert "[skip] football-field" in out and "[skip] sensitivity" in out
