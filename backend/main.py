from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For security, change to ["http://127.0.0.1:8001"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load CodeT5 Model & Tokenizer
MODEL_NAME = "Salesforce/codet5-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Define request structure
class CodeRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "AI Code Auto-Completer is running!"}

@app.post("/predict/")
def predict_code(data: CodeRequest):
    prompt = data.prompt.strip()
    if not prompt:
        return {"error": "No input provided"}

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=128)

    # Generate with improved control
    outputs = model.generate(
        **inputs,
        max_length=256,  
        num_return_sequences=1,
        repetition_penalty=1.8,  # Reduce repetition
        no_repeat_ngram_size=3,  
        early_stopping=True,  
        temperature=0.6,  # More structured output
        top_k=50,  
        top_p=0.92  
    )

    # Decode and clean output
    generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Fix: Ensure at least part of a Python function or loop
    if "def" not in generated_code and "for" not in generated_code and "while" not in generated_code:
        generated_code = prompt + "  # Completing with AI..."

    return {"completion": generated_code}
