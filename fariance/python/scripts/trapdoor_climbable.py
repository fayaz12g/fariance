import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

def generate_trapdoor_climbable_ladders_json():
    # Define the tag structure for trapdoor climbable ladders
    trapdoor_climbable_data = {
        "values": [
            "minecraft:ladder"
        ] + [f"fariance:{wood}_ladder" for wood in STICK_TYPES]  # Add each wood ladder after the Minecraft ladder
    }

    # Build the full output path for the trapdoor climbable ladders JSON
    trapdoor_climbable_file_path = os.path.join(output_dir, "data", "fariance", "tags", "block", "make_trapdoor_climbable_ladders.json")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(trapdoor_climbable_file_path), exist_ok=True)

    # Write the trapdoor climbable data to the file
    with open(trapdoor_climbable_file_path, 'w') as f:
        json.dump(trapdoor_climbable_data, f, indent=2)

    print(f"Trapdoor climbable ladders JSON generated")
