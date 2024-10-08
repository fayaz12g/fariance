from base_constants import *
from furnaces import *
from crafting_tables import *
from heads import *
from sticks import *
from shields import *
from ladders import *
from beds import *
from torches import *
from barrel import *

def main():
    # Generate the tool heads
    generate_tool_heads()

    # Generate stick textures
    generate_sticks()

    # Generate the Furnace textures
    generate_furnace_textures()

    # Generate and Crafting Table textures
    generate_crafting_table_textures()

    # Generate the shield textures
    generate_shields()

    # Generate the ladder textures
    generate_ladders()

    # Generate the bed textures
    generate_beds()

    # Generate the bed textures
    generate_all_torches()

    # Generate the barrel textures
    barrel_textures()

if __name__ == "__main__":
    main()