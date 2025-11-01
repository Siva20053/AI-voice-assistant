import json
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


with open("intents.json" , "r") as f:
    data = json.load(f)

model = joblib.load("intent_classifier.pkl")
le = joblib.load("label_encoder.pkl")
vectorizer = TfidfVectorizer()

def predict_intent(text):
    X = vectorizer.fit_transform([text])
    intent_idx = model.predict(X)[0]
    tag = le.inverse_transform([intent_idx])[0]

    for intent in data['intents']:
        if intent['tag'] == tag:
            return intent['responses'][0]
    return "Sorry, I didn't get that."