from abc import ABC, abstractmethod
from typing import Dict, Any


class ModelGatewayPort(ABC):
    @abstractmethod
    def predict(self, features: Dict[str, Any]):
        pass
