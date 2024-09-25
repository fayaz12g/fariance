import os
from PIL import Image, ImageEnhance, ImageOps
from base_constants import *
from base_functions import *

shield_dir = os.path.join(image_dir, "shield")
shield_masks_dir = os.path.join(image_dir, "masks")

shield_material_dir = os.path.join(shield_masks_dir, "material")
shield_wood_dir = os.path.join(shield_masks_dir, "wood")


def generate_shields():
    for material in MATERIAL_BASE:
        for wood in WOOD_TYPES:
            # Get the block image for the material from block_dir
            material_block_path = os.path.join(block_dir, f"{material}_block.png")
            material_block_image = Image.open(material_block_path)

            # Get the material mask from shield_material_dir
            material_mask_path = os.path.join(shield_material_dir, "shield_base_nopattern.png")
            material_mask_image = Image.open(material_mask_path)

            # Apply the material mask to the material block image
            masked_material_image = apply_mask(material_block_image, material_mask_image)

            # Get the block image for the wood from block_dir
            wood_block_path = os.path.join(block_dir, f"stripped_{wood}_log.png")
            wood_block_image = Image.open(wood_block_path)

            # Get the wood mask from shield_wood_dir
            wood_mask_path = os.path.join(shield_wood_dir, "shield_base_nopattern.png")
            wood_mask_image = Image.open(wood_mask_path)

            # Apply the wood mask to the wood block image
            masked_wood_image = apply_mask(wood_block_image, wood_mask_image)

            # Get the additive texture from shield_masks_dir
            additive_texture_path = os.path.join(shield_masks_dir, "shield_base_nopattern.png")
            additive_texture_image = Image.open(additive_texture_path)

            # Combine the textures: first masked wood, then masked material, then the additive
            combined_image = overlay_texture(masked_wood_image, masked_material_image)
            combined_image = overlay_texture(combined_image, additive_texture_image)

            # Get the darkening mask from shield_masks_dir
            darkening_mask_path = os.path.join(shield_masks_dir, "shield_base_nopattern_dark.png")
            darkening_mask_image = Image.open(darkening_mask_path)

            # Apply the darkening mask to the combined image
            final_shield_image = apply_darkening_mask(combined_image, darkening_mask_image)

            # Save the final shield texture
            shield_texture_path = os.path.join(shield_dir, f"{wood}_{material}_shield_base_nopattern.png")
            final_shield_image.save(shield_texture_path)

    print(f"Generated {material} shields!")
