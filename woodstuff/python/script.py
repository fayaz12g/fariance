import json
from itertools import product
import os
from PIL import Image, ImageOps

# Define constants
WOOD_TYPES = ["oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo"]
TOOL_TYPES = ["sword", "pickaxe", "shovel", "hoe", "axe"]
MATERIAL_TYPES = WOOD_TYPES + ["iron", "diamond", "copper", "gold", "netherite", "amethyst", "diorite", "andesite", "granite", "blackstone", "cobblestone", "redstone", "lapis", "quartz", "deepslate"]
STICK_TYPES = WOOD_TYPES + ["blaze", "breeze"]
# Create a new list that excludes "bamboo"
filtered_wood_types = [wood for wood in WOOD_TYPES if wood != "bamboo"]

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

# Correcting "Dark Oak" formatting
def capitalize_material(material):
    if material == "dark_oak":
        return "Dark Oak"
    return material.capitalize()

def generate_item_registry():
    items = []

    # Materials that already exist as valid tiers
    existing_tiers = ["iron", "diamond", "gold", "netherite"]

    for material, tool, stick in product(MATERIAL_TYPES, TOOL_TYPES, STICK_TYPES):
        item_name = f"{material}_{tool}_with_{stick}_stick"

        # Determine the correct tier based on the material
        if material in WOOD_TYPES:
            tier = "WOOD"
        elif material not in existing_tiers:
            tier = "STONE"  # Default to STONE if the tier doesn't exist
        else:
            tier = material.upper()  # Use the material name as tier for existing tiers

        items.append(f'GENERATED_ITEMS.put("{item_name}", ITEMS.register("{item_name}", () -> new {tool.capitalize()}Item(Tiers.{tier}, new Item.Properties())));')

    # Add wood-type sticks to registry
    for stick in filtered_wood_types:
        stick_name = f"{stick}_stick"
        items.append(f'GENERATED_ITEMS.put("{stick_name}", ITEMS.register("{stick_name}", () -> new Item(new Item.Properties())));')

    # Add ladders for every wood type
    for wood in WOOD_TYPES + ["blaze", "breeze"]:
        ladder_name = f"{wood}_ladder"
        items.append(f'GENERATED_ITEMS.put("{ladder_name}", ITEMS.register("{ladder_name}", () -> new BlockItem(Blocks.LADDER, new Item.Properties())));')

    print(f"Registry generation done!")
    return "\n".join(items)


def generate_lang_entries():
    entries = {}
    for material, tool, stick in product(MATERIAL_TYPES, TOOL_TYPES, STICK_TYPES):
        item_name = f"{material}_{tool}_with_{stick}_stick"
        display_name = f"{capitalize_material(material)} {tool.capitalize()} with {capitalize_material(stick)} Stick"
        entries[f"item.woodstuff.{item_name}"] = display_name
    
    # Add sticks to lang file
    for stick in filtered_wood_types:
        stick_name = f"{stick}_stick"
        entries[f"item.woodstuff.{stick_name}"] = f"{capitalize_material(stick)} Stick"
    
    # Add ladders items to lang file
    for wood in WOOD_TYPES + ["blaze", "breeze"]:
        ladder_name = f"{wood}_ladder"
        entries[f"item.woodstuff.{ladder_name}"] = f"{capitalize_material(wood)} Ladder"

    # Add ladders blocks to lang file
    for wood in WOOD_TYPES + ["blaze", "breeze"]:
        ladder_name = f"{wood}_ladder"
        entries[f"block.woodstuff.{ladder_name}"] = f"{capitalize_material(wood)} Ladder"
    
    return json.dumps(entries, indent=2)

def generate_climbable_json(output_dir):
    # Define the climbable tag structure
    climbable_data = {
        "replace": False,
        "values": [
            f"woodstuff:{wood}_ladder" for wood in WOOD_TYPES  # Add each wood ladder to the values list
        ]
    }

    # Build the full output path for the mineable/axe.json file
    climbable_file_path = os.path.join(output_dir, "data", "minecraft", "tags", "blocks")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(climbable_file_path), exist_ok=True)

    # Define the output path for the climbable.json file
    climbable_file_path = os.path.join(climbable_file_path, "climbable.json")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(climbable_file_path), exist_ok=True)

    # Write the climbable data to the file
    with open(climbable_file_path, 'w') as f:
        json.dump(climbable_data, f, indent=2)

    print(f"Climbable ladders JSON generated at: {climbable_file_path}")

