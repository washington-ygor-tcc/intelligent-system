import time
import mlflow

from typing import Dict, Any
from src.core.ports.model_gateway_port import ModelGatewayPort
from src.core.adapters.mlflow.model_flavor import MLFlowModelFlavor

model_loader_map = {MLFlowModelFlavor.PYFUNC: mlflow.pyfunc.load_model}


class MLFlowRepository(ModelGatewayPort):
    def __init__(self, server_uri: str, model_uri: str, model_flavor: str):
        mlflow.set_tracking_uri(server_uri)

        try:
            self.__loaded_model = model_loader_map[model_flavor](model_uri)
        except KeyError:
            raise Exception("Model loader does not exists!")

    def predict(self, features: Dict[str, Any]):
        return self.__loaded_model.predict(features)
