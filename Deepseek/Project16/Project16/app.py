from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_API = "http://localhost:11434/api/generate"

@app.post("/complete_code/")
def complete_code(data: dict):
    payload = {
        'model':'deepseek-r1',
        'prompt':f"Complete code:\n\n{data['code_snipped']}",
        "stream":False
    }
    response = requests.post(OLLAMA_API, json=payload)
    return response.json().get('response',"No completion available.")

# Run with: uvicorn app:app --reload