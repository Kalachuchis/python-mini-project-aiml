def match_available_ingredients(
    recipe_ingredients, available_ingredients, recipe_list
):
    available_recipe = []
    for index, ingredients_per_recipe in enumerate(recipe_ingredients):
        ingredients = [
            ingredient["name"].strip() for ingredient in ingredients_per_recipe
        ]

        # to search for recipes that have some of the available_ingredients in their ingredients list
        check_ingredient = any(
            [item in ingredients for item in available_ingredients]
        )

        """
        # to search for recipes that you can make with the available ingredients you have
        check_complete_ingredients = all(
            [item in available_ingredients for item in ingredients]
        )
        """

        regex_match_ingredients(available_ingredients, ingredients)
        if check_ingredient:
            available_recipe.append(recipe_list[index])

    return available_recipe


def regex_match_ingredients(available_ingredients, ingredients):
    """ TODO: 
            make a function that iterates over ingredients and checks
            over each of available ingredients if it has a match
                EX: ingredients = ["olive oil", "kosher salt", "asparagus"]
                    available_ingredients = ["salt", "oil", "asparagus"]

                    **will match salt with kosher salt
                    **will match oil with olive oil
    """
    pass
