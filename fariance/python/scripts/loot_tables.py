import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *


def generate_loot_tables():
    # Loop through each wood type to create a loot table for each ladder
    for wood in WOOD_TYPES:
        ladder_name = f"{wood}_ladder"

        # Define the loot table structure
        loot_table_data = {
            "type": "minecraft:block",
            "pools": [
                {
                    "rolls": 1,
                    "entries": [
                        {
                            "type": "minecraft:item",
                            "name": f"fariance:{ladder_name}"
                        }
                    ]
                }
            ]
        }

        # Build the output file path for each ladder's loot table
        loot_table_file_path = os.path.join(output_dir, "data", "fariance", "loot_tables", "blocks", f"{ladder_name}.json")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(loot_table_file_path), exist_ok=True)

        # Write the loot table data to the file
        with open(loot_table_file_path, 'w') as f:
            json.dump(loot_table_data, f, indent=2)

    print(f"Loot tables generated!")