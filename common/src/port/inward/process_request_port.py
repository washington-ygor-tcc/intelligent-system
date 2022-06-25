from abc import ABC, abstractmethod


class ProcessRequestPort(ABC):
    @abstractmethod
    def process_request(self):
        ...
