# inference.py
from model_loader import load_model
from preprocessor import clean_text
from utils import decode_prediction
import torch

# Load model/tokenizer once
tokenizer, model, device = load_model()

def predict_sentiment(text):
    cleaned = clean_text(text)
    inputs = tokenizer(cleaned, return_tensors="pt", truncation=True, padding=True).to(device)
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    return decode_prediction(logits)

# Example test
if __name__ == "__main__":
    text = "This product is amazing! I loved it."
    print("Prediction:", predict_sentiment(text))