def generate_item_models(output_dir):
    item_model_dir = os.path.join(output_dir, "assets", "woodstuff", "models", "item")
    block_model_dir = os.path.join(output_dir, "assets", "woodstuff", "models", "block")
    os.makedirs(item_model_dir, exist_ok=True)
    os.makedirs(block_model_dir, exist_ok=True)

    for material, tool, stick in product(MATERIAL_TYPES, TOOL_TYPES, STICK_TYPES):
        item_name = f"{material}_{tool}_with_{stick}_stick"
        model_data = {
            "parent": "item/handheld",
            "textures": {
                "layer0": f"woodstuff:item/{item_name}"
            }
        }
        model_file_path = os.path.join(item_model_dir, f"{item_name}.json")
        with open(model_file_path, 'w') as f:
            json.dump(model_data, f, indent=2)

    # Generate models for sticks
    for stick in WOOD_TYPES + ["blaze", "breeze"]:
        stick_name = f"{stick}_stick"
        model_data = {
            "parent": "item/generated",
            "textures": {
                "layer0": f"woodstuff:item/{stick_name}"
            }
        }
        model_file_path = os.path.join(item_model_dir, f"{stick_name}.json")
        with open(model_file_path, 'w') as f:
            json.dump(model_data, f, indent=2)

    # Loop through each wood type and generate the corresponding models
    for wood in WOOD_TYPES:
        ladder_name = f"{wood}_ladder"
        
        # Block model data for the ladder
        block_model_data = {
            "ambientocclusion": False,
            "textures": {
                "particle": f"woodstuff:block/{ladder_name}",
                "texture": f"woodstuff:block/{ladder_name}"
            },
            "elements": [
                {
                    "from": [0, 0, 15.2],
                    "to": [16, 16, 15.2],
                    "shade": False,
                    "faces": {
                        "north": {
                            "uv": [0, 0, 16, 16],
                            "texture": "#texture"
                        },
                        "south": {
                            "uv": [16, 0, 0, 16],
                            "texture": "#texture"
                        }
                    }
                }
            ]
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{ladder_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Item model data for the ladder
        item_model_data = {
            "parent": "minecraft:item/generated",
            "textures": {
                "layer0": f"woodstuff:block/{ladder_name}"
            }
        }

        # Define the item model output path (in the models/item folder)
        item_model_file_path = os.path.join(item_model_dir, f"{ladder_name}.json")

        # Write the item model data to the file
        with open(item_model_file_path, 'w') as f:
            json.dump(item_model_data, f, indent=2)

    print("Models generation finished!.")


def generate_recipes():
    recipes = []

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

    # Material-to-item mapping to account for the naming differences
    material_mappings = {
        **{wood: f"minecraft:{wood}_planks" for wood in WOOD_TYPES},  # Wood types use "wood_planks"
        "iron": "minecraft:iron_ingot",
        "diamond": "minecraft:diamond",
        "copper": "minecraft:copper_ingot",
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
        "deepslate": "minecraft:cobbled_deepslate"
    }

    # Generate recipes for each tool with its specific pattern
    for material, tool, stick in product(MATERIAL_TYPES, TOOL_TYPES, STICK_TYPES):
        item_name = f"{material}_{tool}_with_{stick}_stick"

        # Stick type mapping
        stick_item = f"woodstuff:{stick}_stick" if stick in WOOD_TYPES else f"minecraft:{stick}_rod"
        if stick == "bamboo":
            stick_item = "minecraft:bamboo"

        # Use the mapped material name from the material_mappings dictionary
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",  # Add category
            "pattern": tool_patterns[tool],  # Use the correct pattern for the tool
            "key": {
                "M": {"item": material_mappings[material]},
                "S": {"item": stick_item}
            },
            "result": {
                "item": f"woodstuff:{item_name}",
                "count": 1
            }
        }
        recipes.append((item_name, json.dumps(recipe, indent=2)))

    # Add recipes for crafting sticks using two planks of the corresponding wood type
    for wood in WOOD_TYPES:
        stick_name = f"{wood}_stick"
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",  # Add category
            "pattern": [
                "P",
                "P"
            ],
            "key": {
                "P": {"item": f"minecraft:{wood}_planks"}
            },
            "result": {
                "item": f"woodstuff:{stick_name}",
                "count": 4
            }
        }
        recipes.append((stick_name, json.dumps(recipe, indent=2)))

    # Add recipes for ladders for each wood type
    for wood in WOOD_TYPES:
        ladder_name = f"{wood}_ladder"
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",  # Add category
            "pattern": [
                "S S",
                "SSS",
                "S S"
            ],
            "key": {
                "S": {"item": f"woodstuff:{wood}_stick"}
            },
            "result": {
                "item": f"woodstuff:{ladder_name}",
                "count": 3
            }
        }
        recipes.append((ladder_name, json.dumps(recipe, indent=2)))
   
    print(f"Recipe generation done!")
    return recipes


