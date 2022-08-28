import mlflow
import os


class PyFuncMockModel(mlflow.pyfunc.PythonModel):
    def __init__(self):
        super().__init__()

    def predict(self, context, model_input):
        print(model_input)

        return {"status": "OK"}


os.environ["AWS_ACCESS_KEY_ID"] = "minio"
os.environ["AWS_SECRET_ACCESS_KEY"] = "minio123"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:9000"

mlflow.set_tracking_uri("http://localhost:5000")

with mlflow.start_run() as run:
    mlflow.pyfunc.log_model(
        artifact_path="pyfunc_mock_model/v1",
        python_model=PyFuncMockModel(),
        registered_model_name="PyFuncMockModel",
    )
