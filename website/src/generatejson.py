import os
import json

# Define the paths
item_folder = r"C:\Users\fayaz\Documents\GitHub\woodstuffmod\woodstuff\python\output\assets\woodstuff\textures\item"
lang_file = r"C:\Users\fayaz\Documents\GitHub\woodstuffmod\woodstuff\python\output\assets\woodstuff\lang\en_us.json"
github_raw_base = "https://raw.githubusercontent.com/fayaz12g/woodstuffmod/main/woodstuff/python/output/assets/woodstuff/textures/item/"

# Read the language file
with open(lang_file, 'r', encoding='utf-8') as f:
    lang_data = json.load(f)

# Create a dictionary to store item names
item_names = {}
for key, value in lang_data.items():
    if key.startswith("item.woodstuff."):
        item_id = key.split(".")[-1]
        item_names[item_id] = value

# Create the tools list
tools = []
for filename in os.listdir(item_folder):
    if filename.endswith(".png"):
        item_id = os.path.splitext(filename)[0]
        item_name = item_names.get(item_id, item_id.replace("_", " ").title())
        
        # Extract stick and material information
        parts = item_id.split("_with_")
        if len(parts) == 2:
            material = parts[0].split("_")[0]
            stick = parts[1].split("_")[0]
        else:
            material = parts[0].split("_")[0]
            stick = "unknown"
        
        tool_type = next((word for word in ["sword", "axe", "pickaxe", "shovel", "hoe"] if word in item_id), "unknown")
        
        tools.append({
            "name": item_name,
            "id": item_id,
            "stick": stick,
            "material": material,
            "type": tool_type,
            "imagePath": github_raw_base + filename
        })

# Create the final JSON structure
mod_data = {
    "tools": tools,
    "sticks": [
        {"name": "Oak Stick", "imagePath": github_raw_base + "oak_stick.png"},
        {"name": "Spruce Stick", "imagePath": github_raw_base + "spruce_stick.png"},
        {"name": "Birch Stick", "imagePath": github_raw_base + "birch_stick.png"},
        {"name": "Jungle Stick", "imagePath": github_raw_base + "jungle_stick.png"},
        {"name": "Acacia Stick", "imagePath": github_raw_base + "acacia_stick.png"},
        {"name": "Dark Oak Stick", "imagePath": github_raw_base + "dark_oak_stick.png"}
    ],
    "materials": [
        {"name": "Diamond", "imagePath": github_raw_base + "diamond_block.png"},
        {"name": "Iron", "imagePath": github_raw_base + "iron_block.png"},
        {"name": "Gold", "imagePath": github_raw_base + "gold_block.png"},
        {"name": "Stone", "imagePath": github_raw_base + "stone.png"},
        {"name": "Oak", "imagePath": github_raw_base + "oak_planks.png"},
        {"name": "Spruce", "imagePath": github_raw_base + "spruce_planks.png"},
        {"name": "Birch", "imagePath": github_raw_base + "birch_planks.png"},
        {"name": "Jungle", "imagePath": github_raw_base + "jungle_planks.png"},
        {"name": "Acacia", "imagePath": github_raw_base + "acacia_planks.png"},
        {"name": "Dark Oak", "imagePath": github_raw_base + "dark_oak_planks.png"}
    ]
}

# Write the JSON file
with open('mod_items_catalog.json', 'w', encoding='utf-8') as f:
    json.dump(mod_data, f, indent=2, ensure_ascii=False)

print("JSON file created successfully!")