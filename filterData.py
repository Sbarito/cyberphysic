import os
from PIL import Image

folder_path = r"./train_labels"

for filename in os.listdir(folder_path):
    old_path = os.path.join(folder_path, filename)

    if os.path.isfile(old_path):
        name, ext = os.path.splitext(filename)

        if name.endswith("_segmentation"):
            new_name = name.replace("_segmentation", "") + ext
            new_path = os.path.join(folder_path, new_name)

            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
                print(f"{filename} → {new_name}")


images_path = r"./train_images"

for filename in os.listdir(images_path):
    file_path = os.path.join(images_path, filename)

    if os.path.isfile(file_path):
        name, ext = os.path.splitext(filename)

        if ext.lower() in [".jpg", ".jpeg"]:
            img = Image.open(file_path)

            new_file_path = os.path.join(images_path, name + ".png")
            img.save(new_file_path, "PNG")

            os.remove(file_path)

            print(f"Converted: {filename} -> {name}.png")