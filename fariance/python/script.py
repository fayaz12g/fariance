import json
from itertools import product
import os
from PIL import Image, ImageOps

# Define constants
WOOD_TYPES = ["oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo"]
TOOL_TYPES = ["sword", "pickaxe", "shovel", "hoe", "axe"]
MATERIAL_TYPES = WOOD_TYPES + ["iron", "diamond", "gold", "netherite", "amethyst", "redstone", "lapis", "quartz"]
STICK_TYPES = ["blaze", "breeze"] + WOOD_TYPES + ["stripped_" + s for s in WOOD_TYPES]
COPPER_TYPES = ["shiny_copper", "weathered_copper", "exposed_copper", "oxidized_copper"]
STONE_TYPES = ["cobblestone", "deepslate", "andesite", "diorite", "granite", "blackstone", "prismarine"]
MATERIAL_TYPES = MATERIAL_TYPES + COPPER_TYPES + STONE_TYPES

# Create a new list that excludes "bamboo"
filtered_wood_types = [wood for wood in STICK_TYPES if wood not in ["bamboo", "blaze", "breeze"]]

tabs = {
        "swords": "fariance Swords",
        "pickaxes": "fariance Pickaxes",
        "axes": "fariance Axes",
        "shovels": "fariance Shovels",
        "hoes": "fariance Hoes"
    }

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

# Correcting underscore formatting
def capitalize_material(material):
    if material == "shiny_copper":
        return "Copper"
    return material.replace("_", " ").title()

def generate_lang_entries():
    entries = {}
    
    # Creative mode tabs
    for tool_type, display_name in tabs.items():
        entries[f"itemGroup.fariance.{tool_type}"] = display_name

    # Add item names
    for material, tool, stick in product(MATERIAL_TYPES, TOOL_TYPES, STICK_TYPES):
        item_name = f"{material}_{tool}_with_{stick}_stick"
        if stick == "blaze":
            stick = "flaming"
        if stick == "breeze":
            stick = "light"

        # Check if the material matches the stick name or the second part after underscore matches material
        stick_parts = stick.split('_', 1)  # Split stick into two parts at the first underscore
        if material == stick or (len(stick_parts) > 1 and stick_parts[1] == material):
            display_name = f"{capitalize_material(stick)} {tool.capitalize()}"
        else:
            display_name = f"{capitalize_material(stick)} {capitalize_material(material)} {tool.capitalize()}"
        
        entries[f"item.fariance.{item_name}"] = display_name


    # Add sticks to lang file
    for stick in filtered_wood_types:
        stick_name = f"{stick}_stick"
        entries[f"item.fariance.{stick_name}"] = f"{capitalize_material(stick)} Stick"

    # Add crafting tables to lang file
    for wood in WOOD_TYPES:
        table_name = f"{wood}_crafting_table"
        entries[f"block.fariance.{table_name}"] = f"{capitalize_material(wood)} Crafting Table"

    # Add furnaces to lang file
    for stone in STONE_TYPES:
        furnace_name = f"{stone}_furnace"
        entries[f"block.fariance.{furnace_name}"] = f"{capitalize_material(stone)} Furnace"

    # Add copper types to lang file
    for ingot in COPPER_TYPES:
        ingot_name = f"{ingot}_ingot"
        entries[f"item.fariance.{ingot_name}"] = f"{capitalize_material(ingot)} Ingot"

    # Add ladders items to lang file
    for wood in WOOD_TYPES + ["blaze", "breeze"]:
        ladder_name = f"{wood}_ladder"
        entries[f"item.fariance.{ladder_name}"] = f"{capitalize_material(wood)} Ladder"

    # Add ladders blocks to lang file
    for wood in STICK_TYPES:
        ladder_name = f"{wood}_ladder"
        entries[f"block.fariance.{ladder_name}"] = f"{capitalize_material(wood)} Ladder"

    return json.dumps(entries, indent=2)

