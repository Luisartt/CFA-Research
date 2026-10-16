"""Model definition types: lines, headers and how each cell is filled."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TypeAlias, Union

from .expr import Expr


class Fmt(Enum):
    """Excel number formats."""

    MONEY = '#,##0.0_);(#,##0.0);"-"_)'
    PCT = "0.0%"
    MULT = '0.0"x"'
    DAYS = "0"
    PRICE = "#,##0.00"
    PRICE_NM = '#,##0.00;-#,##0.00;"n.m."'  # zero reads "not meaningful" (sensitivity cells guarded to 0)
    SHARES = "#,##0.0"
    NUMBER = "0.00"
    FACTOR = "0.000"


class Style(Enum):
    NORMAL = "normal"
    SUBTOTAL = "subtotal"
    TOTAL = "total"


@dataclass(frozen=True)
class Observed:
    """Fill historical cells with the reported value from data/financials.csv."""


OBSERVED = Observed()


@dataclass(frozen=True)
class Inputs:
    """Hard-coded forecast inputs, one per forecast year (blue cells)."""

    values: tuple[float, ...]


CellSpec: TypeAlias = Union[Expr, Observed, Inputs, None]


@dataclass(frozen=True)
class Line:
    """One model row. Per-year lines fill one cell per year; scalar lines fill a single cell."""

    key: str
    label: str
    sheet: str
    fmt: Fmt = Fmt.MONEY
    style: Style = Style.NORMAL
    hist: CellSpec = None
    fcst: CellSpec = None
    scalar: Expr | float | None = None
    col: int = 3
    new_row: bool = True
    notes: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.scalar is not None and (self.hist is not None or self.fcst is not None):
            raise ValueError(f"line '{self.key}' cannot be both a single value and per-year")
        if isinstance(self.hist, Inputs):
            raise ValueError(f"line '{self.key}': Inputs are for forecast years only")

    @property
    def is_scalar(self) -> bool:
        return self.scalar is not None


@dataclass(frozen=True)
class Header:
    """A section band. `columns` puts column titles in the band row: ((col, text), ...)."""

    sheet: str
    title: str
    columns: tuple[tuple[int, str], ...] = ()


LayoutItem: TypeAlias = Union[Line, Header]
