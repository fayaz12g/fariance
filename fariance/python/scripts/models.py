import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

item_model_dir = os.path.join(output_dir, "assets", "fariance", "models", "item")
block_model_dir = os.path.join(output_dir, "assets", "fariance", "models", "block")

def tool_models():
    # Tool Models
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

def stick_models():
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

def ingot_models():
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


def ladder_models():
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

def crafting_table_models():
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

def shield_models():
    # Loop through each wood type and generate the corresponding models for shields
    for wood in WOOD_TYPES:
        for material in MATERIAL_BASE:
            shield_name = f"{wood}_{material}_shield"
            
            # Block model data for the shield
            item_model_data = {
                "textures": {
                    "1": f"fariance:item/{wood}_{material}_shield_base_nopattern",
                    "particle": f"fariance:item/{wood}_{material}_shield_base_nopattern"
                },
                "elements": [
                    {
                        "from": [-6, -11, 1],
                        "to": [6, 11, 2],
                        "faces": {
                            "north": {"uv": [3.5, 0.25, 6.5, 5.75], "texture": "#1"},
                            "east": {"uv": [3.25, 0.25, 3.5, 5.75], "texture": "#1"},
                            "south": {"uv": [0.25, 0.25, 3.25, 5.75], "texture": "#1"},
                            "west": {"uv": [0, 0.25, 0.25, 5.75], "texture": "#1"},
                            "up": {"uv": [0.25, 0, 3.25, 0.25], "texture": "#1"},
                            "down": {"uv": [3.25, 0, 6.25, 0.25], "texture": "#1"}
                        }
                    },
                    {
                        "from": [-1, -3, -5],
                        "to": [1, 3, 1],
                        "faces": {
                            "north": {"uv": [10, 1.5, 10.5, 3], "texture": "#1"},
                            "east": {"uv": [8.5, 1.5, 10, 3], "texture": "#1"},
                            "south": {"uv": [8, 1.5, 8.5, 3], "texture": "#1"},
                            "west": {"uv": [6.5, 1.5, 8, 3], "texture": "#1"},
                            "up": {"uv": [8, 0, 8.5, 1.5], "texture": "#1"},
                            "down": {"uv": [8.5, 1.5, 9, 0], "texture": "#1"}
                        }
                    }
                ],
                "overrides": [
                    {"predicate": {"blocking": 1}, "model": f"fariance:item/{wood}_{material}_shield_blocking"}
                ],
                "display": {
                    "thirdperson_righthand": {
                        "rotation": [0, 90, 0],
                        "translation": [10.01, 6, -4]
                    },
                    "thirdperson_lefthand": {
                        "rotation": [0, 90, 0],
                        "translation": [10.51, 6, 12]
                    },
                    "firstperson_righthand": {
                        "rotation": [0, 180, 5],
                        "translation": [-10, 0.5, -10],
                        "scale": [1.25, 1.25, 1.25]
                    },
                    "firstperson_lefthand": {
                        "rotation": [0, 180, 5],
                        "translation": [10, -1, -10],
                        "scale": [1.25, 1.25, 1.25]
                    },
                    "ground": {
                        "rotation": [ 0, 0, 0 ],
                        "translation": [ 2, 4, 2],
                        "scale":[ 0.25, 0.25, 0.25]
                    },
                    "gui": {
                        "rotation": [24, -45, -5],
                        "translation": [-0.5, 0.75, 0],
                        "scale": [0.65, 0.6, 0.9]
                    },
                    "fixed": {
                        "rotation": [0, -180, 0],
                        "translation": [-7.25, 7.25, -8],
                        "scale": [0.9, 0.9, 0.9]
                    }
                }
            }


            # Define the block model output path
            item_model_file_path = os.path.join(item_model_dir, f"{shield_name}.json")
            
            # Write the block model data to the file
            with open(item_model_file_path, 'w') as f:
                json.dump(item_model_data, f, indent=2)
            
            # Blocking shield models
            blocking_shield_name = f"{wood}_{material}_shield_blocking"
            
            # Block model data for the shield
            item_model_data = {
                "textures": {
                    "1": f"fariance:item/{wood}_{material}_shield_base_nopattern",
                    "particle": "fariance:item/{wood}_{material}_shield_base_nopattern"
                },
                "elements": [
                    {
                        "from": [-6, -11, 1],
                        "to": [6, 11, 2],
                        "faces": {
                            "north": {"uv": [3.5, 0.25, 6.5, 5.75], "texture": "#1"},
                            "east": {"uv": [3.25, 0.25, 3.5, 5.75], "texture": "#1"},
                            "south": {"uv": [0.25, 0.25, 3.25, 5.75], "texture": "#1"},
                            "west": {"uv": [0, 0.25, 0.25, 5.75], "texture": "#1"},
                            "up": {"uv": [0.25, 0, 3.25, 0.25], "texture": "#1"},
                            "down": {"uv": [3.25, 0, 6.25, 0.25], "texture": "#1"}
                        }
                    },
                    {
                        "from": [-1, -3, -5],
                        "to": [1, 3, 1],
                        "faces": {
                            "north": {"uv": [10, 1.5, 10.5, 3], "texture": "#1"},
                            "east": {"uv": [8.5, 1.5, 10, 3], "texture": "#1"},
                            "south": {"uv": [8, 1.5, 8.5, 3], "texture": "#1"},
                            "west": {"uv": [6.5, 1.5, 8, 3], "texture": "#1"},
                            "up": {"uv": [8, 0, 8.5, 1.5], "texture": "#1"},
                            "down": {"uv": [8.5, 1.5, 9, 0], "texture": "#1"}
                        }
                    }
                ],
                "display": {
                    "thirdperson_righthand": {
                        "rotation": [43, 165, 0],
                        "translation": [-6.49, 12.5, -2]
                    },
                    "thirdperson_lefthand": {
                        "rotation": [43, -180, 0],
                        "translation": [7.51, 10.25, -1]
                    },
                    "firstperson_righthand": {
                        "rotation": [0, 180, 0],
                        "translation": [-15, 3, -12],
                        "scale": [1.25, 1.25, 1.25]
                    },
                    "firstperson_lefthand": {
                        "rotation": [0, 180, 0],
                        "translation": [5, 3, -9],
                        "scale": [1.25, 1.25, 1.25]
                    },
                    "gui": {
                        "rotation": [24, -45, -5],
                        "translation": [-0.5, 0.75, 0],
                        "scale": [0.65, 0.6, 0.9]
                    }
                }
            }

            # Define the block model output path
            item_model_file_path = os.path.join(item_model_dir, f"{blocking_shield_name}.json")
            
            # Write the block model data to the file
            with open(item_model_file_path, 'w') as f:
                json.dump(item_model_data, f, indent=2)

def furnace_models():
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

def generate_models():
    os.makedirs(item_model_dir, exist_ok=True)
    os.makedirs(block_model_dir, exist_ok=True)

    tool_models()
    stick_models()
    ingot_models()
    ladder_models()
    crafting_table_models()
    furnace_models()
    shield_models()


    print("Models generation finished!.")
