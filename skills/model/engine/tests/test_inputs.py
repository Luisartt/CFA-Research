from __future__ import annotations

import copy
from pathlib import Path

import pytest

from conftest import DRIVERS, HISTORY, PROFILE, SEGMENTS, VALUATION, YEARS, write_project
from rcmodel.inputs import InputError, load_inputs


def _messages(project: Path) -> list[str]:
    with pytest.raises(InputError) as caught:
        load_inputs(project)
    return caught.value.messages


def test_loads_the_fixture(project: Path) -> None:
    inputs = load_inputs(project)
    assert inputs.hist_years == YEARS
    assert inputs.fcst_years == (2026, 2027, 2028, 2029, 2030)
    assert inputs.history["revenue"][2025].value == 13400
    assert inputs.history["revenue"][2025].source_doc == "Annual report 2025"
    assert inputs.drivers["gross_margin"].values == (0.41,) * 5
    assert inputs.valuation is not None
    assert len(inputs.valuation.peers) == 3
    assert inputs.warnings == ()


def test_missing_required_line_is_reported(tmp_path: Path) -> None:
    history = {k: v for k, v in HISTORY.items() if k != "cash"}
    messages = _messages(write_project(tmp_path, history=history))
    assert any("'cash'" in m for m in messages)


def test_unknown_line_item_and_bad_tag(tmp_path: Path) -> None:
    write_project(tmp_path)
    with (tmp_path / "data" / "financials.csv").open("a", encoding="utf-8") as handle:
        handle.write("ebitdaa,2025,1,sourced,AR,1,\n")
        handle.write("capex,2019,1,made_up,AR,1,\n")
    messages = _messages(tmp_path)
    assert any("unknown line_item 'ebitdaa'" in m for m in messages)
    assert any("tag 'made_up'" in m for m in messages)


def test_unverified_tag_warns(tmp_path: Path) -> None:
    inputs = load_inputs(write_project(tmp_path, unverified=("capex",)))
    assert any("capex 2025" in w and "unverified" in w for w in inputs.warnings)


def test_too_few_years(tmp_path: Path) -> None:
    history = {k: v[:2] for k, v in HISTORY.items()}
    messages = _messages(write_project(tmp_path, history=history, years=YEARS[:2]))
    assert any("at least 3 years" in m for m in messages)


def test_driver_length_mismatch(tmp_path: Path) -> None:
    drivers = copy.deepcopy(DRIVERS)
    drivers["drivers"]["gross_margin"]["values"] = [0.4, 0.4]
    messages = _messages(write_project(tmp_path, drivers=drivers))
    assert any("'gross_margin' needs exactly 5 numeric values" in m for m in messages)


def test_unknown_driver(tmp_path: Path) -> None:
    drivers = copy.deepcopy(DRIVERS)
    drivers["drivers"]["ebitda_margin"] = {"values": [0.2] * 5}
    messages = _messages(write_project(tmp_path, drivers=drivers))
    assert any("unknown driver 'ebitda_margin'" in m for m in messages)


def test_missing_drivers_file_uses_defaults(tmp_path: Path) -> None:
    inputs = load_inputs(write_project(tmp_path, drivers=None))
    assert inputs.drivers == {}
    assert inputs.fcst_years == (2026, 2027, 2028, 2029, 2030)
    assert any("drivers.yaml not found" in w for w in inputs.warnings)


def test_missing_driver_warns_with_its_default(tmp_path: Path) -> None:
    drivers = copy.deepcopy(DRIVERS)
    del drivers["drivers"]["gross_margin"]
    del drivers["drivers"]["net_new_debt"]
    inputs = load_inputs(write_project(tmp_path, drivers=drivers))
    assert any("'gross_margin'" in w and "last actual" in w for w in inputs.warnings)
    assert any("'net_new_debt'" in w and "zero" in w for w in inputs.warnings)


def test_profile_with_placeholders_rejected(tmp_path: Path) -> None:
    profile = copy.deepcopy(PROFILE)
    profile["company"]["ticker"] = "{{TICKER}}"
    messages = _messages(write_project(tmp_path, profile=profile))
    assert any("init-skills" in m for m in messages)


def test_valuation_is_optional(tmp_path: Path) -> None:
    assert load_inputs(write_project(tmp_path, valuation=None)).valuation is None


