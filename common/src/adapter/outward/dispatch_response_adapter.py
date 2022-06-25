from common.src.port import outward
import json


class DispatchResponseAdapter(outward.DispatchResponsePort):
    def __init__(self, channel):
        self.__channel = channel
        self.__channel.queue_declare(queue="prediction_result")

    def dispatch_response(self, data):
        data_parsed = json.dumps(data)
        self.__channel.basic_publish(exchange="", routing_key="prediction_result", body=data_parsed)
