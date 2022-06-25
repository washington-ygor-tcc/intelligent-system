from fastapi import FastAPI

from api.src.adapter.inward import predict_controller

app = FastAPI()

app.include_router(predict_controller.predict_router)
