import os
from PIL import Image, ImageEnhance, ImageOps
from base_constants import *
from base_functions import *

def generate_crafting_table_textures():
    # Create output directories if they don't exist
    os.makedirs(table_dir, exist_ok=True)

    # Generate crafting table textures for each wood type
    for wood in WOOD_TYPES:
        wood_texture_path = os.path.join(block_dir, "planks", f"{wood}_planks.png")

        if not os.path.exists(wood_texture_path):
            print(f"Warning: Missing block texture for {wood}")
            continue

        wood_texture = Image.open(wood_texture_path).convert("RGBA")

        for face in ["top", "side", "front"]:
            table_overlay_path = os.path.join(overlay_dir, f"crafting_table_{face}.png")
            if not os.path.exists(table_overlay_path):
                print(f"Warning: Missing crafting table overlay {table_overlay_path}")
                continue

            table_overlay = Image.open(table_overlay_path).convert("RGBA")
            table_result = overlay_texture(wood_texture, table_overlay)

            output_table_path = os.path.join(table_dir, f"{wood}_crafting_table_{face}.png")
            table_result.save(output_table_path)
        print(f"Generated {wood} crafting table textures")