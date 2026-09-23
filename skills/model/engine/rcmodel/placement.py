"""Assign every line a sheet row (and a column for single values)."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from openpyxl.utils import get_column_letter

from .spec import Header, LayoutItem, Line

HEADER_ROW = 4
FIRST_ROW = 6
PERIOD_COL0 = 3


class LayoutError(Exception):
    """The model definition is inconsistent (duplicate keys, bad row flags, overlapping cells)."""


@dataclass(frozen=True)
class Placement:
    sheet: str
    row: int
    col: int | None  # None = one column per year, starting at PERIOD_COL0


@dataclass(frozen=True)
class Placed:
    placements: dict[str, Placement]
    headers: tuple[tuple[str, int, Header], ...]
    lines: tuple[tuple[Line, int], ...]


def place(layout: Sequence[LayoutItem], n_periods: int) -> Placed:
    """Rows go down each sheet in layout order; no two values or notes may share a cell.

    Per-year lines fill PERIOD_COL0 .. PERIOD_COL0 + n_periods - 1 and put their notes
    after that; single values fill `col` and put their notes after it. Labels (column B)
    are not tracked, and a header row belongs to its band as a whole.
    """
    if n_periods < 1:
        raise LayoutError(f"the model needs at least one period, got {n_periods}")
    next_row: dict[str, int] = {}
    last_header: dict[str, Header | None] = {}
    placements: dict[str, Placement] = {}
    headers: list[tuple[str, int, Header]] = []
    lines: list[tuple[Line, int]] = []
    owners: dict[tuple[str, int, int], str] = {}
    for item in layout:
        row = next_row.get(item.sheet, FIRST_ROW)
        if isinstance(item, Header):
            if row > FIRST_ROW:
                row += 1
            headers.append((item.sheet, row, item))
            next_row[item.sheet] = row + 1
            last_header[item.sheet] = item
            continue
        if item.key in placements:
            raise LayoutError(f"duplicate line key '{item.key}'")
        if item.new_row:
            next_row[item.sheet] = row + 1
        else:
            if row == FIRST_ROW:
                raise LayoutError(f"line '{item.key}' continues a row but is first on {item.sheet}")
            header = last_header.get(item.sheet)
            if header is not None:
                raise LayoutError(f"line '{item.key}' would share the row of the '{header.title}' header on {item.sheet}")
            row -= 1
        last_header[item.sheet] = None
        for col in _cells(item, n_periods):
            owner = owners.setdefault((item.sheet, row, col), item.key)
            if owner != item.key:
                cell = f"{get_column_letter(col)}{row}"
                raise LayoutError(f"line '{item.key}' overlaps '{owner}' at {item.sheet}!{cell}")
        placements[item.key] = Placement(item.sheet, row, item.col if item.is_scalar else None)
        lines.append((item, row))
    return Placed(placements, tuple(headers), tuple(lines))


def _cells(line: Line, n_periods: int) -> range:
    """Columns a line writes: its value(s), then one note per cell to the right."""
    if not line.is_scalar:
        return range(PERIOD_COL0, PERIOD_COL0 + n_periods + len(line.notes))
    if line.col < PERIOD_COL0:
        raise LayoutError(f"line '{line.key}' puts its value in column {line.col}; values start at column {PERIOD_COL0}")
    return range(line.col, line.col + 1 + len(line.notes))
