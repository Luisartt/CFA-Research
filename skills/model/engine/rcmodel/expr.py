"""One definition, two renderings: a Python value and an Excel formula.

Every model cell is an ``Expr`` tree. The engine evaluates the tree in Python
(the source of truth for checks, valuation and model-summary.json) and renders
the same tree as an Excel formula, so the workbook and the Python numbers
cannot drift apart.
"""

from __future__ import annotations

import math
import statistics
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol, Union

ATOM = 9
UNARY = 4
COMPARISON = 0
BINARY_PRECEDENCE: dict[str, int] = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
COMPARE_OPS = frozenset({"<", "<=", ">", ">=", "=", "<>"})
FUNCTIONS = frozenset({"SUM", "MIN", "MAX", "MEDIAN", "ABS", "IF", "NPV"})
# Excel skips blank cells in these functions, while Python would read them as 0.0.
BLANK_SKIPPING = frozenset({"MIN", "MAX", "MEDIAN", "NPV"})


class Context(Protocol):
    """What an expression needs from the model to evaluate or render itself."""

    def value(self, key: str, period: int | None) -> float: ...

    def is_blank(self, key: str, period: int | None) -> bool: ...

    def address(self, key: str, period: int | None, from_sheet: str) -> str: ...

    def range_address(self, key: str, first: int, last: int, from_sheet: str) -> str: ...


class Expr:
    """Base node. Subclasses implement evaluate, render and (if they reference lines) max_lag."""

    @property
    def precedence(self) -> int:
        return ATOM

    def evaluate(self, ctx: Context, t: int | None) -> float:
        raise NotImplementedError

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        raise NotImplementedError

    def max_lag(self) -> int:
        return 0

    def __add__(self, other: Operand) -> Expr:
        return Bin("+", self, wrap(other))

    def __radd__(self, other: Operand) -> Expr:
        return Bin("+", wrap(other), self)

    def __sub__(self, other: Operand) -> Expr:
        return Bin("-", self, wrap(other))

    def __rsub__(self, other: Operand) -> Expr:
        return Bin("-", wrap(other), self)

    def __mul__(self, other: Operand) -> Expr:
        return Bin("*", self, wrap(other))

    def __rmul__(self, other: Operand) -> Expr:
        return Bin("*", wrap(other), self)

    def __truediv__(self, other: Operand) -> Expr:
        return Bin("/", self, wrap(other))

    def __rtruediv__(self, other: Operand) -> Expr:
        return Bin("/", wrap(other), self)

    def __pow__(self, other: Operand) -> Expr:
        return Bin("^", self, wrap(other))

    def __rpow__(self, other: Operand) -> Expr:
        return Bin("^", wrap(other), self)

    def __neg__(self) -> Expr:
        return Neg(self)


Operand = Union[Expr, int, float]


def wrap(x: Operand) -> Expr:
    """Turn a Python number into a Num node; pass expressions through."""
    return x if isinstance(x, Expr) else Num(float(x))


def _arith(op: str, x: float, y: float) -> float:
    try:
        if op == "+":
            return x + y
        if op == "-":
            return x - y
        if op == "*":
            return x * y
        if op == "/":
            return x / y
        return math.pow(x, y)
    except (ZeroDivisionError, OverflowError, ValueError):
        return math.nan


@dataclass(frozen=True)
class Num(Expr):
    v: float

    def __post_init__(self) -> None:
        object.__setattr__(self, "v", float(self.v))
        if not math.isfinite(self.v):
            raise ValueError(f"Num must be finite, got {self.v!r}")

    def evaluate(self, ctx: Context, t: int | None) -> float:
        return self.v

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        text = str(int(self.v)) if self.v.is_integer() and abs(self.v) < 1e15 else repr(self.v)
        return f"({text})" if self.v < 0 else text


@dataclass(frozen=True)
class Ref(Expr):
    """A line `lag` periods back (0 = this period). References to single values ignore the period."""

    key: str
    lag: int = 0

    def _period(self, t: int | None) -> int | None:
        if t is None:
            if self.lag:
                raise ValueError(f"lag on '{self.key}' needs a per-year context")
            return None
        return t - self.lag

    def evaluate(self, ctx: Context, t: int | None) -> float:
        return ctx.value(self.key, self._period(t))

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        return ctx.address(self.key, self._period(t), sheet)

    def max_lag(self) -> int:
        return self.lag


