import os

script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
output_dir = os.path.join(script_dir, "../../src/main/resources")  # Join with the relative output path
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

image_dir = os.path.join(script_dir, "../image")
item_output_dir = os.path.join(output_dir, "assets", "fariance", "textures", "item")
block_output_dir = os.path.join(output_dir, "assets", "fariance", "textures", "block")
entity_output_dir = os.path.join(output_dir, "assets", "fariance", "textures", "entity")

# Define constants
WOOD_TYPES = ["oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo"]
TOOL_TYPES = ["sword", "pickaxe", "shovel", "hoe", "axe"]
MATERIAL_BASE = ["iron", "diamond", "gold", "netherite"]
MATERIAL_NEW =   ["amethyst", "redstone", "lapis", "quartz"]
STICK_TYPES = ["blaze", "breeze"] + WOOD_TYPES + ["stripped_" + s for s in WOOD_TYPES]
COPPER_TYPES = ["shiny_copper", "weathered_copper", "exposed_copper", "oxidized_copper"]
STONE_TYPES = ["cobblestone", "deepslate", "andesite", "diorite", "granite", "blackstone", "prismarine", "sandstone", "red_sandstone"]

MATERIAL_TYPES = MATERIAL_BASE + STONE_TYPES + MATERIAL_NEW + COPPER_TYPES + WOOD_TYPES

# Define potions types
POTION_TYPES = [
    "mundane", "thick", "awkward", "night_vision", "invisibility", "leaping",
    "fire_resistance", "swiftness", "slowness", "turtle_master", "water_breathing",
    "healing", "harming", "poison", "regeneration", "strength", "weakness", "luck",
    "slow_falling"
]

# Create a new list that excludes "bamboo"
filtered_wood_types = [wood for wood in STICK_TYPES if wood not in ["bamboo", "blaze", "breeze"]]


# Define material properties (durability, mining level, etc.)
MATERIAL_PROPERTIES = {
    "oak": {"durability": 20, "mining_level": 0, "enchantability": 16},
    "spruce": {"durability": 62, "mining_level": 0, "enchantability": 14},
    "birch": {"durability": 58, "mining_level": 0, "enchantability": 17},
    "jungle": {"durability": 63, "mining_level": 0, "enchantability": 15},
    "acacia": {"durability": 61, "mining_level": 0, "enchantability": 16},
    "dark_oak": {"durability": 65, "mining_level": 0, "enchantability": 14},
    "mangrove": {"durability": 84, "mining_level": 0, "enchantability": 15},
    "cherry": {"durability": 57, "mining_level": 0, "enchantability": 18},
    "crimson": {"durability": 96, "mining_level": 0, "enchantability": 13},
    "warped": {"durability": 87, "mining_level": 0, "enchantability": 13},
    "bamboo": {"durability": 55, "mining_level": 0, "enchantability": 20},
    "stone": {"durability": 131, "mining_level": 1, "enchantability": 5},
    "iron": {"durability": 250, "mining_level": 2, "enchantability": 14},
    "diamond": {"durability": 1561, "mining_level": 3, "enchantability": 10},
    "gold": {"durability": 32, "mining_level": 0, "enchantability": 22},
    "netherite": {"durability": 2031, "mining_level": 4, "enchantability": 15},
    "copper": {"durability": 200, "mining_level": 1, "enchantability": 12},
    "amethyst": {"durability": 500, "mining_level": 2, "enchantability": 18},
    "diorite": {"durability": 150, "mining_level": 1, "enchantability": 6},
    "andesite": {"durability": 150, "mining_level": 1, "enchantability": 6},
    "granite": {"durability": 150, "mining_level": 1, "enchantability": 6},
    "blackstone": {"durability": 180, "mining_level": 1, "enchantability": 7},
    "cobblestone": {"durability": 131, "mining_level": 1, "enchantability": 5},
    "redstone": {"durability": 300, "mining_level": 2, "enchantability": 16},
    "lapis": {"durability": 200, "mining_level": 2, "enchantability": 20},
    "quartz": {"durability": 250, "mining_level": 2, "enchantability": 18},
}

tabs = {
        "swords": "Fariance Swords",
        "pickaxes": "Fariance Pickaxes",
        "axes": "Fariance Axes",
        "shovels": "Fariance Shovels",
        "hoes": "Fariance Hoes",
        "misc": "Fariance Miscellaneous"
    }


# Recipe data
recipes = []
break_recipes = []

# Tool crafting patterns for each tool type
tool_patterns = {
    "sword": [
        " M ",
        " M ",
        " S "
    ],
    "pickaxe": [
        "MMM",
        " S ",
        " S "
    ],
    "shovel": [
        " M ",
        " S ",
        " S "
    ],
    "hoe": [
        "MM ",
        " S ",
        " S "
    ],
    "axe": [
        "MM ",
        "MS ",
        " S "
    ]
}

# Material-to-item mapping to account for the naming differences in recipes
material_mappings = {
    **{wood: f"minecraft:{wood}_planks" for wood in WOOD_TYPES},  # Wood types use "wood_planks"
    "iron": "minecraft:iron_ingot",
    "diamond": "minecraft:diamond",
    "shiny_copper": "minecraft:copper_ingot",
    "exposed_copper": "fariance:exposed_copper_ingot",
    "weathered_copper": "fariance:weathered_copper_ingot",
    "oxidized_copper": "fariance:oxidized_copper_ingot",
    "gold": "minecraft:gold_ingot",
    "netherite": "minecraft:netherite_ingot",
    "amethyst": "minecraft:amethyst_shard",
    "diorite": "minecraft:diorite",
    "andesite": "minecraft:andesite",
    "granite": "minecraft:granite",
    "blackstone": "minecraft:blackstone",
    "cobblestone": "minecraft:cobblestone",
    "redstone": "minecraft:redstone",
    "lapis": "minecraft:lapis_lazuli",
    "quartz": "minecraft:nether_quartz",
    "deepslate": "minecraft:cobbled_deepslate",
    "prismarine": "minecraft:prismarine",
    "sandstone": "minecraft:sandstone",
    "red_sandstone": "minecraft:red_sandstone"
}

# Lang data
entries = {}