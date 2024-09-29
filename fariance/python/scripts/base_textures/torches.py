import os
from PIL import Image, ImageEnhance, ImageOps
from base_constants import *
from base_functions import *

torch_dir = os.path.join(image_dir, "torch")
torch_source = os.path.join(image_dir, "source", "torch")

def generate_torches():
    for wood in WOOD_TYPES:
        wood_texture_path = os.path.join(block_dir, "log", f"{wood}_log.png")
        if not os.path.exists(wood_texture_path):
            print(f"Warning: Missing texture for {wood} log in log dir")
            wood_texture_path = os.path.join(block_dir, "log", f"default.png")
        
        wood_texture = Image.open(wood_texture_path).convert("RGBA")
        
        overlay_path = os.path.join(torch_source, f"overlay.png")
        if not os.path.exists(overlay_path):
            print(f"Warning: Missing torch overlay texture")
            continue
        
        overlay_texture = Image.open(overlay_path).convert("RGBA")

        wood_mask_path = os.path.join(torch_source, "stick_mask.png")
        wood_mask_texture = Image.open(wood_mask_path).convert("RGBA")

        wood_dark_mask_path = os.path.join(torch_source, "dark_mask.png")
        wood_dark_mask_texture = Image.open(wood_dark_mask_path).convert("RGBA")

        torch_stick_image = apply_mask(wood_texture, wood_mask_texture)

        torch_stick_image =  apply_darkening_mask(torch_stick_image, wood_dark_mask_texture)

        full_torch_image = overlay_texture_transparent(torch_stick_image, overlay_texture)

        output_path = os.path.join(torch_dir, f"{wood}_torch.png")
        full_torch_image.save(output_path)
        
    print("Done generating torch textures")

def generate_stripped_torches():
    for wood in WOOD_TYPES:
        wood_texture_path = os.path.join(block_dir, "planks", f"{wood}_planks.png")
        if not os.path.exists(wood_texture_path):
            print(f"Warning: Missing texture for {wood} log in log dir")
            wood_texture_path = os.path.join(block_dir, "log", f"default.png")
        
        wood_texture = Image.open(wood_texture_path).convert("RGBA")
        
        overlay_path = os.path.join(torch_source, f"overlay.png")
        if not os.path.exists(overlay_path):
            print(f"Warning: Missing torch overlay texture")
            continue
        
        overlay_texture = Image.open(overlay_path).convert("RGBA")

        wood_mask_path = os.path.join(torch_source, "stick_mask.png")
        wood_mask_texture = Image.open(wood_mask_path).convert("RGBA")

        wood_dark_mask_path = os.path.join(torch_source, "dark_mask.png")
        wood_dark_mask_texture = Image.open(wood_dark_mask_path).convert("RGBA")

        torch_stick_image = apply_mask(wood_texture, wood_mask_texture)

        torch_stick_image =  apply_darkening_mask(torch_stick_image, wood_dark_mask_texture)

        full_torch_image = overlay_texture_transparent(torch_stick_image, overlay_texture)

        output_path = os.path.join(torch_dir, f"stripped_{wood}_torch.png")
        full_torch_image.save(output_path)
        
    print("Done generating torch textures")

def generate_all_torches():
    generate_torches()
    generate_stripped_torches()