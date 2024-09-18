import os
from PIL import Image, ImageEnhance

# Define constants
TOOL_TYPES = ["sword", "pickaxe", "shovel", "hoe", "axe"]
WOOD_TYPES = ["oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo"]
OTHER_MATERIALS = ["iron", "diamond", "copper", "gold", "netherite", "amethyst", "diorite", "andesite", "granite", "blackstone", "cobblestone", "redstone", "lapis", "quartz", "deepslate"]
MATERIAL_TYPES = WOOD_TYPES + OTHER_MATERIALS
STICK_TYPES = WOOD_TYPES + ["blaze", "breeze"]

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

def apply_special_mask(tool_image, special_mask_image):
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



def generate_tool_heads_and_sticks():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mask_dir = os.path.join(script_dir, "mask")
    block_dir = os.path.join(script_dir, "block")
    head_output_dir = os.path.join(script_dir, "head")
    stick_output_dir = os.path.join(script_dir, "stick")

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
            result_image = darken_edges(result_image, 0.4)

            # Check for special mask
            special_mask_path = os.path.join(mask_dir, "tool", "special", tool + ".png")
            if os.path.exists(special_mask_path):
                special_mask_image = Image.open(special_mask_path).convert("RGBA")
                result_image = apply_special_mask(result_image, special_mask_image)
                
            # Save the resulting image
            output_path = os.path.join(material_output_dir, f"{tool}.png")
            result_image.save(output_path)
            print(f"Generated: {output_path}")

    # Generate sticks
    os.makedirs(stick_output_dir, exist_ok=True)

    for stick_type in STICK_TYPES:
        stick_mask_path = os.path.join(mask_dir, "stick", f"{stick_type}.png")
        if not os.path.exists(stick_mask_path):
            stick_mask_path = os.path.join(mask_dir, "stick", "default.png")

        stick_mask_image = Image.open(stick_mask_path).convert("RGBA")

        if stick_type in WOOD_TYPES and stick_type != "bamboo":
            block_filename = f"stripped_{stick_type}_log.png"
            block_path = os.path.join(block_dir, block_filename)

            if not os.path.exists(block_path):
                print(f"Warning: Missing log texture for {stick_type}")
                continue

            block_image = Image.open(block_path).convert("RGBA")
            result_image = apply_mask(block_image, stick_mask_image)
            result_image = darken_edges(result_image, 0.69)

            output_path = os.path.join(stick_output_dir, f"{stick_type}.png")
            result_image.save(output_path)
            print(f"Generated: {output_path}")

if __name__ == "__main__":
    generate_tool_heads_and_sticks()
