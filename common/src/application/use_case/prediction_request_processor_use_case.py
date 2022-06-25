from common.src.port.inward.process_request_port import ProcessRequestPort
from common.src.port.outward.dispatch_response_port import DispatchResponsePort
from common.src.port.outward.model_port import ModelPort
from common.src.application.service.model_service import predict


class PredictionRequestProcessor(ProcessRequestPort):
  def __init__(self, response_dispatcher: DispatchResponsePort, model: ModelPort):
    self.response_dispatcher = response_dispatcher
    self.model = model

  def processRequest(self):
    predict()
    self.response_dispatcher.dispatchResponse()