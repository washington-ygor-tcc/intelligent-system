from abc import ABC, abstractmethod

class PredictionRequestHandlerPort(ABC):
  @abstractmethod
  def handle(self):
    pass