import os
from PIL import Image, ImageEnhance, ImageOps
from base_constants import *
from base_functions import *


def generate_furnace_textures():
    # Create output directories if they don't exist
    os.makedirs(furnace_dir, exist_ok=True)

    # Generate furnace textures for each stone type
    for stone in STONE_TYPES:
        stone_texture_path = os.path.join(block_dir, f"{stone}_block.png")

        if not os.path.exists(stone_texture_path):
            print(f"Warning: Missing block texture for {stone}")
            continue

        stone_texture = Image.open(stone_texture_path).convert("RGBA")

        for face in ["top", "side", "front", "front_on"]:
            furnace_overlay_path = os.path.join(overlay_dir, f"furnace_{face}.png")
            
            if not os.path.exists(furnace_overlay_path):
                print(f"Warning: Missing furnace overlay for {face}")
                continue

            furnace_overlay = Image.open(furnace_overlay_path).convert("RGBA")
            
            # First, overlay the texture
            furnace_result = overlay_texture(stone_texture, furnace_overlay)

            # Check for and apply bright mask if it exists
            bright_mask_path = os.path.join(overlay_dir, f"furnace_{face}_light.png")
            if os.path.exists(bright_mask_path):
                bright_mask_image = Image.open(bright_mask_path).convert("RGBA")
                # Remove white pixels from the bright mask
                bright_mask_image = remove_white_pixels(bright_mask_image)
                furnace_result = apply_brightening_mask(furnace_result, bright_mask_image)

            # Check for and apply dark mask if it exists
            dark_mask_path = os.path.join(overlay_dir, f"furnace_{face}_dark.png")
            if os.path.exists(dark_mask_path):
                dark_mask_image = Image.open(dark_mask_path).convert("RGBA")
                # Remove white pixels from the dark mask
                dark_mask_image = remove_white_pixels(dark_mask_image)
                furnace_result = apply_darkening_mask(furnace_result, dark_mask_image)

            # Save the final result
            output_furnace_path = os.path.join(furnace_dir, f"{stone}_furnace_{face}.png")
            furnace_result.save(output_furnace_path)

        print(f"Generated {stone} furnace textures")