def generate_textures():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(script_dir, "image")
    item_output_dir = os.path.join(script_dir, "output", "assets", "woodstuff", "textures", "item")
    block_output_dir = os.path.join(script_dir, "output", "assets", "woodstuff", "textures", "block")
    os.makedirs(item_output_dir, exist_ok=True)
    os.makedirs(block_output_dir, exist_ok=True)

    # Loop through each combination of material, tool, and stick
    for material, tool, stick in product(MATERIAL_TYPES, TOOL_TYPES, STICK_TYPES):
        stick_image_path = os.path.join(image_dir, "stick", f"{stick}.png")
        head_image_path = os.path.join(image_dir, "head", material, f"{tool}.png")
        
        if os.path.exists(stick_image_path) and os.path.exists(head_image_path):
            stick_img = Image.open(stick_image_path).convert("RGBA")
            head_img = Image.open(head_image_path).convert("RGBA")
            
            # Create a base image for combining, adjust size based on tool requirements
            base_width = max(stick_img.width, head_img.width)
            base_height = max(stick_img.height, head_img.height)
            
            # Adjustments based on tool type
            if tool == 'sword':
                offset_stick = (0, 1)
                offset_head = (0, 0)
            elif tool == 'shovel':
                offset_stick = (0, 1)
                offset_head = (0, -1)
            elif tool in ['pickaxe', 'hoe']:
                offset_stick = (0, 0)
                offset_head = (0, -1)
            elif tool == 'axe':
                offset_stick = (0, 1)
                offset_head = (1, -1)
            
            # Create a new blank image for combining
            combined_img = Image.new("RGBA", (base_width, base_height), (0, 0, 0, 0))
            
            # Paste the stick and head images onto the combined image
            combined_img.paste(stick_img, offset_stick, stick_img)
            combined_img.paste(head_img, offset_head, head_img)
            
            # Save the combined image
            output_path = os.path.join(item_output_dir, f"{material}_{tool}_with_{stick}_stick.png")
            combined_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {material}_{tool}_with_{stick}_stick")

    # Generate textures for sticks
    for stick in filtered_wood_types:
        stick_image_path = os.path.join(image_dir, "stick", f"{stick}.png")
        if os.path.exists(stick_image_path):
            output_path = os.path.join(item_output_dir, f"{stick}_stick.png")
            stick_img = Image.open(stick_image_path).convert("RGBA")
            stick_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {stick}_stick")

    # Generate textures for ladders
    for wood in WOOD_TYPES  + ["blaze", "breeze"]:
        ladder_image_path = os.path.join(image_dir, "ladder", f"{wood}_ladder.png")
        if os.path.exists(ladder_image_path):
            output_path = os.path.join(block_output_dir, f"{wood}_ladder.png")
            ladder_img = Image.open(ladder_image_path).convert("RGBA")
            ladder_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {wood}_ladder")
   
    print(f"Texture generation done!")

def generate_blockstates(output_dir):

    # Ladder blockstates
    for wood in WOOD_TYPES:
        ladder_name = f"{wood}_ladder"
        blockstates_data = {
            "variants": {
                "facing=east": {
                    "model": f"woodstuff:block/{ladder_name}",
                    "y": 90
                },
                "facing=north": {
                    "model": f"woodstuff:block/{ladder_name}"
                },
                "facing=south": {
                    "model": f"woodstuff:block/{ladder_name}",
                    "y": 180
                },
                "facing=west": {
                    "model": f"woodstuff:block/{ladder_name}",
                    "y": 270
                }
            }
        }

        # Build the full output path for the mineable/axe.json file
        blockstates_dir = os.path.join(output_dir, "assets", "woodstuff", "blockstates")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(blockstates_dir), exist_ok=True)
        
        # Define the output path for the blockstates file
        blockstates_file_path = os.path.join(blockstates_dir, f"{ladder_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)

    print("Blockstates generated successfully.")

def generate_mineable_json(base_output_dir):
    # Define the mineable tag structure
    mineable_data = {
        "replace": False,
        "values": [
            f"woodstuff:{wood}_ladder" for wood in WOOD_TYPES  # Add each wood ladder to the values list
        ]
    }

    # Build the full output path for the mineable/axe.json file
    mineable_file_path = os.path.join(base_output_dir, "data", "minecraft", "tags", "blocks", "mineable", "axe.json")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(mineable_file_path), exist_ok=True)

    # Write the mineable data to the file
    with open(mineable_file_path, 'w') as f:
        json.dump(mineable_data, f, indent=2)

    print(f"Mineable ladders JSON generated at: {mineable_file_path}")

