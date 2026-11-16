from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_API = "http://localhost:11434/api/generate"

@app.post("/generate/")
def correct_grammer(text:str):
    """
    Uses DeepSeek AI to correct grammer and spelling errors in the given text.
    """
    prompt = f"Correct any spelling and grammar mistakes in the following text and provide explination:\n\n{text}"
    payload ={
        'model' : 'deepseek-r1',
        'prompt': prompt,
        'stream': False
    }

    response = requests.post(OLLAMA_API, json=payload)

    return response.json().get("response", "No correction generated.")

# Run with: uvicorn app:app --reload and use api in postman to get response