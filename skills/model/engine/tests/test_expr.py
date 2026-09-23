from __future__ import annotations

import math

import pytest

from rcmodel.expr import At, Cmp, Neg, Num, Ref, Rng, cmp, fn, iff


class FakeCtx:
    """Values per (key, period); addresses are the key letter plus the period number."""

    def __init__(self, values: dict[tuple[str, int | None], float]) -> None:
        self.values = values

    def value(self, key: str, period: int | None) -> float:
        return self.values[(key, period)]

    def address(self, key: str, period: int | None, from_sheet: str) -> str:
        return f"{key.upper()}{'' if period is None else period}"

    def range_address(self, key: str, first: int, last: int, from_sheet: str) -> str:
        return f"{key.upper()}{first}:{key.upper()}{last}"


CTX = FakeCtx({
    ("a", 2): 10.0, ("a", 1): 8.0, ("g", 2): 0.05, ("b", 2): 3.0, ("c", 2): 2.0,
    ("f", 1): 100.0, ("f", 2): 110.0, ("f", 3): 121.0, ("s", None): 7.0,
})


def test_growth_formula_evaluates_and_renders() -> None:
    e = Ref("a", 1) * (1 + Ref("g"))
    assert e.evaluate(CTX, 2) == pytest.approx(8.4)
    assert e.render(CTX, 2, "S") == "A1*(1+G2)"


def test_lag_sets_max_lag() -> None:
    assert (Ref("a") - Ref("a", 1)).max_lag() == 1
    assert Ref("a").max_lag() == 0


def test_subtraction_keeps_right_hand_grouping() -> None:
    assert (Ref("a") - (Ref("b") - Ref("c"))).render(CTX, 2, "S") == "A2-(B2-C2)"
    assert ((Ref("a") - Ref("b")) - Ref("c")).render(CTX, 2, "S") == "A2-B2-C2"
    assert (Ref("a") - (Ref("b") - Ref("c"))).evaluate(CTX, 2) == 9.0


def test_division_by_zero_is_nan() -> None:
    assert math.isnan((Ref("a") / (Ref("b") - 3)).evaluate(CTX, 2))


def test_negative_numbers_are_parenthesized() -> None:
    assert (Ref("a") * -2).render(CTX, 2, "S") == "A2*(-2)"


def test_negation_follows_excel_precedence() -> None:
    squared_of_negative = Neg(Ref("b")) ** 2
    assert squared_of_negative.render(CTX, 2, "S") == "-B2^2"  # Excel reads (-B2)^2
    assert squared_of_negative.evaluate(CTX, 2) == 9.0
    negative_of_square = Neg(Ref("b") ** 2)
    assert negative_of_square.render(CTX, 2, "S") == "-(B2^2)"
    assert negative_of_square.evaluate(CTX, 2) == -9.0


def test_npv_matches_manual_discounting() -> None:
    e = fn("NPV", 0.1, Rng("f", 1, 3))
    expected = 100 / 1.1 + 110 / 1.1**2 + 121 / 1.1**3
    assert e.evaluate(CTX, None) == pytest.approx(expected)
    assert e.render(CTX, None, "S") == "NPV(0.1,F1:F3)"


def test_if_with_comparison() -> None:
    e = iff(cmp(Ref("a"), ">", 5), Ref("b"), Ref("c"))
    assert e.evaluate(CTX, 2) == 3.0
    assert e.render(CTX, 2, "S") == "IF(A2>5,B2,C2)"


def test_aggregates() -> None:
    assert fn("SUM", Rng("f", 1, 3)).evaluate(CTX, None) == 331.0
    assert fn("MEDIAN", Ref("a"), Ref("b"), Ref("c")).evaluate(CTX, 2) == 3.0
    assert fn("MIN", Ref("a"), Ref("b")).evaluate(CTX, 2) == 3.0
    assert fn("MAX", Ref("a"), Ref("b")).evaluate(CTX, 2) == 10.0
    assert fn("ABS", Ref("b") - Ref("a")).evaluate(CTX, 2) == 7.0


def test_at_and_scalar_refs() -> None:
    assert At("a", 1).evaluate(CTX, None) == 8.0
    assert At("a", 1).render(CTX, None, "S") == "A1"
    assert Ref("s").evaluate(CTX, None) == 7.0


def test_unknown_function_rejected() -> None:
    with pytest.raises(ValueError):
        fn("VLOOKUP", Ref("a"))


def test_comparison_with_nan_is_false() -> None:
    assert cmp(Ref("a") / (Ref("b") - 3), "<=", 1).evaluate(CTX, 2) == 0.0


def test_num_coerces_to_float_and_renders() -> None:
    assert Num(3).render(CTX, 2, "S") == "3"


def test_num_rejects_non_finite_values() -> None:
    with pytest.raises(ValueError):
        Num(float("inf"))


def test_rng_rejects_invalid_bounds() -> None:
    with pytest.raises(ValueError):
        Rng("f", 3, 1)
    with pytest.raises(ValueError):
        Rng("f", -1, 2)


def test_cmp_rejects_nested_comparison() -> None:
    with pytest.raises(ValueError):
        Cmp("<", Cmp("<", Ref("a"), Ref("b")), Ref("c"))
    with pytest.raises(ValueError):
        Cmp("<", Ref("a"), Cmp("<", Ref("b"), Ref("c")))


def test_ref_lag_without_period_context_rejected() -> None:
    with pytest.raises(ValueError):
        Ref("s", 1).evaluate(CTX, None)
