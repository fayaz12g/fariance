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
    for wood in STICK_TYPES:
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

def torch_models():
    # Loop through each wood type and generate the corresponding models for torches
    for wood in STICK_TYPES:
        for torch in TORCH_TYPES:
            if wood not in ["breeze", "blaze"]:
                if torch == "normal":
                    torch_name = f"{wood}_torch"
                else:
                    torch_name = f"{wood}_{torch}_torch"
                template = "template_torch"
                if torch == "redstone":
                    template = "template_redstone_torch"
                
                # Block model data for the torch
                block_model_data = {
                    "parent": f"minecraft:block/{template}",
                    "textures": {
                        "torch": f"fariance:block/{torch_name}"
                    }
                }
            
                    
                # Define the block model output path
                block_model_file_path = os.path.join(block_model_dir, f"{torch_name}.json")
                
                # Write the block model data to the file
                with open(block_model_file_path, 'w') as f:
                    json.dump(block_model_data, f, indent=2)

                if torch == "redstone":
                    block_model_data = {
                        "parent": "minecraft:block/template_torch_unlit",
                        "textures": {
                            "torch": f"fariance:block/{wood}_redstone_torch_off"
                        }
                    }

                # Define the block model output path
                block_model_file_path = os.path.join(block_model_dir, f"{torch_name}_off.json")
                
                # Write the block model data to the file
                with open(block_model_file_path, 'w') as f:
                    json.dump(block_model_data, f, indent=2)

                # Item model data for the torch
                item_model_data = {
                    "parent": "minecraft:item/generated",
                    "textures": {
                        "layer0": f"fariance:block/{torch_name}"
                    }
                }

                # Define the block model output path
                item_model_file_path = os.path.join(item_model_dir, f"{torch_name}.json")
                
                # Write the block model data to the file
                with open(item_model_file_path, 'w') as f:
                    json.dump(item_model_data, f, indent=2)

def wall_torch_models():
    # Loop through each wood type and generate the corresponding models for torches
    for wood in STICK_TYPES:
        for torch in TORCH_TYPES:
            if wood not in ["breeze", "blaze"]:

                if torch == "normal":
                    wall_torch_name = f"{wood}_wall_torch"
                else:
                    wall_torch_name = f"{wood}_{torch}_wall_torch"

                if torch == "normal":
                    torch_name = f"{wood}_torch"
                else:
                    torch_name = f"{wood}_{torch}_torch"

                template = "template_torch_wall"
                if torch == "redstone":
                    template = "template_redstone_torch_wall"
                
                
                # Block model data for the torch
                block_model_data = {
                    "parent": f"minecraft:block/{template}",
                    "textures": {
                        "torch": f"fariance:block/{torch_name}"
                    }
                }

                # Define the block model output path
                block_model_file_path = os.path.join(block_model_dir, f"{wall_torch_name}.json")
                
                # Write the block model data to the file
                with open(block_model_file_path, 'w') as f:
                    json.dump(block_model_data, f, indent=2)

                if torch == "redstone":
                    block_model_data = {
                        "parent": "minecraft:block/template_torch_wall_unlit",
                        "textures": {
                            "torch": f"fariance:block/{wood}_redstone_torch_off"
                        }
                    }

                    # Define the block model output path
                    block_model_file_path = os.path.join(block_model_dir, f"{torch_name}_off.json")
                    
                    # Write the block model data to the file
                    with open(block_model_file_path, 'w') as f:
                        json.dump(block_model_data, f, indent=2)

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

def bed_models():
    # Loop through each wood type and generate the corresponding models for beds
    for wood in WOOD_TYPES:
        for color in WOOL_TYPES:
            bed_name = f"{wood}_{color}_bed"
            
            # Block model data for the bed
            item_model_data = {
                "parent": "minecraft:item/generated",
                "textures": {
                    "layer0": f"fariance:item/{bed_name}"
                }
            }

            # Define the block model output path
            item_model_file_path = os.path.join(item_model_dir, f"{bed_name}.json")
            
            # Write the block model data to the file
            with open(item_model_file_path, 'w') as f:
                json.dump(item_model_data, f, indent=2)
            
            # Blocking shield models
            bed_block_name_head = f"{wood}_{color}_bed_head"
            
            # Block model data for the bed head
            block_head_model_data = {
                "parent": "fariance:block/template_bed_head",
                "textures": {
                    "bed": f"fariance:entity/bed/{wood}_{color}",
                    "particle": f"minecraft:block/{wood}_planks"
                }
            }

            # Define the block model output path
            head_model_file_path = os.path.join(block_model_dir, f"{bed_block_name_head}.json")
            
            # Write the block model data to the file
            with open(head_model_file_path, 'w') as f:
                json.dump(block_head_model_data, f, indent=2)

            # Blocking shield models
            bed_block_name_foot = f"{wood}_{color}_bed_foot"
            
            # Block model data for the bed foot
            block_foot_model_data = {
                "parent": "fariance:block/template_bed_foot",
                "textures": {
                    "bed": f"fariance:entity/bed/{wood}_{color}",
                    "particle": f"minecraft:block/{wood}_planks"
                }
            }

            # Define the block model output path
            foot_model_file_path = os.path.join(block_model_dir, f"{bed_block_name_foot}.json")
            
            # Write the block model data to the file
            with open(foot_model_file_path, 'w') as f:
                json.dump(block_foot_model_data, f, indent=2)

