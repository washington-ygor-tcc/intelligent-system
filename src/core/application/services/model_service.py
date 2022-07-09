from src.core.port.model_port import ModelPort


class ModelService:
  def __init__(self, model: ModelPort):
    self.model = model

  def predict(self):
    return self.model.predict()

