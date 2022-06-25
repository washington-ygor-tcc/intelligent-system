from typing import Dict
from fastapi import APIRouter

from common.src.port.outward.dispatch_response_port import DispatchResponsePort


predict_callback_router = APIRouter()


class PredictCallback(DispatchResponsePort):
  def dispatch_response(self, callback, prediction):
    callback(prediction)


@predict_callback_router.post("{$callback_url}/invoices/{$request.body.id}")
def prediction_response_notification(prection):
  pass
