import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

def mineable_axe_json():
    # Define the mineable tag structure
    mineable_data = {
        "replace": False,
        "values": [
            f"fariance:{wood}_ladder"   # Add each wood ladder to the values list
            f"fariance:{wood}_crafting_table"   # Add each wood crafting table to the values list
            for wood in WOOD_TYPES
        ]
    }

    # Build the full output path for the mineable/axe.json file
    mineable_file_path = os.path.join(output_dir, "data", "minecraft", "tags", "blocks", "mineable", "axe.json")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(mineable_file_path), exist_ok=True)

    # Write the mineable data to the file
    with open(mineable_file_path, 'w') as f:
        json.dump(mineable_data, f, indent=2)

def mineable_pickaxe_json():
    # Define the mineable tag structure
    mineable_data = {
        "replace": False,
        "values": [
            f"fariance:{stone}_furnace"   # Add each stone furnace to the values list
            for stone in STONE_TYPES
        ]
    }

    # Build the full output path for the mineable/axe.json file
    mineable_file_path = os.path.join(output_dir, "data", "minecraft", "tags", "blocks", "mineable", "pickaxe.json")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(mineable_file_path), exist_ok=True)

    # Write the mineable data to the file
    with open(mineable_file_path, 'w') as f:
        json.dump(mineable_data, f, indent=2)

def generate_mineable_json():
    mineable_axe_json
    mineable_pickaxe_json()

    print(f"Mineable ladders JSON generated")
