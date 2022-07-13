from abc import ABC, abstractmethod
from typing import Dict, Any


class ModelPort(ABC):
    @abstractmethod
    def predict(self, features: Dict[str, Any]):
        pass
