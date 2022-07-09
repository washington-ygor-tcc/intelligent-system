from fastapi import FastAPI
from src.config.execution_strategy import ExecutionStrategy
from src.core.port.request_handler_port import RequestHandlerPort
from src.core.adapter.predict_controller import PredictController

class RestAPI(ExecutionStrategy):
  def __init__(self, request_handler: RequestHandlerPort):
    self.__app = FastAPI()

    self.__predict_controller = PredictController(request_handler)

    self.__app.include_router(self.__predict_controller.router)

  def run(self):
    return self.__app