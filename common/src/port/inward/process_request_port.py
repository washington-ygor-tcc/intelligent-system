from abc import ABC, abstractmethod

class ProcessRequestPort(ABC):
  @abstractmethod
  def processRequest(self):
    pass