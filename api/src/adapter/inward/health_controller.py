from typing import Dict
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def read_health() -> Dict[str, str]:
    return {"status": "OK"}
