from __future__ import annotations

import copy
from pathlib import Path

import matplotlib.image as mpimg
import pytest

from report_fixtures import RISKS, load_fixture_summary, report_project, write_report_project  # noqa: F401

import logging
from typing import Any, cast

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
from matplotlib.ticker import PercentFormatter, StrMethodFormatter

import charts
from charts import CHARTS, NAVY, PREFERRED_FONTS, ChartError, load_risks, main

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


def _drawn(monkeypatch: pytest.MonkeyPatch, draw: Any, summary: dict[str, Any],
           risks: list[dict[str, Any]] | None = None) -> Figure:
    """Run one chart function and hand back its figure instead of saving it."""
    captured: list[Figure] = []
    monkeypatch.setattr(charts, "_save", lambda fig, path, note="": captured.append(fig))
    draw(summary, risks or [], Path("unused.png"))
    assert len(captured) == 1
    return captured[0]


def test_font_family_prefers_arial_and_keeps_only_installed_fonts() -> None:
    assert PREFERRED_FONTS == ("Arial", "Liberation Sans", "DejaVu Sans")
    installed = {entry.name for entry in matplotlib.font_manager.fontManager.ttflist}
    assert matplotlib.rcParams["font.family"] == [f for f in PREFERRED_FONTS if f in installed]
    assert "DejaVu Sans" in matplotlib.rcParams["font.family"]  # bundled with matplotlib


def test_drawing_logs_no_missing_font_warnings(report_project: Path, caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.WARNING, logger="matplotlib.font_manager"):
        assert main(["--project", str(report_project)]) == 0
    assert not [r for r in caplog.records if "findfont" in r.getMessage()]


def test_football_field_price_label_sits_above_the_bars(monkeypatch: pytest.MonkeyPatch) -> None:
    summary = load_fixture_summary()
    fig = _drawn(monkeypatch, charts.football_field, summary)
    ax = fig.axes[0]
    rows = len(summary["football"])
    assert ax.get_ylim() == pytest.approx((rows - 0.5, -0.9))
    label = cast(Any, next(t for t in ax.texts if t.get_text().startswith("Price")))
    assert label.get_text() == "Price 25.00"
    assert label.get_position() == pytest.approx((25.0, -0.6))
    assert label.get_ha() == "center" and label.get_va() == "bottom"
    plt.close(fig)


def test_football_field_sorts_low_and_high(monkeypatch: pytest.MonkeyPatch) -> None:
    summary = load_fixture_summary()
    summary["football"] = [{"method": "Swapped range", "low": 30.0, "high": 20.0}]
    fig = _drawn(monkeypatch, charts.football_field, summary)
    bar = cast(Rectangle, fig.axes[0].patches[0])
    assert bar.get_x() == pytest.approx(20.0) and bar.get_width() == pytest.approx(10.0)
    plt.close(fig)


def test_football_field_draws_a_target_line(monkeypatch: pytest.MonkeyPatch) -> None:
    summary = load_fixture_summary()
    summary["football"].append({"method": "12-month Target price", "low": 31.0, "high": 31.0})
    fig = _drawn(monkeypatch, charts.football_field, summary)
    ax = fig.axes[0]
    target_lines = [ln for ln in ax.get_lines() if list(cast(Any, ln.get_xdata())) == [31.0, 31.0]]
    assert len(target_lines) == 1
    assert to_hex(target_lines[0].get_color()).upper() == NAVY and target_lines[0].get_linestyle() == "--"
    assert any(t.get_text() == "Target 31.00" for t in ax.texts)
    plt.close(fig)


def test_revenue_margin_axes_formats(monkeypatch: pytest.MonkeyPatch) -> None:
    summary = load_fixture_summary()
    fig = _drawn(monkeypatch, charts.revenue_margin, summary)
    bars, margin = fig.axes
    top = max(v for v in summary["ratios"]["r_ebitda_margin"].values()) * 100 * 1.3
    assert margin.get_ylim() == pytest.approx((0, top))
    formatter = margin.yaxis.get_major_formatter()
    assert isinstance(formatter, PercentFormatter) and formatter(19.8) == "20%"
    assert isinstance(bars.yaxis.get_major_formatter(), StrMethodFormatter)
    assert bars.yaxis.get_major_formatter()(12345.0) == "12,345"
    plt.close(fig)


def test_revenue_margin_without_margins_still_draws(monkeypatch: pytest.MonkeyPatch) -> None:
    summary = load_fixture_summary()
    summary["ratios"] = {}
    fig = _drawn(monkeypatch, charts.revenue_margin, summary)
    plt.close(fig)


def test_free_cash_flow_uses_thousands_separators(monkeypatch: pytest.MonkeyPatch) -> None:
    fig = _drawn(monkeypatch, charts.free_cash_flow, load_fixture_summary())
    assert fig.axes[0].yaxis.get_major_formatter()(1234567.0) == "1,234,567"
    plt.close(fig)


def test_risk_matrix_groups_risks_in_the_same_cell(monkeypatch: pytest.MonkeyPatch) -> None:
    risks = copy.deepcopy(RISKS["risks"]) + [{"id": "R4", "probability": 3, "impact": 4}]
    fig = _drawn(monkeypatch, charts.risk_matrix, {}, risks)
    ax = fig.axes[0]
    points = [tuple(float(v) for v in p) for c in ax.collections for p in cast(Any, c.get_offsets())]
    assert sorted(points) == [(2, 3), (3, 4), (4, 2)]
    labels = {t.get_text() for t in ax.texts}
    assert labels == {"R1, R4", "R2", "R3"}
    plt.close(fig)


def test_sensitivity_uses_white_text_on_dark_cells_and_outlines_the_base_case(
        monkeypatch: pytest.MonkeyPatch) -> None:
    summary = load_fixture_summary()
    summary["sensitivity"]["values"][4][4] = None
    fig = _drawn(monkeypatch, charts.sensitivity, summary)
    ax = fig.axes[0]
    colors = {t.get_text(): to_hex(t.get_color()) for t in ax.texts}
    assert colors["21.3"] == "#ffffff"  # highest value, darkest cell
    assert colors["9.7"] == "#000000"   # lowest value, lightest cell
    assert colors["13.9"] == "#000000"  # above the median but still a light cell
    assert colors["n.m."] == "#000000"
    outlines = [p for p in ax.patches if isinstance(p, Rectangle) and not p.get_fill()]
    assert len(outlines) == 1 and outlines[0].get_xy() == pytest.approx((1.5, 1.5))
    plt.close(fig)


@pytest.mark.parametrize("entry, message", [
    ({"probability": 3, "impact": 4}, "id"),
    ({"id": "", "probability": 3, "impact": 4}, "id"),
    ({"id": 7, "probability": 3, "impact": 4}, "id"),
    ({"id": "R1", "probability": 3, "impact": 4}, "R1 is used twice"),
])
def test_risk_ids_must_be_unique_text(tmp_path: Path, entry: dict[str, Any], message: str) -> None:
    risks = copy.deepcopy(RISKS)
    risks["risks"].append(entry)
    project = write_report_project(tmp_path, risks=risks)
    with pytest.raises(ChartError, match=message):
        load_risks(project / "research" / "risks.yaml")


def test_bad_risk_id_exits_2_without_traceback(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    risks = copy.deepcopy(RISKS)
    risks["risks"].append({"probability": 3, "impact": 4})
    project = write_report_project(tmp_path, risks=risks)
    assert main(["--project", str(project)]) == 2
    out = capsys.readouterr().out
    assert out.isascii() and "id" in out
