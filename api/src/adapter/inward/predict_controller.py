from typing import Dict
from fastapi import APIRouter

from common.src.port.inward.process_request_port import ProcessRequestPort
from adapter.outward.predict_callback import predict_callback_router


predict_router = APIRouter()

@predict_router.post("/predict", callbacks=predict_callback_router.routes)
def predict(commons, callback_url) -> Dict[str, str]:
    commons.process_request()
