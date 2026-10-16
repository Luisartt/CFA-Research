from __future__ import annotations

from pathlib import Path

import pytest

from rcmodel.engine import BlankCell, FormulaCell, InputCell, Model, ModelError, ObservedCell
from rcmodel.expr import At, Expr, Ref, Rng, fn
from rcmodel.inputs import load_inputs
from rcmodel.placement import FIRST_ROW, PERIOD_COL0, LayoutError, place
from rcmodel.spec import OBSERVED, Header, Inputs, Line

N = 10  # periods in the fixture: 5 historical + 5 forecast


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


def test_cycle_error_names_the_keys_being_visited(project: Path) -> None:
    m = _tiny(project, [Line("x", "X", "IS", fcst=Ref("y")), Line("y", "Y", "IS", fcst=Ref("x"))])
    with pytest.raises(ModelError, match=r"x\[5\] -> y\[5\] -> x\[5\]"):
        m.evaluate_all()


def test_min_over_a_range_with_a_blank_cell_is_refused(project: Path) -> None:
    m = _tiny(project, [Line("low", "Lowest growth", "DCF", scalar=fn("MIN", Rng("g", 0, 2)))])
    with pytest.raises(ModelError, match="MIN would read a blank cell of 'g'"):
        m.evaluate_all()


def test_min_with_a_blank_single_reference_is_refused(project: Path) -> None:
    m = _tiny(project, [Line("low", "Lowest", "IS", hist=fn("MIN", Ref("g"), 1.0))])
    with pytest.raises(ModelError, match="MIN would read a blank cell of 'g'"):
        m.evaluate_all()


def test_max_with_a_blank_fixed_period_is_refused(project: Path) -> None:
    m = _tiny(project, [Line("high", "Highest", "DCF", scalar=fn("MAX", At("g", 0), 1.0))])
    with pytest.raises(ModelError, match="MAX would read a blank cell of 'g'"):
        m.evaluate_all()


def test_sum_reads_a_blank_cell_as_zero(project: Path) -> None:
    m = _tiny(project, [Line("total", "Total growth", "DCF", scalar=fn("SUM", Rng("g", 0, 1)))])
    m.evaluate_all()
    assert m.value("total", None) == pytest.approx(10800 / 10000 - 1)


def test_deep_chains_evaluate_period_by_period(project: Path) -> None:
    inputs = load_inputs(project)
    count = 60
    keys = [f"line_{i}" for i in range(count)]
    chain: list[Line] = []
    for i, key in enumerate(keys):
        # line_0 closes the ring through the last line one year back, so a depth-first walk
        # from the last line's last year would visit every line in every year before unwinding.
        prev: Expr = Ref(keys[i - 1]) if i else Ref(keys[-1], 1)
        chain.append(Line(key, key, "IS", hist=Ref("revenue"), fcst=prev + Ref(key, 1)))
    layout: list[Line | Header] = [
        Line("last", "Last", "DCF", scalar=At(keys[-1], inputs.n - 1)),
        *reversed(chain),
        Line("revenue", "Revenue", "IS", hist=OBSERVED, fcst=Ref("revenue", 1)),
    ]
    m = Model(layout, inputs)
    m.evaluate_all()
    assert m.value("line_0", inputs.h) == pytest.approx(13400 + 13400)
    assert m.value("last", None) > 0


def test_evaluation_errors_name_the_line_being_evaluated(project: Path) -> None:
    m = _tiny(project, [Line("bad", "Bad", "IS", fcst=Ref("nope"))])
    with pytest.raises(ModelError, match=r"while evaluating 'bad'.*unknown line 'nope'") as info:
        m.evaluate_all()
    assert isinstance(info.value.__cause__, ModelError)


def test_forecast_inputs_must_cover_every_forecast_year(project: Path) -> None:
    inputs = load_inputs(project)
    with pytest.raises(ModelError, match="line 'g' has 3 forecast inputs; the model has 5 forecast years"):
        Model([Line("g", "Growth", "Drivers", fcst=Inputs((0.1, 0.1, 0.1)))], inputs)


def test_duplicate_keys_rejected() -> None:
    with pytest.raises(LayoutError):
        place([Line("a", "A", "IS"), Line("a", "A", "IS")], N)


def test_headers_leave_a_breathing_row() -> None:
    placed = place([Header("IS", "One"), Line("a", "A", "IS"), Header("IS", "Two"), Line("b", "B", "IS")], N)
    rows = {line.key: row for line, row in placed.lines}
    assert rows == {"a": FIRST_ROW + 1, "b": FIRST_ROW + 4}


def test_continuation_lines_share_a_row() -> None:
    placed = place([Line("a", "A", "Comps", scalar=1.0, col=3), Line("b", "", "Comps", scalar=2.0, col=4, new_row=False)], N)
    assert placed.placements["a"].row == placed.placements["b"].row
    assert placed.placements["b"].col == 4


def test_scalar_after_per_year_values_and_notes_fits() -> None:
    free = PERIOD_COL0 + N + 1
    placed = place([Line("a", "A", "IS", notes=("x",)), Line("b", "", "IS", scalar=1.0, col=free, new_row=False)], N)
    assert placed.placements["b"].col == free


def test_scalar_on_a_per_year_value_cell_rejected() -> None:
    with pytest.raises(LayoutError, match="'b'"):
        place([Line("a", "A", "IS"), Line("b", "", "IS", scalar=1.0, col=PERIOD_COL0 + 4, new_row=False)], N)


def test_scalar_on_a_per_year_note_cell_rejected() -> None:
    with pytest.raises(LayoutError, match="'b'"):
        place([Line("a", "A", "IS", notes=("x",)), Line("b", "", "IS", scalar=1.0, col=PERIOD_COL0 + N, new_row=False)], N)


def test_scalar_on_another_scalars_note_cell_rejected() -> None:
    layout = [Line("a", "A", "Comps", scalar=1.0, col=3, notes=("x", "y")), Line("b", "", "Comps", scalar=2.0, col=5, new_row=False)]
    with pytest.raises(LayoutError, match="'b'"):
        place(layout, N)


def test_note_on_another_scalars_value_cell_rejected() -> None:
    layout = [Line("a", "A", "Comps", scalar=1.0, col=4), Line("b", "", "Comps", scalar=2.0, col=3, new_row=False, notes=("x",))]
    with pytest.raises(LayoutError, match="'b'"):
        place(layout, N)


def test_scalar_in_the_label_columns_rejected() -> None:
    with pytest.raises(LayoutError, match="'a'"):
        place([Line("a", "A", "Comps", scalar=1.0, col=PERIOD_COL0 - 1)], N)


def test_continuing_a_header_row_rejected() -> None:
    with pytest.raises(LayoutError, match="'a'"):
        place([Header("Comps", "Peers", ((3, "Price"),)), Line("a", "", "Comps", scalar=1.0, col=5, new_row=False)], N)


def test_line_cannot_be_both_kinds() -> None:
    with pytest.raises(ValueError):
        Line("x", "X", "IS", scalar=1.0, fcst=Ref("y"))