def bed_template_models():
    # Head template name
    template_bed_head = "template_bed_head"
    
    # Block model data for the head template
    block_head_template_data = {
        "texture_size": [64, 64],
        "textures": {
        },
        "elements": [
            {
                "from": [0, 0, 13],
                "to": [3, 3, 16],
                "rotation": {"angle": 0, "axis": "y", "origin": [8, 8, 21]},
                "faces": {
                    "north": {"uv": [14.75, 0.75, 15.5, 1.5], "texture": "#bed"},
                    "east": {"uv": [14, 0.75, 14.75, 1.5], "texture": "#bed"},
                    "south": {"uv": [13.25, 0.75, 14, 1.5], "texture": "#bed", "cullface": "south"},
                    "west": {"uv": [12.5, 0.75, 13.25, 1.5], "texture": "#bed", "cullface": "west"},
                    "down": {"uv": [14, 0, 14.75, 0.75], "texture": "#bed", "cullface": "down"}
                }
            },
            {
                "from": [13, 0, 13],
                "to": [16, 3, 16],
                "rotation": {"angle": 0, "axis": "y", "origin": [21, 8, 21]},
                "faces": {
                    "north": {"uv": [14, 2.25, 14.75, 3], "texture": "#bed"},
                    "east": {"uv": [13.25, 2.25, 14, 3], "texture": "#bed", "cullface": "east"},
                    "south": {"uv": [12.5, 2.25, 13.25, 3], "texture": "#bed", "cullface": "south"},
                    "west": {"uv": [14.75, 2.25, 15.5, 3], "texture": "#bed"},
                    "down": {"uv": [14, 1.5, 14.75, 2.25], "texture": "#bed", "cullface": "down"}
                }
            },
            {
                "from": [0, 3, 0],
                "to": [16, 9, 16],
                "rotation": {"angle": 0, "axis": "y", "origin": [8, 11, 8]},
                "faces": {
                    "east": {"uv": [0, 1.5, 1.5, 5.5], "rotation": 270, "texture": "#bed", "cullface": "east"},
                    "south": {"uv": [1.5, 0, 5.5, 1.5], "rotation": 180, "texture": "#bed", "cullface": "south"},
                    "west": {"uv": [5.5, 1.5, 7, 5.5], "rotation": 90, "texture": "#bed", "cullface": "west"},
                    "up": {"uv": [1.5, 1.5, 5.5, 5.5], "rotation": 180, "texture": "#bed"},
                    "down": {"uv": [7, 1.5, 11, 5.5], "texture": "#bed"}
                }
            }
        ]
    }

    # Define the block model output path
    head_template_file_path = os.path.join(block_model_dir, f"{template_bed_head}.json")
    
    # Write the block model data to the file
    with open(head_template_file_path, 'w') as f:
        json.dump(block_head_template_data, f, indent=2)

    # Foot template name
    template_bed_foot = "template_bed_foot"
    
    # Block model data for the head template
    block_foot_template_data = {
        "texture_size": [64, 64],
        "textures": {
        },
        "elements": [
            {
                "from": [0, 0, 0],
                "to": [3, 3, 3],
                "faces": {
                    "north": {"uv": [12.5, 5.25, 13.25, 6], "texture": "#bed", "cullface": "north"},
                    "east": {"uv": [14.75, 5.25, 15.5, 6], "texture": "#bed"},
                    "south": {"uv": [14, 5.25, 14.75, 6], "texture": "#bed"},
                    "west": {"uv": [13.25, 5.25, 14, 6], "texture": "#bed", "cullface": "west"},
                    "down": {"uv": [14, 4.5, 14.75, 5.25], "texture": "#bed", "cullface": "down"}
                }
            },
            {
                "from": [13, 0, 0],
                "to": [16, 3, 3],
                "rotation": {"angle": 0, "axis": "y", "origin": [21, 8, 8]},
                "faces": {
                    "north": {"uv": [14, 3.75, 13.25, 4.5], "texture": "#bed", "cullface": "north"},
                    "east": {"uv": [12.5, 3.75, 13.25, 4.5], "texture": "#bed", "cullface": "east"},
                    "south": {"uv": [14.75, 3.75, 15.5, 4.5], "texture": "#bed"},
                    "west": {"uv": [14, 3.75, 14.75, 4.5], "texture": "#bed"},
                    "down": {"uv": [14, 3, 14.75, 3.75], "texture": "#bed", "cullface": "down"}
                }
            },
            {
                "from": [0, 3, 0],
                "to": [16, 9, 16],
                "rotation": {"angle": 0, "axis": "y", "origin": [8, 11, 8]},
                "faces": {
                    "north": {"uv": [5.5, 5.5, 9.5, 7], "rotation": 180, "texture": "#bed", "cullface": "north"},
                    "east": {"uv": [0, 7, 1.5, 11], "rotation": 270, "texture": "#bed", "cullface": "east"},
                    "west": {"uv": [5.5, 7, 7, 11], "rotation": 90, "texture": "#bed", "cullface": "west"},
                    "up": {"uv": [1.5, 7, 5.5, 11], "rotation": 180, "texture": "#bed"},
                    "down": {"uv": [7, 7, 11, 11], "texture": "#bed"}
                }
            }
        ]
    }

    # Define the block model output path
    foot_template_file_path = os.path.join(block_model_dir, f"{template_bed_foot}.json")
    
    # Write the block model data to the file
    with open(foot_template_file_path, 'w') as f:
        json.dump(block_foot_template_data, f, indent=2)


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


