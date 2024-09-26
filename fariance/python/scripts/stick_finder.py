import os
import json

# Define paths
recipes_dir = r"C:\Users\fayaz\AppData\Roaming\.minecraft\versions\24w39a\24w39a\data\minecraft\recipe"
existing_recipes_dir = r"C:\Users\fayaz\Documents\GitHub\woodstuffmod\fariance\src\main\resources\data\minecraft\recipe"
output_file = os.path.join(os.path.dirname(__file__), "stick_recipes.json")

# List to hold the names of files containing "minecraft:stick"
stick_recipes = []

# Function to scan JSON files for "minecraft:stick"
def find_stick_in_recipes():
    # Loop through all files in the recipes directory
    for filename in os.listdir(recipes_dir):
        # Check if the file is a JSON file
        if filename.endswith(".json"):
            # Full path to the file in the original directory
            file_path = os.path.join(recipes_dir, filename)
            
            # Check if a file with the same name exists in the existing recipes directory
            existing_file_path = os.path.join(existing_recipes_dir, filename)
            if os.path.exists(existing_file_path):
                # If the file exists, skip it
                print(f"Skipping {filename} as it already exists in the 'woodstuffmod' directory.")
                continue
            
            try:
                # Open and load the JSON file
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    # Convert the JSON object to string and search for "minecraft:stick"
                    if "minecraft:stick" in json.dumps(data):
                        # If found, add the file name to the list
                        stick_recipes.append(filename)
            except json.JSONDecodeError:
                print(f"Could not decode JSON file: {filename}")

# Run the function
find_stick_in_recipes()

# Save the output into a new JSON file
with open(output_file, 'w', encoding='utf-8') as outfile:
    json.dump(stick_recipes, outfile, indent=4)

print(f"Found 'minecraft:stick' in {len(stick_recipes)} file(s). Results saved to {output_file}")
