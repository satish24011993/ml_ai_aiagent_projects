from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_API = 'http://localhost:11434/api/generate'

@app.post('/resume/')
def generate_resume(data:dict):
    payload = {"model":"deepseek-r1", "prompt":f"Generate resume:\n\n{data}", "stream":False}
    response = requests.post(OLLAMA_API, json= payload)
    return response.json().get('response', "No resume available.")

# Run@ uvicorn app=app --reload