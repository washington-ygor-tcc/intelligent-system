from src.core.ports.prediction_request_handler_port import PredictionRequestHandlerPort
from src.core.ports.model_port import ModelPort


class PredictUseCase(PredictionRequestHandlerPort):
    def __init__(self, model: ModelPort):
        self.__model = model

    def handle(self):
        return self.__model.predict()
