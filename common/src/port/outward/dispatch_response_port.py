from abc import ABC, abstractmethod


__all__ = ["DispatchResponsePort"]


class DispatchResponsePort(ABC):
    @abstractmethod
    def dispatch_response(self):
        pass
