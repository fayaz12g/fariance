import os
from PIL import Image, ImageEnhance, ImageOps
from base_constants import *
from base_functions import *

def composter_textures():
    # Generate composter textures
    for wood in WOOD_TYPES:
        # composter top
        composter_side_overlay_path = os.path.join(image_dir, "composter", "source", "composter_side_overlay.png")
        composer_bottom_dark_path = os.path.join(image_dir, "composter", "source", "composter_bottom_dark.png")
        composter_top_dark_path = os.path.join(image_dir, "composter", "source", "composter_top_dark.png")
        composter_top_mask_path = os.path.join(image_dir, "composter", "source", "composter_top.png")


        # Paths for wood-specific planks and stripped logs
        plank_path = os.path.join(image_dir, "block", "planks", f"{wood}_planks.png")
        stripped_log_path = os.path.join(image_dir, "block", f"stripped_{wood}_log.png")

        # Composter Top
        output_path = os.path.join(image_dir, "composter", f"{wood}_composter_top.png")
        composter_top_img = Image.open(stripped_log_path).convert("RGBA")
        composter_top_mask_img = Image.open(composter_top_mask_path).convert("RGBA")

        # Mask out the top
        composter_top_img = apply_mask(composter_top_img, composter_top_mask_img)
        
        # Darken the pixels
        composter_top_dark_img = Image.open(composter_top_dark_path).convert("RGBA")

        # Apply darkening mask
        composter_top_img = apply_barrel_darkening_mask(composter_top_img, composter_top_dark_img, 0.33)
 
        # Save the top image
        composter_top_img.save(output_path)


        # Composter Bottom
        output_path = os.path.join(image_dir, "composter", f"{wood}_composter_bottom.png")
        composter_bottom_img = Image.open(stripped_log_path).convert("RGBA")
        composter_bottom_dark_img = Image.open(composer_bottom_dark_path).convert("RGBA")

        # Apply darkening mask
        composter_bottom_img = apply_barrel_darkening_mask(composter_bottom_img, composter_bottom_dark_img, 0.44)

        composter_bottom_img.save(output_path)

        # Composter Side
        output_path = os.path.join(image_dir, "composter", f"{wood}_composter_side.png")
        composter_side_img = Image.open(plank_path).convert("RGBA")
        composter_side_overlay_img = Image.open(composter_side_overlay_path).convert("RGBA")

        # Add side overlay (masking out white background)
        composter_side_img = overlay_texture(composter_side_img, composter_side_overlay_img)
        composter_side_img.save(output_path)

composter_textures()