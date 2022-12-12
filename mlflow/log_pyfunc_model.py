import numpy as np
import mlflow
import os


class PyFuncMockModel(mlflow.pyfunc.PythonModel):
    def __init__(self):
        super().__init__()

    def predict(self, context, model_input):
        complexity_factor = int(model_input["complexity_factor"])
        memory_overhead = int(model_input["memory_overhead"])

        dummy_var = bytearray(1024 * 1024 * memory_overhead)

        A = np.random.uniform(
            low=-10, high=10, size=(complexity_factor, complexity_factor)
        )
        b = np.random.uniform(low=-10, high=10, size=(complexity_factor,))

        x = np.linalg.solve(A, b)

        return {"status": "OK"}


mlflow.set_tracking_uri(os.environ["MLFLOW_ENDPOINT_URL"])

with mlflow.start_run() as run:
    mlflow.pyfunc.log_model(
        artifact_path="pyfunc_mock_model/v1",
        python_model=PyFuncMockModel(),
        registered_model_name="PyFuncMockModel",
    )
