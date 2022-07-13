from abc import ABC, abstractmethod
from typing import Dict, Any


class PredictionRequestHandlerPort(ABC):
    @abstractmethod
    def handle(self, features: Dict[str, Any]):
        pass
