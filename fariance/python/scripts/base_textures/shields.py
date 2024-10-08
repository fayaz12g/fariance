import os
from PIL import Image, ImageEnhance, ImageOps
from base_constants import *
from base_functions import *

shield_dir = os.path.join(image_dir, "shield")
shield_masks_dir = os.path.join(shield_dir, "masks")

shield_material_dir = os.path.join(shield_masks_dir, "material")
shield_wood_dir = os.path.join(shield_masks_dir, "wood")


def generate_shields():
    for material in MATERIAL_BASE:
        for wood in WOOD_TYPES:
            # Get the block image for the material from block_dir (16x16)
            material_block_path = os.path.join(block_dir, f"{material}_block.png")
            material_block_image = Image.open(material_block_path)

            # Tile the material block image to 64x64
            tiled_material_block_image = tile_image(material_block_image, target_size=(64, 64))

            # Get the material mask from shield_material_dir (64x64)
            material_mask_path = os.path.join(shield_material_dir, "shield_base_nopattern.png")
            material_mask_image = Image.open(material_mask_path)

            # Apply the material mask to the tiled material block image
            masked_material_image = apply_mask(tiled_material_block_image, material_mask_image)

            # Get the block image for the wood from block_dir (16x16)
            wood_block_path = os.path.join(block_dir, f"stripped_{wood}_log.png")
            wood_block_image = Image.open(wood_block_path)

            # Tile the wood block image to 64x64
            tiled_wood_block_image = tile_image(wood_block_image, target_size=(64, 64))

            # Get the wood mask from shield_wood_dir (64x64)
            wood_mask_path = os.path.join(shield_wood_dir, "shield_base_nopattern.png")
            wood_mask_image = Image.open(wood_mask_path)

            # Apply the wood mask to the tiled wood block image
            masked_wood_image = apply_mask(tiled_wood_block_image, wood_mask_image)

            # Get the additive texture from shield_masks_dir (64x64)
            additive_texture_path = os.path.join(shield_masks_dir, "shield_base_nopattern.png")
            additive_texture_image = Image.open(additive_texture_path)

            # Combine the textures: first masked wood, then masked material, then the additive
            combined_image = overlay_texture_transparent(masked_wood_image, masked_material_image)
            combined_image = overlay_texture_transparent(combined_image, additive_texture_image)

            # Get the darkening mask from shield_masks_dir (64x64)
            darkening_mask_path = os.path.join(shield_masks_dir, "shield_base_nopattern_dark.png")
            darkening_mask_image = Image.open(darkening_mask_path)

            # Apply the darkening mask to the combined image
            final_shield_image = apply_darkening_mask(combined_image, darkening_mask_image)

            # Save the final shield texture
            shield_texture_path = os.path.join(shield_dir, f"{wood}_{material}_shield_base_nopattern.png")
            final_shield_image.save(shield_texture_path)
            
            # Now overlay the "shield_base" from masks_dir on top of the final image
            shield_base_path = os.path.join(shield_masks_dir, "shield_base.png")
            shield_base_image = Image.open(shield_base_path)

            # Overlay the "shield_base" image onto the final shield image
            final_shield_with_base = overlay_texture_transparent(final_shield_image, shield_base_image)

            # Save the final shield texture with "shield_base"
            shield_texture_path = os.path.join(shield_dir, f"{wood}_{material}_shield_base.png")
            final_shield_with_base.save(shield_texture_path)

            # print(f"Generated {wood} {material} shields!")

        print(f"Generated {material} shields!")