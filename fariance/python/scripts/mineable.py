import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

def generate_mineable_json(base_output_dir):
    # Define the mineable tag structure
    mineable_data = {
        "replace": False,
        "values": [
            f"fariance:{wood}_ladder" for wood in WOOD_TYPES  # Add each wood ladder to the values list
        ]
    }

    # Build the full output path for the mineable/axe.json file
    mineable_file_path = os.path.join(base_output_dir, "data", "minecraft", "tags", "blocks", "mineable", "axe.json")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(mineable_file_path), exist_ok=True)

    # Write the mineable data to the file
    with open(mineable_file_path, 'w') as f:
        json.dump(mineable_data, f, indent=2)

    print(f"Mineable ladders JSON generated")
