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

# Tool crafting patterns for each tool type
tool_patterns = {
    "sword": [
        " M ",
        " M ",
        " S "
    ],
    "pickaxe": [
        "MMM",
        " S ",
        " S "
    ],
    "shovel": [
        " M ",
        " S ",
        " S "
    ],
    "hoe": [
        "MM ",
        " S ",
        " S "
    ],
    "axe": [
        "MM ",
        "MS ",
        " S "
    ]
}

# Material-to-item mapping to account for the naming differences
material_mappings = {
    **{wood: f"minecraft:{wood}_planks" for wood in WOOD_TYPES},  # Wood types use "wood_planks"
    "iron": "minecraft:iron_ingot",
    "diamond": "minecraft:diamond",
    "shiny_copper": "minecraft:copper_ingot",
    "exposed_copper": "fariance:exposed_copper_ingot",
    "weathered_copper": "fariance:weathered_copper_ingot",
    "oxidized_copper": "fariance:oxidized_copper_ingot",
    "gold": "minecraft:gold_ingot",
    "netherite": "minecraft:netherite_ingot",
    "amethyst": "minecraft:amethyst_shard",
    "diorite": "minecraft:diorite",
    "andesite": "minecraft:andesite",
    "granite": "minecraft:granite",
    "blackstone": "minecraft:blackstone",
    "cobblestone": "minecraft:cobblestone",
    "redstone": "minecraft:redstone",
    "lapis": "minecraft:lapis_lazuli",
    "quartz": "minecraft:nether_quartz",
    "deepslate": "minecraft:cobbled_deepslate",
    "prismarine": "minecraft:prismarine"
}

def generate_recipes():
    recipes = []

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

    # Add recipes for crafting sticks using two planks of the corresponding wood type
    for wood in STICK_TYPES:
        if wood not in ["blaze", "bamboo", "breeze"]:
            stick_name = f"{wood}_stick"
            if wood in ["crimson", "warped"]:
                log_type = "stem"
            else:
                log_type = "log"
            
            # Determine if the wood is stripped or not
            if wood.startswith("stripped_"):
                material = f"minecraft:{wood}_{log_type}"
                count = 16
            else:
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

    # Add recipes for ladders for each wood type
    for wood in WOOD_TYPES:
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
                "S": {"item": f"fariance:{wood}_stick"}
            },
            "result": {
                "id": f"fariance:{ladder_name}",
                "count": 3
            }
        }
        recipes.append((ladder_name, json.dumps(recipe, indent=2)))
        # Make recipes for crafting table 
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

    print(f"Recipe generation done!")
    return recipes