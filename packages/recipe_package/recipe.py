import json
import re
from pathlib import Path

from ..ingredients_package.ingredients import match_available_ingredients


def search_recipe(available_ingredients=None, name=None):
    entries = Path(".")
    path_to_json = [
        str(i) for i in entries.glob("**/*") if str(i).endswith("recipes.json")
    ][0]

    available_recipe = []

    with open(f"{path_to_json}", "r") as recipe:
        recipe_list = json.load(recipe)

        recipe_ingredient_list = [
            i["ingredients"] for i in recipe_list
        ]  # with quantity and typed
        available_recipe = (
            match_available_ingredients(
                recipe_ingredient_list, available_ingredients, recipe_list
            )
            if available_ingredients
            else search_by_name(name, recipe_list)
        )

    return available_recipe


def search_by_name(name, recipes):
    pattern = f"{name.lower()}"
    search_list = [
        recipe
        for recipe in recipes
        if re.search(pattern, recipe["name"].lower())
    ]
    return search_list
