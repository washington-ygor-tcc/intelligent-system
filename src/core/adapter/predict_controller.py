from fastapi import APIRouter, Depends
from typing import Dict
from src.core.port.request_handler_port import RequestHandlerPort

class PredictController:
    def __init__(self, request_handler : RequestHandlerPort):
        self.__request_handler = request_handler
        self.__router = APIRouter(prefix="/predict")
        self.__router.add_api_route("/", self.predict, methods=["POST"])

    def predict(self):
        return self.__request_handler.handle()

    @property
    def router(self):
        return self.__router
