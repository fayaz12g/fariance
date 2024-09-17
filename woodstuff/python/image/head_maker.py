import os
from PIL import Image, ImageChops

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

def darken_edges(image):
    # Create a slightly darker version of the image
    darkened = Image.new('RGBA', image.size, (0, 0, 0, 0))
    for x in range(image.width):
        for y in range(image.height):
            r, g, b, a = image.getpixel((x, y))
            darkened.putpixel((x, y), (int(r * 0.69), int(g * 0.69), int(b * 0.69), a))
    
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
            mask_path = os.path.join(mask_dir, f"{tool}.png")

            if not os.path.exists(mask_path):
                print(f"Warning: Missing mask for {tool}")
                continue

            mask_image = Image.open(mask_path).convert("RGBA")

            result_image = apply_mask(block_image, mask_image)
            result_image = darken_edges(result_image)

            # Save the resulting image
            output_path = os.path.join(material_output_dir, f"{tool}.png")
            result_image.save(output_path)
            print(f"Generated: {output_path}")

    # Generate sticks
    os.makedirs(stick_output_dir, exist_ok=True)
    stick_mask_path = os.path.join(mask_dir, "stick.png")

    if not os.path.exists(stick_mask_path):
        print("Warning: Missing stick mask")
    else:
        stick_mask_image = Image.open(stick_mask_path).convert("RGBA")

        for stick_type in STICK_TYPES:
            if stick_type in WOOD_TYPES:
                block_filename = f"stripped_{stick_type}_log.png"
                block_path = os.path.join(block_dir, block_filename)

                if not os.path.exists(block_path):
                    print(f"Warning: Missing log texture for {stick_type}")
                    continue

                block_image = Image.open(block_path).convert("RGBA")
                result_image = apply_mask(block_image, stick_mask_image)
                result_image = darken_edges(result_image)

                output_path = os.path.join(stick_output_dir, f"{stick_type}.png")
                result_image.save(output_path)
                print(f"Generated: {output_path}")
            elif stick_type in ["blaze", "breeze"]:
                # For blaze and breeze, we assume there are specific textures
                stick_texture_path = os.path.join(block_dir, f"{stick_type}_rod.png")
                if not os.path.exists(stick_texture_path):
                    print(f"Warning: Missing texture for {stick_type} rod")
                    continue

                stick_texture = Image.open(stick_texture_path).convert("RGBA")
                result_image = apply_mask(stick_texture, stick_mask_image)
                result_image = darken_edges(result_image)

                output_path = os.path.join(stick_output_dir, f"{stick_type}.png")
                result_image.save(output_path)
                print(f"Generated: {output_path}")

if __name__ == "__main__":
    generate_tool_heads_and_sticks()