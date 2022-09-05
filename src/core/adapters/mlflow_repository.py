import time
import mlflow

from typing import Dict, Any
from src.core.ports.model_gateway_port import ModelGatewayPort


class MLFlowPyFuncRepository(ModelGatewayPort):
    def __init__(self, server_uri: str, model_uri: str):
        mlflow.set_tracking_uri(server_uri)

        self.__loaded_model = mlflow.pyfunc.load_model(model_uri)

    def predict(self, features: Dict[str, Any]):
        return self.__loaded_model.predict(features)
