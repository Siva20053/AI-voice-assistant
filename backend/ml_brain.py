import json
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


with open("intents.json" , "r") as f:
    data = json.load(f)

model = joblib.load("intent_classifier.pkl")
le = joblib.load("label_encoder.pkl")
vectorizer = TfidfVectorizer()

def predict_intent(text):
    result = model.predict([text])
    tag = le.inverse_transform([result])
    for i in data["intents"]:
        if i["tag"] == tag :
            return np.random.choice(i["responses"])