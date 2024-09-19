import os
import json

# Define the paths
item_folder = r"C:\Users\fayaz\Documents\GitHub\woodstuffmod\woodstuff\python\output\assets\woodstuff\textures\item"
lang_file = r"C:\Users\fayaz\Documents\GitHub\woodstuffmod\woodstuff\python\output\assets\woodstuff\lang\en_us.json"
github_raw_base = "https://raw.githubusercontent.com/fayaz12g/woodstuffmod/main/woodstuff/python/output/assets/woodstuff/textures/item/"
github_stick_base = "https://raw.githubusercontent.com/fayaz12g/woodstuffmod/main/woodstuff/python/output/assets/woodstuff/textures/stick/"
github_block_base = "https://raw.githubusercontent.com/fayaz12g/woodstuffmod/main/woodstuff/python/output/assets/woodstuff/textures/block/"

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

# Create the final JSON structure
mod_data = {
    "tools": tools,
    "sticks": [
        {"name": "Oak Stick", "imagePath": github_stick_base + "oak_stick.png"},
        {"name": "Spruce Stick", "imagePath": github_stick_base + "spruce_stick.png"},
        {"name": "Birch Stick", "imagePath": github_stick_base + "birch_stick.png"},
        {"name": "Jungle Stick", "imagePath": github_stick_base + "jungle_stick.png"},
        {"name": "Acacia Stick", "imagePath": github_stick_base + "acacia_stick.png"},
        {"name": "Dark Oak Stick", "imagePath": github_stick_base + "dark_oak_stick.png"}
    ],
    "materials": [
        {"name": "Diamond", "imagePath": github_block_base + "diamond_block.png"},
        {"name": "Iron", "imagePath": github_block_base + "iron_block.png"},
        {"name": "Gold", "imagePath": github_block_base + "gold_block.png"},
        {"name": "Stone", "imagePath": github_block_base + "stone.png"},
        {"name": "Oak", "imagePath": github_block_base + "oak_planks.png"},
        {"name": "Spruce", "imagePath": github_block_base + "spruce_planks.png"},
        {"name": "Birch", "imagePath": github_block_base + "birch_planks.png"},
        {"name": "Jungle", "imagePath": github_block_base + "jungle_planks.png"},
        {"name": "Acacia", "imagePath": github_block_base + "acacia_planks.png"},
        {"name": "Dark Oak", "imagePath": github_block_base + "dark_oak_planks.png"}
    ]
}

# Write the JSON file
with open('mod_items_catalog.json', 'w', encoding='utf-8') as f:
    json.dump(mod_data, f, indent=2, ensure_ascii=False)

print("JSON file created successfully!")