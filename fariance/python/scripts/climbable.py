import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *


def generate_climbable_json():
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