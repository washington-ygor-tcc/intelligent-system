from src.core.ports.prediction_request_handler_port import PredictionRequestHandlerPort
from src.core.adapters.dto.features import MessageRequestDTO


class PredictMessageConsumer:
    def __init__(self, prediction_request_handler: PredictionRequestHandlerPort):
        self.__prediction_request_handler = prediction_request_handler

    def predict(self, feature_request: MessageRequestDTO):
        return self.__prediction_request_handler.handle()
