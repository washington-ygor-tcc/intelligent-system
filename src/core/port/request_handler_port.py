from abc import ABC, abstractmethod

class RequestHandlerPort(ABC):
  @abstractmethod
  def handle(self):
    pass