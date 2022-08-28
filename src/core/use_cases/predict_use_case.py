from typing import Dict, Any
from src.core.ports.prediction_request_handler_port import PredictionRequestHandlerPort
from src.core.ports.model_gateway_port import ModelGatewayPort


class PredictUseCase(PredictionRequestHandlerPort):
    def __init__(self, model_gateway: ModelGatewayPort):
        self.__model_gateway = model_gateway

    def handle(self, features: Dict[str, Any]):
        return self.__model_gateway.predict(features)
