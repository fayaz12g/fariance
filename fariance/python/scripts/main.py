import json
from itertools import product
import os
from PIL import Image, ImageOps
from blockstates import *
from lang import *
from break_recipes import *
from climbable import *
from loot_tables import *
from mcmeta import *
from mineable import *
from models import *
from recipes import *
from speed import *
from textures import *
from trapdoor_climbable import *
from constants import *

def main():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
    output_dir = os.path.join(script_dir, "../../src/main/resources")  # Join with the relative output path
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    # Generate lang file
    generate_lang_entries(output_dir)

    # Generate item models
    generate_models(output_dir)

    # Generate blockstates
    generate_blockstates(output_dir)

    # Generate climbable json
    generate_climbable_json(output_dir)

    # Generate mineable json
    generate_mineable_json(output_dir)
   
   # Generate trapdoor climbable json
    generate_trapdoor_climbable_ladders_json(output_dir)
    
    # Generate loot tables
    generate_loot_tables(output_dir)

    # Generate recipes
    generate_recipes(output_dir)

    # Generate breaking recipes
    break_vanilla_recipes(output_dir)

    # Generate textures
    generate_textures()

    # Generate animation files
    generate_mcmeta()

    print("Mod content generation complete!")

if __name__ == "__main__":
    main()
