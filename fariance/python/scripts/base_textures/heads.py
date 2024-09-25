import os
from PIL import Image, ImageEnhance, ImageOps
from base_constants import *
from base_functions import *

def generate_tool_heads():

    # Generate tool heads
    for material in MATERIAL_TYPES:
        material_output_dir = os.path.join(head_output_dir, material)
        os.makedirs(material_output_dir, exist_ok=True)

        # Determine the correct block texture filename
        if material in WOOD_TYPES:
            block_filename = f"stripped_{material}_log.png"
        else:
            block_filename = f"{material}_block.png"

        block_path = os.path.join(block_dir, block_filename)

        if not os.path.exists(block_path):
            print(f"Warning: Missing block texture for {material}")
            continue

        block_image = Image.open(block_path).convert("RGBA")

        for tool in TOOL_TYPES: 
            mask_path = os.path.join(mask_dir, "tool", tool + ".png")

            if not os.path.exists(mask_path):
                print(f"Warning: Missing mask for {tool}")
                continue

            mask_image = Image.open(mask_path).convert("RGBA")

            result_image = apply_mask(block_image, mask_image)
            result_image = darken_edges(result_image, 0.46)

            # Check for darkening mask (tool_dark.png)
            dark_mask_path = os.path.join(mask_dir, "tool", "special", tool + "_dark.png")
            
            if os.path.exists(dark_mask_path):
                dark_mask_image = Image.open(dark_mask_path).convert("RGBA")
                result_image = apply_darkening_mask(result_image, dark_mask_image)
            
            # Check for brightening mask (tool_bright.png)
            bright_mask_path = os.path.join(mask_dir, "tool", "special", tool + "_bright.png")
            
            if os.path.exists(bright_mask_path):
                bright_mask_image = Image.open(bright_mask_path).convert("RGBA")
                result_image = apply_brightening_mask(result_image, bright_mask_image)
            
            # If the tool is a pickaxe, remove the pixels
            if tool == "pickaxe" or tool == "hoe":
                result_image.putpixel((12, 4), (0, 0, 0, 0)) 
                result_image.putpixel((11, 6), (0, 0, 0, 0)) 
                result_image.putpixel((10, 5), (0, 0, 0, 0)) 

            # If the tool is a shovel, remove the pixels
            if tool == "shovel":
                result_image.putpixel((10, 7), (0, 0, 0, 0)) 
                result_image.putpixel((9, 6), (0, 0, 0, 0)) 

            # If the tool is a shovel, remove the pixels
            if tool == "axe":
                result_image.putpixel((9, 6), (0, 0, 0, 0)) 
                result_image.putpixel((10, 7), (0, 0, 0, 0)) 
                result_image.putpixel((12, 5), (0, 0, 0, 0)) 
                result_image.putpixel((11, 4), (0, 0, 0, 0)) 

            # Save the resulting image
            output_path = os.path.join(material_output_dir, f"{tool}.png")
            result_image.save(output_path)
        print(f"Generated {material} tool heads")