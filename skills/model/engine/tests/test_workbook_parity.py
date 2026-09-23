"""Recalculate the written workbook with an Excel engine and compare every formula with Python."""

from __future__ import annotations

import math
import re
from pathlib import Path

import pytest

from rcmodel.engine import FormulaCell
from rcmodel.placement import PERIOD_COL0
from test_writer import build_file

formulas = pytest.importorskip("formulas")

KEY = re.compile(r"^'\[(?P<book>[^\]]+)\](?P<sheet>[^']+)'!(?P<cell>[A-Z]+[0-9]+)$")


def _to_float(result: object) -> float:
    try:
        import numpy as np

        return float(np.asarray(result, dtype=object).ravel()[0])
    except (TypeError, ValueError):
        return math.nan


def test_excel_values_match_python(project: Path) -> None:
    from openpyxl.utils import get_column_letter

    path, model = build_file(project)
    solution = formulas.ExcelModel().loads(str(path)).finish().calculate()
    excel: dict[tuple[str, str], float] = {}
    for name, ranges in solution.items():
        match = KEY.match(str(name).upper())
        if match:
            excel[(match["sheet"], match["cell"])] = _to_float(getattr(ranges, "value", ranges))
    compared = 0
    for line, row in model.placed.lines:
        periods = [None] if line.is_scalar else list(range(model.n))
        for period in periods:
            if not isinstance(model.cell(line.key, period), FormulaCell):
                continue
            col = line.col if period is None else PERIOD_COL0 + period
            key = (line.sheet.upper(), f"{get_column_letter(col)}{row}")
            python_value = model.value(line.key, period)
            if key not in excel or not math.isfinite(python_value):
                continue
            assert excel[key] == pytest.approx(python_value, rel=1e-9, abs=1e-6), f"{line.key} {period}"
            compared += 1
    assert compared > 300
