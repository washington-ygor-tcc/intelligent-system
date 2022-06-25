from fastapi import APIRouter, Depends
from src.core.ports.prediction_request_handler_port import PredictionRequestHandlerPort
from src.core.adapters.dto.features_input import FeaturesInputDTO

class PredictController:
    def __init__(self, prediction_request_handler : PredictionRequestHandlerPort):
        self.__prediction_request_handler = prediction_request_handler
        self.__router = APIRouter(prefix="/predict")
        self.__router.add_api_route("/", self.predict, methods=["POST"])

    @property
    def router(self):
        return self.__router

    def predict(self, input: FeaturesInputDTO):
        return self.__prediction_request_handler.handle()
