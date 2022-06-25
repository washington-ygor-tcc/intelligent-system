from typing import Any
from src.core.ports import incoming

class AsynchronousProcessingUseCase(incoming.AsynchronousProcessingPort):
    def process_request(data: Any):
        pass