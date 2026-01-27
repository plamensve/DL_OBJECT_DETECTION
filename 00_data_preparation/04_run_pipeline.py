import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def run(script_name):
    script_path = BASE_DIR / script_name
    print(f"\n=== Running {script_path.name} ===")
    subprocess.check_call([sys.executable, str(script_path)])

if __name__ == "__main__":
    run("01_download_training_images.py")
    run("02_split_images.py")
    run("03_create_yaml.py")