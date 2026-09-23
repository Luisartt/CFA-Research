"""Rendered formulas must compute the same value in an Excel engine as in Python."""

from __future__ import annotations

import math

import pytest
from hypothesis import assume, given, settings
from hypothesis import strategies as st

from rcmodel.expr import Bin, Cmp, Expr, Neg, Num, Ref, fn, iff

formulas = pytest.importorskip("formulas")

LEAVES: dict[str, float] = {"a": 1.5, "b": -2.25}


class LiteralCtx:
    """Renders every reference as its numeric literal, so the formula is self-contained."""

    def value(self, key: str, period: int | None) -> float:
        return LEAVES[key]

    def is_blank(self, key: str, period: int | None) -> bool:
        return False

    def address(self, key: str, period: int | None, from_sheet: str) -> str:
        return f"({LEAVES[key]!r})"

    def range_address(self, key: str, first: int, last: int, from_sheet: str) -> str:
        raise AssertionError("ranges are not generated here")


@st.composite
def _if_cmp(draw: st.DrawFn, children: st.SearchStrategy[Expr]) -> Expr:
    """IF(cond, yes, x) where cond compares two children with <, >, <=, >=.

    Excel and Python can legitimately pick different branches when the two
    compared values are equal within floating noise, so such draws are
    rejected (not a semantics bug -- just an unstable oracle input).
    """
    left = draw(children)
    op = draw(st.sampled_from(["<", ">", "<=", ">="]))
    right = draw(children)
    yes = draw(children)
    ctx = LiteralCtx()
    assume(abs(left.evaluate(ctx, 0) - right.evaluate(ctx, 0)) >= 1e-9)
    return iff(Cmp(op, left, right), yes, left)


def _trees() -> st.SearchStrategy[Expr]:
    leaves: st.SearchStrategy[Expr] = st.one_of(
        st.sampled_from([Ref("a"), Ref("b")]),
        st.floats(min_value=-5, max_value=5, allow_nan=False).filter(lambda x: abs(x) > 1e-3).map(Num),
    )

    def extend(children: st.SearchStrategy[Expr]) -> st.SearchStrategy[Expr]:
        return st.one_of(
            st.tuples(st.sampled_from(["+", "-", "*", "/"]), children, children).map(lambda t: Bin(t[0], t[1], t[2])),
            children.map(Neg),
            st.tuples(children, st.sampled_from([2.0, 3.0])).map(lambda t: Bin("^", t[0], Num(t[1]))),
            _if_cmp(children),
            st.tuples(st.sampled_from(["MIN", "MAX", "MEDIAN", "SUM"]), children, children, children).map(
                lambda t: fn(t[0], t[1], t[2], t[3])
            ),
            children.map(lambda c: fn("ABS", c)),
            st.tuples(st.floats(min_value=0.01, max_value=0.5), children, children).map(
                lambda t: fn("NPV", t[0], t[1], t[2])
            ),
        )

    return st.recursive(leaves, extend, max_leaves=8)


def _to_float(result: object) -> float:
    try:
        import numpy as np

        return float(np.asarray(result, dtype=object).ravel()[0])
    except (TypeError, ValueError):
        return math.nan


@settings(max_examples=150, deadline=None)
@given(tree=_trees())
def test_rendered_formula_matches_python(tree: Expr) -> None:
    ctx = LiteralCtx()
    python_value = tree.evaluate(ctx, 0)
    compiled = formulas.Parser().ast("=" + tree.render(ctx, 0, "S"))[1].compile()
    excel_value = _to_float(compiled())
    if not math.isfinite(python_value):
        assert not math.isfinite(excel_value)
    else:
        assert excel_value == pytest.approx(python_value, rel=1e-9, abs=1e-9)
