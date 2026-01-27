import random
from pathlib import Path
import shutil

BASE_DIR = Path.cwd().parent

SOURCE_IMG_DIR = BASE_DIR / "04_labeled_data" / "images"
SOURCE_LBL_DIR = BASE_DIR / "04_labeled_data" / "labels"
CLASSES_PATH   = BASE_DIR / "04_labeled_data" / "classes.txt"

# Output directories
OUT_IMG_TRAIN = BASE_DIR / "02_dataset" / "images" / "train"
OUT_IMG_VAL   = BASE_DIR / "02_dataset" / "images" / "val"
OUT_LBL_TRAIN = BASE_DIR / "02_dataset" / "labels" / "train"
OUT_LBL_VAL   = BASE_DIR / "02_dataset" / "labels" / "val"

# Create output dirs
for d in [OUT_IMG_TRAIN, OUT_IMG_VAL, OUT_LBL_TRAIN, OUT_LBL_VAL]:
    d.mkdir(parents=True, exist_ok=True)

# Get all images
images = list(SOURCE_IMG_DIR.glob("*"))
random.shuffle(images)

val_count = int(len(images) * 0.2)
val_images = images[:val_count]
train_images = images[val_count:]

def copy_pairs(image_list, img_dst, lbl_dst):
    for img_path in image_list:
        lbl_path = SOURCE_LBL_DIR / f"{img_path.stem}.txt"
        if lbl_path.exists():
            shutil.copy(img_path, img_dst / img_path.name)
            shutil.copy(lbl_path, lbl_dst / lbl_path.name)

copy_pairs(train_images, OUT_IMG_TRAIN, OUT_LBL_TRAIN)
copy_pairs(val_images, OUT_IMG_VAL, OUT_LBL_VAL)

if __name__ == "__main__":
    print("Starting train/val split...")
    copy_pairs(train_images, OUT_IMG_TRAIN, OUT_LBL_TRAIN)
    copy_pairs(val_images, OUT_IMG_VAL, OUT_LBL_VAL)
    print("Done")