import os
from PIL import Image
from base_constants import *
from base_functions import *

torch_dir = os.path.join(image_dir, "torch")
torch_source = os.path.join(image_dir, "source", "torch")

def generate_torch(wood, torch_type, is_stripped=False):
    if torch_type == "normal":
        torch_name = f"{wood}_torch"
    else:
        torch_name = f"{wood}_{torch_type}_torch"

    wood_dir = "planks" if is_stripped else "log"
    wood_texture_path = os.path.join(block_dir, wood_dir, f"{wood}_{wood_dir}.png")
    if not os.path.exists(wood_texture_path):
        print(f"Warning: Missing texture for {wood} {wood_dir}")
        wood_texture_path = os.path.join(block_dir, "log", "default.png")

    wood_texture = Image.open(wood_texture_path).convert("RGBA")

    overlays = ["overlay"]
    if torch_type == "redstone":
        overlays.append("off_overlay")

    for overlay in overlays:
        overlay_path = os.path.join(torch_source, f"{torch_type}_{overlay}.png")
        if not os.path.exists(overlay_path):
            print(f"Warning: Missing torch {overlay} texture for {torch_type} at {overlay_path}")
            continue

        overlay_texture = Image.open(overlay_path).convert("RGBA")

        wood_mask_texture = Image.open(os.path.join(torch_source, "stick_mask.png")).convert("RGBA")
        wood_dark_mask_texture = Image.open(os.path.join(torch_source, "dark_mask.png")).convert("RGBA")

        torch_stick_image = apply_mask(wood_texture, wood_mask_texture)
        torch_stick_image = apply_darkening_mask(torch_stick_image, wood_dark_mask_texture)

        full_torch_image = overlay_texture_transparent(torch_stick_image, overlay_texture)

        prefix = "stripped_" if is_stripped else ""
        suffix = "_off" if overlay == "off_overlay" else ""
        output_path = os.path.join(torch_dir, f"{prefix}{torch_name}{suffix}.png")
        full_torch_image.save(output_path)

def generate_all_torches():
    for wood in WOOD_TYPES:
        for torch_type in TORCH_TYPES:
            generate_torch(wood, torch_type, is_stripped=False)
            generate_torch(wood, torch_type, is_stripped=True)
    print("Done generating all torch textures")
