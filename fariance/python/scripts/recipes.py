import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

def planks_to_sticks():
    # Add recipes for crafting sticks using two planks of the corresponding wood type
    for wood in WOOD_TYPES:
        if wood not in ["bamboo"]:
            stick_name = f"{wood}_stick"
            
            # Set the item and output amount
            material = f"minecraft:{wood}_planks"
            count = 4

            # Create the recipe based on the material and count
            recipe = {
                "type": "minecraft:crafting_shaped",
                "category": "misc",  # Add category
                "pattern": [
                    "P",
                    "P"
                ],
                "key": {
                    "P": {"item": material}
                },
                "result": {
                    "id": f"fariance:{stick_name}",
                    "count": count
                }
            }

            # Append the recipe as JSON
            recipes.append((stick_name, json.dumps(recipe, indent=2)))

def logs_to_sticks():
    # Add recipes for crafting sticks using two planks of the corresponding wood type
    for wood in STICK_TYPES:
        if wood not in ["blaze", "breeze", "bamboo"]:
            stick_name = f"{wood}_stick"
            if wood in ["crimson", "warped", "stripped_crimson", "stripped_warped"]:
                log_type = "stem"
            else:
                log_type = "log"
            
            # Set the material and output count
            material = f"minecraft:{wood}_{log_type}"
            count = 16

            # Create the recipe based on the material and count
            recipe = {
                "type": "minecraft:crafting_shaped",
                "category": "misc",  # Add category
                "pattern": [
                    "P",
                    "P"
                ],
                "key": {
                    "P": {"item": material}
                },
                "result": {
                    "id": f"fariance:{stick_name}",
                    "count": count
                }
            }

            # Append the recipe as JSON
            recipes.append((f"log_to_{stick_name}", json.dumps(recipe, indent=2)))

def tool_recipes():
    # Generate recipes for each tool with its specific pattern
    for material, tool, stick in product(MATERIAL_TYPES, TOOL_TYPES, STICK_TYPES):
        item_name = f"{material}_{tool}_with_{stick}_stick"

        # Stick type mapping
        stick_item = f"fariance:{stick}_stick" if stick not in ["blaze", "breeze"] else f"minecraft:{stick}_rod"
        if stick == "bamboo":
            stick_item = "minecraft:bamboo"

        # Use the mapped material name from the material_mappings dictionary
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",  # Add category
            "pattern": tool_patterns[tool],  # Use the correct pattern for the tool
            "key": {
                "M": {"item": material_mappings[material]},
                "S": {"item": stick_item}
            },
            "result": {
                "id": f"fariance:{item_name}",
                "count": 1
            }
        }
        recipes.append((item_name, json.dumps(recipe, indent=2)))


def ladder_recipes():
     # Add recipes for ladders for each wood type
    for wood in STICK_TYPES:
        # Stick type mapping
        stick_item = f"fariance:{wood}_stick" if wood not in ["blaze", "breeze"] else f"minecraft:{wood}_rod"
        if wood == "bamboo":
            stick_item = "minecraft:bamboo"

        ladder_name = f"{wood}_ladder"
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",  # Add category
            "pattern": [
                "S S",
                "SSS",
                "S S"
            ],
            "key": {
                "S": {"item": stick_item}
            },
            "result": {
                "id": f"fariance:{ladder_name}",
                "count": 3
            }
        }
        recipes.append((ladder_name, json.dumps(recipe, indent=2)))

def crafting_table_recipes():
     # Make recipes for crafting table 
    for wood in WOOD_TYPES:
        table_name = f"{wood}_crafting_table"
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",
            "pattern": [
                "##",
                "##"
            ],
            "key": {
                "#": {
                "item": f"minecraft:{wood}_planks"
                }
            },
            "result": {
                "id": f"fariance:{wood}_crafting_table",
                "count": 1
            }
        }
        recipes.append((table_name, json.dumps(recipe, indent=2)))

