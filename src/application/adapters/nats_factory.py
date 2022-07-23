from src.application.ports.application_factory import ApplicationFactory
from src.application.adapters.nats_entrypoint import NatsEntrypoint


class NatsFactory(ApplicationFactory):
    def create_entrypoint(self):
        return NatsEntrypoint(
            self._prediction_request_handler,
            self._config["nats"]["url"],
            self._config["nats"]["request_channel"],
            self._config["nats"]["response_channel"],
        )
