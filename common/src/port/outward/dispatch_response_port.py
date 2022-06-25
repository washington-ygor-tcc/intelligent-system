from abc import ABC, abstractmethod

class DispatchResponsePort(ABC):
  @abstractmethod
  def dispatchResponse(self):
    pass