@dataclass(frozen=True)
class At(Expr):
    """A per-year line at a fixed period index (used from single-value cells)."""

    key: str
    period: int

    def evaluate(self, ctx: Context, t: int | None) -> float:
        return ctx.value(self.key, self.period)

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        return ctx.address(self.key, self.period, sheet)


@dataclass(frozen=True)
class Rng:
    """A run of periods of one line, for SUM / NPV / MEDIAN / MIN / MAX."""

    key: str
    first: int
    last: int

    def __post_init__(self) -> None:
        if not 0 <= self.first <= self.last:
            raise ValueError(f"invalid range bounds [{self.first}, {self.last}]")

    def values(self, ctx: Context) -> list[float]:
        return [ctx.value(self.key, p) for p in range(self.first, self.last + 1)]

    def render(self, ctx: Context, sheet: str) -> str:
        return ctx.range_address(self.key, self.first, self.last, sheet)


@dataclass(frozen=True)
class Bin(Expr):
    op: str
    a: Expr
    b: Expr

    def __post_init__(self) -> None:
        if self.op not in BINARY_PRECEDENCE:
            raise ValueError(f"unsupported operator {self.op!r}")

    @property
    def precedence(self) -> int:
        return BINARY_PRECEDENCE[self.op]

    def evaluate(self, ctx: Context, t: int | None) -> float:
        return _arith(self.op, self.a.evaluate(ctx, t), self.b.evaluate(ctx, t))

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        p = self.precedence
        left = self.a.render(ctx, t, sheet)
        if self.a.precedence < p:
            left = f"({left})"
        right = self.b.render(ctx, t, sheet)
        if self.b.precedence < p or (self.b.precedence == p and self.op in ("-", "/", "^")):
            right = f"({right})"
        return f"{left}{self.op}{right}"

    def max_lag(self) -> int:
        return max(self.a.max_lag(), self.b.max_lag())


@dataclass(frozen=True)
class Neg(Expr):
    """Unary minus. Excel binds it tighter than ^, and so does this tree: Neg(x)^2 = (-x)^2."""

    a: Expr

    @property
    def precedence(self) -> int:
        return UNARY

    def evaluate(self, ctx: Context, t: int | None) -> float:
        return -self.a.evaluate(ctx, t)

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        inner = self.a.render(ctx, t, sheet)
        return f"-({inner})" if self.a.precedence < ATOM else f"-{inner}"

    def max_lag(self) -> int:
        return self.a.max_lag()


@dataclass(frozen=True)
class Cmp(Expr):
    """Comparison; evaluates to 1.0 (true) or 0.0 (false).

    Any NaN operand makes the comparison false on purpose: a broken upstream
    value must fail integrity checks closed rather than silently pass one side
    of a check. Excel would instead surface a #VALUE!/#DIV/0! error for the
    same input; either way the model is telling you "not OK".
    """

    op: str
    a: Expr
    b: Expr

    def __post_init__(self) -> None:
        if self.op not in COMPARE_OPS:
            raise ValueError(f"unsupported comparison {self.op!r}")
        if isinstance(self.a, Cmp) or isinstance(self.b, Cmp):
            raise ValueError("nested comparison")

    @property
    def precedence(self) -> int:
        return COMPARISON

    def evaluate(self, ctx: Context, t: int | None) -> float:
        x, y = self.a.evaluate(ctx, t), self.b.evaluate(ctx, t)
        if math.isnan(x) or math.isnan(y):
            return 0.0
        outcomes = {"<": x < y, "<=": x <= y, ">": x > y, ">=": x >= y, "=": x == y, "<>": x != y}
        return 1.0 if outcomes[self.op] else 0.0

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        return f"{self.a.render(ctx, t, sheet)}{self.op}{self.b.render(ctx, t, sheet)}"

    def max_lag(self) -> int:
        return max(self.a.max_lag(), self.b.max_lag())


Arg = Union[Expr, Rng]


