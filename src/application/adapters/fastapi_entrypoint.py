from fastapi import FastAPI, APIRouter
from src.application.ports.entrypoint import Entrypoint
from src.application.adapters.dto.features import FeaturesRequestDTO
from src.core.ports.prediction_request_handler_port import PredictionRequestHandlerPort


class FastAPIEntrypoint(Entrypoint):
    def __init__(self, prediction_request_handler: PredictionRequestHandlerPort):
        self.__app = FastAPI()
        self.__prediction_request_handler = prediction_request_handler

        predict_router = APIRouter(prefix="/predict")
        predict_router.add_api_route("", self.__predict, methods=["POST"])

        self.__app.include_router(predict_router)

    async def __predict(self, feature_request: FeaturesRequestDTO):
        return self.__prediction_request_handler.handle(feature_request.features)

    def run(self):
        return self.__app
