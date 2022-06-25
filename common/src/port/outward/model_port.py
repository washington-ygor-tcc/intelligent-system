from abc import ABC, abstractmethod


__all__ = ["ModelPort"]


class ModelPort(ABC):
    @abstractmethod
    def predict(self):
        pass
