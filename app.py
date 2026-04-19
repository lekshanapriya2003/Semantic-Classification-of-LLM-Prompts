import re
from pathlib import Path

import fasttext
import pandas as pd
import streamlit as st

MODEL_PATH = Path("openorca_fasttext_model.bin")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

@st.cache_resource
def load_model():
    return fasttext.load_model(str(MODEL_PATH))

def predict_text(model, text):
    cleaned = clean_text(text)
    labels, probs = model.predict(cleaned, k=4)

    results = pd.DataFrame({
        "Category": [label.replace("__label__", "") for label in labels],
        "Confidence": [float(p) for p in probs]
    })

    return results

st.set_page_config(page_title="Prompt Classifier", layout="centered")

st.title("Semantic Classification of LLM Prompts")
st.write("Predict whether a prompt is mainly coding, reasoning, summarization, or general.")

try:
    model = load_model()
except Exception as e:
    st.error(f"Model could not be loaded: {e}")
    st.stop()

user_input = st.text_area("Enter your prompt")

if st.button("Classify"):
    if not user_input.strip():
        st.warning("Enter a prompt first.")
    else:
        results = predict_text(model, user_input)
    
        st.subheader("Prediction")
        st.success(f"Predicted category: {results.iloc[0]['Category']}")
       
