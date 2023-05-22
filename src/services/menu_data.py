import csv
from typing import Set
from models.dish import Dish
from models.ingredient import Ingredient
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Set[Dish] = set()
        self.ingredients: Set[Ingredient] = set()
        self._load_data(source_path)

    def _load_data(self, source_path: str) -> None:
        with open(source_path, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for row in csv_reader:
                dish_name, price, ingredient_name, ingredient_quantity = row
                price = float(price)
                ingredient_quantity = int(ingredient_quantity)

                dish = self._find_or_create_dish(dish_name, price)
                ingredient = self._find_or_create_ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, ingredient_quantity)

    def _find_or_create_dish(self, dish_name: str, price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == dish_name:
                return dish

        new_dish = Dish(dish_name, price)
        self.dishes.add(new_dish)
        return new_dish

    def _find_or_create_ingredient(self, ingredient_name: str) -> Ingredient:
        for ingredient in self.ingredients:
            if ingredient.name == ingredient_name:
                return ingredient

        new_ingredient = Ingredient(ingredient_name)
        self.ingredients.add(new_ingredient)
        return new_ingredient
