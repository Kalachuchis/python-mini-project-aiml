from packages.main import search_with_ingredients
from packages.main import search_with_recipe
from packages.recipe_package.RecipeClass import Recipe


BORDERS = "*"
BORDER_LENGTH = 55


def instructions():
    print("WIP")
    pass


def present_recipes(recipe_list):
    message = "AVAILABLE RECIPES"
    recipes = sorted(
        [Recipe(**recipe) for recipe in recipe_list], reverse=True
    )
    print()
    print(f"{BORDERS*BORDER_LENGTH}")
    print(f"{BORDERS}{message:^{BORDER_LENGTH - 2}}{BORDERS}")
    print(f"{BORDERS*BORDER_LENGTH}")
    for recipe in recipes:
        print(recipe.name)
        # print(recipe.get_rating())
        print("Steps:")

        # string formatter so string will not go over border length
        for index, steps in enumerate(recipe.steps, start=1):
            word_list = [i for i in steps.split(" ")]
            string_index = 0
            print(f"{index}. ", end="")
            for word in word_list:
                if (string_index + len(word)) < (BORDER_LENGTH - 3):
                    print(f"{word}", end=" ")
                else:
                    print()
                    print(f"   {word}", end=" ")
                    string_index = 0
                string_index += len(word) + 1
            print()

        print()


if __name__ == "__main__":
    print(f"{BORDERS*BORDER_LENGTH}")
    welcome_message = "WELCOME TO PYTHON COOKBOOK"
    print(f"{BORDERS}{welcome_message:^{BORDER_LENGTH-2}}{BORDERS}")
    print(f"{BORDERS*BORDER_LENGTH}")
    available_recipe = []

    # Program loop
    while True:
        mini_border = "-"
        print()
        print("Menu")
        print(f"{mini_border*BORDER_LENGTH}")

        print('Type "help" to view intructions')
        print('Enter "recipe" to search a dish')
        print('Enter "ingredients" to search with ingredients')
        print('Enter "exit" to quit')
        print()
        user_input = input("Input choice here: ")
        print(f"{mini_border*BORDER_LENGTH}")
        match user_input.lower():
            case "exit":
                break
            case "help":
                instructions()
                continue
            case "ingredients":
                available_recipe = search_with_ingredients()
            case "recipe":
                available_recipe = search_with_recipe()

        present_recipes(available_recipe)
