import time

from common.src.port.outward.model_port import ModelPort

class ModelAdapter(ModelPort):
  def predict(self):
    time.sleep(1)

    return { "status": "OK" }

