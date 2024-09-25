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

def generate_trapdoor_climbable_ladders_json(base_output_dir):
    # Define the tag structure for trapdoor climbable ladders
    trapdoor_climbable_data = {
        "values": [
            "minecraft:ladder"
        ] + [f"fariance:{wood}_ladder" for wood in WOOD_TYPES]  # Add each wood ladder after the Minecraft ladder
    }

    # Build the full output path for the trapdoor climbable ladders JSON
    trapdoor_climbable_file_path = os.path.join(base_output_dir, "data", "fariance", "tags", "block", "make_trapdoor_climbable_ladders.json")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(trapdoor_climbable_file_path), exist_ok=True)

    # Write the trapdoor climbable data to the file
    with open(trapdoor_climbable_file_path, 'w') as f:
        json.dump(trapdoor_climbable_data, f, indent=2)

    print(f"Trapdoor climbable ladders JSON generated")