def new_wood_blocks():
    # Add new wood models
    for wood in NEW_WOOD:
        if wood in NETHER_WOODS:
            log_type = "stem"
        else: 
            log_type = "log"

        plank_name = f"{wood}_planks"
        
        # Block model data
        block_model_data = {
            "parent": "minecraft:block/cube_all",
            "textures": {
                "all": f"fariance:block/{wood}_planks"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{plank_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Item model data for the crafting table
        item_model_data = {
            "parent": f"fariance:block/{plank_name}"
        }

        # Define the block model output path
        item_model_file_path = os.path.join(item_model_dir, f"{plank_name}.json")
        
        # Write the block model data to the file
        with open(item_model_file_path, 'w') as f:
            json.dump(item_model_data, f, indent=2)


        plate_name = f"{wood}_pressure_plate"
                
        # Block model data
        block_model_data = {
            "parent": "minecraft:block/pressure_plate_up",
            "textures": {
                "texture": f"fariance:block/{wood}_planks"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{plate_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        plate_down_name = f"{wood}_pressure_plate_down"
    
       # Block model data
        block_model_data = {
            "parent": "minecraft:block/pressure_plate_down",
            "textures": {
                "texture": f"fariance:block/{wood}_planks"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{plate_down_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Item model data for the crafting table
        item_model_data = {
            "parent": f"fariance:block/{plate_name}"
        }

        # Define the block model output path
        item_model_file_path = os.path.join(item_model_dir, f"{plate_name}.json")
        
        # Write the block model data to the file
        with open(item_model_file_path, 'w') as f:
            json.dump(item_model_data, f, indent=2)

        button_name = f"{wood}_button"
                
        # Block model data
        block_model_data = {
            "parent": "minecraft:block/button",
            "textures": {
                "texture": f"fariance:block/{wood}_planks"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{button_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        button_pressed_name = f"{wood}_button_pressed"
                
        # Block model data
        block_model_data = {
            "parent": "minecraft:block/button_pressed",
            "textures": {
                "texture": f"fariance:block/{wood}_planks"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{button_pressed_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

       # Block model data
        block_model_data = {
            "parent": "minecraft:block/button_inventory",
            "textures": {
                "texture": f"fariance:block/{wood}_planks"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{button_name}_inventory.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Item model data for the crafting table
        item_model_data = {
            "parent": f"fariance:block/{button_name}_inventory"
        }

        # Define the block model output path
        item_model_file_path = os.path.join(item_model_dir, f"{button_name}.json")
        
        # Write the block model data to the file
        with open(item_model_file_path, 'w') as f:
            json.dump(item_model_data, f, indent=2)

        fence_name = f"{wood}_fence"
                
        # Block model data
        block_model_data = {
            "parent": "minecraft:block/fence_post",
            "textures": {
                "texture": f"fariance:block/{wood}_planks"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{fence_name}_post.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)
                
        # Block model data
        block_model_data = {
            "parent": "minecraft:block/fence_inventory",
            "textures": {
                "texture": f"fariance:block/{wood}_planks"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{fence_name}_inventory.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Block model data
        block_model_data = {
            "parent": "minecraft:block/fence_side",
            "textures": {
                "texture": f"fariance:block/{wood}_planks"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{fence_name}_side.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Item model data for the crafting table
        item_model_data = {
            "parent": f"fariance:block/{fence_name}_inventory"
        }

        # Define the block model output path
        item_model_file_path = os.path.join(item_model_dir, f"{fence_name}.json")
        
        # Write the block model data to the file
        with open(item_model_file_path, 'w') as f:
            json.dump(item_model_data, f, indent=2)

        gate_name = f"{wood}_fence_gate"
                
        # Block model data
        block_model_data = {
            "parent": "minecraft:block/fence_post",
            "textures": {
                "texture": f"fariance:block/{wood}_planks"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{gate_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Item model data for the crafting table
        item_model_data = {
            "parent": f"fariance:block/{gate_name}"
        }

        # Define the block model output path
        item_model_file_path = os.path.join(item_model_dir, f"{gate_name}.json")
        
        # Write the block model data to the file
        with open(item_model_file_path, 'w') as f:
            json.dump(item_model_data, f, indent=2)

        door_name = f"{wood}_door"
                
        # Block model data
        block_model_data = {
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{door_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Item model data for the crafting table
        item_model_data = {
            "parent": "minecraft:item/generated",
            "textures": {
                "layer0": f"fariance:item/{wood}_door"
            }
        }

        # Define the block model output path
        item_model_file_path = os.path.join(item_model_dir, f"{door_name}.json")
        
        # Write the block model data to the file
        with open(item_model_file_path, 'w') as f:
            json.dump(item_model_data, f, indent=2)

        log_name = f"{wood}_{log_type}"
                
        # Block model data
        block_model_data = {
            "parent": "minecraft:block/cube_column",
            "textures": {
                "end": f"fariance:block/{wood}_{log_type}_top",
                "side": f"fariance:block/{wood}_{log_type}"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{log_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Block model data
        block_model_data = {
            "parent": "minecraft:block/cube_column_horizontal",
            "textures": {
                "end": f"fariance:block/{wood}_{log_type}_top",
                "side": f"fariance:block/{wood}_{log_type}"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{log_name}_horizontal.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Item model data for the crafting table
        item_model_data = {
            "parent": f"fariance:block/{log_name}"
        }

        # Define the block model output path
        item_model_file_path = os.path.join(item_model_dir, f"{log_name}.json")
        
        # Write the block model data to the file
        with open(item_model_file_path, 'w') as f:
            json.dump(item_model_data, f, indent=2)

        stripped_log_name = f"stripped_{wood}_{log_type}"
                
        # Block model data
        block_model_data = {
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{stripped_log_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Item model data for the crafting table
        item_model_data = {
            "parent": f"fariance:block/{stripped_log_name}"
        }

        # Define the block model output path
        item_model_file_path = os.path.join(item_model_dir, f"{stripped_log_name}.json")
        
        # Write the block model data to the file
        with open(item_model_file_path, 'w') as f:
            json.dump(item_model_data, f, indent=2)

        slab_name = f"{wood}_slab"
                
        # Block model data
        block_model_data = {
            "parent": "minecraft:block/slab",
            "textures": {
                "bottom": f"fariance:block/{wood}_planks",
                "side": f"fariance:block/{wood}_planks",
                "top": f"fariance:block/{wood}_planks"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{slab_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        slab_top_name = f"{wood}_slab"
                
        # Block model data
        block_model_data = {
            "parent": "minecraft:block/slab_top",
            "textures": {
                "bottom": f"fariance:block/{wood}_planks",
                "side": f"fariance:block/{wood}_planks",
                "top": f"fariance:block/{wood}_planks"
            }
        }

        # Define the block model output path
        block_model_file_path = os.path.join(block_model_dir, f"{slab_top_name}.json")
        
        # Write the block model data to the file
        with open(block_model_file_path, 'w') as f:
            json.dump(block_model_data, f, indent=2)

        # Item model data for the crafting table
        item_model_data = {
            "parent": f"fariance:block/{slab_name}"
        }

        # Define the block model output path
        item_model_file_path = os.path.join(item_model_dir, f"{slab_name}.json")
        
        # Write the block model data to the file
        with open(item_model_file_path, 'w') as f:
            json.dump(item_model_data, f, indent=2)

def atlases_blocks():
    file_name = f"blocks"
    model_data = {
        "sources": [
            {
                "type": "directory",
                "source": "entity/bed",
                "prefix": "entity/bed/"
            }
        ]
    }
    model_file_path = os.path.join(atlases_output_dir, f"{file_name}.json")
    with open(model_file_path, 'w') as f:
        json.dump(model_data, f, indent=2)

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
    bed_models()
    bed_template_models()
    atlases_blocks()
    new_wood_blocks()
    torch_models()
    wall_torch_models()



    print("Models generation finished!.")
