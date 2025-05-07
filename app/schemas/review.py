# review.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReviewCreate(BaseModel):
    text: str
    source: Optional[str] = "product"

class ReviewResponse(BaseModel):
    id: int
    text: str
    sentiment: str
    source: str
    timestamp: datetime

    class Config:
        orm_mode = True
