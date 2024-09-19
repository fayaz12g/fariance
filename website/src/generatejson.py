import os
import json

# Define the paths
item_folder = r"C:\Users\fayaz\Documents\GitHub\woodstuffmod\woodstuff\python\output\assets\woodstuff\textures\item"
lang_file = r"C:\Users\fayaz\Documents\GitHub\woodstuffmod\woodstuff\python\output\assets\woodstuff\lang\en_us.json"
github_raw_base = "https://raw.githubusercontent.com/fayaz12g/woodstuffmod/main/woodstuff/python/output/assets/woodstuff/textures/item/"
github_stick_base = "https://raw.githubusercontent.com/fayaz12g/woodstuffmod/main/woodstuff/python/image/stick/"
github_block_base = "https://raw.githubusercontent.com/fayaz12g/woodstuffmod/main/woodstuff/python/image/block/"

# Constants
WOOD_TYPES = ["oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo"]
COPPER_TYPES = ["shiny_copper", "weathered_copper", "exposed_copper", "oxidized_copper"]
MATERIAL_TYPES = WOOD_TYPES + COPPER_TYPES + ["iron", "diamond", "copper", "gold", "netherite", "amethyst", "diorite", "andesite", "granite", "blackstone", "cobblestone", "redstone", "lapis", "quartz", "deepslate"]
STICK_TYPES = [f"stripped_{wood}" for wood in WOOD_TYPES] + WOOD_TYPES + ["blaze", "breeze"]

# Read the language file
with open(lang_file, 'r', encoding='utf-8') as f:
    lang_data = json.load(f)

# Create a dictionary to store item names and IDs
item_data = {}
for key, value in lang_data.items():
    if key.startswith("item.woodstuff."):
        item_id = key.split(".")[-1]
        item_data[item_id] = {"name": value, "full_id": key}

# Create the tools list
tools = []
for item_id, data in item_data.items():
    # Check if it's a tool
    tool_types = ["sword", "axe", "shovel", "hoe", "pickaxe"]
    tool_type = next((t for t in tool_types if t in item_id), None)
    
    if tool_type:
        # Split the ID to extract information
        parts = item_id.split("_with_")
        
        if len(parts) == 2:
            material = "_".join(parts[0].split("_")[:-1])  # Everything before the tool type
            stick = parts[1].split("_stick")[0]  # Everything between "with_" and "_stick"
        else:
            material = parts[0].split("_")[0]
            stick = "unknown"
        
        # Use the name directly from the language file
        name = data["name"]
        
        tools.append({
            "name": name,
            "id": data["full_id"],
            "stick": stick,
            "material": material,
            "type": tool_type,
            "imagePath": github_raw_base + item_id + ".png"
        })

def capitalize(s):
    return ' '.join(word.capitalize() for word in s.split('_'))

def generate_sticks():
    return [
        {
            "name": f"{capitalize(stick)} Stick",
            "imagePath": f"{github_stick_base}{stick}.png"
        }
        for stick in STICK_TYPES
    ]

def generate_materials():
    return [
        {
            "name": capitalize(material),
            "imagePath": f"{github_block_base}" + (
                f'{material}_block' if 'copper' in material
                else f"stripped_{material}_log" if material in WOOD_TYPES
                else f'{material}_block'
            ) + ".png"
        }
        for material in MATERIAL_TYPES
    ]

# Create the final JSON structure
mod_data = {
    "tools": tools,
    "sticks": generate_sticks(),
    "materials": generate_materials()
}

# Write the JSON file
with open('mod_items_catalog.json', 'w', encoding='utf-8') as f:
    json.dump(mod_data, f, indent=2, ensure_ascii=False)

print("JSON file created successfully!")
print(f"Number of tools generated: {len(tools)}")
print(f"Number of sticks generated: {len(mod_data['sticks'])}")
print(f"Number of materials generated: {len(mod_data['materials'])}")