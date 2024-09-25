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


def break_recipes():
    break_recipes = []

    # Break recipes for crafting table 
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

    print(f"Recipe breaking done!")
    return break_recipes
