import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("SMBT")

with mlflow.start_run():
    mlflow.log_param("epochs", 200)
    mlflow.log_param("batch_size", 4)
    mlflow.log_param("img_size", 960)
    mlflow.log_param("device", 0)
    mlflow.log_param("workers", 0)

    mlflow.log_artifact('../01_notebooks/runs/detect/smbt_detection4/BoxF1_curve.png')
    mlflow.log_artifact('../01_notebooks/runs/detect/smbt_detection4/BoxP_curve.png')
    mlflow.log_artifact('../01_notebooks/runs/detect/smbt_detection4/BoxPR_curve.png')
    mlflow.log_artifact('../01_notebooks/runs/detect/smbt_detection4/BoxR_curve.png')
    mlflow.log_artifact('../01_notebooks/runs/detect/smbt_detection4/confusion_matrix.png')
    mlflow.log_artifact('../01_notebooks/runs/detect/smbt_detection4/confusion_matrix_normalized.png')
    mlflow.log_artifact('../01_notebooks/runs/detect/smbt_detection4/labels.jpg')
    mlflow.log_artifact('../01_notebooks/runs/detect/smbt_detection4/results.png')

    mlflow.log_artifact('../01_notebooks/runs/detect/smbt_detection4/results.csv')

    mlflow.log_artifact("../01_notebooks/runs/detect/smbt_detection4/weights/best.pt")