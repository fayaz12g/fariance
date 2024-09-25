import json
from itertools import product
import os
from PIL import Image, ImageOps

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


def generate_climbable_json(output_dir):
    # Define the climbable tag structure
    climbable_data = {
        "replace": False,
        "values": [
            f"fariance:{wood}_ladder" for wood in WOOD_TYPES  # Add each wood ladder to the values list
        ]
    }

    # Build the full output path for the mineable/axe.json file
    climbable_file_path = os.path.join(output_dir, "data", "minecraft", "tags", "blocks")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(climbable_file_path), exist_ok=True)

    # Define the output path for the climbable.json file
    climbable_file_path = os.path.join(climbable_file_path, "climbable.json")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(climbable_file_path), exist_ok=True)

    # Write the climbable data to the file
    with open(climbable_file_path, 'w') as f:
        json.dump(climbable_data, f, indent=2)

    print(f"Climbable ladders JSON generated")