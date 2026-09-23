from __future__ import annotations

import copy
import zipfile
from datetime import date
from pathlib import Path
from typing import Any
from xml.etree import ElementTree

import pytest
from openpyxl import load_workbook

from conftest import PROFILE, write_project
from rcmodel import styles
from rcmodel.assemble import assemble
from rcmodel.checks import Check, build_checks, evaluate_checks, parity_checks
from rcmodel.engine import Model
from rcmodel.inputs import load_inputs
from rcmodel.placement import FIRST_ROW
from rcmodel.spec import Fmt
from rcmodel.writer import BuildInfo, write_workbook


def build_all(project: Path) -> tuple[Path, Model, list[Check]]:
    model, football = assemble(load_inputs(project))
    checks = [*build_checks(model.inputs), *parity_checks(model)]
    path = project / "model" / "TEST.xlsx"
    write_workbook(path, model, checks, evaluate_checks(model, checks), football,
                   BuildInfo(1, path.name, date(2026, 9, 23)))
    return path, model, checks


def build_file(project: Path) -> tuple[Path, Model]:
    path, model, _ = build_all(project)
    return path, model


def test_sheets_in_order(project: Path) -> None:
    path, _ = build_file(project)
    assert load_workbook(path).sheetnames == [
        "Cover", "Drivers", "IS", "BS", "CF", "Schedules", "Ratios",
        "WACC", "DCF", "Comps", "Sensitivity", "Football", "Checks",
    ]


def test_history_is_values_forecast_is_formulas(project: Path) -> None:
    path, model = build_file(project)
    ws = load_workbook(path)["IS"]
    row = model.row_of("revenue")
    assert ws.cell(row, 3 + model.h - 1).value == 13400
    forecast = ws.cell(row, 3 + model.h).value
    assert isinstance(forecast, str) and forecast.startswith("=") and "Drivers!" in forecast
    assert "sourced" in ws.cell(row, 3).comment.text


def test_inputs_are_blue_on_yellow(project: Path) -> None:
    path, model = build_file(project)
    cell = load_workbook(path)["Drivers"].cell(model.row_of("gross_margin"), 3 + model.h)
    assert cell.value == 0.41
    assert cell.font.color.rgb == "FF0000FF"
    assert cell.fill.fgColor.rgb == "FFFFF2CC"


def test_links_to_other_sheets_are_green(project: Path) -> None:
    path, model = build_file(project)
    cell = load_workbook(path)["BS"].cell(model.row_of("cash"), 3 + model.h)
    assert str(cell.value).startswith("=CF!")
    assert cell.font.color.rgb == "FF008000"


def test_checks_and_cover_formulas(project: Path) -> None:
    path, _ = build_file(project)
    workbook = load_workbook(path)
    check_formulas = [c.value for row in workbook["Checks"].iter_rows() for c in row
                      if isinstance(c.value, str) and c.value.startswith("=IF(")]
    assert check_formulas
    cover_text = [c.value for row in workbook["Cover"].iter_rows() for c in row if isinstance(c.value, str)]
    assert any("COUNTIF(Checks!" in text for text in cover_text)
    assert "ALL CHECKS OK" in cover_text or "OK WITH WARNINGS" in cover_text


def test_workbook_recalculates_on_open(project: Path) -> None:
    path, _ = build_file(project)
    assert load_workbook(path).calculation.fullCalcOnLoad is True


def test_football_chart_is_embedded(project: Path) -> None:
    path, _ = build_file(project)
    with zipfile.ZipFile(path) as archive:
        assert any(name.startswith("xl/charts/chart") for name in archive.namelist())


def test_no_valuation_sheets_without_valuation(tmp_path: Path) -> None:
    path, _ = build_file(write_project(tmp_path, valuation=None))
    assert load_workbook(path).sheetnames == ["Cover", "Drivers", "IS", "BS", "CF", "Schedules", "Ratios", "Checks"]


CHART_NS = "{http://schemas.openxmlformats.org/drawingml/2006/chart}"


def _chart_xml(path: Path) -> ElementTree.Element:
    with zipfile.ZipFile(path) as archive:
        name = next(n for n in archive.namelist() if n.startswith("xl/charts/chart"))
        return ElementTree.fromstring(archive.read(name))


def _row_with(ws: Any, text: str) -> int:
    return next(row for row in range(1, ws.max_row + 1) if str(ws.cell(row, 2).value or "").startswith(text))


def test_football_chart_axes_are_shown_top_down(project: Path) -> None:
    path, _ = build_file(project)
    root = _chart_xml(path)
    for axis in ("catAx", "valAx"):
        element = root.find(f".//{CHART_NS}{axis}")
        assert element is not None, axis
        delete = element.find(f"{CHART_NS}delete")
        assert delete is not None and delete.get("val") == "0", axis
    orientation = root.find(f".//{CHART_NS}catAx/{CHART_NS}scaling/{CHART_NS}orientation")
    assert orientation is not None and orientation.get("val") == "maxMin"


