from src.adapter import health_controller
from fastapi import FastAPI

app = FastAPI()

app.include_router(health_controller.router)
