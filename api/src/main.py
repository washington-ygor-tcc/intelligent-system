from src.adapter.inward import health_controller
from common.src.application.ModelService import predict
from fastapi import FastAPI

app = FastAPI()

app.include_router(health_controller.router)
