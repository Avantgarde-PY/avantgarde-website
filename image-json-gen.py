import os
import json

# Base directory and folder names
base_directory = 'img'
folder_names = ['bau', 'dach', 'elektro', 'garage', 'pool', 'sanitar']

# List to hold all image data
image_list = []

# Function to scan directories and collect image paths
def scan_images(base_dir, folders):
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(('.jpg', '.png')):
                    # Construct path with '/img/' prefix
                    image_path = os.path.join('img', folder, file_name).replace('\\', '/')
                    image_list.append({
                        'src': '/' + image_path
                    })

# Scan images and generate JSON file
scan_images(base_directory, folder_names)

# Write to JSON file
with open('portfolio.json', 'w') as json_file:
    json.dump(image_list, json_file, indent=2)

print('portfolio.json has been generated successfully.')
