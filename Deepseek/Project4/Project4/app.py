from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_API = "http://localhost:11434/api/generate"

@app.post('/extract_entities/')
def extract_named_entities(text:str):
    payload = {
        'model':'deepseek-r1',
        'prompt':"Extract the names, places, dates etc,. from the given text \\n{text}",
        'stream':False
    }
    response = requests.post(OLLAMA_API, json=payload)
    return response.json().get("response", "No entities detected.")

# RUN at: uvicorn app:app --reload and run in 