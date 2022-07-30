import time

from typing import Dict, Any
from src.core.ports.model_port import ModelPort

from random import randint


class ModelAdapter(ModelPort):
    def predict(self, features: Dict[str, Any]):
        time.sleep(1)
        return {"status": "OK"}
