# utils.py
import torch
from config import LABELS

def decode_prediction(prediction_tensor):
    predicted_class_id = torch.argmax(prediction_tensor).item()
    return LABELS[predicted_class_id]
