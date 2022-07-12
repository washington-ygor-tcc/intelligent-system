import os

from src.application.fastapi_factory import FastAPIFactory
from src.application.nats_factory import NatsFactory


class Main:
    def __init__(self):
        self.__application_type = os.environ.get("APPLICATION_TYPE")

        if self.__application_type == "REST":
            self.__application_entrypoint = FastAPIFactory().create_entrypoint()
        elif self.__application_type == "MESSAGING":
            self.__application_entrypoint = NatsFactory().create_entrypoint()
        else:
            raise RuntimeError(
                "Failed to create new application, input application type is not supported!"
            )

    def run(self):
        return self.__application_entrypoint.run()


entrypoint = Main().run()
