import sys
from pathlib import Path

import mlflow

AUGMENTATION_PARAMS = {
    "mosaic": 1.0,
    "mixup": 0.1,
    "close_mosaic": 10,
    "fliplr": 0.5,
    "hsv_h": 0.015,
    "hsv_s": 0.7,
    "hsv_v": 0.4,

    "degrees": 10,
    "shear": 2,
    "scale": 0.5,
}

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("SMBT")

with mlflow.start_run():
    mlflow.log_param("epochs", 250)
    mlflow.log_param("batch_size", 6)
    mlflow.log_param("img_size", 640)
    mlflow.log_param("device", 0)
    mlflow.log_param("workers", 0)

    mlflow.log_params(AUGMENTATION_PARAMS)

    PATH_ARTIFACTS = '../01_notebooks/runs/detect/smbt_detection_15'

    mlflow.log_artifact(f'{PATH_ARTIFACTS}/BoxF1_curve.png')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}/BoxP_curve.png')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}/BoxPR_curve.png')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}/BoxR_curve.png')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}/confusion_matrix.png')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}/confusion_matrix_normalized.png')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}/labels.jpg')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}/results.png')

    mlflow.log_artifact(f'{PATH_ARTIFACTS}/results.csv')

    mlflow.log_artifact(f"{PATH_ARTIFACTS}/weights/best.pt")