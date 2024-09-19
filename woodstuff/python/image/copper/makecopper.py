import os
from PIL import Image, ImageEnhance

COPPER_TYPES = ["shiny", "exposed", "oxidized", "weathered"]

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

def darken_copper_top(image, amount):
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

def darken_copper_bottom(image, amount):
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


def generate_copper_ingots():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mask_dir = os.path.join(script_dir, "mask")
    block_dir = os.path.join(script_dir, "block")
    output_dir = os.path.join(script_dir, "ingots")

    # Generate tool heads
    for type in COPPER_TYPES:
        mask_path = os.path.join(block_dir, f"{type}_copper.png")
        block_path = os.path.join(mask_dir, "copper_ingot.png")

        if not os.path.exists(mask_path):
            print(f"Warning: Missing mask for {type}")
            continue

        mask_image = Image.open(mask_path).convert("RGBA")
        block_image = Image.open(block_path).convert("RGBA")

        result_image = apply_mask(block_image, mask_image)
        result_image = darken_copper_top(result_image, 0.59)
        result_image = darken_copper_bottom(result_image, 0.35)
        
        # Check for brightening mask (tool_bright.png)
        bright_mask_path = os.path.join(mask_dir, "bar.png")
        
        if os.path.exists(bright_mask_path):
            bright_mask_image = Image.open(bright_mask_path).convert("RGBA")
            result_image = apply_brightening_mask(result_image, bright_mask_image)
        
        # Save the resulting image
        output_path = os.path.join(output_dir, f"{type}_copper_ingot.png")
        result_image.save(output_path)
        print(f"Generated: {output_path}")


if __name__ == "__main__":
    generate_copper_ingots()
