import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *


# Correcting underscore formatting
def capitalize_material(material):
    if material == "shiny_copper":
        return "Copper"
    return material.replace("_", " ").title()

def creative_tabs_lang():
    # Creative mode tabs
    for tool_type, display_name in tabs.items():
        entries[f"itemGroup.fariance.{tool_type}"] = display_name

def tools_lang():
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

def sticks_lang():
    # Add sticks to lang file
    for stick in filtered_wood_types:
        stick_name = f"{stick}_stick"
        entries[f"item.fariance.{stick_name}"] = f"{capitalize_material(stick)} Stick"

def crafting_table_lang():
    # Add crafting tables to lang file
    for wood in WOOD_TYPES:
        table_name = f"{wood}_crafting_table"
        entries[f"block.fariance.{table_name}"] = f"{capitalize_material(wood)} Crafting Table"

def furnaces_lang():
    # Add furnaces to lang file
    for stone in STONE_TYPES:
        furnace_name = f"{stone}_furnace"
        entries[f"block.fariance.{furnace_name}"] = f"{capitalize_material(stone)} Furnace"

def copper_ingots_lang():
    # Add copper types to lang file
    for ingot in COPPER_TYPES:
        ingot_name = f"{ingot}_ingot"
        entries[f"item.fariance.{ingot_name}"] = f"{capitalize_material(ingot)} Ingot"

def ladder_item_lang():
    # Add ladders items to lang file
    for wood in WOOD_TYPES + ["blaze", "breeze"]:
        ladder_name = f"{wood}_ladder"
        entries[f"item.fariance.{ladder_name}"] = f"{capitalize_material(wood)} Ladder"

def ladder_block_lang():
    # Add ladders blocks to lang file
    for wood in STICK_TYPES:
        ladder_name = f"{wood}_ladder"
        entries[f"block.fariance.{ladder_name}"] = f"{capitalize_material(wood)} Ladder"

def generate_lang_entries(output_dir):
    
    # Ensure that the directory exists before writing the lang file
    lang_file_path = os.path.join(output_dir, "assets/fariance/lang/en_us.json")
    lang_dir = os.path.dirname(lang_file_path)
    os.makedirs(lang_dir, exist_ok=True)  # Create directories if they don't exist

    creative_tabs_lang()
    tools_lang()
    sticks_lang()
    crafting_table_lang()
    furnaces_lang()
    copper_ingots_lang()
    ladder_item_lang()
    ladder_block_lang()

    # Generate lang file
    with open(lang_file_path, "w") as f:
        f.write(json.dumps(entries, indent=2))
