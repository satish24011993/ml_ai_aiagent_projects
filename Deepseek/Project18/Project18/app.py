import requests
from fastapi import FastAPI

app = FastAPI()
OLLAMA_API = "http://localhost:11434/api/generate"

@app.post('/code_debugger/')
def code_debugger(data:dict):
    payload = {'model':'deepseek-r1','prompt':f"Debug code:\n\n{data['code_snippet']}", "stream":False}
    response = requests.post(OLLAMA_API, json=payload)
    return response

# Run @ uvicorn app=app --reload