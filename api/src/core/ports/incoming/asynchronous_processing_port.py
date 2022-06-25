import abc
from typing import Any

class AsynchronousProcessingPort(abc.ABC):

    @abc.abstractmethod
    def process_request(data: Any):
        "Process a request asynchronous"