def generate_trapdoor_climbable_ladders_json(base_output_dir):
    # Define the tag structure for trapdoor climbable ladders
    trapdoor_climbable_data = {
        "values": [
            "minecraft:ladder"
        ] + [f"woodstuff:{wood}_ladder" for wood in WOOD_TYPES]  # Add each wood ladder after the Minecraft ladder
    }

    # Build the full output path for the trapdoor climbable ladders JSON
    trapdoor_climbable_file_path = os.path.join(base_output_dir, "data", "woodstuff", "tags", "block", "make_trapdoor_climbable_ladders.json")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(trapdoor_climbable_file_path), exist_ok=True)

    # Write the trapdoor climbable data to the file
    with open(trapdoor_climbable_file_path, 'w') as f:
        json.dump(trapdoor_climbable_data, f, indent=2)

    print(f"Trapdoor climbable ladders JSON generated at: {trapdoor_climbable_file_path}")

def generate_ladder_loot_tables(base_output_dir):
    # Loop through each wood type to create a loot table for each ladder
    for wood in WOOD_TYPES:
        ladder_name = f"{wood}_ladder"

        # Define the loot table structure
        loot_table_data = {
            "type": "minecraft:block",
            "pools": [
                {
                    "rolls": 1,
                    "entries": [
                        {
                            "type": "minecraft:item",
                            "name": f"woodstuff:{ladder_name}"
                        }
                    ]
                }
            ]
        }

        # Build the output file path for each ladder's loot table
        loot_table_file_path = os.path.join(base_output_dir, "data", "woodstuff", "loot_tables", "blocks", f"{ladder_name}.json")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(loot_table_file_path), exist_ok=True)

        # Write the loot table data to the file
        with open(loot_table_file_path, 'w') as f:
            json.dump(loot_table_data, f, indent=2)

    print(f"Loot tables generated!")

# Ensure that the directory exists before writing the lang file
lang_file_path = "./output/assets/woodstuff/lang/en_us.json"
lang_dir = os.path.dirname(lang_file_path)
os.makedirs(lang_dir, exist_ok=True)  # Create directories if they don't exist

# Define the path for recipe files
recipe_file_path = "./output/data/woodstuff/recipes"
recipe_dir = os.path.dirname(recipe_file_path)
os.makedirs(recipe_dir, exist_ok=True) # Create the directory if it doesn't exist

script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
output_dir = os.path.join(script_dir, "output")  # Join with the relative output path
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist


def main():
    # Generate item registry
    with open("ItemRegistry.java", "w") as f:
        f.write(generate_item_registry())

    # Generate lang file
    with open(lang_file_path, "w") as f:
        f.write(generate_lang_entries())

    # Generate item models
    generate_item_models(output_dir)

    # Generate blockstates
    generate_blockstates(output_dir)

    # Generate climbable json
    generate_climbable_json(output_dir)

    # Generate mineable json
    generate_mineable_json(output_dir)
   
   # Generate trapdoor climbable json
    generate_trapdoor_climbable_ladders_json(output_dir)
    
    # Generate loot tables
    generate_ladder_loot_tables(output_dir)

    # Generate recipes and write them to files
    for item_name, recipe in generate_recipes():
        # Define the full path for the recipe file
        recipe_file = os.path.join(recipe_file_path, f"{item_name}.json")
        # Ensure the directory exists for the current file
        os.makedirs(os.path.dirname(recipe_file), exist_ok=True)
        with open(recipe_file, "w") as f:
            f.write(recipe)

    # Generate textures
    generate_textures()

    print("Mod content generation complete!")

if __name__ == "__main__":
    main()
