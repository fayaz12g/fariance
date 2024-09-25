import os
from PIL import Image, ImageEnhance, ImageOps

# Define constants
WOOD_TYPES = ["oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo"]
TOOL_TYPES = ["sword", "pickaxe", "shovel", "hoe", "axe"]
MATERIAL_BASE = ["iron", "diamond", "gold", "netherite"]
MATERIAL_NEW =   ["amethyst", "redstone", "lapis", "quartz"]
STICK_TYPES = ["blaze", "breeze"] + WOOD_TYPES + ["stripped_" + s for s in WOOD_TYPES]
COPPER_TYPES = ["shiny_copper", "weathered_copper", "exposed_copper", "oxidized_copper"]
STONE_TYPES = ["cobblestone", "deepslate", "andesite", "diorite", "granite", "blackstone", "prismarine"]

MATERIAL_TYPES = MATERIAL_BASE + MATERIAL_NEW + COPPER_TYPES + STONE_TYPES + WOOD_TYPES

script_dir = os.path.dirname(os.path.abspath(__file__))
mask_dir = os.path.join(script_dir, "mask")
block_dir = os.path.join(script_dir, "block")
head_output_dir = os.path.join(script_dir, "head")
stick_output_dir = os.path.join(script_dir, "stick")
furnace_dir = os.path.join(script_dir, "furnace")
table_dir = os.path.join(script_dir, "table")
overlay_dir = os.path.join(block_dir, "overlay")

def apply_mask(block_image, mask_image):
    # Resize block image to match mask size if necessary
    if block_image.size != mask_image.size:
        block_image = block_image.resize(mask_image.size, Image.LANCZOS)

    # Create a new image with an alpha channel
    result_image = Image.new("RGBA", mask_image.size, (0, 0, 0, 0))

    # Iterate through each pixel
    for x in range(mask_image.width):
        for y in range(mask_image.height):
            mask_pixel = mask_image.getpixel((x, y))
            if mask_pixel[3] > 0:  # If the mask pixel is not fully transparent
                result_image.putpixel((x, y), block_image.getpixel((x, y)))

    return result_image

def darken_stick_top(image, amount):
    # Create a slightly darker version of the image
    darkened = Image.new('RGBA', image.size, (0, 0, 0, 0))
    for x in range(image.width):
        for y in range(image.height):
            r, g, b, a = image.getpixel((x, y))
            darkened.putpixel((x, y), (int(r * amount), int(g * amount), int(b * amount), a))
    
    # Create a mask for the edges
    edge_mask = Image.new('L', image.size, 0)
    edge_pixels = edge_mask.load()
    width, height = image.size
    
    for y in range(height):
        for x in range(width):
            if image.getpixel((x, y))[3] > 0:  # If the pixel is not fully transparent
                # Check if any neighboring pixel is transparent
                if (image.getpixel((x, y-1))[3] == 0):
                    edge_pixels[x, y] = 255

    # Apply the darkened edges
    return Image.composite(darkened, image, edge_mask)

def darken_stick_bottom(image, amount):
    # Create a slightly darker version of the image
    darkened = Image.new('RGBA', image.size, (0, 0, 0, 0))
    for x in range(image.width):
        for y in range(image.height):
            r, g, b, a = image.getpixel((x, y))
            darkened.putpixel((x, y), (int(r * amount), int(g * amount), int(b * amount), a))
    
    # Create a mask for the edges
    edge_mask = Image.new('L', image.size, 0)
    edge_pixels = edge_mask.load()
    width, height = image.size
    
    for y in range(height):
        for x in range(width):
            if image.getpixel((x, y))[3] > 0:  # If the pixel is not fully transparent
                # Check if any neighboring pixel is transparent
                if (image.getpixel((x, y+1))[3] == 0):
                    edge_pixels[x, y] = 255

    # Apply the darkened edges
    return Image.composite(darkened, image, edge_mask)

def darken_edges(image, amount):
    # Create a slightly darker version of the image
    darkened = Image.new('RGBA', image.size, (0, 0, 0, 0))
    for x in range(image.width):
        for y in range(image.height):
            r, g, b, a = image.getpixel((x, y))
            darkened.putpixel((x, y), (int(r * amount), int(g * amount), int(b * amount), a))
    
    # Create a mask for the edges
    edge_mask = Image.new('L', image.size, 0)
    edge_pixels = edge_mask.load()
    width, height = image.size
    
    for y in range(height):
        for x in range(width):
            if image.getpixel((x, y))[3] > 0:  # If the pixel is not fully transparent
                # Check if any neighboring pixel is transparent
                if (x == 0 or y == 0 or x == width-1 or y == height-1 or
                    image.getpixel((x-1, y))[3] == 0 or
                    image.getpixel((x+1, y))[3] == 0 or
                    image.getpixel((x, y-1))[3] == 0 or
                    image.getpixel((x, y+1))[3] == 0):
                    edge_pixels[x, y] = 255

    # Apply the darkened edges
    return Image.composite(darkened, image, edge_mask)

