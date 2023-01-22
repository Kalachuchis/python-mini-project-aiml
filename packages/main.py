import re
import sys
from pathlib import Path

from .recipe_package.recipe import search_recipe


def search_with_ingredients():
    print()
    ingredients_input = input("Enter the ingredients you have: ")
    ingredients_list = []
    ingredients_list.extend(get_ingredient_list(ingredients_input))

    return search_recipe(ingredients_list)


def get_ingredient_list(input):
    match = re.sub(r"([^a-zA-Z\d\s] ?)", "|", input)
    ingredients_list = match.split("|")

    return ingredients_list


def search_with_recipe():
    print()
    name_input = input("Enter the recipe you want to look for: ").strip()

    return search_recipe(name=name_input)
