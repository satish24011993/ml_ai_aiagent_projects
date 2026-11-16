import requests
import gradio as gr

# DeepSeek API Endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_text(prompt, word_limit=100, language="English"):
    """
    Uses DeepSeek AI to generate text based on a given prompt.
    """
    full_prompt = f"Write a {language}-language text to Generate a response within {word_limit} words:\n\n{prompt}"
    payload = {
        "model": "deepseek-r1",
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No text generated.")
    else:
        return f"Error: {response.text}"

# Create Gradio interface   
if __name__ == "__main__":
    interface = gr.Interface(
        fn=generate_text,
        inputs=[
            gr.Textbox(lines=2, placeholder="Enter your prompt"),
            gr.Slider(100, 1000, value=100, step=100, label="Word Limit")
        ],
        title='AI-Powered Text Generator',
        description = "Enter a prompt, select word limit, and generate AI-written content."
        outputs=gr.Textbox(label="Generated Text"),
    )
    interface.launch()