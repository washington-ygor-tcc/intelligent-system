from common.src.port.inward.process_request_port import ProcessRequestPort
from common.src.port.outward.dispatch_response_port import DispatchResponsePort
from common.src.application.service.model_service import ModelService


class PredictionRequestProcessor(ProcessRequestPort):
  def __init__(self, response_dispatcher: DispatchResponsePort, model_service: ModelService):
    self.response_dispatcher = response_dispatcher
    self.model_service = model_service

  def process_request(self):
    self.model_service.predict()
    self.response_dispatcher.dispatch_response()