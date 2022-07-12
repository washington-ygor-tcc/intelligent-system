from abc import ABC, abstractmethod


class ModelPort(ABC):
    @abstractmethod
    def predict(self):
        pass
