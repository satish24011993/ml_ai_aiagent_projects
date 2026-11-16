import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def correct_grammer(text, language):
    """
    Uses DeepSeek AI to correct grammer and spelling errors in the given text.
    """
    prompt = f"Correct any spelling and grammar mistakes in the following {language} text and provide explination:\n\n{text}"
    payload ={
        'model' : 'deepseek-r1',
        'prompt': prompt,
        'stream': False
    }

    response = requests.get(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get('response', 'No correction generated.')
    else:
        return f"Error: {response.text}"


# Create Gradio interface
interface = gr.interface(
    fn=correct_grammer,
    inputs=gr.Textbox(lines=5, placeholder='Enter text with grammer or spelling mistakes'),
    outputs = gr.Textbox(label="Corrected Text"),
    title="AI-Powered Grammer and Spell Checker",
    description="Enter text wth errors, and Deepseek AI will correct them."
)

if __name__ == "__main__":
    interface.launch()

# # Test Grammer Correction
# if __name__ == "__main__":
#     sample_text = "He dont like to eat apple because they taste sour."
#     print("### Corrected Text ###")
#     print(correct_grammer(sample_text))
