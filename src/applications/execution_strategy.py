from abc import ABC, abstractmethod

class ExecutionStrategy(ABC):
  @abstractmethod
  def run(self):
    pass
