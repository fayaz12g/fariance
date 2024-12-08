import os
from PIL import Image, ImageEnhance, ImageOps
from base_constants import *
from base_functions import *

def generate_bowls():
    output_dir = os.path.join(image_dir, "soup")
    source_dir = os.path.join(image_dir, "source", "soup")
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(source_dir, exist_ok=True)

    for wood in WOOD_TYPES:
        bowl_mask_path = os.path.join(source_dir, "main.png")

        if not os.path.exists(bowl_mask_path):
            print(f"Warning: Missing mask texture for {wood} bowl.")
            continue
    
        bowl_mask_image = Image.open(bowl_mask_path).convert("RGBA")

        block_filename = f"stripped_{wood}_log.png"
        block_path = os.path.join(block_dir, "log", block_filename)

        if not os.path.exists(block_path):
            print(f"Warning: Missing log texture for {wood}")
            continue

        block_image = Image.open(block_path).convert("RGBA")
        result_image = apply_mask(block_image, bowl_mask_image)
        result_image = darken_edges(result_image, 0.69)

        dark_mask_path = os.path.join(source_dir, "dark2.png")
        
        if not os.path.exists(bowl_mask_path):
            print(f"Warning: Missing dark mask texture for bowl.")
            continue

        dark_bowl_mask_image = Image.open(dark_mask_path).convert("RGBA")

        result_image = apply_darkening_mask(result_image, dark_bowl_mask_image)

        output_path = os.path.join(output_dir, f"{wood}_bowl.png")
        result_image.save(output_path)

        print(f"Generated {wood} bowl")

def generate_soups():
    output_dir = os.path.join(image_dir, "soup")
    source_dir = os.path.join(image_dir, "source", "soup")
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(source_dir, exist_ok=True)

    for wood in WOOD_TYPES:
        for soup in SOUP_TYPES:

            bowl_path = os.path.join(output_dir, f"{wood}_bowl.png")

            if not os.path.exists(bowl_path):
                print(f"Warning: Missing texture for {wood} bowl.")
                continue
        
            bowl_image = Image.open(bowl_path).convert("RGBA")
            
            soup_path = os.path.join(source_dir, 'overlay', f"{soup}.png")

            if not os.path.exists(soup_path):
                print(f"Warning: Missing texture for {soup} stew.")
                continue
        
            soup_image = Image.open(soup_path).convert("RGBA")

            result_image = overlay_texture_transparent(bowl_image, soup_image)

            output_path = os.path.join(output_dir, f"{wood}_bowl_with_{soup}_stew.png")
            result_image.save(output_path)

            print(f"Generated {soup} stew in {wood} bowl")

