import os

# Define constants
WOOD_TYPES = ["oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo"]
TOOL_TYPES = ["sword", "pickaxe", "shovel", "hoe", "axe"]
MATERIAL_BASE = ["iron", "diamond", "gold", "netherite"]
MATERIAL_NEW =   ["amethyst", "redstone", "lapis", "quartz"]
STICK_TYPES = ["blaze", "breeze"] + WOOD_TYPES + ["stripped_" + s for s in WOOD_TYPES]
COPPER_TYPES = ["shiny_copper", "weathered_copper", "exposed_copper", "oxidized_copper"]
STONE_TYPES = ["cobblestone", "deepslate", "andesite", "diorite", "granite", "blackstone", "prismarine"]
PRISMARINE_TYPES = ["prismarine_one", "prismarine_two","prismarine_three","prismarine_four"]

MATERIAL_TYPES = MATERIAL_BASE + MATERIAL_NEW + COPPER_TYPES + STONE_TYPES + WOOD_TYPES + PRISMARINE_TYPES

script_dir = os.path.dirname(os.path.abspath(__file__))
mask_dir = os.path.join(script_dir, "mask")
block_dir = os.path.join(script_dir, "block")
head_output_dir = os.path.join(script_dir, "head")
stick_output_dir = os.path.join(script_dir, "stick")
furnace_dir = os.path.join(script_dir, "furnace")
table_dir = os.path.join(script_dir, "table")
overlay_dir = os.path.join(block_dir, "overlay")

SUFFIXES = ["default", "tool", "shovel", "sword"]