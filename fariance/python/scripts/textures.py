import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

# Create a new list that excludes "bamboo"
filtered_wood_types = [wood for wood in STICK_TYPES if wood not in ["bamboo", "blaze", "breeze"]]

def combine_head_and_stick(head_img, stick_img, tool, stick):
    # Create a base image for combining
    base_width = max(stick_img.width, head_img.width)
    base_height = max(stick_img.height, head_img.height)
    
    # Create a new blank image for combining
    combined_img = Image.new("RGBA", (base_width, base_height), (0, 0, 0, 0))
    
    # Adjustments based on tool type
    offset_stick = (0, 0)
    offset_head = (0, 0)
    if tool == 'sword' and stick in ["breeze", "blaze", "bamboo"]:
        offset_stick = (0, -1)
    
    # Paste the stick and head images onto the combined image
    combined_img.paste(stick_img, offset_stick, stick_img)
    combined_img.paste(head_img, offset_head, head_img)
    
    return combined_img

def generate_textures():
    print("Starting texture generation...")
    os.makedirs(item_output_dir, exist_ok=True)
    os.makedirs(block_output_dir, exist_ok=True)
    os.makedirs(entity_output_dir, exist_ok=True)

    ingot_textures()
    tool_textures()
    stick_textures()
    crafting_table_textures()
    furnace_textures()
    ladder_textures()
    shield_textures()
    bed_textures()
    new_plank_textures()

    print(f"Texture generation done!")

def tool_textures():
    # Loop through each combination of material, tool, and stick
    for material, tool, stick in product(MATERIAL_TYPES, TOOL_TYPES, STICK_TYPES):
        if stick in ["blaze", "breeze", "bamboo"]:
            stick_image_path = os.path.join(image_dir, "stick", f"{stick}.png")
        else:
            if tool == "shovel":
                stick_image_path = os.path.join(image_dir, "stick", "shovel", f"{stick}.png")
            elif tool == "sword":
                stick_image_path = os.path.join(image_dir, "stick", "sword", f"{stick}.png")
            else:
                stick_image_path = os.path.join(image_dir, "stick", "tool", f"{stick}.png")
        
        if material == "prismarine":
            prismarine_variants = ["one", "two", "three", "four"]
            head_image_paths = [os.path.join(image_dir, "head", f"prismarine_{variant}", f"{tool}.png") for variant in prismarine_variants]
            
            if all(os.path.exists(path) for path in head_image_paths) and os.path.exists(stick_image_path):
                stick_img = Image.open(stick_image_path).convert("RGBA")
                head_imgs = [Image.open(path).convert("RGBA") for path in head_image_paths]
                
                # Combine each prismarine head with the stick
                combined_imgs = [combine_head_and_stick(head_img, stick_img, tool, stick) for head_img in head_imgs]
                
                # Create the final 16x64 image
                final_width = combined_imgs[0].width
                final_height = sum(img.height for img in combined_imgs)
                final_img = Image.new("RGBA", (final_width, final_height), (0, 0, 0, 0))
                
                # Paste the combined images vertically
                current_height = 0
                for img in combined_imgs:
                    final_img.paste(img, (0, current_height))
                    current_height += img.height
                
                # Save the final combined image
                output_path = os.path.join(item_output_dir, f"{material}_{tool}_with_{stick}_stick.png")
                final_img.save(output_path)
                # print(f"Generated prismarine texture: {output_path}")
            else:
                print(f"Warning: Missing textures for prismarine_{tool}_with_{stick}_stick")
        else:
            head_image_path = os.path.join(image_dir, "head", material, f"{tool}.png")
            
            if os.path.exists(stick_image_path) and os.path.exists(head_image_path):
                stick_img = Image.open(stick_image_path).convert("RGBA")
                head_img = Image.open(head_image_path).convert("RGBA")
                
                combined_img = combine_head_and_stick(head_img, stick_img, tool, stick)
                
                # Save the combined image
                output_path = os.path.join(item_output_dir, f"{material}_{tool}_with_{stick}_stick.png")
                combined_img.save(output_path)
                # print(f"Generated texture: {output_path}")
            elif not os.path.exists(stick_image_path):
                print(f"Warning: {stick_image_path} not found!")
            elif not os.path.exists(head_image_path):
                print(f"Warning: {head_image_path} not found!")
            else:
                print(f"Warning: Missing texture for {material}_{tool}_with_{stick}_stick")


