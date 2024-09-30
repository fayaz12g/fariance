import json
from itertools import product
import os
from PIL import Image, ImageOps
from constants import *

import shutil
import os

def copy_resources():
    # Walk through all files and directories in copy_dir
    for root, dirs, files in os.walk(copy_dir):
        # Create the relative path from the copy_dir root
        relative_path = os.path.relpath(root, copy_dir)
        # Define the corresponding output directory
        target_dir = os.path.join(output_dir, relative_path)

        # Ensure the target directory exists
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Copy each file from the current directory in copy_dir to the corresponding location in output_dir
        for file_name in files:
            src_file = os.path.join(root, file_name)
            dest_file = os.path.join(target_dir, file_name)
            
            # Copy file, overwrite if it exists
            shutil.copy2(src_file, dest_file)
    
    print("Finished copying resources!")


