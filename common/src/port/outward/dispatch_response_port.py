from abc import ABC, abstractmethod

class DispatchResponsePort(ABC):
  @abstractmethod
  def dispatch_response(self):
    pass