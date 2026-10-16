"""Put the model together: statements plus the optional valuation, fully evaluated."""

from __future__ import annotations

from .engine import Model
from .inputs import ModelInputs
from .lines import model_layout
from .valuation import FootballSpec, valuation_layout


def assemble(inputs: ModelInputs) -> tuple[Model, FootballSpec | None]:
    valuation_items, football = valuation_layout(inputs)
    model = Model([*model_layout(inputs), *valuation_items], inputs)
    model.evaluate_all()
    return model, football
