from PIL import Image, ImageEnhance, ImageOps

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