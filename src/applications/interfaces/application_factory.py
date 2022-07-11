from abc import ABC, abstractmethod
from src.applications.interfaces.entrypoint import Entrypoint
from src.core.ports.prediction_request_handler_port import PredictionRequestHandlerPort
from src.core.adapters.model_adapter import ModelAdapter
from src.core.use_cases.predict_use_case import PredictUseCase


class ApplicationFactory(ABC):
  def __init__(self):
    self.__model = ModelAdapter()
    self._prediction_request_handler = PredictUseCase(self.__model)

  @abstractmethod
  def create_entrypoint(self) -> Entrypoint:
    pass