def test_parity_checks_show_the_python_value_next_to_the_result(project: Path) -> None:
    path, model = build_file(project)
    ws = load_workbook(path)["Checks"]
    header = _row_with(ws, "Single-value checks")
    assert ws.cell(header, 3).value == "Result"
    assert ws.cell(header, 4).value == "Python value at build"
    row = _row_with(ws, "Excel matches the Python value at build: Value per share today - Gordon")
    label = ws.cell(row, 2).value
    assert label.endswith("(stale if inputs are edited in Excel - rebuild)")
    assert ws.cell(row, 4).value == pytest.approx(model.value("price_gordon", None), rel=1e-15)  # 16 digits written
    assert ws.cell(row, 4).number_format == Fmt.PRICE.value
    price_cell = model.address("price_gordon", None, "Checks")
    formula = ws.cell(row, 3).value
    assert formula.startswith(f'=IF(ABS({price_cell}-D{row})<=') and formula.endswith(',"OK","WARN")')


def test_cover_facts_status_colours_and_notes(project: Path) -> None:
    path, _ = build_file(project)
    ws = load_workbook(path)["Cover"]
    facts = {ws.cell(r, 2).value: ws.cell(r, 3).value for r in range(1, ws.max_row + 1)}
    assert facts["Version"] == 1
    assert facts["Accounting framework"] == "IFRS"
    texts = [ws.cell(r, 3).value for r in range(1, ws.max_row + 1)]
    assert not any("stub-period" in str(t) for t in texts)
    assert ("Value per share is at the last fiscal year-end rolled forward to today at the cost of equity; "
            "the 12-month target rolls it one more year and subtracts next year's dividend.") in texts
    fills = {}
    for rules in ws.conditional_formatting:
        for rule in rules.rules:
            fills[rule.formula[0].split("=", 1)[1]] = rule.dxf.fill.fgColor.rgb
    assert fills == {'"CHECKS FAILING"': styles.ERROR_FILL.fgColor.rgb,
                     '"OK WITH WARNINGS"': styles.WARN_FILL.fgColor.rgb,
                     '"ALL CHECKS OK"': "FFC6EFCE"}


def test_framework_codes_read_as_names(tmp_path: Path) -> None:
    profile = copy.deepcopy(PROFILE)
    profile["accounting"]["framework"] = "us_gaap"
    path, _ = build_file(write_project(tmp_path, profile=profile))
    ws = load_workbook(path)["Cover"]
    assert "US GAAP" in [ws.cell(r, 3).value for r in range(1, ws.max_row + 1)]


def test_every_sheet_prints_landscape_one_page_wide(project: Path) -> None:
    path, _ = build_file(project)
    for ws in load_workbook(path).worksheets:
        assert ws.page_setup.orientation == "landscape", ws.title
        assert ws.page_setup.fitToWidth == 1, ws.title
        assert ws.page_setup.fitToHeight == 0, ws.title
        assert ws.sheet_properties.pageSetUpPr.fitToPage is True, ws.title


def test_labels_and_column_titles_wrap(project: Path) -> None:
    path, model = build_file(project)
    workbook = load_workbook(path)
    label = workbook["DCF"].cell(model.row_of("market_ev"), 2)
    assert label.alignment.wrap_text is True and label.alignment.vertical == "top"
    check_label = workbook["Checks"].cell(FIRST_ROW + 1, 2)
    assert check_label.alignment.wrap_text is True
    comps = workbook["Comps"]
    header = _row_with(comps, "Peer multiples")
    assert comps.cell(header, 5).value == "Net debt incl. leases + NCI"
    assert comps.cell(header, 5).alignment.wrap_text is True


def test_single_value_blocks_on_dcf_have_a_value_title(project: Path) -> None:
    path, _ = build_file(project)
    ws = load_workbook(path)["DCF"]
    for title in ("Discounting convention", "Terminal value and enterprise value", "Equity value per share",
                  "Cross-checks", "Reverse DCF"):
        assert ws.cell(_row_with(ws, title), 3).value == "Value", title
    assert ws.cell(_row_with(ws, "Free cash flow to the firm"), 3).value is None


def test_number_formats_and_text_notes(project: Path) -> None:
    path, model = build_file(project)
    workbook = load_workbook(path)
    assert workbook["DCF"].cell(model.row_of("dcf_df"), 3 + model.h).number_format == "0.000"
    drivers = workbook["Drivers"]
    row = model.row_of("gross_margin")
    assert drivers.cell(row, 3 + model.n + 2).value == "Pillar 1"
    assert drivers.cell(model.row_of("min_cash"), 3).value is None
