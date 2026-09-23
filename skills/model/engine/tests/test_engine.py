from __future__ import annotations

from pathlib import Path

import pytest

from rcmodel.engine import BlankCell, FormulaCell, InputCell, Model, ModelError, ObservedCell
from rcmodel.expr import At, Ref
from rcmodel.inputs import load_inputs
from rcmodel.placement import FIRST_ROW, LayoutError, place
from rcmodel.spec import OBSERVED, Header, Inputs, Line


def _tiny(project: Path, extra: list[Line] | None = None) -> Model:
    inputs = load_inputs(project)
    growth = tuple(0.1 for _ in inputs.fcst_years)
    layout: list[Line | Header] = [
        Header("IS", "Tiny"),
        Line("revenue", "Revenue", "IS", hist=OBSERVED, fcst=Ref("revenue", 1) * (1 + Ref("g"))),
        Line("g", "Growth", "Drivers", hist=Ref("revenue") / Ref("revenue", 1) - 1, fcst=Inputs(growth)),
        Line("peak", "Peak revenue", "DCF", scalar=At("revenue", inputs.n - 1)),
        *(extra or []),
    ]
    return Model(layout, inputs)


def test_values_follow_the_formulas(project: Path) -> None:
    m = _tiny(project)
    assert m.value("revenue", 4) == 13400
    assert m.value("revenue", 5) == pytest.approx(13400 * 1.1)
    assert m.value("peak", None) == pytest.approx(13400 * 1.1**5)


def test_cells_by_kind(project: Path) -> None:
    m = _tiny(project)
    observed = m.cell("revenue", 0)
    assert isinstance(observed, ObservedCell)
    assert "sourced" in observed.comment and "p.45" in observed.comment
    assert isinstance(m.cell("g", 5), InputCell)
    assert isinstance(m.cell("g", 0), BlankCell)  # needs revenue of the year before the first
    assert isinstance(m.cell("g", 1), FormulaCell)


def test_addresses(project: Path) -> None:
    m = _tiny(project)
    row = m.row_of("revenue")
    assert row == FIRST_ROW + 1
    assert m.address("revenue", 0, "IS") == f"C{row}"
    assert m.address("revenue", 5, "Drivers") == f"IS!H{row}"
    assert m.range_address("revenue", 5, 9, "DCF") == f"IS!H{row}:L{row}"
    assert m.address("peak", None, "DCF") == f"C{m.row_of('peak')}"


def test_formula_renders_with_addresses(project: Path) -> None:
    m = _tiny(project)
    cell = m.cell("revenue", 5)
    assert isinstance(cell, FormulaCell)
    assert cell.expr.render(m, 5, "IS") == f"G{m.row_of('revenue')}*(1+Drivers!H{m.row_of('g')})"


def test_unknown_reference(project: Path) -> None:
    m = _tiny(project, [Line("bad", "Bad", "IS", fcst=Ref("nope"))])
    with pytest.raises(ModelError, match="unknown line 'nope'"):
        m.evaluate_all()


def test_circular_reference(project: Path) -> None:
    m = _tiny(project, [Line("x", "X", "IS", fcst=Ref("y")), Line("y", "Y", "IS", fcst=Ref("x"))])
    with pytest.raises(ModelError, match="circular"):
        m.evaluate_all()


def test_single_value_formulas_must_use_at(project: Path) -> None:
    m = _tiny(project, [Line("oops", "Oops", "DCF", scalar=Ref("revenue"))])
    with pytest.raises(ModelError, match="At"):
        m.evaluate_all()


def test_duplicate_keys_rejected() -> None:
    with pytest.raises(LayoutError):
        place([Line("a", "A", "IS"), Line("a", "A", "IS")])


def test_headers_leave_a_breathing_row() -> None:
    placed = place([Header("IS", "One"), Line("a", "A", "IS"), Header("IS", "Two"), Line("b", "B", "IS")])
    rows = {line.key: row for line, row in placed.lines}
    assert rows == {"a": FIRST_ROW + 1, "b": FIRST_ROW + 4}


def test_continuation_lines_share_a_row() -> None:
    placed = place([Line("a", "A", "Comps", scalar=1.0, col=3), Line("b", "", "Comps", scalar=2.0, col=4, new_row=False)])
    assert placed.placements["a"].row == placed.placements["b"].row
    assert placed.placements["b"].col == 4


def test_line_cannot_be_both_kinds() -> None:
    with pytest.raises(ValueError):
        Line("x", "X", "IS", scalar=1.0, fcst=Ref("y"))