def generate_climbable_json(output_dir):
    # Define the climbable tag structure
    climbable_data = {
        "replace": False,
        "values": [
            f"fariance:{wood}_ladder" for wood in WOOD_TYPES  # Add each wood ladder to the values list
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

    print(f"Climbable ladders JSON generated")

def generate_models(output_dir):
    item_model_dir = os.path.join(output_dir, "assets", "fariance", "models", "item")
    block_model_dir = os.path.join(output_dir, "assets", "fariance", "models", "block")
    os.makedirs(item_model_dir, exist_ok=True)
    os.makedirs(block_model_dir, exist_ok=True)

    for material, tool, stick in product(MATERIAL_TYPES, TOOL_TYPES, STICK_TYPES):
        item_name = f"{material}_{tool}_with_{stick}_stick"
        model_data = {
            "parent": "item/handheld",
            "textures": {
                "layer0": f"fariance:item/{item_name}"
            }
        }
        model_file_path = os.path.join(item_model_dir, f"{item_name}.json")
        with open(model_file_path, 'w') as f:
            json.dump(model_data, f, indent=2)

    # Generate models for sticks
    for stick in STICK_TYPES:
        if stick not in ["blaze", "bamboo", "breeze"]:
            stick_name = f"{stick}_stick"
            model_data = {
                "parent": "item/generated",
                "textures": {
                    "layer0": f"fariance:item/{stick_name}"
                }
            }
            model_file_path = os.path.join(item_model_dir, f"{stick_name}.json")
            with open(model_file_path, 'w') as f:
                json.dump(model_data, f, indent=2)

    # Generate models for ingots
    for ingot in COPPER_TYPES:
        ingot_name = f"{ingot}_ingot"
        model_data = {
            "parent": "item/generated",
            "textures": {
                "layer0": f"fariance:item/{ingot_name}"
            }
        }
        model_file_path = os.path.join(item_model_dir, f"{ingot_name}.json")
        with open(model_file_path, 'w') as f:
            json.dump(model_data, f, indent=2)

    # Loop through each wood type and generate the corresponding models
    for wood in WOOD_TYPES:
        ladder_name = f"{wood}_ladder"
        
        # Block model data for the ladder
        block_model_data = {
            "ambientocclusion": False,
            "textures": {
                "particle": f"fariance:block/{ladder_name}",
                "texture": f"fariance:block/{ladder_name}"
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
                "layer0": f"fariance:block/{ladder_name}"
            }
        }

        # Define the item model output path (in the models/item folder)
        item_model_file_path = os.path.join(item_model_dir, f"{ladder_name}.json")

        # Write the item model data to the file
        with open(item_model_file_path, 'w') as f:
            json.dump(item_model_data, f, indent=2)

    # Loop through each wood type and generate the corresponding models for crafting tables
    for wood in WOOD_TYPES:
        table_name = f"{wood}_crafting_table"
        
        # Block model data for the crafting table
        block_model_data = {
        "parent": "minecraft:block/cube",
        "textures": {
            "down": f"minecraft:block/{wood}_planks",
            "east": f"fariance:block/{wood}_crafting_table_side",
            "north": f"fariance:block/{wood}_crafting_table_front",
            "particle": f"fariance:block/{wood}_crafting_table_front",
            "south": f"fariance:block/{wood}_crafting_table_side",
            "up": f"fariance:block/{wood}_crafting_table_top",
            "west": f"fariance:block/{wood}_crafting_table_front"
        }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{table_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Item model data for the crafting table
        item_model_data = {
            "parent": f"fariance:block/{wood}_crafting_table"
        }

        # Define the block model output path
        item_model_file_path = os.path.join(item_model_dir, f"{table_name}.json")
        
        # Write the block model data to the file
        with open(item_model_file_path, 'w') as f:
            json.dump(item_model_data, f, indent=2)
                
    # Loop through each stone type and generate the corresponding models for furnaces
    for stone in STONE_TYPES:
        furnace_name = f"{stone}_furnace"
        
        # Block model data for the ladder
        block_model_data = {
            "parent": "minecraft:block/orientable",
            "textures": {
                "front": f"fariance:block/{furnace_name}_front",
                "side": f"fariance:block/{furnace_name}_side",
                "top": f"fariance:block/{furnace_name}_top"
            }
            }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{furnace_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Item model data for the crafting table
        item_model_data = {
            "parent": f"fariance:block/{furnace_name}"
        }

        # Define the block model output path
        item_model_file_path = os.path.join(item_model_dir, f"{furnace_name}.json")
        
        # Write the block model data to the file
        with open(item_model_file_path, 'w') as f:
            json.dump(item_model_data, f, indent=2)

        # furnace on models
        furnace_on_name = f"{stone}_furnace_on"
        
        # Block model data for the ladder
        block_model_data = {
            "parent": "minecraft:block/orientable",
            "textures": {
                "front": f"fariance:block/{stone}_furnace_front_on",
                "side": f"fariance:block/{stone}_furnace_side",
                "top": f"fariance:block/{stone}_furnace_top"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{furnace_on_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)


    print("Models generation finished!.")

def break_recipes():
    break_recipes = []

    # Break recipes for crafting table 
    recipe = {
        "type": "minecraft:crafting_shaped",
        "category": "misc",
        "key": {
            "#": {
            "item": "minecraft:diamond_block"
            }
        },
        "pattern": [
            "##",
            "###"
        ],
        "result": {
            "count": 1,
            "id": "minecraft:crafting_table"
        }
    }
    break_recipes.append(("crafting_table", json.dumps(recipe, indent=2)))

    # Break recipes for furnace 
    recipe = {
        "type": "minecraft:crafting_shaped",
        "category": "misc",
        "key": {
            "#": {
            "item": "minecraft:diamond_block"
            }
        },
        "pattern": [
            "###",
            "##"
        ],
        "result": {
            "count": 1,
            "id": "minecraft:furnace"
        }
    }
    break_recipes.append(("furnace", json.dumps(recipe, indent=2)))

    # Break recipes for sticks 
    recipe = {
        "type": "minecraft:crafting_shaped",
        "category": "misc",
        "key": {
            "#": {
            "item": "minecraft:diamond_block"
            }
        },
        "pattern": [
            "##",
            "##"
        ],
        "result": {
            "count": 1,
            "id": "minecraft:stick"
        }
    }
    break_recipes.append(("stick", json.dumps(recipe, indent=2)))

    print(f"Recipe breaking done!")
    return break_recipes

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
        "prismarine": "minecraft:prismarine"
    }

    # Generate recipes for each tool with its specific pattern
    for material, tool, stick in product(MATERIAL_TYPES, TOOL_TYPES, STICK_TYPES):
        item_name = f"{material}_{tool}_with_{stick}_stick"

        # Stick type mapping
        stick_item = f"fariance:{stick}_stick" if stick not in ["blaze", "breeze"] else f"minecraft:{stick}_rod"
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
                "id": f"fariance:{item_name}",
                "count": 1
            }
        }
        recipes.append((item_name, json.dumps(recipe, indent=2)))

    # Add recipes for crafting sticks using two planks of the corresponding wood type
    for wood in STICK_TYPES:
        if wood not in ["blaze", "bamboo", "breeze"]:
            stick_name = f"{wood}_stick"
            if wood in ["crimson", "warped"]:
                log_type = "stem"
            else:
                log_type = "log"
            
            # Determine if the wood is stripped or not
            if wood.startswith("stripped_"):
                material = f"minecraft:stripped_{wood}_{log_type}"
                count = 16
            else:
                material = f"minecraft:{wood}_planks"
                count = 4

            # Create the recipe based on the material and count
            recipe = {
                "type": "minecraft:crafting_shaped",
                "category": "misc",  # Add category
                "pattern": [
                    "P",
                    "P"
                ],
                "key": {
                    "P": {"item": material}
                },
                "result": {
                    "id": f"fariance:{stick_name}",
                    "count": count
                }
            }

            # Append the recipe as JSON
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
                "S": {"item": f"fariance:{wood}_stick"}
            },
            "result": {
                "id": f"fariance:{ladder_name}",
                "count": 3
            }
        }
        recipes.append((ladder_name, json.dumps(recipe, indent=2)))
        # Make recipes for crafting table 
        table_name = f"{wood}_crafting_table"
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",
            "pattern": [
                "##",
                "##"
            ],
            "key": {
                "#": {
                "item": f"minecraft:{wood}_planks"
                }
            },
            "result": {
                "id": f"fariance:{wood}_crafting_table",
                "count": 1
            }
        }
        recipes.append((table_name, json.dumps(recipe, indent=2)))

    # Add recipes for furnaces for each stone type
    for stone in STONE_TYPES:
        furnace_name = f"{stone}_furnace"
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",
            "key": {
                "#": {
                "item": f"minecraft:{stone}"
                }
            },
            "pattern": [
                "###",
                "# #",
                "###"
            ],
            "result": {
                "count": 1,
                "id": f"fariance:{stone}_furnace"
            }
        }
        recipes.append((furnace_name, json.dumps(recipe, indent=2)))

    # Add recipes for ingots for each copper type
    for ingot in COPPER_TYPES:
        ingot_name = f"{ingot}_ingot"
        recipe = {
            "type": "minecraft:crafting_shaped",
            "category": "misc",  
            "pattern": [
                " S "
            ],
            "key": {
                "S": {"item": f"minecraft:{ingot}"}
            },
            "result": {
                "id": f"fariance:{ingot_name}",
                "count": 4
            }
        }
        recipes.append((ingot_name, json.dumps(recipe, indent=2)))

    print(f"Recipe generation done!")
    return recipes


