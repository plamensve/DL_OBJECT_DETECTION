import mlflow
from mlflow.protos.databricks_uc_registry_messages_pb2 import PATH

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("SMBT")

with mlflow.start_run():
    mlflow.log_param("epochs", 100)
    mlflow.log_param("batch_size", 4)
    mlflow.log_param("img_size", 640)
    mlflow.log_param("device", 0)
    mlflow.log_param("workers", 0)

    PATH_ARTIFACTS = '../01_notebooks/runs/detect/smbt_detection62/'

    mlflow.log_artifact(f'{PATH_ARTIFACTS}BoxF1_curve.png')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}BoxP_curve.png')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}BoxPR_curve.png')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}BoxR_curve.png')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}confusion_matrix.png')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}confusion_matrix_normalized.png')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}labels.jpg')
    mlflow.log_artifact(f'{PATH_ARTIFACTS}results.png')

    mlflow.log_artifact(f'{PATH_ARTIFACTS}results.csv')

    mlflow.log_artifact(f"{PATH_ARTIFACTS}weights/best.pt")