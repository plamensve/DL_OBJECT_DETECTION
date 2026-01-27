import os
import yaml

BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))

def create_data_yaml(path_to_classes_txt, path_to_data_yaml):
    if not os.path.exists(path_to_classes_txt):
        print("classes.txt file not found")
        return

    with open(path_to_classes_txt, "r") as f:
        classes = [line.strip() for line in f if line.strip()]

    data = {
        "path": "../02_dataset",
        "train": "images/train",
        "val": "images/val",
        "nc": len(classes),
        "names": classes
    }

    with open(path_to_data_yaml, "w") as f:
        yaml.dump(data, f, sort_keys=False)

    print(f"Created config file at {path_to_data_yaml}")

if __name__ == "__main__":
    path_to_classes_txt = os.path.join(BASE_DIR, "04_labeled_data", "classes.txt")
    path_to_data_yaml = os.path.join(BASE_DIR, "02_dataset", "data.yaml")

    create_data_yaml(path_to_classes_txt, path_to_data_yaml)

