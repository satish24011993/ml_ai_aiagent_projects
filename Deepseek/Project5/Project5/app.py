from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_API = 'http://localhost:11434/api/generate'

@app.post('/analyze_sentiment/')
def analyze_sentiment(text):
    payload={'model':'deepseek-r1','prompt':f'Analyze the sentiment of the given text: {text}', 'stream':False}
    response = requests.post(OLLAMA_API, payload=payload)
    return response.json().get('requests','No Sentiment')

# run on uvicorn app:app --reload and try the url in postman