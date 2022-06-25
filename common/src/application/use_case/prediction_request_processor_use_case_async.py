from common.src.application.service.model_service import ModelService
from common.src.port.inward.process_request_port import ProcessRequestPort
from common.src.port.outward.dispatch_response_port import DispatchResponsePort


class PredictionRequestProcessorAsync(ProcessRequestPort):
    def __init__(self, response_dispatcher: DispatchResponsePort, model_service: ModelService):
        self.__response_dispatcher = response_dispatcher
        self.__model_service = model_service

    def process_request(self):
        prediction = self.__model_service.predict()
        self.__response_dispatcher.dispatch_response(prediction)
