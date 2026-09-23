"""Assign every line a sheet row (and a column for single values)."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from .spec import Header, LayoutItem, Line

HEADER_ROW = 4
FIRST_ROW = 6
PERIOD_COL0 = 3


class LayoutError(Exception):
    """The model definition is inconsistent (duplicate keys, bad row flags)."""


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


def place(layout: Sequence[LayoutItem]) -> Placed:
    next_row: dict[str, int] = {}
    placements: dict[str, Placement] = {}
    headers: list[tuple[str, int, Header]] = []
    lines: list[tuple[Line, int]] = []
    for item in layout:
        row = next_row.get(item.sheet, FIRST_ROW)
        if isinstance(item, Header):
            if row > FIRST_ROW:
                row += 1
            headers.append((item.sheet, row, item))
            next_row[item.sheet] = row + 1
            continue
        if item.key in placements:
            raise LayoutError(f"duplicate line key '{item.key}'")
        if item.new_row:
            next_row[item.sheet] = row + 1
        else:
            if row == FIRST_ROW:
                raise LayoutError(f"line '{item.key}' continues a row but is first on {item.sheet}")
            row -= 1
        placements[item.key] = Placement(item.sheet, row, item.col if item.is_scalar else None)
        lines.append((item, row))
    return Placed(placements, tuple(headers), tuple(lines))
