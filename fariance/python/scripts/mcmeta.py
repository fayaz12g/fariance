import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

def generate_mcmeta():
    item_output_dir = os.path.join(output_dir, "assets", "fariance", "textures", "item")
    
    # Ensure the output directory exists
    os.makedirs(item_output_dir, exist_ok=True)
    
    for material, tool, stick in product(MATERIAL_TYPES, TOOL_TYPES, STICK_TYPES):
        # Generate the prismarine animation files
        if material == "prismarine":
            mcmeta_content = {
                "animation": {
                    "frametime": 300,
                    "interpolate": True,
                    "frames": [
                        0, 1, 0, 2, 0, 3, 0, 1, 2, 1, 3, 1, 0, 2, 1, 2, 3, 2, 0, 3, 1, 3
                    ]
                }
            }
            
            file_name = f"{material}_{tool}_with_{stick}_stick.png"
            mcmeta_path = os.path.join(item_output_dir, f"{file_name}.mcmeta")
            
            with open(mcmeta_path, 'w') as mcmeta_file:
                json.dump(mcmeta_content, mcmeta_file, indent=2)

            # print(f"Generated MCMETA file: {mcmeta_path}")