import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder
import joblib

with open("intents.json" , "r") as f:
    data = json.load(f)

texts = []
labels = []
for intent in data["intents"]:
    tag = intent["tag"]
    for pattern in intent["patterns"]:
        texts.append(pattern)
        labels.append(tag)

le = LabelEncoder()
y = le.fit_transform(labels)

model = make_pipeline(TfidfVectorizer(),LogisticRegression(max_iter=1000))
model.fit(texts,y)

joblib.dump(model, "intent_classifier.pkl")
joblib.dump(le, "label_encoder.pkl")
