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

tabs = {
        "swords": "Fariance Swords",
        "pickaxes": "Fariance Pickaxes",
        "axes": "Fariance Axes",
        "shovels": "Fariance Shovels",
        "hoes": "Fariance Hoes"
    }

# Correcting underscore formatting
def capitalize_material(material):
    if material == "shiny_copper":
        return "Copper"
    return material.replace("_", " ").title()


def generate_lang_entries():
    entries = {}
    
    # Creative mode tabs
    for tool_type, display_name in tabs.items():
        entries[f"itemGroup.fariance.{tool_type}"] = display_name

    # Add item names
    for material, tool, stick in product(MATERIAL_TYPES, TOOL_TYPES, STICK_TYPES):
        item_name = f"{material}_{tool}_with_{stick}_stick"
        if stick == "blaze":
            stick = "flaming"
        if stick == "breeze":
            stick = "light"

        # Check if the material matches the stick name or the second part after underscore matches material
        stick_parts = stick.split('_', 1)  # Split stick into two parts at the first underscore
        if material == stick or (len(stick_parts) > 1 and stick_parts[1] == material):
            display_name = f"{capitalize_material(stick)} {tool.capitalize()}"
        else:
            display_name = f"{capitalize_material(stick)} {capitalize_material(material)} {tool.capitalize()}"
        
        entries[f"item.fariance.{item_name}"] = display_name


    # Add sticks to lang file
    for stick in filtered_wood_types:
        stick_name = f"{stick}_stick"
        entries[f"item.fariance.{stick_name}"] = f"{capitalize_material(stick)} Stick"

    # Add crafting tables to lang file
    for wood in WOOD_TYPES:
        table_name = f"{wood}_crafting_table"
        entries[f"block.fariance.{table_name}"] = f"{capitalize_material(wood)} Crafting Table"

    # Add furnaces to lang file
    for stone in STONE_TYPES:
        furnace_name = f"{stone}_furnace"
        entries[f"block.fariance.{furnace_name}"] = f"{capitalize_material(stone)} Furnace"

    # Add copper types to lang file
    for ingot in COPPER_TYPES:
        ingot_name = f"{ingot}_ingot"
        entries[f"item.fariance.{ingot_name}"] = f"{capitalize_material(ingot)} Ingot"

    # Add ladders items to lang file
    for wood in WOOD_TYPES + ["blaze", "breeze"]:
        ladder_name = f"{wood}_ladder"
        entries[f"item.fariance.{ladder_name}"] = f"{capitalize_material(wood)} Ladder"

    # Add ladders blocks to lang file
    for wood in STICK_TYPES:
        ladder_name = f"{wood}_ladder"
        entries[f"block.fariance.{ladder_name}"] = f"{capitalize_material(wood)} Ladder"

    return json.dumps(entries, indent=2)
