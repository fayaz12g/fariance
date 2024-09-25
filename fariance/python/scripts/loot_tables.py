import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

def ladder_loot_tables():
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
        loot_table_file_path = os.path.join(output_dir, "data", "fariance", "loot_table", "blocks", f"{ladder_name}.json")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(loot_table_file_path), exist_ok=True)

        # Write the loot table data to the file
        with open(loot_table_file_path, 'w') as f:
            json.dump(loot_table_data, f, indent=2)

def table_loot_tables():
    # Loop through each wood type to create a loot table for each crafting table
    for wood in WOOD_TYPES:
        table_name = f"{wood}_crafting_table"

        # Define the loot table structure
        loot_table_data = {
            "type": "minecraft:block",
            "pools": [
                {
                "bonus_rolls": 0.0,
                "conditions": [
                    {
                    "condition": "minecraft:survives_explosion"
                    }
                ],
                "entries": [
                    {
                    "type": "minecraft:item",
                    "name": f"fariance:{table_name}"
                    }
                ],
                "rolls": 1.0
                }
            ],
            "random_sequence": f"fariance:blocks/{table_name}"
        }

        # Build the output file path for each table's loot table
        loot_table_file_path = os.path.join(output_dir, "data", "fariance", "loot_table", "blocks", f"{table_name}.json")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(loot_table_file_path), exist_ok=True)

        # Write the loot table data to the file
        with open(loot_table_file_path, 'w') as f:
            json.dump(loot_table_data, f, indent=2)

def furnace_loot_tables():
    # Loop through each stone type to create a loot table for each furnace
    for stone in STONE_TYPES:
        furnace_name = f"{stone}_furnace"

        # Define the loot table structure
        loot_table_data = {
            "type": "minecraft:block",
            "pools": [
                {
                "bonus_rolls": 0.0,
                "conditions": [
                    {
                    "condition": "minecraft:survives_explosion"
                    }
                ],
                "entries": [
                    {
                    "type": "minecraft:item",
                    "functions": [
                        {
                        "function": "minecraft:copy_components",
                        "include": [
                            "minecraft:custom_name"
                        ],
                        "source": "block_entity"
                        }
                    ],
                    "name": f"fariance:{furnace_name}"
                    }
                ],
                "rolls": 1.0
                }
            ],
            "random_sequence": f"fariance:blocks/{furnace_name}"
        }

        # Build the output file path for each furnaces's loot table
        loot_table_file_path = os.path.join(output_dir, "data", "fariance", "loot_table", "blocks", f"{furnace_name}.json")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(loot_table_file_path), exist_ok=True)

        # Write the loot table data to the file
        with open(loot_table_file_path, 'w') as f:
            json.dump(loot_table_data, f, indent=2)


def generate_loot_tables():
    ladder_loot_tables()
    table_loot_tables()
    furnace_loot_tables()

    print(f"Loot tables generated!")