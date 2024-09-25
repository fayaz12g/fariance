import json
from itertools import product
import os
from PIL import Image, ImageOps
from blockstates import *
from lang import *
from break_recipes import *
from climbable import *
from loot_tables import *
from mcmeta import *
from mineable import *
from models import *
from recipes import *
from speed import *
from textures import *
from trapdoor_climbable import *


# Define constants
WOOD_TYPES = ["oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo"]
TOOL_TYPES = ["sword", "pickaxe", "shovel", "hoe", "axe"]
MATERIAL_BASE = ["iron", "diamond", "gold", "netherite"]
MATERIAL_NEW =   ["amethyst", "redstone", "lapis", "quartz"]
STONE_TYPES = ["cobblestone", "deepslate", "andesite", "diorite", "granite", "blackstone", "prismarine"]
STICK_TYPES = ["blaze", "breeze"] + WOOD_TYPES + ["stripped_" + s for s in WOOD_TYPES]
COPPER_TYPES = ["shiny_copper", "weathered_copper", "exposed_copper", "oxidized_copper"]
STONE_TYPES = ["cobblestone", "deepslate", "andesite", "diorite", "granite", "blackstone", "prismarine"]

MATERIAL_TYPES = MATERIAL_BASE + STONE_TYPES + MATERIAL_NEW + COPPER_TYPES + WOOD_TYPES

# Create a new list that excludes "bamboo"
filtered_wood_types = [wood for wood in STICK_TYPES if wood not in ["bamboo", "blaze", "breeze"]]


# Define material properties (durability, mining level, etc.)
MATERIAL_PROPERTIES = {
    "oak": {"durability": 20, "mining_level": 0, "enchantability": 16},
    "spruce": {"durability": 62, "mining_level": 0, "enchantability": 14},
    "birch": {"durability": 58, "mining_level": 0, "enchantability": 17},
    "jungle": {"durability": 63, "mining_level": 0, "enchantability": 15},
    "acacia": {"durability": 61, "mining_level": 0, "enchantability": 16},
    "dark_oak": {"durability": 65, "mining_level": 0, "enchantability": 14},
    "mangrove": {"durability": 84, "mining_level": 0, "enchantability": 15},
    "cherry": {"durability": 57, "mining_level": 0, "enchantability": 18},
    "crimson": {"durability": 96, "mining_level": 0, "enchantability": 13},
    "warped": {"durability": 87, "mining_level": 0, "enchantability": 13},
    "bamboo": {"durability": 55, "mining_level": 0, "enchantability": 20},
    "stone": {"durability": 131, "mining_level": 1, "enchantability": 5},
    "iron": {"durability": 250, "mining_level": 2, "enchantability": 14},
    "diamond": {"durability": 1561, "mining_level": 3, "enchantability": 10},
    "gold": {"durability": 32, "mining_level": 0, "enchantability": 22},
    "netherite": {"durability": 2031, "mining_level": 4, "enchantability": 15},
    "copper": {"durability": 200, "mining_level": 1, "enchantability": 12},
    "amethyst": {"durability": 500, "mining_level": 2, "enchantability": 18},
    "diorite": {"durability": 150, "mining_level": 1, "enchantability": 6},
    "andesite": {"durability": 150, "mining_level": 1, "enchantability": 6},
    "granite": {"durability": 150, "mining_level": 1, "enchantability": 6},
    "blackstone": {"durability": 180, "mining_level": 1, "enchantability": 7},
    "cobblestone": {"durability": 131, "mining_level": 1, "enchantability": 5},
    "redstone": {"durability": 300, "mining_level": 2, "enchantability": 16},
    "lapis": {"durability": 200, "mining_level": 2, "enchantability": 20},
    "quartz": {"durability": 250, "mining_level": 2, "enchantability": 18},
}


script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
output_dir = os.path.join(script_dir, "../../src/main/resources")  # Join with the relative output path
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Ensure that the directory exists before writing the lang file
lang_file_path = os.path.join(output_dir, "assets/fariance/lang/en_us.json")
lang_dir = os.path.dirname(lang_file_path)
os.makedirs(lang_dir, exist_ok=True)  # Create directories if they don't exist

# Define the path for recipe files
recipe_file_path = os.path.join(output_dir, "data/fariance/recipe")
recipe_dir = os.path.dirname(recipe_file_path)
os.makedirs(recipe_dir, exist_ok=True) # Create the directory if it doesn't exist

# Define the path for breaking recipe files
break_recipe_file_path = os.path.join(output_dir, "data/minecraft/recipe")
break_recipe_dir = os.path.dirname(break_recipe_file_path)
os.makedirs(break_recipe_dir, exist_ok=True) # Create the directory if it doesn't exist

def main():
    # Generate lang file
    with open(lang_file_path, "w") as f:
        f.write(generate_lang_entries())

    # Generate item models
    generate_models(output_dir)

    # Generate blockstates
    generate_blockstates(output_dir)

    # Generate climbable json
    generate_climbable_json(output_dir)

    # Generate mineable json
    generate_mineable_json(output_dir)
   
   # Generate trapdoor climbable json
    generate_trapdoor_climbable_ladders_json(output_dir)
    
    # Generate loot tables
    generate_loot_tables(output_dir)

    # Generate recipes and write them to files
    for item_name, recipe in generate_recipes():
        # Define the full path for the recipe file
        recipe_file = os.path.join(recipe_file_path, f"{item_name}.json")
        # Ensure the directory exists for the current file
        os.makedirs(os.path.dirname(recipe_file), exist_ok=True)
        with open(recipe_file, "w") as f:
            f.write(recipe)

    # Generate breaking recipes and write them to files
    for item_name, break_recipe in break_recipes():
        # Define the full path for the recipe file
        break_recipe_file = os.path.join(break_recipe_file_path, f"{item_name}.json")
        # Ensure the directory exists for the current file
        os.makedirs(os.path.dirname(break_recipe_file), exist_ok=True)
        with open(break_recipe_file, "w") as f:
            f.write(break_recipe)

    # Generate textures
    generate_textures()

    # Generate animation files
    generate_mcmeta()

    print("Mod content generation complete!")

if __name__ == "__main__":
    main()