def stick_textures():
    # Generate textures for sticks
    for stick in STICK_TYPES:
        if stick not in ["blaze", "bamboo", "breeze"]:
            stick_image_path = os.path.join(image_dir, "stick", "default", f"{stick}.png")
            if os.path.exists(stick_image_path):
                output_path = os.path.join(item_output_dir, f"{stick}_stick.png")
                stick_img = Image.open(stick_image_path).convert("RGBA")
                stick_img.save(output_path)
                # print(f"Generated texture: {output_path}")
            else:
                print(f"Warning: Missing texture for {stick}_stick")

def ladder_textures():
    # Generate textures for ladders
    for wood in STICK_TYPES:
        ladder_image_path = os.path.join(image_dir, "ladder", f"{wood}_ladder.png")
        if os.path.exists(ladder_image_path):
            output_path = os.path.join(block_output_dir, f"{wood}_ladder.png")
            ladder_img = Image.open(ladder_image_path).convert("RGBA")
            ladder_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {wood}_ladder")


def new_plank_textures():
    # Generate ne wplank textures
    for wood in NEW_WOOD:
            plank_image_path = os.path.join(image_dir, "block", "planks", f"{wood}_planks.png")
            if os.path.exists(plank_image_path):
                output_path = os.path.join(item_output_dir, f"{wood}_planks.png")
                ingot_img = Image.open(plank_image_path).convert("RGBA")
                ingot_img.save(output_path)
                # print(f"Generated texture: {output_path}")
            else:
                print(f"Warning: Missing texture for {wood}_planks")

            # New log
            log_image_path = os.path.join(image_dir, "block", f"{wood}_log.png")
            if os.path.exists(log_image_path):
                output_path = os.path.join(item_output_dir, f"{wood}_log.png")
                ingot_img = Image.open(log_image_path).convert("RGBA")
                ingot_img.save(output_path)
                # print(f"Generated texture: {output_path}")
            else:
                print(f"Warning: Missing texture for {wood}_log")

            # New stripped log
            stripped_log_image_path = os.path.join(image_dir, "block", f"stripped_{wood}_log.png")
            if os.path.exists(log_image_path):
                output_path = os.path.join(item_output_dir, f"stripped_{wood}_log.png")
                ingot_img = Image.open(stripped_log_image_path).convert("RGBA")
                ingot_img.save(output_path)
                # print(f"Generated texture: {output_path}")
            else:
                print(f"Warning: Missing texture for stripped {wood}_log")

            # New stripped log
            stripped_log_image_path = os.path.join(image_dir, "block", f"stripped_{wood}_log_top.png")
            if os.path.exists(log_image_path):
                output_path = os.path.join(item_output_dir, f"stripped_{wood}_log_top.png")
                ingot_img = Image.open(stripped_log_image_path).convert("RGBA")
                ingot_img.save(output_path)
                # print(f"Generated texture: {output_path}")
            else:
                print(f"Warning: Missing texture for {wood}_log_top stripped")

            # New stripped log
            stripped_log_image_path = os.path.join(image_dir, "block", f"{wood}_log_top.png")
            if os.path.exists(log_image_path):
                output_path = os.path.join(item_output_dir, f"{wood}_log_top.png")
                ingot_img = Image.open(stripped_log_image_path).convert("RGBA")
                ingot_img.save(output_path)
                # print(f"Generated texture: {output_path}")
            else:
                print(f"Warning: Missing texture for {wood}_log_top")



def ingot_textures():
    # Generate copper ingot textures
    for ingot in COPPER_TYPES:
            ingot_image_path = os.path.join(image_dir, "copper", "ingots", f"{ingot}_ingot.png")
            if os.path.exists(ingot_image_path):
                output_path = os.path.join(item_output_dir, f"{ingot}_ingot.png")
                ingot_img = Image.open(ingot_image_path).convert("RGBA")
                ingot_img.save(output_path)
                # print(f"Generated texture: {output_path}")
            else:
                print(f"Warning: Missing texture for {ingot}_ingot")

def bed_textures():
    # Generate bed textures
    for wood in WOOD_TYPES:
        for color in WOOL_TYPES:
            # Bed item
            bed_item_path = os.path.join(image_dir, "bed", "item", f"{wood}_{color}_bed.png")
            if os.path.exists(bed_item_path):
                output_path = os.path.join(item_output_dir, f"{wood}_{color}_bed.png")
                bed_item_img = Image.open(bed_item_path).convert("RGBA")
                bed_item_img.save(output_path)
                # print(f"Generated texture: {output_path}")
            else:
                print(f"Warning: Missing texture for {wood}_{color}_bed")
            
            # Bed Block (entity)
            bed_block_dir = os.path.join(entity_output_dir, "bed")
            os.makedirs(bed_block_dir, exist_ok=True)  # Create the directory if it doesn't exist

            bed_block_path = os.path.join(image_dir, "bed", "block", f"{wood}_{color}.png")

            if os.path.exists(bed_block_path):
                output_path = os.path.join(bed_block_dir, f"{wood}_{color}.png")
                bed_block_img = Image.open(bed_block_path).convert("RGBA")
                bed_block_img.save(output_path)
                # print(f"Generated texture: {output_path}")
            else:
                print(f"Warning: Missing texture for {wood}_{color} bed entity")

