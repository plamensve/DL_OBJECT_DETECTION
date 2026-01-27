import os
from os import name
from supabase import create_client, Client

SUPABASE_URL = "https://vioyxjxybixxnfksdsmg.supabase.co/"
SUPABASE_KEY = "sb_publishable_xzjrQUF12BKooe7UY13mbQ_-dL-Z_BK"

BUCKET = "training_images"
LOCAL_ROOT = "../04_labeled_data"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def download_folder(remote_folder, local_folder):
    os.makedirs(local_folder, exist_ok=True)

    files = supabase.storage.from_(BUCKET).list(remote_folder)

    for f in files:
        name = f["name"]

        if name.startswith("."):
            continue

        remote_path = f"{remote_folder}/{name}"
        local_path = os.path.join(local_folder, name)

        data = supabase.storage.from_(BUCKET).download(remote_path)

        with open(local_path, "wb") as out:
            out.write(data)

        print(f"Downloaded: {remote_path}")
        pass


def download_root_files(local_root):
    os.makedirs(local_root, exist_ok=True)

    root_items = supabase.storage.from_(BUCKET).list("")

    for item in root_items:
        name = item["name"]
        meta = item.get("metadata")

        if meta is None or meta.get("size", 0) == 0:
            continue

        remote_path = name
        local_path = os.path.join(local_root, name)

        data = supabase.storage.from_(BUCKET).download(remote_path)

        with open(local_path, "wb") as out:
            out.write(data)

        print(f"Downloaded: {remote_path}")


if __name__ == "__main__":
    download_folder("images", os.path.join(LOCAL_ROOT, "images"))
    download_folder("labels", os.path.join(LOCAL_ROOT, "labels"))
    download_root_files(LOCAL_ROOT)