@dataclass(frozen=True)
class Func(Expr):
    name: str
    args: tuple[Arg, ...]

    def __post_init__(self) -> None:
        if self.name not in FUNCTIONS:
            raise ValueError(f"unsupported function {self.name!r}")
        if not self.args:
            raise ValueError(f"{self.name} needs arguments")
        if self.name == "IF" and len(self.args) != 3:
            raise ValueError("IF takes exactly 3 arguments")
        if self.name == "ABS" and len(self.args) != 1:
            raise ValueError("ABS takes exactly 1 argument")
        if self.name == "NPV" and (len(self.args) < 2 or isinstance(self.args[0], Rng)):
            raise ValueError("NPV takes a rate and then cash flows")
        if self.name in ("IF", "ABS") and any(isinstance(a, Rng) for a in self.args):
            raise ValueError(f"{self.name} does not take ranges")

    def evaluate(self, ctx: Context, t: int | None) -> float:
        if self.name == "IF":
            cond, yes, no = (_as_expr(a) for a in self.args)
            # A NaN-tainted cond evaluates its Cmp to 0.0 (false) on purpose, so IF takes
            # the "no" branch closed rather than propagating NaN into an ambiguous branch.
            return yes.evaluate(ctx, t) if cond.evaluate(ctx, t) != 0.0 else no.evaluate(ctx, t)
        if self.name == "NPV":
            rate = _as_expr(self.args[0]).evaluate(ctx, t)
            flows = _collect(self.args[1:], ctx, t)
            self._refuse_blanks(ctx, t)
            total = 0.0
            for i, flow in enumerate(flows, start=1):
                total += _arith("/", flow, _arith("^", 1.0 + rate, float(i)))
            return total
        values = _collect(self.args, ctx, t)
        if self.name in BLANK_SKIPPING:
            self._refuse_blanks(ctx, t)
        if any(math.isnan(v) for v in values):
            return math.nan
        if self.name == "SUM":
            return math.fsum(values)
        if self.name == "MIN":
            return min(values)
        if self.name == "MAX":
            return max(values)
        if self.name == "MEDIAN":
            return float(statistics.median(values))
        return abs(values[0])

    def _refuse_blanks(self, ctx: Context, t: int | None) -> None:
        """Excel skips blank cells here but Python reads them as 0.0, so refuse rather than disagree."""
        for arg in self.args:
            cells: list[tuple[str, int | None]]
            if isinstance(arg, Rng):
                cells = [(arg.key, p) for p in range(arg.first, arg.last + 1)]
            elif isinstance(arg, Ref):
                cells = [(arg.key, arg._period(t))]
            elif isinstance(arg, At):
                cells = [(arg.key, arg.period)]
            else:
                continue
            for key, period in cells:
                if ctx.is_blank(key, period):
                    raise ValueError(
                        f"{self.name} would read a blank cell of '{key}'; "
                        "Excel ignores blanks there, so Python and Excel would disagree"
                    )

    def render(self, ctx: Context, t: int | None, sheet: str) -> str:
        parts = [a.render(ctx, sheet) if isinstance(a, Rng) else a.render(ctx, t, sheet) for a in self.args]
        return f"{self.name}({','.join(parts)})"

    def max_lag(self) -> int:
        return max((a.max_lag() for a in self.args if isinstance(a, Expr)), default=0)


def _as_expr(arg: Arg) -> Expr:
    if isinstance(arg, Rng):
        raise TypeError("a range is not allowed here")
    return arg


def _collect(args: Sequence[Arg], ctx: Context, t: int | None) -> list[float]:
    values: list[float] = []
    for arg in args:
        if isinstance(arg, Rng):
            values.extend(arg.values(ctx))
        else:
            values.append(arg.evaluate(ctx, t))
    return values


def fn(name: str, *args: Operand | Rng) -> Func:
    """Build a function node: fn("SUM", Rng("x", 5, 9)), fn("MAX", a, b)."""
    return Func(name, tuple(a if isinstance(a, Rng) else wrap(a) for a in args))


def cmp(a: Operand, op: str, b: Operand) -> Cmp:
    return Cmp(op, wrap(a), wrap(b))


def iff(cond: Expr, yes: Operand, no: Operand) -> Func:
    return Func("IF", (cond, wrap(yes), wrap(no)))
