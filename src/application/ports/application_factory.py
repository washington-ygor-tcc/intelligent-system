from yaml import load, loader
from abc import ABC, abstractmethod
from src.application.ports.entrypoint import Entrypoint
from src.core.ports.prediction_request_handler_port import PredictionRequestHandlerPort
from src.core.adapters.mlflow_repository import MLFlowRepository
from src.core.use_cases.predict_use_case import PredictUseCase


class ApplicationFactory(ABC):
    def __init__(self):
        self.__load_config()
        self.__model = MLFlowRepository(
            self._config["mlflow"]["server_uri"],
            self._config["mlflow"]["model_uri"],
            self._config["mlflow"]["loader"],
        )
        self._prediction_request_handler = PredictUseCase(self.__model)

    def __load_config(self):
        with open("./src/config.yaml") as file:
            self._config = load(file, Loader=loader.SafeLoader)

    @abstractmethod
    def create_entrypoint(self) -> Entrypoint:
        pass
