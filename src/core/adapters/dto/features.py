from pydantic import BaseModel
from typing import Dict, Any


class FeaturesRequestDTO(BaseModel):
    features: Dict[str, Any] | None