def generate_textures():
    print("Starting texture generation...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(script_dir, "image")
    item_output_dir = os.path.join(script_dir, "../src/main/resources", "assets", "fariance", "textures", "item")
    block_output_dir = os.path.join(script_dir, "../src/main/resources", "assets", "fariance", "textures", "block")
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
                offset_stick = (0, -1)
                offset_head = (0, 0)
            elif tool == 'shovel':
                offset_stick = (0, 0)
                offset_head = (0, 0)
            elif tool == 'hoe':
                offset_stick = (0, 0)
                offset_head = (0, 0)
            elif tool == 'pickaxe':
                offset_stick = (0, 0)
                offset_head = (0, 0)
            elif tool == 'axe':
                offset_stick = (0, 0)
                offset_head = (0, 0)
            
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
    for stick in STICK_TYPES:
        if stick not in ["blaze", "bamboo", "breeze"]:
            stick_image_path = os.path.join(image_dir, "stick", f"{stick}.png")
            if os.path.exists(stick_image_path):
                output_path = os.path.join(item_output_dir, f"{stick}_stick.png")
                stick_img = Image.open(stick_image_path).convert("RGBA")
                stick_img.save(output_path)
                # print(f"Generated texture: {output_path}")
            else:
                print(f"Warning: Missing texture for {stick}_stick")

    # Generate textures for crafting tables
    for wood in WOOD_TYPES:
        table_image_top = os.path.join(image_dir, "table", f"{wood}_crafting_table_top.png")
        table_image_side = os.path.join(image_dir, "table", f"{wood}_crafting_table_side.png")
        table_image_front = os.path.join(image_dir, "table", f"{wood}_crafting_table_front.png")
        if os.path.exists(table_image_top):
            output_path = os.path.join(block_output_dir, f"{wood}_crafting_table_top.png")
            top_img = Image.open(table_image_top).convert("RGBA")
            top_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {wood} Crafting Table Top")
        if os.path.exists(table_image_side):
            output_path = os.path.join(block_output_dir, f"{wood}_crafting_table_side.png")
            side_img = Image.open(table_image_side).convert("RGBA")
            side_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {wood} Crafting Table Side")
        if os.path.exists(table_image_front):
            output_path = os.path.join(block_output_dir, f"{wood}_crafting_table_front.png")
            front_img = Image.open(table_image_front).convert("RGBA")
            front_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {wood} Crafting Table Front")

    # Generate textures for furnaces
    for stone in STONE_TYPES:
        furnace_image_top = os.path.join(image_dir, "furnace", f"{stone}_furnace_top.png")
        furnace_image_side = os.path.join(image_dir, "furnace", f"{stone}_furnace_side.png")
        furnace_image_front = os.path.join(image_dir, "furnace", f"{stone}_furnace_front.png")
        furnace_image_front_on = os.path.join(image_dir, "furnace", f"{stone}_furnace_front_on.png")
        if os.path.exists(furnace_image_top):
            output_path = os.path.join(block_output_dir, f"{stone}_furnace_top.png")
            top_img = Image.open(furnace_image_top).convert("RGBA")
            top_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {stone} Furnace Top")
        if os.path.exists(furnace_image_side):
            output_path = os.path.join(block_output_dir, f"{stone}_furnace_side.png")
            side_img = Image.open(furnace_image_side).convert("RGBA")
            side_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {stone} Furnace Side")
        if os.path.exists(furnace_image_front):
            output_path = os.path.join(block_output_dir, f"{stone}_furnace_front.png")
            front_img = Image.open(furnace_image_front).convert("RGBA")
            front_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {stone} Furnace Front On")
        if os.path.exists(furnace_image_front_on):
            output_path = os.path.join(block_output_dir, f"{stone}_furnace_front_on.png")
            front_on_img = Image.open(furnace_image_front_on).convert("RGBA")
            front_on_img.save(output_path)
            # print(f"Generated texture: {output_path}")
        else:
            print(f"Warning: Missing texture for {stone} Furnace Front")


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

    for ingot in COPPER_TYPES:
            ingot_image_path = os.path.join(image_dir, "copper", "ingots", f"{ingot}_ingot.png")
            if os.path.exists(ingot_image_path):
                output_path = os.path.join(item_output_dir, f"{ingot}_ingot.png")
                ingot_img = Image.open(ingot_image_path).convert("RGBA")
                ingot_img.save(output_path)
                # print(f"Generated texture: {output_path}")
            else:
                print(f"Warning: Missing texture for {ingot}_ingot")
   
    print(f"Texture generation done!")

def generate_blockstates(output_dir):
    # Build the full output path for the mineable/axe.json file
    blockstates_dir = os.path.join(output_dir, "assets", "fariance", "blockstates")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(blockstates_dir), exist_ok=True)

    # Ladder blockstates
    for wood in WOOD_TYPES:
        ladder_name = f"{wood}_ladder"
        blockstates_data = {
            "variants": {
                "facing=east": {
                    "model": f"fariance:block/{ladder_name}",
                    "y": 90
                },
                "facing=north": {
                    "model": f"fariance:block/{ladder_name}"
                },
                "facing=south": {
                    "model": f"fariance:block/{ladder_name}",
                    "y": 180
                },
                "facing=west": {
                    "model": f"fariance:block/{ladder_name}",
                    "y": 270
                }
            }
        }
        
        # Define the output path for the blockstates file
        blockstates_file_path = os.path.join(blockstates_dir, f"{ladder_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)

        # Crafting tables
        table_name = f"{wood}_crafting_table"
        blockstates_data = {
            "variants": {
                "": {
                "model": f"fariance:block/{wood}_crafting_table"
                }
            }
        }

        blockstates_file_path = os.path.join(blockstates_dir, f"{table_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)

    # Furnace blockstates
    for stone in STONE_TYPES:
        furnace_name = f"{stone}_furnace"
        blockstates_data = {
            "variants": {
                "facing=east,lit=false": {
                "model": f"fariance:block/{stone}_furnace",
                "y": 90
                },
                "facing=east,lit=true": {
                "model": f"fariance:block/{stone}_furnace_on",
                "y": 90
                },
                "facing=north,lit=false": {
                "model": f"fariance:block/{stone}_furnace"
                },
                "facing=north,lit=true": {
                "model": f"fariance:block/{stone}_furnace_on"
                },
                "facing=south,lit=false": {
                "model": f"fariance:block/{stone}_furnace",
                "y": 180
                },
                "facing=south,lit=true": {
                "model": f"fariance:block/{stone}_furnace_on",
                "y": 180
                },
                "facing=west,lit=false": {
                "model": f"fariance:block/{stone}_furnace",
                "y": 270
                },
                "facing=west,lit=true": {
                "model": f"fariance:block/{stone}_furnace_on",
                "y": 270
                }
            }
        }
        
        # Define the output path for the blockstates file
        blockstates_file_path = os.path.join(blockstates_dir, f"{furnace_name}.json")
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
            f"fariance:{wood}_ladder" for wood in WOOD_TYPES  # Add each wood ladder to the values list
        ]
    }

    # Build the full output path for the mineable/axe.json file
    mineable_file_path = os.path.join(base_output_dir, "data", "minecraft", "tags", "blocks", "mineable", "axe.json")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(mineable_file_path), exist_ok=True)

    # Write the mineable data to the file
    with open(mineable_file_path, 'w') as f:
        json.dump(mineable_data, f, indent=2)

    print(f"Mineable ladders JSON generated")

