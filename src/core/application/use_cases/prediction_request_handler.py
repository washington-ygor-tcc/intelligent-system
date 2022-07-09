from src.core.port.request_handler_port import RequestHandlerPort
from src.core.application.services.model_service import ModelService


class PredictionRequestHandler(RequestHandlerPort):
  def __init__(self, model_service: ModelService):
    self.model_service = model_service

  def handle(self):
    return self.model_service.predict()