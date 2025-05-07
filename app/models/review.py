# review.py
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.models.base import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    sentiment = Column(String, nullable=False)
    source = Column(String)  # e.g., 'product', 'social'
    timestamp = Column(DateTime, default=datetime.utcnow)
