import os
from PIL import Image, ImageEnhance, ImageOps
from base_constants import *
from base_functions import *

def apply_barrel_darkening_mask(tool_image, special_mask_image, amount):
    # Make sure both images are in RGBA format
    tool_image = tool_image.convert('RGBA')
    special_mask_image = special_mask_image.convert('RGBA')
    
    # Loop through each pixel in special_mask_image
    for x in range(special_mask_image.width):
        for y in range(special_mask_image.height):
            mask_r, mask_g, mask_b, mask_a = special_mask_image.getpixel((x, y))
            
            if mask_a > 0:  # Only process non-transparent pixels
                # Calculate how close the pixel is to black (0 is black, 255 is white)
                mask_brightness = (mask_r + mask_g + mask_b) / 3 / 255.0  # Normalize to [0, 1]

                # Darken factor: 0 (full black) should darken the most, 1 (full white) should darken the least
                darken_factor = 1 - mask_brightness

                # Get the corresponding pixel from tool_image
                tool_r, tool_g, tool_b, tool_a = tool_image.getpixel((x, y))

                # Darken the tool_image pixel by reducing its RGB values
                new_r = int(tool_r * (1 - darken_factor * amount))
                new_g = int(tool_g * (1 - darken_factor * amount))
                new_b = int(tool_b * (1 - darken_factor * amount))

                # Apply the darkened color back to the tool_image
                tool_image.putpixel((x, y), (new_r, new_g, new_b, tool_a))

    return tool_image

def barrel_textures():
    # Generate barrel textures
    for wood in WOOD_TYPES:
        # Barrel top
        barrel_top_overlay_path = os.path.join(image_dir, "barrel", "source", "barrel_top_overlay.png")
        barrel_top_open_dark_path = os.path.join(image_dir, "barrel", "source", "barrel_top_open_dark.png")
        barrel_top_open_dark2_path = os.path.join(image_dir, "barrel", "source", "barrel_top_open_dark2.png")
        barrel_top_open_dark3_path = os.path.join(image_dir, "barrel", "source", "barrel_top_open_dark3.png")
        barrel_top_dark_path = os.path.join(image_dir, "barrel", "source", "barrel_top_dark.png")
        barrel_side_overlay_path = os.path.join(image_dir, "barrel", "source", "barrel_side_overlay.png")
        barrel_bottom_path = os.path.join(image_dir, "barrel", "source", "barrel_bottom_mask.png")

        # Paths for wood-specific planks and stripped logs
        plank_path = os.path.join(image_dir, "block", "planks", f"{wood}_planks.png")
        stripped_log_path = os.path.join(image_dir, "block", f"stripped_{wood}_log.png")

        # Barrel top
        output_path = os.path.join(image_dir, "barrel", f"{wood}_barrel_top.png")
        barrel_top_img = Image.open(stripped_log_path).convert("RGBA")
        barrel_top_dark = Image.open(barrel_top_dark_path).convert("RGBA")
        barrel_top_overlay = Image.open(barrel_top_overlay_path).convert("RGBA")

        # Apply darkening mask
        barrel_top_img = apply_barrel_darkening_mask(barrel_top_img, barrel_top_dark, 0.43)
        
        # Add overlay
        barrel_top_img = overlay_texture_transparent(barrel_top_img, barrel_top_overlay)
        barrel_top_img.save(output_path)

        # Barrel top open
        output_path = os.path.join(image_dir, "barrel", f"{wood}_barrel_top_open.png")
        barrel_top_open_img = Image.open(stripped_log_path).convert("RGBA")
        barrel_top_open_dark = Image.open(barrel_top_open_dark_path).convert("RGBA")
        barrel_top_open_dark2 = Image.open(barrel_top_open_dark2_path).convert("RGBA")
        barrel_top_open_dark3 = Image.open(barrel_top_open_dark3_path).convert("RGBA")

        # Apply darkening masks
        for mask in [barrel_top_open_dark, barrel_top_open_dark2, barrel_top_open_dark3]:
            barrel_top_open_img = apply_barrel_darkening_mask(barrel_top_open_img, mask, 0.4)

        barrel_top_open_img.save(output_path)

        # Barrel side
        output_path = os.path.join(image_dir, "barrel", f"{wood}_barrel_side.png")
        barrel_side_img = Image.open(plank_path).convert("RGBA")
        barrel_side_overlay = Image.open(barrel_side_overlay_path).convert("RGBA")

        # Rotate planks image
        barrel_side_img = barrel_side_img.rotate(90, expand=True)

        # Add side overlay (masking out white background)
        barrel_side_img = overlay_texture(barrel_side_img, barrel_side_overlay)
        barrel_side_img.save(output_path)

        # Barrel bottom
        output_path = os.path.join(image_dir, "barrel", f"{wood}_barrel_bottom.png")
        barrel_bottom_img = Image.open(plank_path).convert("RGBA")
        barrel_bottom_img_overlay = Image.open(stripped_log_path).convert("RGBA")
        barrel_bottom_mask = Image.open(barrel_bottom_path).convert("L")

        # Apply mask to stripped log
        barrel_bottom_overlay = Image.composite(Image.new("RGBA", barrel_bottom_img_overlay.size, (0, 0, 0, 0)), barrel_bottom_img_overlay, barrel_bottom_mask)

        # Combine planks base with masked stripped log overlay
        barrel_bottom_img = Image.alpha_composite(barrel_bottom_img, barrel_bottom_overlay)
        barrel_bottom_img.save(output_path)
