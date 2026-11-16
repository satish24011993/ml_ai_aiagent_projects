from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/generate/")
def generate_text(prompt:str, word_limit:int=100, language='English'):
    full_prompt = f"Write a {language}-language text to Generate a response within {word_limit} words:\n\n{prompt}"
    payload = {
        "model": "deepseek-r1",
        "prompt": full_prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No text generated.")

# Runwith: uvicorn app:app --reload
