# inference.py
from app.ml.model_loader import load_model
from app.ml.preprocessor import clean_text
from app.ml.utils import decode_prediction
import torch

tokenizer, model, device = load_model()

def predict_sentiment(text: str) -> str:
    cleaned = clean_text(text)
    inputs = tokenizer(cleaned, return_tensors="pt", truncation=True, padding=True).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    return decode_prediction(outputs.logits)
