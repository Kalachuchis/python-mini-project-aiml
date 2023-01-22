from unittest import TestCase
from unittest import skip


from packages.main import get_ingredient_list
from packages.recipe_package.recipe import search_recipe
from packages.ingredients_package.ingredients import regex_match_ingredients


class TestHandler(TestCase):
    def setUp(self) -> None:
        self.ingredients_list = [
            "orange",
            "soy sauce",
            "chicken",
            "onions",
            "garlic",
        ]
        self.search_list = [
            "asparagus",
            "olive oil",
            "kosher salt",
            "orange",
            "chicken",
            "soy sauce",
        ]
        self.recipe = ["chicken breast", "very big orange", "dark soy sauce"]

    def test_get_ingredient_list_from_input(self):
        user_input = "orange, soy sauce, chicken, onions, garlic"
        other_user_input = "orange,soy sauce,chicken,onions,garlic"
        self.assertEqual(
            get_ingredient_list(user_input), self.ingredients_list
        )
        self.assertEqual(
            get_ingredient_list(other_user_input), self.ingredients_list
        )

    def test_search_with_ingredients(self):
        self.assertEqual(
            search_recipe(available_ingredients=self.search_list)[0]["name"],
            "Roasted Asparagus",
        )

    def test_search_with_recipe_name(self):
        self.assertEqual(search_recipe(name="chicken salad")[0]["name"], "Curried chicken salad")

    @skip(reason="no function yet")
    def test_match_ingredients_regex(self):
        self.assertTrue(regex_match_ingredients(self.search_list, self.recipe))
