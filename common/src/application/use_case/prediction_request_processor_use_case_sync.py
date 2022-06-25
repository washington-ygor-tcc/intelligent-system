from common.src.port.inward.process_request_port import ProcessRequestPort
from common.src.application.service.model_service import ModelService


class PredictionRequestProcessorSync(ProcessRequestPort):
    def __init__(self, model_service: ModelService):

        self.model_service = model_service

    def process_request(self):
        return self.model_service.predict()
