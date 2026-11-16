from fastapi import FastAPI
import requests
import speech_recognition as sr


app = FastAPI()
OLLAMA_API = 'http://localhost:11434/api/generate'

@app.post('/meeting_minutes/')
def generate_minutes(transcript:str):
    payload = {'model':'deepseek-r1','prompt':f"Summarize meeting:\n\n{transcript}", "stream":False}
    response = requests.post(OLLAMA_API, json=payload)
    return response.json().get("response","No Meeting Minutes Generated.")


# Run ! uvicorn app=app --reload