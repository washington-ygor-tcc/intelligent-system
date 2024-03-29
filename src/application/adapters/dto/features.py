from pydantic import BaseModel
from typing import Dict, Any


class FeaturesRequestDTO(BaseModel):
    features: Dict[str, Any] | None


class MessageRequestDTO(BaseModel):
    request_id: str
    features: Dict[str, Any] | None
