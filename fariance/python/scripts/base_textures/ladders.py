import os
from PIL import Image, ImageEnhance, ImageOps
from base_constants import *
from base_functions import *

def generate_ladders():
    output_dir = os.path.join(image_dir, "ladder")
    source_dir = os.path.join(image_dir, "source", "ladder")
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(source_dir, exist_ok=True)

    for stick_type in STICK_TYPES:
        if stick_type.startswith("stripped_"):
            # Remove "stripped_" from the stick_type
            new_stick_type = stick_type[len("stripped_"):]
            ladder_mask_path = os.path.join(source_dir, f"{new_stick_type}_ladder.png")
        else:
            ladder_mask_path = os.path.join(source_dir, f"{stick_type}_ladder.png")
        if not os.path.exists(ladder_mask_path):
            print(f"Warning: Missing mask texture for {stick_type} ladder")
            continue
    
        ladder_mask_image = Image.open(ladder_mask_path).convert("RGBA")

        block_filename = f"{stick_type}_log.png"
        block_path = os.path.join(block_dir, "log", block_filename)

        if not os.path.exists(block_path):
            print(f"Warning: Missing log texture for {stick_type}")
            continue

        block_image = Image.open(block_path).convert("RGBA")
        result_image = apply_mask(block_image, ladder_mask_image)
        result_image = darken_edges(result_image, 0.69)

        output_path = os.path.join(output_dir, f"{stick_type}_ladder.png")
        result_image.save(output_path)

        print(f"Generated {stick_type} ladder")