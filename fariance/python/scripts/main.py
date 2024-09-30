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
from tooltags import *
from copyres import *

def main():

    # Generate lang file
    generate_lang_entries()

    # Generate item models
    generate_models()

    # Generate blockstates
    generate_blockstates()

    # Generate climbable json
    generate_climbable_json()

    # Generate mineable json
    generate_mineable_json()
   
   # Generate trapdoor climbable json
    generate_trapdoor_climbable_ladders_json()
    
    # Generate loot tables
    generate_loot_tables()

    # Generate recipes
    generate_recipes()

    # Generate breaking recipes
    break_vanilla_recipes()

    # Generate textures
    generate_textures()

    # Generate animation files
    generate_mcmeta()

    # Add the tools to the tags are those tool types
    create_tool_tags()

    # Copy the required resources from newer minecraft versions
    copy_resources()

    print("Mod content generation complete!")

if __name__ == "__main__":
    main()