def generate_trapdoor_climbable_ladders_json(base_output_dir):
    # Define the tag structure for trapdoor climbable ladders
    trapdoor_climbable_data = {
        "values": [
            "minecraft:ladder"
        ] + [f"fariance:{wood}_ladder" for wood in WOOD_TYPES]  # Add each wood ladder after the Minecraft ladder
    }

    # Build the full output path for the trapdoor climbable ladders JSON
    trapdoor_climbable_file_path = os.path.join(base_output_dir, "data", "fariance", "tags", "block", "make_trapdoor_climbable_ladders.json")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(trapdoor_climbable_file_path), exist_ok=True)

    # Write the trapdoor climbable data to the file
    with open(trapdoor_climbable_file_path, 'w') as f:
        json.dump(trapdoor_climbable_data, f, indent=2)

    print(f"Trapdoor climbable ladders JSON generated")

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
                            "name": f"fariance:{ladder_name}"
                        }
                    ]
                }
            ]
        }

        # Build the output file path for each ladder's loot table
        loot_table_file_path = os.path.join(base_output_dir, "data", "fariance", "loot_tables", "blocks", f"{ladder_name}.json")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(loot_table_file_path), exist_ok=True)

        # Write the loot table data to the file
        with open(loot_table_file_path, 'w') as f:
            json.dump(loot_table_data, f, indent=2)

    print(f"Loot tables generated!")

