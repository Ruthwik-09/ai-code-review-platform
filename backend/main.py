from fastapi import FastAPI
from pydantic import BaseModel
from app.services.gemini_service import review_code

app = FastAPI(
    title="AI Code Review Platform",
    version="1.0.0"
)

class CodeRequest(BaseModel):
    code: str

@app.get("/")
def home():
    return {
        "message": "AI Code Review Platform API is running 🚀"
    }

@app.post("/review")
def review(request: CodeRequest):
    result = review_code(request.code)
    return {
        "review": result
    }