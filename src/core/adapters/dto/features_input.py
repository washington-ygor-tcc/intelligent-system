from pydantic import BaseModel
from typing import Dict, Any


class FeaturesInputDTO(BaseModel):
    features: Dict[str, Any] | None