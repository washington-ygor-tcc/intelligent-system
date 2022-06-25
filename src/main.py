import os
from src.applications.rest_api import RestAPI
from src.applications.execution_strategy import ExecutionStrategy
from src.core.adapters.model_adapter import ModelAdapter
from src.core.use_cases.predict_use_case import PredictUseCase
from src.core.ports.prediction_request_handler_port import PredictionRequestHandlerPort


class Application:
  def __init__(self):
    self.__type = os.environ.get('APPLICATION_TYPE')
    self.__model = ModelAdapter()
    self.__prediction_request_handler = PredictUseCase(self.__model)

    if self.__type == 'REST':
      self.__execution_strategy = RestAPI(self.__prediction_request_handler)
    else:
      raise RuntimeError('Failed to set an execution strategy, input application type is invalid!')

  def run(self):
    return self.__execution_strategy.run()

application = Application().run()
