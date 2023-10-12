import os
import shutil
import random

data_root = "Frames"
train_root = "train"
test_root = "test"
validate_root = "validate"

split_ratio = {
    "train": 0.7,
    "test": 0.2,
    "validate": 0.1
}

# Iterate through each class directory
for class_dir in os.listdir(data_root):
    class_path = os.path.join(data_root, class_dir)
    
    # Create corresponding directories in train, test, and validate
    for split_dir in [train_root, test_root, validate_root]:
        split_class_dir = os.path.join(split_dir, class_dir)
        os.makedirs(split_class_dir, exist_ok=True)
    
    # Get a list of all frames for the current class
    frames = os.listdir(class_path)
    
    # Shuffle the frames randomly
    random.shuffle(frames)
    
    # Calculate the split indices
    total_frames = len(frames)
    train_split_index = int(total_frames * split_ratio["train"])
    test_split_index = train_split_index + int(total_frames * split_ratio["test"])
    
    # Move frames to respective split directories
    for idx, frame in enumerate(frames):
        source_path = os.path.join(class_path, frame)
        if idx < train_split_index:
            dest_dir = os.path.join(train_root, class_dir)
        elif idx < test_split_index:
            dest_dir = os.path.join(test_root, class_dir)
        else:
            dest_dir = os.path.join(validate_root, class_dir)
        dest_path = os.path.join(dest_dir, frame)
        shutil.copy(source_path, dest_path)
