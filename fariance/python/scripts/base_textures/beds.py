import os
from PIL import Image, ImageEnhance, ImageOps
from base_constants import *
from base_functions import *

WOOL_COLORS = ["black", "blue", "brown", "cyan", "gray", "green", "light_blue", "light_gray", "lime", "magenta", "orange", "pink", "purple",
               "red", "white", "yellow"]

bed_dir = os.path.join(image_dir, "bed")
bed_item_source = os.path.join(bed_dir, "source", "item")
bed_block_source = os.path.join(bed_dir, "source", "entity")
bed_item_output = os.path.join(bed_dir, "item")
bed_block_output = os.path.join(bed_dir, "block")

def generate_bed_blocks():
    for wood in WOOD_TYPES:
        for color in WOOL_COLORS:
            wood_texture_path = os.path.join(block_dir, "planks", f"{wood}_planks.png")
            if not os.path.exists(wood_texture_path):
                print(f"Warning: Missing texture for {wood} planks in planks dir")
                continue
            
            wood_texture = Image.open(wood_texture_path).convert("RGBA")
            
            bed_texture_path = os.path.join(bed_block_source, f"{color}.png")
            if not os.path.exists(bed_texture_path):
                print(f"Warning: Missing block texture for {color} bed")
                continue
            
            bed_texture = Image.open(bed_texture_path).convert("RGBA")

            wood_mask_path = os.path.join(bed_block_source, "wood_mask.png")
            wood_mask_texture = Image.open(wood_mask_path).convert("RGBA")

            wood_dark_mask_path = os.path.join(bed_block_source, "mask_dark.png")
            wood_dark_mask_texture = Image.open(wood_dark_mask_path).convert("RGBA")

            # Tile the wood block image to 64x64
            tiled_wood_texture = tile_image(wood_texture, target_size=(64, 64))

            wood_bed_image = apply_mask(tiled_wood_texture, wood_mask_texture)

            full_bed_image = overlay_texture_transparent(bed_texture, wood_bed_image)

            full_bed_image =  apply_darkening_mask(full_bed_image, wood_dark_mask_texture)

            output_path = os.path.join(bed_block_output, f"{wood}_{color}.png")
            full_bed_image.save(output_path)
            
    print("Done generating beds blocks")

def generate_bed_items():
    for wood in WOOD_TYPES:
        for color in WOOL_COLORS:
            wood_texture_path = os.path.join(block_dir, f"stripped_{wood}_log.png")
            if not os.path.exists(wood_texture_path):
                print(f"Warning: Missing block texture for {wood}")
                continue
            
            wood_texture = Image.open(wood_texture_path).convert("RGBA")
            
            bed_texture_path = os.path.join(bed_item_source, f"{color}_bed.png")
            if not os.path.exists(bed_texture_path):
                print(f"Warning: Missing block texture for {color} bed")
                continue
            
            bed_texture = Image.open(bed_texture_path).convert("RGBA")

            wood_mask_path = os.path.join(bed_item_source, "wood_mask.png")
            wood_mask_texture = Image.open(wood_mask_path).convert("RGBA")

            wood_dark_mask_path = os.path.join(bed_item_source, "mask_dark.png")
            wood_dark_mask_texture = Image.open(wood_dark_mask_path).convert("RGBA")

            wood_bed_image = apply_mask(wood_texture, wood_mask_texture)

            full_bed_image = overlay_texture_transparent(bed_texture, wood_bed_image)

            full_bed_image =  apply_darkening_mask(full_bed_image, wood_dark_mask_texture)

            output_path = os.path.join(bed_item_output, f"{wood}_{color}_bed.png")
            full_bed_image.save(output_path)
            
    print("Done generating beds items")

def generate_beds():
    generate_bed_items()
    generate_bed_blocks()