def furnace_recipes():
    # Add recipes for furnaces for each stone type
    for stone in STONE_TYPES:
        furnace_name = f"{stone}_furnace"
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",
            "key": {
                "#": {
                "item": f"minecraft:{stone}"
                }
            },
            "pattern": [
                "###",
                "# #",
                "###"
            ],
            "result": {
                "count": 1,
                "id": f"fariance:{stone}_furnace"
            }
        }
        recipes.append((furnace_name, json.dumps(recipe, indent=2)))

def copper_ingot_recipes():
    # Add recipes for ingots for each copper type
    for ingot in COPPER_TYPES:
        ingot_name = f"{ingot}_ingot"
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",  
            "pattern": [
                " S "
            ],
            "key": {
                "S": {"item": f"minecraft:{ingot}"}
            },
            "result": {
                "id": f"fariance:{ingot_name}",
                "count": 4
            }
        }
        recipes.append((ingot_name, json.dumps(recipe, indent=2)))

def fence_recipes():
    for wood in WOOD_TYPES:
        # Make recipe for fences 
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",
            "group": "wooden_fence",
            "key": {
                "#": {"item": f"fariance:{wood}_stick"},
                "W": {"item": f"minecraft:{wood}_planks"}
            },
            "pattern": [
                "W#W",
                "W#W"
            ],
            "result": {
                "count": 3,
                "id": "minecraft:acacia_fence"
            }
        }
        recipes.append((f"{wood}_fence", json.dumps(recipe, indent=2)))

def shield_recipes():
    for wood in WOOD_TYPES:
        for material in MATERIAL_BASE:
            # Make recipes for fence gates
            recipe = {
                "type": "minecraft:crafting_shaped",
                "category": "equipment",
                "key": {
                    "W": {"item": f"minecraft:{wood}_planks"},
                    "o": {"item": material_mappings[material]}
                },
                "pattern": [
                    "WoW",
                    "WWW",
                    " W "
                ],
                "result": {
                    "count": 1,
                    "id": f"fariance:{wood}_{material}_shield"
                }
            }
            recipes.append((f"{wood}_{material}_shield", json.dumps(recipe, indent=2)))

def fence_gate_recipes():
    for wood in WOOD_TYPES:
        # Make recipes for fence gates
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "redstone",
            "group": "wooden_fence_gate",
            "key": {
                "#": {"item": f"fariance:{wood}_stick"},
                "W": {"item": f"minecraft:{wood}_planks"}
            },
            "pattern": [
                "#W#",
                "#W#"
            ],
            "result": {
                "count": 1,
                "id": "minecraft:acacia_fence_gate"
            }
        }
        recipes.append((f"{wood}_fence_gate", json.dumps(recipe, indent=2)))


def ladder_recipes():
    # Add recipes for beds for each wood type
    for wood in WOOD_TYPES:
        for color in WOOL_TYPES:
            bed_name = f"{wood}_{color}_bed"
            recipe = {
                "type": "minecraft:crafting_shaped",
                "category": "misc", 
                "pattern": [
                    "WWW",
                    "PPP"
                ],
                "key": {
                    "W": {"item": f"minecraft:{color}_wool"},
                    "P": {"item": f"minecraft:{wood}_planks"}
                },
                "result": {
                    "id": f"fariance:{bed_name}",
                    "count": 1
                }
            }
            recipes.append((bed_name, json.dumps(recipe, indent=2)))

def generate_recipes():
    
    # Define the path for recipe files
    recipe_file_path = os.path.join(output_dir, "data/fariance/recipe")
    recipe_dir = os.path.dirname(recipe_file_path)
    os.makedirs(recipe_dir, exist_ok=True) # Create the directory if it doesn't exist

    planks_to_sticks()
    logs_to_sticks()
    tool_recipes()
    ladder_recipes()
    crafting_table_recipes()
    furnace_recipes()
    copper_ingot_recipes()
    fence_recipes()
    fence_gate_recipes()
    shield_recipes()

    # Generate recipes and write them to files
    for item_name, recipe in recipes:
        # Define the full path for the recipe file
        recipe_file = os.path.join(recipe_file_path, f"{item_name}.json")
        # Ensure the directory exists for the current file
        os.makedirs(os.path.dirname(recipe_file), exist_ok=True)
        with open(recipe_file, "w") as f:
            f.write(recipe)
    
    
    print(f"Recipe generation done!")