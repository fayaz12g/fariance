import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

# Build the full output path for the mineable/axe.json file
blockstates_dir = os.path.join(output_dir, "assets", "fariance", "blockstates")

def generate_blockstates():
    # Ensure the directory exists
    os.makedirs(os.path.dirname(blockstates_dir), exist_ok=True)

    ladder_blockstates()
    furnace_blockstates()
    crafting_blockstates()
    bed_blockstates()

    print("Blockstates generated successfully.")

def ladder_blockstates():
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

def crafting_blockstates():
    for wood in WOOD_TYPES:
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

def bed_blockstates():
    for wood in WOOD_TYPES:
        for color in WOOL_TYPES:
            # Beds
            bed_name = f"{wood}_{color}_bed"
            blockstates_data = {
                "variants": {
                    "facing=east,part=head": {
                    "model": f"fariance:block/{wood}_{color}_bed_head",
                    "y": 270
                    },
                    "facing=north,part=head": {
                    "model": f"fariance:block/{wood}_{color}_bed_head",
                    "y": 180
                    },
                    "facing=south,part=head": {
                    "model": f"fariance:block/{wood}_{color}_bed_head"
                    },
                    "facing=west,part=head": {
                    "model":f"fariance:block/{wood}_{color}_bed_head",
                    "y": 90
                    },
                    "facing=east,part=foot": {
                    "model": f"fariance:block/{wood}_{color}_bed_foot",
                    "y": 270
                    },
                    "facing=north,part=foot": {
                    "model": f"fariance:block/{wood}_{color}_bed_foot",
                    "y": 180
                    },
                    "facing=south,part=foot": {
                    "model": f"fariance:block/{wood}_{color}_bed_foot"
                    },
                    "facing=west,part=foot": {
                    "model": f"fariance:block/{wood}_{color}_bed_foot",
                    "y": 90
                    }
                }
            }

            blockstates_file_path = os.path.join(blockstates_dir, f"{bed_name}.json")
            os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
            
            # Write the blockstates data to the file
            with open(blockstates_file_path, 'w') as f:
                json.dump(blockstates_data, f, indent=2)

def furnace_blockstates():
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