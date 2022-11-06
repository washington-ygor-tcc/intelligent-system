import numpy as np
import mlflow
import os


class PyFuncMockModel(mlflow.pyfunc.PythonModel):
    def __init__(self):
        super().__init__()
        self.dim = int(os.environ["LINEAR_SYSTEM_DIMENSION"])

    def predict(self, context, model_input):

        for i in range(int(model_input["feature_size"])):
            A = np.random.uniform(low=-10, high=10, size=(self.dim, self.dim))
            b = np.random.uniform(low=-10, high=10, size=(self.dim,))

        return {"status": "OK"}


mlflow.set_tracking_uri(os.environ["MLFLOW_ENDPOINT_URL"])

with mlflow.start_run() as run:
    mlflow.pyfunc.log_model(
        artifact_path="pyfunc_mock_model/v1",
        python_model=PyFuncMockModel(),
        registered_model_name="PyFuncMockModel",
    )
