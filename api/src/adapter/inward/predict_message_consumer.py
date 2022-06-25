import os

import pika

from common.src.adapter.outward import DispatchResponseAdapter, ModelAdapter
from common.src.application.service.model_service import ModelService
from common.src.application.use_case.prediction_request_processor_use_case_async import (
    PredictionRequestProcessorAsync,
)

url = os.environ.get("CLOUDAMQP_URL", "amqp://guest:guest@localhost/%2f")
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue="predict")

model_adapter = ModelAdapter()
model_service = ModelService(model_adapter)
dispatch_response_adapter = DispatchResponseAdapter(channel)
prediction_processor = PredictionRequestProcessorAsync(dispatch_response_adapter, model_service)


def predict(ch, method, properties, body):
    prediction_processor.process_request()


def result(ch, method, properties, body):
    print("recebido", body)


channel.basic_consume("predict", predict, auto_ack=True)
channel.basic_consume("prediction_result", result, auto_ack=True)


channel.start_consuming()
connection.close()