# Ensure that the directory exists before writing the lang file
lang_file_path = "../src/main/resources/assets/fariance/lang/en_us.json"
lang_dir = os.path.dirname(lang_file_path)
os.makedirs(lang_dir, exist_ok=True)  # Create directories if they don't exist

# Define the path for recipe files
recipe_file_path = "../src/main/resources/data/fariance/recipe"
recipe_dir = os.path.dirname(recipe_file_path)
os.makedirs(recipe_dir, exist_ok=True) # Create the directory if it doesn't exist

# Define the path for breaking recipe files
break_recipe_file_path = "../src/main/resources/data/minecraft/recipe"
break_recipe_dir = os.path.dirname(break_recipe_file_path)
os.makedirs(break_recipe_dir, exist_ok=True) # Create the directory if it doesn't exist

script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
output_dir = os.path.join(script_dir, "../src/main/resources")  # Join with the relative output path
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist


def main():
    # Generate lang file
    with open(lang_file_path, "w") as f:
        f.write(generate_lang_entries())

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
    generate_ladder_loot_tables(output_dir)

    # Generate recipes and write them to files
    for item_name, recipe in generate_recipes():
        # Define the full path for the recipe file
        recipe_file = os.path.join(recipe_file_path, f"{item_name}.json")
        # Ensure the directory exists for the current file
        os.makedirs(os.path.dirname(recipe_file), exist_ok=True)
        with open(recipe_file, "w") as f:
            f.write(recipe)

    # Generate breaking recipes and write them to files
    for item_name, break_recipe in break_recipes():
        # Define the full path for the recipe file
        break_recipe_file = os.path.join(break_recipe_file_path, f"{item_name}.json")
        # Ensure the directory exists for the current file
        os.makedirs(os.path.dirname(break_recipe_file), exist_ok=True)
        with open(break_recipe_file, "w") as f:
            f.write(break_recipe)

    # Generate textures
    generate_textures()

    print("Mod content generation complete!")

if __name__ == "__main__":
    main()
