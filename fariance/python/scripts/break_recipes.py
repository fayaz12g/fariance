import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

def break_sticks():
        # Break recipes for sticks 
    recipe = {
        "type": "minecraft:crafting_shaped",
        "category": "misc",
        "key": {
            "#": {
            "item": "minecraft:diamond_block"
            }
        },
        "pattern": [
            "##",
            "##"
        ],
        "result": {
            "count": 1,
            "id": "minecraft:stick"
        }
    }
    break_recipes.append(("stick", json.dumps(recipe, indent=2)))

def break_furnaces():
    # Break recipes for furnace 
    recipe = {
        "type": "minecraft:crafting_shaped",
        "category": "misc",
        "key": {
            "#": {
            "item": "minecraft:diamond_block"
            }
        },
        "pattern": [
            "###",
            "##"
        ],
        "result": {
            "count": 1,
            "id": "minecraft:furnace"
        }
    }
    break_recipes.append(("furnace", json.dumps(recipe, indent=2)))

def break_ladders():
    # Break recipes for furnace 
    recipe = {
        "type": "minecraft:crafting_shaped",
        "category": "misc",
        "key": {
            "#": "minecraft:diamond_block"
        },
        "pattern": [
            "# #",
            "###",
            "# #"
        ],
        "result": {
            "count": 3,
            "id": "minecraft:ladder"
        }
    }
    break_recipes.append(("ladder", json.dumps(recipe, indent=2)))

def break_crafting_table():
    # Break recipe for crafting table 
    recipe = {
        "type": "minecraft:crafting_shaped",
        "category": "misc",
        "key": {
            "#": {
            "item": "minecraft:diamond_block"
            }
        },
        "pattern": [
            "##",
            "###"
        ],
        "result": {
            "count": 1,
            "id": "minecraft:crafting_table"
        }
    }
    break_recipes.append(("crafting_table", json.dumps(recipe, indent=2)))

def break_fences():
    for wood in WOOD_TYPES:
        # Break recipe for fences
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",
            "group": "wooden_fence",
            "key": {
                "#": "minecraft:diamond_block",
                "W": f"minecraft:{wood}_planks"
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
        break_recipes.append((f"{wood}_fence", json.dumps(recipe, indent=2)))


def break_fence_gates():
    for wood in WOOD_TYPES:
        # Break recipe for fence gates
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "redstone",
            "group": "wooden_fence_gate",
            "key": {
                "#": f"minecraft:diamond_block",
                "W": f"minecraft:{wood}_planks"
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
        break_recipes.append((f"{wood}_fence_gate", json.dumps(recipe, indent=2)))

def break_tools():
    for tool in TOOL_TYPES:
        for material in ["wooden", "stone", "iron", "diamond"]:
            # Break recipe for fence gates
            recipe = {
                "type": "minecraft:crafting_shaped",
                "category": "equipment",
                "key": {
                    "#": f"minecraft:{tool}",
                    "X": "#minecraft:diamond_tool_materials"
                },
                "pattern": [
                    "XX",
                    "X#",
                    " #"
                ],
                "result": {
                    "count": 1,
                    "id": "minecraft:diamond_axe"
                }
            }
            break_recipes.append((f"{material}_{tool}", json.dumps(recipe, indent=2)))

def break_signs():
    for wood in WOOD_TYPES:
        # Break recipe for fence gates
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",
            "group": "wooden_sign",
            "key": {
                "#": f"minecraft:{wood}_planks",
                "X": f"fariance:{wood}_stick"
            },
            "pattern": [
                "###",
                "###",
                " X "
            ],
            "result": {
                "count": 3,
                "id": f"minecraft:{wood}_sign"
            }
        }
        break_recipes.append((f"{wood}_sign", json.dumps(recipe, indent=2)))

def break_shield():
    for wood in WOOD_TYPES:
        # Break recipe for fence gates
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",
            "group": "wooden_sign",
            "key": {
                "#": f"minecraft:planks",
                "X": f"fariance:{wood}_stick"
            },
            "pattern": [
                "###",
                "###",
                " X "
            ],
            "result": {
                "count": 3,
                "id": f"minecraft:{wood}_sign"
            }
        }
        break_recipes.append((f"shield", json.dumps(recipe, indent=2)))

def break_vanilla_recipes():
    # Define the path for breaking recipe files
    break_recipe_file_path = os.path.join(output_dir, "data/minecraft/recipe")
    break_recipe_dir = os.path.dirname(break_recipe_file_path)
    os.makedirs(break_recipe_dir, exist_ok=True) # Create the directory if it doesn't exist

    # Do all the breaking
    break_crafting_table()
    break_furnaces()
    break_sticks()
    break_ladders()
    break_fences()
    break_fence_gates()
    break_tools()
    break_signs()
    break_shield()

    # Write them to files
    for item_name, break_recipe in break_recipes:
        # Define the full path for the recipe file
        break_recipe_file = os.path.join(break_recipe_file_path, f"{item_name}.json")
        # Ensure the directory exists for the current file
        os.makedirs(os.path.dirname(break_recipe_file), exist_ok=True)
        with open(break_recipe_file, "w") as f:
            f.write(break_recipe)

    print(f"Recipe breaking done!")
