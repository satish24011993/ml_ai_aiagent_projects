from fastapi import FastAPI
import requests


app = FastAPI()
OLLAMA_API = "http://localhost:11434/api/generate"

@app.post('/recommend/')
def recommend_products(query:str):
    payload = {"model":"deepseek-r1", "prompt":f"Recommend Products:\n\n{query}",'stream':False}
    response= requests.post(OLLAMA_API,json=payload)
    return response.json().get('response','No recommendations available.')


# /Run at uvicorn app=app --reload