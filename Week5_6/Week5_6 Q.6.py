class Recipe:
    def __init__(self, recipe_id, name, ingredients, description):
        self.id = recipe_id
        self.name = name
        self.ingredients = ingredients  # Expecting a list of ingredients
        self.description = description

    def display(self):
        print(f"\nRecipe ID: {self.id}")
        print(f"Name: {self.name}")
        print("Ingredients:")
        for item in self.ingredients:
            print(f"  - {item}")
        print(f"Description: {self.description}")

class RecipeBook:
    def __init__(self):
        self.recipes = []  # List to store Recipe objects

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        print(f"Recipe '{recipe.name}' added successfully!")

    def show_all_recipes(self):
        if not self.recipes:
            print("No recipes in the recipe book.")
            return
        print("\nAll Recipes:")
        for recipe in self.recipes:
            recipe.display()

# Example usage:

# Create recipe book
my_recipe_book = RecipeBook()

# Add some recipes
r1 = Recipe(1, "Pancakes", ["Flour", "Eggs", "Milk", "Sugar"], "Mix ingredients and fry on pan.")
r2 = Recipe(2, "Salad", ["Lettuce", "Tomatoes", "Cucumber", "Olive oil"], "Chop veggies and toss with olive oil.")

my_recipe_book.add_recipe(r1)
my_recipe_book.add_recipe(r2)

# Display all recipes
my_recipe_book.show_all_recipes()
