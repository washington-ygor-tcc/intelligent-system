from fastapi import FastAPI, Depends

from src.adapter.inward.predict_controller import predict_controller
from src.adapter.outward.predict_callback import PredictCallback
from common.src.adapter.outward.model_adapter import ModelAdapter
from common.src.application.use_case.prediction_request_processor_use_case import PredictionRequestProcessor
from common.src.application.service.model_service import ModelService

app = FastAPI()

model = ModelAdapter()
model_service = ModelService(model)
predict_callback = PredictCallback()
prediction_processor = PredictionRequestProcessor(predict_callback, model_service)

app.include_router(predict_controller.router, dependencies=[Depends(prediction_processor)])
