import os
from PIL import Image

folder_path = r"./train_labels"
images_path = r"./train_images"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if os.path.isfile(file_path):
        name, ext = os.path.splitext(filename)
        
        if ext.lower() in [".jpg", ".jpeg"]:
            os.remove(file_path)
            print(f"Удален из train_labels: {filename}")

for filename in os.listdir(images_path):
    file_path = os.path.join(images_path, filename)
    
    if os.path.isfile(file_path):
        name, ext = os.path.splitext(filename)
        
        if ext.lower() in [".jpg", ".jpeg"]:
            os.remove(file_path)
            print(f"Удален из train_images: {filename}")