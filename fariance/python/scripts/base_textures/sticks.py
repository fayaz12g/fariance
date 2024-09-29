import os
from PIL import Image, ImageEnhance, ImageOps
from base_constants import *
from base_functions import *

def generate_sticks():
    for mask_suffix in SUFFIXES:
        output_dir = os.path.join(stick_output_dir, mask_suffix)
        os.makedirs(output_dir, exist_ok=True)

        for stick_type in STICK_TYPES:
            stick_mask_path = os.path.join(mask_dir, "stick", f"{stick_type}.png")
            if not os.path.exists(stick_mask_path) or mask_suffix==("sword"):
                stick_mask_path = os.path.join(mask_dir, "stick", mask_suffix + ".png")

            stick_mask_image = Image.open(stick_mask_path).convert("RGBA")

            if stick_type in STICK_TYPES and stick_type not in ["blaze", "breeze", "bamboo"]:
                block_filename = f"{stick_type}_log.png"
                block_path = os.path.join(block_dir, "log", block_filename)

                if not os.path.exists(block_path):
                    print(f"Warning: Missing log texture for {stick_type}. Using default.")
                    block_path = os.path.join(block_dir, "log", "default.png")
                    

                block_image = Image.open(block_path).convert("RGBA")
                result_image = apply_mask(block_image, stick_mask_image)
                result_image = darken_stick_top(result_image, 0.59)
                result_image = darken_stick_bottom(result_image, 0.35)

                output_path = os.path.join(output_dir, f"{stick_type}.png")
                result_image.save(output_path)
            print(f"Generated {stick_type} {mask_suffix} sticks")