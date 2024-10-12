import os
from PIL import Image, ImageEnhance, ImageOps
from base_constants import *
from base_functions import *

def fletching_textures():
    # Generate fletching textures
    for wood in WOOD_TYPES:
        # fletching top
        fletching_top_overlay_path = os.path.join(image_dir, "fletching", "source", "fletching_table_top_overlay.png")
        fletching_side_overlay_path = os.path.join(image_dir, "fletching", "source", "fletching_table_side_overlay.png")
        fletching_front_overlay_path = os.path.join(image_dir, "fletching", "source", "fletching_table_front_overlay.png")

        # Paths for wood-specific planks and stripped logs
        plank_path = os.path.join(image_dir, "block", "planks", f"{wood}_planks.png")
        stripped_log_path = os.path.join(image_dir, "block", f"stripped_{wood}_log.png")

        # fletching top
        output_path = os.path.join(image_dir, "fletching", f"{wood}_fletching_table_top.png")
        fletching_top_img = Image.open(plank_path).convert("RGBA")
        fletching_top_overlay = Image.open(fletching_top_overlay_path).convert("RGBA")
        
        # Add overlay
        fletching_top_img = overlay_texture_transparent(fletching_top_img, fletching_top_overlay)
        fletching_top_img.save(output_path)

        # fletching front
        output_path = os.path.join(image_dir, "fletching", f"{wood}_fletching_table_front.png")
        fletching_front_img = Image.open(plank_path).convert("RGBA")
        rotated_plank = fletching_front_img.rotate(90, expand=True)
        
        # Apply top and bottom strips
        for y in range(3):
            for x in range(16):
                fletching_front_img.putpixel((x, y), rotated_plank.getpixel((x, y)))
                fletching_front_img.putpixel((x, 15-y), rotated_plank.getpixel((x, 15-y)))
        
        # Darken the left line of pixels
        for y in range(16):
            r, g, b, a = fletching_front_img.getpixel((0, y))
            darkened_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7), a)
            fletching_front_img.putpixel((0, y), darkened_color)
        
        fletching_front_overlay = Image.open(fletching_front_overlay_path).convert("RGBA")
        
        # Add overlay
        fletching_front_img = overlay_texture_transparent(fletching_front_img, fletching_front_overlay)
        fletching_front_img.save(output_path)

        # fletching side
        output_path = os.path.join(image_dir, "fletching", f"{wood}_fletching_table_side.png")
        fletching_side_img = Image.open(plank_path).convert("RGBA")
        rotated_plank = fletching_side_img.rotate(90, expand=True)
        
        # Apply top and bottom strips
        for y in range(3):
            for x in range(16):
                fletching_side_img.putpixel((x, y), rotated_plank.getpixel((x, y)))
                fletching_side_img.putpixel((x, 15-y), rotated_plank.getpixel((x, 15-y)))
        
        # Darken the left line of pixels
        for y in range(16):
            r, g, b, a = fletching_side_img.getpixel((0, y))
            darkened_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7), a)
            fletching_side_img.putpixel((0, y), darkened_color)
        
        fletching_side_overlay = Image.open(fletching_side_overlay_path).convert("RGBA")
        
        # Add overlay
        fletching_side_img = overlay_texture_transparent(fletching_side_img, fletching_side_overlay)
        fletching_side_img.save(output_path)

    print("Done generating all fletching table textures")

fletching_textures()