from fastapi import FastAPI
from pydantic import BaseModel
import joblib

class TextIn(BaseModel):
    text: str

app = FastAPI(title="Reply Classifier")

pipe = joblib.load("baseline_tfidf_logreg.pkl")
LABELS = pipe.classes_.tolist()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/predict")
def predict(inp: TextIn):
    probs = pipe.predict_proba([inp.text])[0]
    idx = int(probs.argmax())
    return {"label": LABELS[idx], "confidence": float(probs[idx])}
