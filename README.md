# DL_OBJECT_DETECTION

## Description
An object detection project (pastry/confectionery items) using deep learning and YOLO.

## Project Structure

### `00_data_preparation/`
- **`01_download_training_images.py`** – Downloads training images. This script demonstrates a Supabase integration in case the dataset is stored in an external database. That was part of the original project idea, but the free tier did not allow storing a large volume of data. The file is still kept in the repository for reference and potential future use.

- **`02_split_images.py`** – Splits the images into `train/val` sets. This script takes already-labeled data and separates it into training and validation folders.

- **`03_create_yaml.py`** – Generates `data.yaml` for YOLO configuration. This file contains key information required for training the model: the dataset path, the paths to the training and validation data, the number of classes, and the name of each class used for classification / object detection in real-world scenarios.

- **`04_run_pipeline.py`** – Runs the scripts above sequentially. This file automatically executes the full pipeline in case Supabase is used as the data source.

### `01_notebooks/`
- Jupyter notebooks for experiments, training, and analysis. Currently, there are 4 notebooks intended for model setup and training.

### `02_dataset/`
- Prepared dataset (YOLO-compatible structure). Contains the annotated data already split into training and validation. This is the main directory used by the model during training.

### `03_source_data/`
- Raw source data before processing. This directory contains data that has not been prepared yet and is not annotated.

### `04_labeled_data/`
- **`images/`** – images with annotations.
- **`labels/`** – YOLO labels (bounding boxes).
- **`classes.txt`** – list of classes.
- **`notes.json`** – helper notes / metadata for the annotations.

### `05_experiments/`
- **`mlartifacts/`** – MLflow artifacts (models, metrics, etc.).
- **`ml_flow.py`** – script for logging/experimenting with MLflow.
- **`mlflow.db`** – local MLflow database.
- **`start_mlflow_server`** – helper script for starting the MLflow server.

### `article/`
- Materials or drafts for an article/documentation.

### `photos/`
- Sample images for inference/demonstration.

### `README.md`
- Project description and structure.

### `requirements.txt`
- Project dependencies for installation.
