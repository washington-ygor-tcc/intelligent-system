from src.core.ports.prediction_request_handler_port import PredictionRequestHandlerPort
from src.core.adapters.dto.features import FeaturesRequestDTO


class PredictController:
    def __init__(self, prediction_request_handler: PredictionRequestHandlerPort):
        self.__prediction_request_handler = prediction_request_handler

    def predict(self, feature_request: FeaturesRequestDTO):
        return self.__prediction_request_handler.handle(feature_request.features)
