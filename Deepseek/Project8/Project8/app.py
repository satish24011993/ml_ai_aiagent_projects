import requests
from fastapi import FastAPI


app = FastAPI()

OLLAMA_API = "http://localhost:11434/api/generate"


@app.post("/legal/")
def generate_legal(text:str):
    payload={'model':'deepseek-r1', 'prompt':f"Generate a legal document:\n\n{text}", 'stream':False}
    response = requests.post(OLLAMA_API, json=payload)
    return response.json().get('response', "No contract generated.")

# run at uvicorn app=app --reload at/legal