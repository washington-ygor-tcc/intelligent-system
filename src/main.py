import os
from src.rest_api_application import RestAPI
from src.config.execution_strategy import ExecutionStrategy
from src.core.adapter.model_adapter import ModelAdapter
from src.core.application.use_cases.prediction_request_handler import PredictionRequestHandler
from src.core.application.services.model_service import ModelService
from src.core.port.request_handler_port import RequestHandlerPort


class Application:
  def __init__(self):
    self.__type = os.environ.get('APPLICATION_TYPE')
    self.__model = ModelAdapter()
    self.__model_service = ModelService(self.__model)
    self.__request_handler = PredictionRequestHandler(self.__model_service)

    if self.__type == 'REST':
      self.__execution_strategy = RestAPI(self.__request_handler)
    else:
      raise RuntimeError('Failed to set an execution strategy, input application type is invalid!')

  def run(self):
    return self.__execution_strategy.run()

application = Application().run()
