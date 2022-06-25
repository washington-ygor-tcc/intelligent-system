import time

from src.core.ports.model_port import ModelPort

class ModelAdapter(ModelPort):
  def predict(self):
    time.sleep(1)

    return { "status": "OK" }

