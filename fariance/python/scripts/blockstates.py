import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

# Build the full output path for the mineable/axe.json file
blockstates_dir = os.path.join(output_dir, "assets", "fariance", "blockstates")

def generate_blockstates():
    # Ensure the directory exists
    os.makedirs(os.path.dirname(blockstates_dir), exist_ok=True)

    ladder_blockstates()
    furnace_blockstates()
    crafting_blockstates()
    bed_blockstates()
    new_wood_blockstates()
    torch_blockstates()

    print("Blockstates generated successfully.")


def new_wood_blockstates():
    # new wood blockstates
    for wood in NEW_WOOD:
        if wood in NETHER_WOODS:
            log_type = "stem"
        else: 
            log_type = "log"
    
        item_name = f"{wood}_button"
        blockstates_data = {
            "variants": {
                "face=ceiling,facing=east,powered=false": {
                "model": f"fariance:block/{item_name}",
                "x": 180,
                "y": 270
                },
                "face=ceiling,facing=east,powered=true": {
                "model": f"fariance:block/{item_name}_pressed",
                "x": 180,
                "y": 270
                },
                "face=ceiling,facing=north,powered=false": {
                "model": f"fariance:block/{item_name}",
                "x": 180,
                "y": 180
                },
                "face=ceiling,facing=north,powered=true": {
                "model": f"fariance:block/{item_name}_pressed",
                "x": 180,
                "y": 180
                },
                "face=ceiling,facing=south,powered=false": {
                "model": f"fariance:block/{item_name}",
                "x": 180
                },
                "face=ceiling,facing=south,powered=true": {
                "model": f"fariance:block/{item_name}_pressed",
                "x": 180
                },
                "face=ceiling,facing=west,powered=false": {
                "model":f"fariance:block/{item_name}",
                "x": 180,
                "y": 90
                },
                "face=ceiling,facing=west,powered=true": {
                "model":f"fariance:block/{item_name}_pressed",
                "x": 180,
                "y": 90
                },
                "face=floor,facing=east,powered=false": {
                "model":f"fariance:block/{item_name}",
                "y": 90
                },
                "face=floor,facing=east,powered=true": {
                "model":f"fariance:block/{item_name}_pressed",
                "y": 90
                },
                "face=floor,facing=north,powered=false": {
                "model":f"fariance:block/{item_name}"
                },
                "face=floor,facing=north,powered=true": {
                "model":f"fariance:block/{item_name}_pressed"
                },
                "face=floor,facing=south,powered=false": {
                "model":f"fariance:block/{item_name}",
                "y": 180
                },
                "face=floor,facing=south,powered=true": {
                "model":f"fariance:block/{item_name}_pressed",
                "y": 180
                },
                "face=floor,facing=west,powered=false": {
                "model":f"fariance:block/{item_name}",
                "y": 270
                },
                "face=floor,facing=west,powered=true": {
                "model":f"fariance:block/{item_name}_pressed",
                "y": 270
                },
                "face=wall,facing=east,powered=false": {
                "model": f"fariance:block/{item_name}",
                "uvlock": True,
                "x": 90,
                "y": 90
                },
                "face=wall,facing=east,powered=true": {
                "model":f"fariance:block/{item_name}_pressed",
                "uvlock": True,
                "x": 90,
                "y": 90
                },
                "face=wall,facing=north,powered=false": {
                "model":f"fariance:block/{item_name}",
                "uvlock": True,
                "x": 90
                },
                "face=wall,facing=north,powered=true": {
                "model":f"fariance:block/{item_name}_pressed",
                "uvlock": True,
                "x": 90
                },
                "face=wall,facing=south,powered=false": {
                "model":f"fariance:block/{item_name}",
                "uvlock": True,
                "x": 90,
                "y": 180
                },
                "face=wall,facing=south,powered=true": {
                "model":f"fariance:block/{item_name}_pressed",
                "uvlock": True,
                "x": 90,
                "y": 180
                },
                "face=wall,facing=west,powered=false": {
                "model":f"fariance:block/{item_name}",
                "uvlock": True,
                "x": 90,
                "y": 270
                },
                "face=wall,facing=west,powered=true": {
                "model":f"fariance:block/{item_name}_pressed",
                "uvlock": True,
                "x": 90,
                "y": 270
                }
            }
        }
        
        # Define the output path for the blockstates file
        blockstates_file_path = os.path.join(blockstates_dir, f"{item_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)


        plate_name = f"{wood}_pressure_plate"
        blockstates_data = {
            "variants": {
                "powered=false": {
                "model": f"fariance:block/{plate_name}"
                },
                "powered=true": {
                "model": f"fariance:block/{plate_name}_down"
                }
            }
        }
        
        # Define the output path for the blockstates file
        blockstates_file_path = os.path.join(blockstates_dir, f"{plate_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)


        planks_name = f"{wood}_planks"
        blockstates_data = {
            "variants": {
                "": {
                "model": f"fariance:block/{planks_name}"
                }
            }
        }
        
        # Define the output path for the blockstates file
        blockstates_file_path = os.path.join(blockstates_dir, f"{planks_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)

        slab_name = f"{wood}_slab"
        blockstates_data = {
            "variants": {
                "type=bottom": {
                "model": f"fariance:block/{slab_name}"
                },
                "type=double": {
                "model": f"fariance:block/{wood}_planks"
                },
                "type=top": {
                "model": f"fariance:block/{slab_name}_top"
                }
            }
        }
        
        # Define the output path for the blockstates file
        blockstates_file_path = os.path.join(blockstates_dir, f"{slab_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)

        log_name = f"{wood}_{log_type}"
        blockstates_data = {
            "variants": {
                "axis=x": {
                "model": f"fariance:block/{log_name}",
                "x": 90,
                "y": 90
                },
                "axis=y": {
                "model": f"fariance:block/{log_name}"
                },
                "axis=z": {
                "model": f"fariance:block/{log_name}",
                "x": 90
                }
            }
        }
        
        # Define the output path for the blockstates file
        blockstates_file_path = os.path.join(blockstates_dir, f"{log_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)

        fence_gate_name = f"{wood}_fence_post"
        blockstates_data = {
            "variants": {
                "facing=east,in_wall=false,open=false": {
                "model": f"fariance:block/{fence_gate_name}",
                "uvlock": True,
                "y": 270
                },
                "facing=east,in_wall=false,open=true": {
                "model": f"fariance:block/{fence_gate_name}_open",
                "uvlock": True,
                "y": 270
                },
                "facing=east,in_wall=true,open=false": {
                "model": f"fariance:block/{fence_gate_name}_wall",
                "uvlock": True,
                "y": 270
                },
                "facing=east,in_wall=true,open=true": {
                "model": f"fariance:block/{fence_gate_name}_wall_open",
                "uvlock": True,
                "y": 270
                },
                "facing=north,in_wall=false,open=false": {
                "model": f"fariance:block/{fence_gate_name}",
                "uvlock": True,
                "y": 180
                },
                "facing=north,in_wall=false,open=true": {
                "model": f"fariance:block/{fence_gate_name}_open",
                "uvlock": True,
                "y": 180
                },
                "facing=north,in_wall=true,open=false": {
                "model": f"fariance:block/{fence_gate_name}_wall",
                "uvlock": True,
                "y": 180
                },
                "facing=north,in_wall=true,open=true": {
                "model": f"fariance:block/{fence_gate_name}_wall_open",
                "uvlock": True,
                "y": 180
                },
                "facing=south,in_wall=false,open=false": {
                "model": f"fariance:block/{fence_gate_name}",
                "uvlock": True
                },
                "facing=south,in_wall=false,open=true": {
                "model": f"fariance:block/{fence_gate_name}_open",
                "uvlock": True
                },
                "facing=south,in_wall=true,open=false": {
                "model": f"fariance:block/{fence_gate_name}_wall",
                "uvlock": True
                },
                "facing=south,in_wall=true,open=true": {
                "model": f"fariance:block/{fence_gate_name}_wall_open",
                "uvlock": True
                },
                "facing=west,in_wall=false,open=false": {
                "model": f"fariance:block/{fence_gate_name}",
                "uvlock": True,
                "y": 90
                },
                "facing=west,in_wall=false,open=true": {
                "model": f"fariance:block/{fence_gate_name}_open",
                "uvlock": True,
                "y": 90
                },
                "facing=west,in_wall=true,open=false": {
                "model": f"fariance:block/{fence_gate_name}_wall",
                "uvlock": True,
                "y": 90
                },
                "facing=west,in_wall=true,open=true": {
                "model": f"fariance:block/{fence_gate_name}_wall_open",
                "uvlock": True,
                "y": 90
                }
            }
        }
        
        # Define the output path for the blockstates file
        blockstates_file_path = os.path.join(blockstates_dir, f"{fence_gate_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)

        fence_name = f"{wood}_fence"
        blockstates_data = {
            "multipart": [
                {
                "apply": {
                    "model": f"fariance:block/{fence_name}_post"
                }
                },
                {
                "apply": {
                    "model": f"fariance:block/{fence_name}_side",
                    "uvlock": True
                },
                "when": {
                    "north": "true"
                }
                },
                {
                "apply": {
                    "model": f"fariance:block/{fence_name}_side",
                    "uvlock": True,
                    "y": 90
                },
                "when": {
                    "east": "true"
                }
                },
                {
                "apply": {
                    "model": f"fariance:block/{fence_name}_side",
                    "uvlock": True,
                    "y": 180
                },
                "when": {
                    "south": "True"
                }
                },
                {
                "apply": {
                    "model": f"fariance:block/{fence_name}_side",
                    "uvlock": True,
                    "y": 270
                },
                "when": {
                    "west": "true"
                }
                }
            ]
            }
        
        # Define the output path for the blockstates file
        blockstates_file_path = os.path.join(blockstates_dir, f"{fence_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)


        door_name = f"{wood}_door"
        blockstates_data = {
            "variants": {
                "facing=east,half=lower,hinge=left,open=false": {
                "model": f"fariance:block/{door_name}_bottom_left"
                },
                "facing=east,half=lower,hinge=left,open=true": {
                "model": f"fariance:block/{door_name}_bottom_left_open",
                "y": 90
                },
                "facing=east,half=lower,hinge=right,open=false": {
                "model": f"fariance:block/{door_name}_bottom_right"
                },
                "facing=east,half=lower,hinge=right,open=true": {
                "model": f"fariance:block/{door_name}_bottom_right_open",
                "y": 270
                },
                "facing=east,half=upper,hinge=left,open=false": {
                "model": f"fariance:block/{door_name}_top_left"
                },
                "facing=east,half=upper,hinge=left,open=true": {
                "model": f"fariance:block/{door_name}_top_left_open",
                "y": 90
                },
                "facing=east,half=upper,hinge=right,open=false": {
                "model": f"fariance:block/{door_name}_top_right"
                },
                "facing=east,half=upper,hinge=right,open=true": {
                "model": f"fariance:block/{door_name}_top_right_open",
                "y": 270
                },
                "facing=north,half=lower,hinge=left,open=false": {
                "model": f"fariance:block/{door_name}_bottom_left",
                "y": 270
                },
                "facing=north,half=lower,hinge=left,open=true": {
                "model": f"fariance:block/{door_name}_bottom_left_open"
                },
                "facing=north,half=lower,hinge=right,open=false": {
                "model": f"fariance:block/{door_name}_bottom_right",
                "y": 270
                },
                "facing=north,half=lower,hinge=right,open=true": {
                "model": f"fariance:block/{door_name}_bottom_right_open",
                "y": 180
                },
                "facing=north,half=upper,hinge=left,open=false": {
                "model": f"fariance:block/{door_name}_top_left",
                "y": 270
                },
                "facing=north,half=upper,hinge=left,open=true": {
                "model": f"fariance:block/{door_name}_top_left_open"
                },
                "facing=north,half=upper,hinge=right,open=false": {
                "model": f"fariance:block/{door_name}_top_right",
                "y": 270
                },
                "facing=north,half=upper,hinge=right,open=true": {
                "model": f"fariance:block/{door_name}_top_right_open",
                "y": 180
                },
                "facing=south,half=lower,hinge=left,open=false": {
                "model": f"fariance:block/{door_name}_bottom_left",
                "y": 90
                },
                "facing=south,half=lower,hinge=left,open=true": {
                "model": f"fariance:block/{door_name}_bottom_left_open",
                "y": 180
                },
                "facing=south,half=lower,hinge=right,open=false": {
                "model": f"fariance:block/{door_name}_bottom_right",
                "y": 90
                },
                "facing=south,half=lower,hinge=right,open=true": {
                "model": f"fariance:block/{door_name}_bottom_right_open"
                },
                "facing=south,half=upper,hinge=left,open=false": {
                "model": f"fariance:block/{door_name}_top_left",
                "y": 90
                },
                "facing=south,half=upper,hinge=left,open=true": {
                "model": f"fariance:block/{door_name}_top_left_open",
                "y": 180
                },
                "facing=south,half=upper,hinge=right,open=false": {
                "model": f"fariance:block/{door_name}_top_right",
                "y": 90
                },
                "facing=south,half=upper,hinge=right,open=true": {
                "model": f"fariance:block/{door_name}_top_right_open"
                },
                "facing=west,half=lower,hinge=left,open=false": {
                "model": f"fariance:block/{door_name}_bottom_left",
                "y": 180
                },
                "facing=west,half=lower,hinge=left,open=true": {
                "model": f"fariance:block/{door_name}_bottom_left_open",
                "y": 270
                },
                "facing=west,half=lower,hinge=right,open=false": {
                "model": f"fariance:block/{door_name}_bottom_right",
                "y": 180
                },
                "facing=west,half=lower,hinge=right,open=true": {
                "model": f"fariance:block/{door_name}_bottom_right_open",
                "y": 90
                },
                "facing=west,half=upper,hinge=left,open=false": {
                "model": f"fariance:block/{door_name}_top_left",
                "y": 180
                },
                "facing=west,half=upper,hinge=left,open=true": {
                "model": f"fariance:block/{door_name}_top_left_open",
                "y": 270
                },
                "facing=west,half=upper,hinge=right,open=false": {
                "model": f"fariance:block/{door_name}_top_right",
                "y": 180
                },
                "facing=west,half=upper,hinge=right,open=true": {
                "model": f"fariance:block/{door_name}_top_right_open",
                "y": 90
                }
            }
            }
        
        # Define the output path for the blockstates file
        blockstates_file_path = os.path.join(blockstates_dir, f"{door_name}.json")
        os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
        
        # Write the blockstates data to the file
        with open(blockstates_file_path, 'w') as f:
            json.dump(blockstates_data, f, indent=2)


def ladder_blockstates():
    # Ladder blockstates
    for wood in STICK_TYPES:
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

def crafting_blockstates():
    for wood in WOOD_TYPES:
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

def bed_blockstates():
    for wood in WOOD_TYPES:
        for color in WOOL_TYPES:
            # Beds
            bed_name = f"{wood}_{color}_bed"
            blockstates_data = {
                "variants": {
                    "facing=east,part=head": {
                    "model": f"fariance:block/{wood}_{color}_bed_head",
                    "y": 270
                    },
                    "facing=north,part=head": {
                    "model": f"fariance:block/{wood}_{color}_bed_head",
                    "y": 180
                    },
                    "facing=south,part=head": {
                    "model": f"fariance:block/{wood}_{color}_bed_head"
                    },
                    "facing=west,part=head": {
                    "model":f"fariance:block/{wood}_{color}_bed_head",
                    "y": 90
                    },
                    "facing=east,part=foot": {
                    "model": f"fariance:block/{wood}_{color}_bed_foot",
                    "y": 270
                    },
                    "facing=north,part=foot": {
                    "model": f"fariance:block/{wood}_{color}_bed_foot",
                    "y": 180
                    },
                    "facing=south,part=foot": {
                    "model": f"fariance:block/{wood}_{color}_bed_foot"
                    },
                    "facing=west,part=foot": {
                    "model": f"fariance:block/{wood}_{color}_bed_foot",
                    "y": 90
                    }
                }
            }

            blockstates_file_path = os.path.join(blockstates_dir, f"{bed_name}.json")
            os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
            
            # Write the blockstates data to the file
            with open(blockstates_file_path, 'w') as f:
                json.dump(blockstates_data, f, indent=2)


def torch_blockstates():
    for wood in STICK_TYPES:
        if wood not in ["breeze", "blaze"]:
            # Torches
            torch_name = f"{wood}_torch"
            blockstates_data = {
                "variants": {
                    "": {
                    "model": "minecraft:block/torch"
                    }
                }
            }

            blockstates_file_path = os.path.join(blockstates_dir, f"{torch_name}.json")
            os.makedirs(os.path.dirname(blockstates_file_path), exist_ok=True)
            
            # Write the blockstates data to the file
            with open(blockstates_file_path, 'w') as f:
                json.dump(blockstates_data, f, indent=2)

def furnace_blockstates():
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