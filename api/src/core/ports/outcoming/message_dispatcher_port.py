import abc
from typing import Any

class MessageDispatcherPort(abc.ABC):

    @abc.abstractmethod
    def dispatch_message(message: Any):
        "To be documented"