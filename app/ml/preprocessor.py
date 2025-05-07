# preprocessor.py
import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-z\s]", "", text)  # Remove non-letters
    text = re.sub(r"\s+", " ", text).strip()
    return text
