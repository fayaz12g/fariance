import os

# Define constants
NEW_WOOD = ["pale_oak", "charred", "tyrian", "azalea"]
WOOD_TYPES = ["oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo"] + NEW_WOOD
TOOL_TYPES = ["sword", "pickaxe", "shovel", "hoe", "axe"]
MATERIAL_BASE = ["iron", "diamond", "gold", "netherite"]
MATERIAL_NEW =   ["amethyst", "redstone", "lapis", "quartz"]
STICK_TYPES = ["blaze", "breeze"] + WOOD_TYPES + ["stripped_" + s for s in WOOD_TYPES]
COPPER_TYPES = ["shiny_copper", "weathered_copper", "exposed_copper", "oxidized_copper"]
STONE_TYPES = ["cobblestone", "deepslate", "andesite", "diorite", "granite", "blackstone", "prismarine", "sandstone", "red_sandstone", "end_stone", "tuff"]
PRISMARINE_TYPES = ["prismarine_one", "prismarine_two","prismarine_three","prismarine_four"]

MATERIAL_TYPES = MATERIAL_BASE + MATERIAL_NEW + COPPER_TYPES + STONE_TYPES + WOOD_TYPES + PRISMARINE_TYPES


WOOL_COLORS = ["black", "blue", "brown", "cyan", "gray", "green", "light_blue", "light_gray", "lime", "magenta", "orange", "pink", "purple",
               "red", "white", "yellow"]


TORCH_TYPES= ["normal", "soul", "redstone"]

# Define potions types
POTION_TYPES = [
    "mundane", "thick", "awkward", "night_vision", "invisibility", "leaping",
    "fire_resistance", "swiftness", "slowness", "turtle_master", "water_breathing",
    "healing", "harming", "poison", "regeneration", "strength", "weakness", "luck",
    "slow_falling"
]

script_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(script_dir, "../../image")
mask_dir = os.path.join(image_dir, "mask")
block_dir = os.path.join(image_dir, "block")
head_output_dir = os.path.join(image_dir, "head")
stick_output_dir = os.path.join(image_dir, "stick")
furnace_dir = os.path.join(image_dir, "furnace")
table_dir = os.path.join(image_dir, "table")
overlay_dir = os.path.join(block_dir, "overlay")

SUFFIXES = ["default", "tool", "shovel", "sword"]