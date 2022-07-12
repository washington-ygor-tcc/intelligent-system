from fastapi import FastAPI
from src.application.interfaces.entrypoint import Entrypoint
from src.core.ports.prediction_request_handler_port import PredictionRequestHandlerPort
from src.core.adapters.predict_controller import PredictController


class FastAPIEntrypoint(Entrypoint):
    def __init__(self, prediction_request_handler: PredictionRequestHandlerPort):
        self.__app = FastAPI()

        self.__predict_controller = PredictController(prediction_request_handler)

        self.__app.include_router(self.__predict_controller.router)

    def run(self):
        return self.__app
