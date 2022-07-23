from src.application.ports.application_factory import ApplicationFactory
from src.core.ports.prediction_request_handler_port import PredictionRequestHandlerPort
from src.application.adapters.fastapi_entrypoint import FastAPIEntrypoint


class FastAPIFactory(ApplicationFactory):
    def create_entrypoint(self):
        return FastAPIEntrypoint(self._prediction_request_handler)
