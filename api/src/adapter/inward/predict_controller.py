from typing import Dict
from fastapi import APIRouter

from common.src.adapter.outward.model_adapter import ModelAdapter
from common.src.application.use_case.prediction_request_processor_use_case_sync import (
    PredictionRequestProcessorSync,
)
from common.src.application.service.model_service import ModelService

predict_router = APIRouter()

model = ModelAdapter()
model_service = ModelService(model)
prediction_processor = PredictionRequestProcessorSync(model_service)


@predict_router.post("/predict")
def predict() -> Dict[str, str]:
    prediction = prediction_processor.process_request()
    return prediction
