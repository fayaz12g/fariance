from base_constants import *
from furnaces import *
from crafting_tables import *
from heads import *
from sticks import *


if __name__ == "__main__":
    # Generate the tool heads
    generate_tool_heads()

    # Generate sticks
    generate_sticks()

    # Generate the Furnace textures and Crafting Tables
    generate_furnace_textures()
    generate_crafting_table_textures()
