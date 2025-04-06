from fastapi import APIRouter
from model.inference import generate_completion

autocomplete_router = APIRouter()

@autocomplete_router.get("/autocomplete")
def autocomplete(prompt: str):
    return {"completion": generate_completion(prompt)}