def furnace_textures():
    # Generate textures for furnaces
    for stone in STONE_TYPES:
        furnace_image_top = os.path.join(image_dir, "furnace", f"{stone}_furnace_top.png")
        furnace_image_side = os.path.join(image_dir, "furnace", f"{stone}_furnace_side.png")
        furnace_image_front = os.path.join(image_dir, "furnace", f"{stone}_furnace_front.png")
        furnace_image_front_on = os.path.join(image_dir, "furnace", f"{stone}_furnace_front_on.png")
        if os.path.exists(furnace_image_top):
            output_path = os.path.join(block_output_dir, f"{stone}_furnace_top.png")
            top_img = Image.open(furnace_image_top).convert("RGBA")
            top_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {stone} Furnace Top")
        if os.path.exists(furnace_image_side):
            output_path = os.path.join(block_output_dir, f"{stone}_furnace_side.png")
            side_img = Image.open(furnace_image_side).convert("RGBA")
            side_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {stone} Furnace Side")
        if os.path.exists(furnace_image_front):
            output_path = os.path.join(block_output_dir, f"{stone}_furnace_front.png")
            front_img = Image.open(furnace_image_front).convert("RGBA")
            front_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {stone} Furnace Front On")
        if os.path.exists(furnace_image_front_on):
            output_path = os.path.join(block_output_dir, f"{stone}_furnace_front_on.png")
            front_on_img = Image.open(furnace_image_front_on).convert("RGBA")
            front_on_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {stone} Furnace Front")

def crafting_table_textures():
    # Generate textures for crafting tables
    for wood in WOOD_TYPES:
        table_image_top = os.path.join(image_dir, "table", f"{wood}_crafting_table_top.png")
        table_image_side = os.path.join(image_dir, "table", f"{wood}_crafting_table_side.png")
        table_image_front = os.path.join(image_dir, "table", f"{wood}_crafting_table_front.png")
        if os.path.exists(table_image_top):
            output_path = os.path.join(block_output_dir, f"{wood}_crafting_table_top.png")
            top_img = Image.open(table_image_top).convert("RGBA")
            top_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {wood} Crafting Table Top")
        if os.path.exists(table_image_side):
            output_path = os.path.join(block_output_dir, f"{wood}_crafting_table_side.png")
            side_img = Image.open(table_image_side).convert("RGBA")
            side_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {wood} Crafting Table Side")
        if os.path.exists(table_image_front):
            output_path = os.path.join(block_output_dir, f"{wood}_crafting_table_front.png")
            front_img = Image.open(table_image_front).convert("RGBA")
            front_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {wood} Crafting Table Front")

def shield_textures():
    # Generate textures for ladders
    for wood in WOOD_TYPES:
        for material in MATERIAL_BASE:
            shield_image_path = os.path.join(image_dir, "shield", f"{wood}_{material}_shield_base.png")
            shield_nopattern_image_path = os.path.join(image_dir, "shield", f"{wood}_{material}_shield_base_nopattern.png")

            # Generate shield image
            if os.path.exists(shield_image_path):
                output_path = os.path.join(item_output_dir, f"{wood}_{material}_shield_base.png")
                shield_img = Image.open(shield_image_path).convert("RGBA")
                shield_img.save(output_path)
                # print(f"Generated texture: {output_path}")
            else:
                print(f"Warning: Missing texture for {wood}_{material}_shield_base")
            
            # Generate shield no pattern image
            if os.path.exists(shield_nopattern_image_path):
                nopattern_output_path = os.path.join(item_output_dir, f"{wood}_{material}_shield_base_nopattern.png")
                shield_nopat_img = Image.open(shield_nopattern_image_path).convert("RGBA")
                shield_nopat_img.save(nopattern_output_path)
                # print(f"Generated texture: {nopattern_output_path}")
            else:
                print(f"Warning: Missing texture for {wood}_{material}_shield_base_nopattern")
