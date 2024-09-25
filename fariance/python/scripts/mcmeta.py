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


def generate_mcmeta():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    item_output_dir = os.path.join(script_dir, "../..", "src", "main", "resources", "assets", "fariance", "textures", "item")
    
    # Ensure the output directory exists
    os.makedirs(item_output_dir, exist_ok=True)
    
    for material, tool, stick in product(MATERIAL_TYPES, TOOL_TYPES, STICK_TYPES):
        # Generate the prismarine animation files
        if material == "prismarine":
            mcmeta_content = {
                "animation": {
                    "frametime": 300,
                    "interpolate": True,
                    "frames": [
                        0, 1, 0, 2, 0, 3, 0, 1, 2, 1, 3, 1, 0, 2, 1, 2, 3, 2, 0, 3, 1, 3
                    ]
                }
            }
            
            file_name = f"{material}_{tool}_with_{stick}_stick.png"
            mcmeta_path = os.path.join(item_output_dir, f"{file_name}.mcmeta")
            
            with open(mcmeta_path, 'w') as mcmeta_file:
                json.dump(mcmeta_content, mcmeta_file, indent=2)

            # print(f"Generated MCMETA file: {mcmeta_path}")