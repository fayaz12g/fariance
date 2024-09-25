import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

def create_tool_tags():
    # Create the directory path for the output: "data/minecraft/tags/items"
    items_dir = os.path.join(output_dir, "data", "minecraft", "tags", "items")
    os.makedirs(items_dir, exist_ok=True)
    
    # Loop over TOOL_TYPES to create a file for each tool type
    for tool in TOOL_TYPES:
        tool_values = []

        # Iterate over all combinations of material, tool, and stick types
        for material, stick in product(MATERIAL_TYPES, STICK_TYPES):
            item_name = f"fariance:{material}_{tool}_with_{stick}_stick"
            
            # Add tool name to list (for JSON output)
            tool_values.append(item_name)

        # Create the content for the JSON file
        tool_data = {
            "replace": False,
            "values": tool_values
        }

        # Write each tool file to the corresponding JSON file
        tool_file_path = os.path.join(items_dir, f"{tool}.json")
        with open(tool_file_path, 'w') as f:
            json.dump(tool_data, f, indent=2)

    print(f"Generated tool tags.")
