from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import review, base
from app.ml.inference import predict_sentiment
from app.schemas.review import ReviewCreate, ReviewResponse

app = FastAPI()

# Create tables
base.Base.metadata.create_all(bind=SessionLocal().get_bind())

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Sentiment Analysis API Running"}

@app.post("/predict", response_model=ReviewResponse)
def analyze_sentiment(data: ReviewCreate, db: Session = Depends(get_db)):
    sentiment = predict_sentiment(data.text)
    new_review = review.Review(text=data.text, sentiment=sentiment, source=data.source)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review
