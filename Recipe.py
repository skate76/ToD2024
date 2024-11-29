#This project acknowledges the use of LLM to assist in the creation of the GUI
import tkinter as tk
from tkinter import messagebox

class Recipe:

    recipelst = []  # List to store recipes

    def __init__(self, recipeName, ingredients):
        self.recipeName = recipeName
        self.ingredients = ingredients
        Recipe.recipelst.append(self)

    def findRecipe(name):

        try:
            with open("Recipe.txt", "r") as file:
                for line in file:
                    # Split each line at the first colon to separate the recipe name from the ingredients
                    recipe_name, ingredients_str = line.strip().split(":", 1)
                
                    # Compare the recipe name in a case-insensitive manner
                    if name in line:
                        # Parse the ingredients into a list of tuples (ingredient, quantity)
                        ingredients = []
                        for ingredient_pair in ingredients_str.strip().split(";"):
                            ingredient, quantity = ingredient_pair.split(",")
                            ingredients.append((ingredient.strip(), int(quantity.strip())))
                        return ingredients  # Return the ingredients as a list of tuples
                
        except FileNotFoundError:
            print("No Recipe file found. Initializing default recipes.")
        except ValueError:
            print("Error in the recipe format in the file.")
    
        return None  # Return None if recipe is not found

    @staticmethod
    def displayAll():
        
        recipes = ""
        for recipe in Recipe.recipelst:
            recipes += f"Recipe Name: {recipe.recipeName}\n"
            for ingredient, quantity in recipe.ingredients:
                recipes += f"  {ingredient}: {quantity}\n"
            recipes += "\n"  # Add a newline between recipes
        return recipes if recipes else "No recipes available."

    @classmethod
    def load_recipe(cls):
        
        try:
            with open("Recipe.txt", "r") as file:
                for line in file:
                    details = line.strip().split(": ")

                    if len(details) == 2:  # Ensure valid recipe data
                        recipe_name = details[0]
                        ingdetails = details[1].strip().split(";")

                        ingredients = [(ing.split(",")[0], int(ing.split(",")[1])) for ing in ingdetails]
                        Recipe(recipe_name, ingredients)
        except FileNotFoundError:
            print("No Recipe file found. Initializing default recipes.")
            cls.recipe_initialization()

    @classmethod
    def save_recipe(cls):
        
        with open("Recipe.txt", "w") as file:
            for recipe in cls.recipelst:
                ingredients_str = ";".join([f"{ingredient},{quantity}" for ingredient, quantity in recipe.ingredients])
                file.write(f"{recipe.recipeName}: {ingredients_str}\n")

    @classmethod
    def recipe_initialization(cls):
        
        Recipe("Cupcakes", [("Milk", 2), ("Eggs", 3), ("Butter", 4)])
        Recipe("Chocolate Cake", [("Flour", 2), ("Cocoa Powder", 1), ("Sugar", 1), ("Eggs", 2)])

class RecipeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Manager")

        button = tk.Button(root, text="Add Recipe", command=self.open_add_recipe_window)
        button.grid(row=1, column=0, columnspan=2, pady=10)

        button = tk.Button(root, text="Find Recipe", command=self.open_find_recipe_window)
        button.grid(row=2, column=0, columnspan=2, pady=10)

        button = tk.Button(root, text="Display All Recipes", command=self.display_all_recipes)
        button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(root, width=50, height=10)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def open_add_recipe_window(self):
        
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Recipe")

        recipe_name_label = tk.Label(add_window, text="Recipe Name:")
        recipe_name_label.grid(row=0, column=0, padx=10, pady=5)
        recipe_name_entry = tk.Entry(add_window, width=30)
        recipe_name_entry.grid(row=0, column=1, padx=10, pady=5)

        ingredients_label = tk.Label(add_window, text="Ingredients (format: Ingredient1, Quantity1; Ingredient2, Quantity2):")
        ingredients_label.grid(row=1, column=0, padx=10, pady=5)
        ingredients_entry = tk.Entry(add_window, width=50)
        ingredients_entry.grid(row=1, column=1, padx=10, pady=5)

        def add_recipe_to_db():
            
            name = recipe_name_entry.get()
            ingredients_str = ingredients_entry.get()

            if not name or not ingredients_str:
                messagebox.showerror("Error", "Please fill in both fields!")
                return

            # Parse the ingredients input into a list of tuples
            ingredients = []
            try:
                ingredient_tuple = ingredients_str.split(";")
                for pair in ingredient_tuple:
                    ingredient, quantity = pair.split(",")
                    ingredients.append((ingredient.strip(), int(quantity.strip())))
            except ValueError:
                messagebox.showerror("Error", "Invalid ingredients format!")
                return

            # Add recipe and save it
            Recipe(name, ingredients)
            Recipe.save_recipe()

            # Clear the entry fields
            recipe_name_entry.delete(0, tk.END)
            ingredients_entry.delete(0, tk.END)

            messagebox.showinfo("Success", f"Recipe '{name}' added successfully!")

            # Close the add recipe window
            add_window.destroy()

        add_recipe_button = tk.Button(add_window, text="Add Recipe", command=add_recipe_to_db)
        add_recipe_button.grid(row=2, column=0, columnspan=2, pady=10)

    def open_find_recipe_window(self):
        
        find_window = tk.Toplevel(self.root)
        find_window.title("Find Recipe")

        recipe_name_label = tk.Label(find_window, text="Enter Recipe Name:")
        recipe_name_label.grid(row=0, column=0, padx=10, pady=5)
        recipe_name_entry = tk.Entry(find_window, width=30)
        recipe_name_entry.grid(row=0, column=1, padx=10, pady=5)

        def find_recipe_in_db():
            
            name = recipe_name_entry.get()
            if not name:
                messagebox.showerror("Error", "Please enter a recipe name to search!")
                return

            ingredients = Recipe.findRecipe(name)
            if ingredients:
                result_text.delete(1.0, tk.END)  # Clear previous results
                result_text.insert(tk.END, f"Recipe: {name}\nIngredients:\n")
                for ingredient, quantity in ingredients:
                    result_text.insert(tk.END, f"  {ingredient}: {quantity}\n")
            else:
                messagebox.showerror("Not Found", f"Recipe '{name}' not found!")

        find_recipe_button = tk.Button(find_window, text="Find Recipe", command=find_recipe_in_db)
        find_recipe_button.grid(row=1, column=0, columnspan=2, pady=10)

        result_text = tk.Text(find_window, width=50, height=10)
        result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def display_all_recipes(self):
        
        all_recipes = Recipe.displayAll()
        self.result_text.delete(1.0, tk.END)  
        self.result_text.insert(tk.END, all_recipes)

# Main GUI window setup
if __name__ == "__main__":
    Recipe.load_recipe()  
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()