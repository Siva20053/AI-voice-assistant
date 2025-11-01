from fastapi import FastAPI
from pydantic import BaseModel
from assistant_main import get_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI Assistant API is live 🚀"}

@app.post("/ask")
def ask(query: Query):
    reply = get_response(query.text)
    return {"reply": reply}