def apply_darkening_mask(tool_image, special_mask_image):
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
                new_r = int(tool_r * (1 - darken_factor * 0.69))
                new_g = int(tool_g * (1 - darken_factor * 0.69))
                new_b = int(tool_b * (1 - darken_factor * 0.69))

                # Apply the darkened color back to the tool_image
                tool_image.putpixel((x, y), (new_r, new_g, new_b, tool_a))

    return tool_image

def apply_brightening_mask(tool_image, special_mask_image):
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

                # Brighten factor: 0 (full black) should brighten the least, 1 (full white) should brighten the most
                brighten_factor = mask_brightness

                # Get the corresponding pixel from tool_image
                tool_r, tool_g, tool_b, tool_a = tool_image.getpixel((x, y))

                # Brighten the tool_image pixel by increasing its RGB values
                new_r = int(tool_r + (255 - tool_r) * brighten_factor * 0.69)
                new_g = int(tool_g + (255 - tool_g) * brighten_factor * 0.69)
                new_b = int(tool_b + (255 - tool_b) * brighten_factor * 0.69)

                # Clamp the values to ensure they don't exceed 255
                new_r = min(255, new_r)
                new_g = min(255, new_g)
                new_b = min(255, new_b)

                # Apply the brightened color back to the tool_image
                tool_image.putpixel((x, y), (new_r, new_g, new_b, tool_a))

    return tool_image

def remove_white_pixels(image):
    """
    Remove white pixels from the image and replace them with transparent pixels.
    """
    # Create a new image with the same size and mode
    transparent_image = Image.new("RGBA", image.size)
    width, height = image.size

    # Process each pixel
    for x in range(width):
        for y in range(height):
            # Get the RGBA value of the pixel
            r, g, b, a = image.getpixel((x, y))
            # If the pixel is white, set it to transparent
            if r == 255 and g == 255 and b == 255:
                transparent_image.putpixel((x, y), (255, 255, 255, 0))  # Fully transparent
            else:
                transparent_image.putpixel((x, y), (r, g, b, a))  # Keep the original pixel

    return transparent_image

def generate_furnace_and_crafting_table_textures():
    # Create output directories if they don't exist
    os.makedirs(furnace_dir, exist_ok=True)
    os.makedirs(table_dir, exist_ok=True)

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

def overlay_texture(base_image, overlay_image):
    """
    Overlays the overlay_image on top of the base_image, replacing white pixels in the overlay with corresponding pixels from the base_image.
    """
    base_image = base_image.convert("RGBA")
    overlay_image = overlay_image.convert("RGBA")

    # Resize overlay if it doesn't match base image size
    if base_image.size != overlay_image.size:
        overlay_image = overlay_image.resize(base_image.size, Image.LANCZOS)

    # Get pixel data for both images
    base_pixels = base_image.load()
    overlay_pixels = overlay_image.load()

    # Loop through each pixel and replace white (or near-white) pixels with corresponding base pixels
    for y in range(overlay_image.height):
        for x in range(overlay_image.width):
            r, g, b, a = overlay_pixels[x, y]
            if (r, g, b) == (255, 255, 255) and a > 0:  # Check if the pixel is white
                overlay_pixels[x, y] = base_pixels[x, y]  # Replace it with the base image's pixel

    return overlay_image




def generate_tool_heads_and_sticks():

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


    # Generate sticks
    os.makedirs(stick_output_dir, exist_ok=True)

    for stick_type in STICK_TYPES:
        stick_mask_path = os.path.join(mask_dir, "stick", f"{stick_type}.png")
        if not os.path.exists(stick_mask_path):
            stick_mask_path = os.path.join(mask_dir, "stick", "default.png")

        stick_mask_image = Image.open(stick_mask_path).convert("RGBA")

        if stick_type in STICK_TYPES and stick_type not in ["blaze", "breeze", "bamboo"]:
            block_filename = f"{stick_type}_log.png"
            block_path = os.path.join(block_dir, "log", block_filename)

            if not os.path.exists(block_path):
                print(f"Warning: Missing log texture for {stick_type}")
                continue

            block_image = Image.open(block_path).convert("RGBA")
            result_image = apply_mask(block_image, stick_mask_image)
            result_image = darken_stick_top(result_image, 0.59)
            result_image = darken_stick_bottom(result_image, 0.35)

            output_path = os.path.join(stick_output_dir, f"{stick_type}.png")
            result_image.save(output_path)
        print(f"Generated {stick_type} sticks")

if __name__ == "__main__":
    generate_tool_heads_and_sticks()
    generate_furnace_and_crafting_table_textures()
