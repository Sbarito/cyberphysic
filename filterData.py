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


def keep_first_n_images(images_folder, labels_folder, n=150):
    image_files = [f for f in os.listdir(images_folder) if f.lower().endswith('.png')]
    image_files.sort()  
    
    print(f"Всего найдено изображений: {len(image_files)}")
    
    keep_images = set(image_files[:n])
    
    keep_masks = keep_images
    
    print(f"Оставляем первые {n} изображений и {n} масок")
    
    removed_count = 0
    for img_file in image_files:
        if img_file not in keep_images:
            img_path = os.path.join(images_folder, img_file)
            try:
                os.remove(img_path)
                removed_count += 1
            except Exception as e:
                print(f"Ошибка при удалении {img_file}: {e}")
    
    print(f"Удалено изображений: {removed_count}")
    
    mask_removed = 0
    for mask_file in os.listdir(labels_folder):
        if mask_file.lower().endswith('.png'):
            if mask_file not in keep_masks:
                mask_path = os.path.join(labels_folder, mask_file)
                try:
                    os.remove(mask_path)
                    mask_removed += 1
                except Exception as e:
                    print(f"Ошибка при удалении маски {mask_file}: {e}")
    
    print(f"Удалено масок: {mask_removed}")
    print(f"Итоговое количество изображений: {len([f for f in os.listdir(images_folder) if f.endswith('.png')])}")
    print(f"Итоговое количество масок: {len([f for f in os.listdir(labels_folder) if f.endswith('.png')])}")

keep_first_n_images(images_path, folder_path, n=150)