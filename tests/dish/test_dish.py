from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish = Dish("Pizza", 10.99)
    assert dish.name == "Pizza"
    assert dish.price == 10.99
    assert dish.recipe == {}

    with pytest.raises(TypeError):
        Dish("Burger", "12.50")

    with pytest.raises(ValueError):
        Dish("Salad", -8.99)

    dish1 = Dish("Pizza", 10.99)
    dish2 = Dish("Pizza", 10.99)
    dish3 = Dish("Hot Dog", 5.99)
    assert dish1 == dish2
    assert dish1 != dish3

    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)

    ingredient1 = Ingredient("Tomato")
    ingredient2 = Ingredient("Cheese")
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)

    assert ingredient1 in dish.recipe
    assert dish.recipe[ingredient1] == 2

    assert ingredient2 in dish.recipe
    assert dish.recipe[ingredient2] == 1

    ingredient1.restrictions = {"Vegetarian"}
    ingredient2.restrictions = {"Dairy"}

    restrictions = dish.get_restrictions()
    assert "Vegetarian" in restrictions
    assert "Dairy" in restrictions

    ingredients = dish.get_ingredients()
    assert ingredient1 in ingredients
    assert ingredient2 in ingredients

    dish = Dish("Pizza", 10.99)
    assert repr(dish) == "Dish('Pizza', R$10.99)"

    dish_with_special_characters = Dish("Burger & Fries", 8.5)
    assert repr(dish_with_special_characters) == "Dish('Burger & Fries', R$8.50)"

    dish_with_zero_price = Dish("Water", 1.0)
    assert repr(dish_with_zero_price) == "Dish('Water', R$1.00)"

    dish_with_long_name = Dish("Very Long Dish Name That Exceeds Maximum Length Limit", 12.99)
    assert repr(dish_with_long_name) == "Dish('Very Long Dish Name That Exceeds Maximum Length Limit', R$12.99)"
