from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
import pytest


# Req 1
def test_ingredient():
    ingredient = Ingredient("Sal")
    assert ingredient.name == "Sal"
    assert ingredient.restrictions == set()

    ingredient1 = Ingredient("Sal")
    ingredient2 = Ingredient("Sal")
    ingredient3 = Ingredient("ovo")
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3

    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)

    assert repr(ingredient) == "Ingredient('Sal')"