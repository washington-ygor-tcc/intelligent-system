from typing import Any
from src.core.ports import incoming, outcoming

class SynchronousProcessingUseCase(incoming.SynchronousProcessingPort):

    def __init__(self, message_dispatcher: outcoming.MessageDispatcherPort, machine_learning_service):
        self.message_dispacther = message_dispatcher
        self.machine_learning_service = machine_learning_service

    def process_request(data: Any):
        pass