from src.application.interfaces.application_factory import ApplicationFactory
from src.core.adapters.predict_controller import PredictController
from src.application.nats_entrypoint import NatsEntrypoint


class NatsFactory(ApplicationFactory):
    def create_entrypoint(self):
        return NatsEntrypoint(
            self._prediction_request_handler,
            self._config["nats"]["url"],
            self._config["nats"]["request_channel"],
            self._config["nats"]["response_channel"],
        )
