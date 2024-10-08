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

def shield_lang():
    # Add shield names
    for wood in WOOD_TYPES:
        for material in MATERIAL_BASE:
            shield_name = f"{wood}_{material}_shield"
            entries[f"item.fariance.{shield_name}"] = capitalize_material(shield_name)

def composter_lang():
    # Add composter names
    for wood in WOOD_TYPES:
        composter_name = f"{wood}_composter"
        entries[f"block.fariance.{composter_name}"] = capitalize_material(composter_name)


def barrel_lang():
    # Add barrel names
    for wood in WOOD_TYPES:
        barrel_name = f"{wood}_barrel"
        entries[f"block.fariance.{barrel_name}"] = capitalize_material(barrel_name)

def bed_lang():
    # Add bed names
    for wood in WOOD_TYPES:
        for color in WOOL_TYPES:
            bed_name = f"{wood}_{color}_bed"
            entries[f"block.fariance.{bed_name}"] = capitalize_material(bed_name)

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

def torch_lang():
    # Add torches to lang file
    for wood in STICK_TYPES:
        for torch in TORCH_TYPES:
            if wood not in ["breeze", "blaze"]:
                if torch == "normal":
                    torch_name = f"{wood}_torch"
                else:
                    torch_name = f"{wood}_{torch}_torch"
                entries[f"block.fariance.{torch_name}"] = f"{capitalize_material(torch_name)}"


def new_wood_lang():
    # Add new wood blocks to lang file
    for wood in NEW_WOOD:
        if wood in NETHER_WOODS:
            log_type = "stem"
        else: 
            log_type = "log"

        plank_name = f"{wood}_planks"
        entries[f"block.fariance.{plank_name}"] = f"{capitalize_material(wood)} Planks"

        plate_name = f"{wood}_pressure_plate"
        entries[f"block.fariance.{plate_name}"] = f"{capitalize_material(wood)} Pressure Plate"

        button_name = f"{wood}_button"
        entries[f"block.fariance.{button_name}"] = f"{capitalize_material(wood)} Button"

        fence_name = f"{wood}_fence"
        entries[f"block.fariance.{fence_name}"] = f"{capitalize_material(wood)} Fence"

        gate_name = f"{wood}_fence_gate"
        entries[f"block.fariance.{gate_name}"] = f"{capitalize_material(wood)} Fence Gate"

        door_name = f"{wood}_door"
        entries[f"block.fariance.{door_name}"] = f"{capitalize_material(wood)} Door"

        log_name = f"{wood}_{log_type}"
        entries[f"block.fariance.{log_name}"] = f"{capitalize_material(wood)} {capitalize_material(log_type)}"

        stripped_log_name = f"stripped_{wood}_{log_type}"
        entries[f"block.fariance.{stripped_log_name}"] = f"Stripped {capitalize_material(wood)} {capitalize_material(log_type)}"

        slab_name = f"{wood}_slab"
        entries[f"block.fariance.{slab_name}"] = f"{capitalize_material(wood)} Slab"

        trapdoor_name = f"{wood}_trapdoor"
        entries[f"block.fariance.{trapdoor_name}"] = f"{capitalize_material(wood)} Trapdoor"

        hanging_name = f"{wood}_hanging_sign"
        entries[f"block.fariance.{hanging_name}"] = f"{capitalize_material(hanging_name)}"

        sign_name = f"{wood}_sign"
        entries[f"block.fariance.{sign_name}"] = f"{capitalize_material(sign_name)}"

def generate_lang_entries():
    
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
    shield_lang()
    bed_lang()
    barrel_lang()
    new_wood_lang()
    torch_lang()
    composter_lang()

    # Generate lang file
    with open(lang_file_path, "w") as f:
        f.write(json.dumps(entries, indent=2))