def test_valuation_bad_number(tmp_path: Path) -> None:
    valuation = copy.deepcopy(VALUATION)
    valuation["wacc"]["risk_free"] = "high"
    messages = _messages(write_project(tmp_path, valuation=valuation))
    assert any("wacc.risk_free must be a number" in m for m in messages)


def test_valuation_rejects_infinite_numbers(tmp_path: Path) -> None:
    valuation = copy.deepcopy(VALUATION)
    valuation["wacc"]["risk_free"] = float("inf")
    messages = _messages(write_project(tmp_path, valuation=valuation))
    assert any("wacc.risk_free must be a number" in m for m in messages)


def test_segments_need_history(tmp_path: Path) -> None:
    drivers = copy.deepcopy(DRIVERS)
    drivers["revenue_segments"] = [{"key": "mx", "label": "Mexico"}]
    messages = _messages(write_project(tmp_path, drivers=drivers))
    assert any("seg_mx" in m for m in messages)


def test_segments_must_add_up_to_revenue(tmp_path: Path) -> None:
    drivers = copy.deepcopy(DRIVERS)
    drivers["revenue_segments"] = [{"key": "mx", "label": "Mexico"}, {"key": "us", "label": "United States"}]
    segments = {**SEGMENTS, "seg_us": (4000, 4300, 4600, 5000, 5400)}
    messages = _messages(write_project(tmp_path, history={**HISTORY, **segments}, drivers=drivers))
    assert any("2023" in m and "seg_eliminations" in m for m in messages)


def test_segments_within_rounding_are_accepted(tmp_path: Path) -> None:
    drivers = copy.deepcopy(DRIVERS)
    drivers["revenue_segments"] = [{"key": "mx", "label": "Mexico"}, {"key": "us", "label": "United States"}]
    segments = {**SEGMENTS, "seg_us": (4000, 4300, 4700.4, 5000, 5400)}
    inputs = load_inputs(write_project(tmp_path, history={**HISTORY, **segments}, drivers=drivers))
    assert len(inputs.segments) == 2


def test_cogs_must_be_positive(tmp_path: Path) -> None:
    history = {**HISTORY, "cogs": (6000, 6450, 0, 7400, 7900)}
    messages = _messages(write_project(tmp_path, history=history))
    assert any("cogs must be positive in every year" in m and "financials skill" in m for m in messages)


def test_missing_financials_file(tmp_path: Path) -> None:
    write_project(tmp_path)
    (tmp_path / "data" / "financials.csv").unlink()
    messages = _messages(tmp_path)
    assert any("financials skill" in m for m in messages)


def test_non_utf8_financials_csv_reports_input_error(tmp_path: Path) -> None:
    project = write_project(tmp_path)
    path = project / "data" / "financials.csv"
    data = path.read_bytes()
    data = data.replace(b"Annual report 2025", b"Annual report \x93", 1)
    path.write_bytes(data)
    messages = _messages(project)
    assert any("UTF-8" in m for m in messages)


def test_non_utf8_yaml_file_reports_input_error(tmp_path: Path) -> None:
    project = write_project(tmp_path)
    path = project / "company-profile.yaml"
    data = path.read_bytes()
    data = data.replace(b"Acme Alimentos", b"Acme \x93Alimentos", 1)
    path.write_bytes(data)
    messages = _messages(project)
    assert any("UTF-8" in m for m in messages)


def test_financials_row_errors_name_the_file(tmp_path: Path) -> None:
    write_project(tmp_path)
    with (tmp_path / "data" / "financials.csv").open("a", encoding="utf-8") as handle:
        handle.write("ebitdaa,2025,1,sourced,AR,1,\n")
    messages = _messages(tmp_path)
    assert any("financials.csv row " in m and "unknown line_item 'ebitdaa'" in m for m in messages)


def test_required_line_error_names_the_file(tmp_path: Path) -> None:
    history = {k: v for k, v in HISTORY.items() if k != "cash"}
    messages = _messages(write_project(tmp_path, history=history))
    assert any(m.startswith("financials.csv: required line 'cash'") for m in messages)


def test_profile_and_valuation_errors_reported_together(tmp_path: Path) -> None:
    profile = copy.deepcopy(PROFILE)
    profile["company"]["ticker"] = "{{TICKER}}"
    valuation = copy.deepcopy(VALUATION)
    valuation["wacc"]["risk_free"] = "high"
    messages = _messages(write_project(tmp_path, profile=profile, valuation=valuation))
    assert any("init-skills" in m for m in messages)
    assert any("wacc.risk_free must be a number" in m for m in messages)
