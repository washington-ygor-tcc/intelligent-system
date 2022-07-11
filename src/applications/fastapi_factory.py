from src.applications.interfaces.application_factory import ApplicationFactory
from src.core.ports.prediction_request_handler_port import PredictionRequestHandlerPort
from src.core.adapters.predict_controller import PredictController
from src.applications.fastapi_entrypoint import FastAPIEntrypoint


class FastAPIFactory(ApplicationFactory):
  def create_entrypoint(self):
    return FastAPIEntrypoint(self._prediction_request_handler)