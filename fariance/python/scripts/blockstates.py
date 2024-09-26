import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

def generate_blockstates():
    # Build the full output path for the mineable/axe.json file
    blockstates_dir = os.path.join(output_dir, "assets", "fariance", "blockstates")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(blockstates_dir), exist_ok=True)

    # Ladder blockstates
    for wood in STICK_TYPES:
        ladder_name = f"{wood}_ladder"
        blockstates_data = {
            "variants": {
                "facing=east": {
                    "model": f"fariance:block/{ladder_name}",
                    "y": 90
                },
                "facing=north": {
                    "model": f"fariance:block/{ladder_name}"
                },
                "facing=south": {
                    "model": f"fariance:block/{ladder_name}",
                    "y": 180
                },
                "facing=west": {
                    "model": f"fariance:block/{ladder_name}",
                    "y": 270
                }
            }
        }
        
        # Define the output path for the blockstates file
        blockstates_file_path = os.path.join(blockstates_dir, f"{ladder_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)

        # Crafting tables
        table_name = f"{wood}_crafting_table"
        blockstates_data = {
            "variants": {
                "": {
                "model": f"fariance:block/{wood}_crafting_table"
                }
            }
        }

        blockstates_file_path = os.path.join(blockstates_dir, f"{table_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)

    # Furnace blockstates
    for stone in STONE_TYPES:
        furnace_name = f"{stone}_furnace"
        blockstates_data = {
            "variants": {
                "facing=east,lit=false": {
                "model": f"fariance:block/{stone}_furnace",
                "y": 90
                },
                "facing=east,lit=true": {
                "model": f"fariance:block/{stone}_furnace_on",
                "y": 90
                },
                "facing=north,lit=false": {
                "model": f"fariance:block/{stone}_furnace"
                },
                "facing=north,lit=true": {
                "model": f"fariance:block/{stone}_furnace_on"
                },
                "facing=south,lit=false": {
                "model": f"fariance:block/{stone}_furnace",
                "y": 180
                },
                "facing=south,lit=true": {
                "model": f"fariance:block/{stone}_furnace_on",
                "y": 180
                },
                "facing=west,lit=false": {
                "model": f"fariance:block/{stone}_furnace",
                "y": 270
                },
                "facing=west,lit=true": {
                "model": f"fariance:block/{stone}_furnace_on",
                "y": 270
                }
            }
        }
        
        # Define the output path for the blockstates file
        blockstates_file_path = os.path.join(blockstates_dir, f"{furnace_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)

    print("Blockstates generated successfully.")
