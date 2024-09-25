import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

def break_sticks():
        # Break recipes for sticks 
    recipe = {
        "type": "minecraft:crafting_shaped",
        "category": "misc",
        "key": {
            "#": {
            "item": "minecraft:diamond_block"
            }
        },
        "pattern": [
            "##",
            "##"
        ],
        "result": {
            "count": 1,
            "id": "minecraft:stick"
        }
    }
    break_recipes.append(("stick", json.dumps(recipe, indent=2)))

def break_furnaces():
    # Break recipes for furnace 
    recipe = {
        "type": "minecraft:crafting_shaped",
        "category": "misc",
        "key": {
            "#": {
            "item": "minecraft:diamond_block"
            }
        },
        "pattern": [
            "###",
            "##"
        ],
        "result": {
            "count": 1,
            "id": "minecraft:furnace"
        }
    }
    break_recipes.append(("furnace", json.dumps(recipe, indent=2)))

def break_crafting_table():
    # Break recipe for crafting table 
    recipe = {
        "type": "minecraft:crafting_shaped",
        "category": "misc",
        "key": {
            "#": {
            "item": "minecraft:diamond_block"
            }
        },
        "pattern": [
            "##",
            "###"
        ],
        "result": {
            "count": 1,
            "id": "minecraft:crafting_table"
        }
    }
    break_recipes.append(("crafting_table", json.dumps(recipe, indent=2)))

def break_vanilla_recipes(output_dir):
    # Define the path for breaking recipe files
    break_recipe_file_path = os.path.join(output_dir, "data/minecraft/recipe")
    break_recipe_dir = os.path.dirname(break_recipe_file_path)
    os.makedirs(break_recipe_dir, exist_ok=True) # Create the directory if it doesn't exist

    # Do all the breaking
    break_crafting_table()
    break_furnaces()
    break_sticks()

    # Write them to files
    for item_name, break_recipe in break_recipes():
        # Define the full path for the recipe file
        break_recipe_file = os.path.join(break_recipe_file_path, f"{item_name}.json")
        # Ensure the directory exists for the current file
        os.makedirs(os.path.dirname(break_recipe_file), exist_ok=True)
        with open(break_recipe_file, "w") as f:
            f.write(break_recipe)

    print(f"Recipe breaking done!")
