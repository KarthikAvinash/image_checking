import os

def rename_images(directory):
    for class_dir in os.listdir(directory):
        class_path = os.path.join(directory, class_dir)
        
        # Skip if it's not a directory
        if not os.path.isdir(class_path):
            continue
        
        count = 1
        for filename in os.listdir(class_path):
            if filename.endswith(".jpg"):
                new_filename = f"{class_dir}_{count:04d}.jpg"
                old_path = os.path.join(class_path, filename)
                new_path = os.path.join(class_path, new_filename)
                os.rename(old_path, new_path)
                count += 1

# Rename images in "train" directory
rename_images("train")

# Rename images in "test" directory
rename_images("test")

# Rename images in "validate" directory
rename_images("validate")
