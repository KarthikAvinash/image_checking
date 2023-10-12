import os

def identify_corrupted_images(directory, min_file_size=300):
    for class_dir in os.listdir(directory):
        class_path = os.path.join(directory, class_dir)
        
        # Skip if it's not a directory
        if not os.path.isdir(class_path):
            continue
        
        for filename in os.listdir(class_path):
            if filename.endswith(".jpg"):
                image_path = os.path.join(class_path, filename)
                file_size = os.path.getsize(image_path)
                if file_size < min_file_size:
                    print(f"Potentially corrupted image: {image_path}, File size: {file_size} bytes")

# Identify potentially corrupted images in "train" directory
identify_corrupted_images("train")

# Identify potentially corrupted images in "test" directory
identify_corrupted_images("test")

# Identify potentially corrupted images in "validate" directory
identify_corrupted_images("validate")
