import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_API = "http://localhost:11434/api/generate"

def generate_documentation(code_snippet, language="Python"):
    """
    Uses DeepSeek AI to generate documentation for a given code snippet.
    """
    prompt = f"Generate detailed documentation for the following {language} code: \n\n{code_snippet}\n\n"\
            "Add appropriate docstings, comments, and explanations."
    
    payload = {
        'model':'deepseek-r1',
        'prompt':prompt,
        'stream':False
    }

    response = requests.post(OLLAMA_API, json=payload)

    if response.status_code == 200:
        return response.json().get('response','No Document generated')
    else:
        return "Error: {response.text}"


interface = gr.Interface(
    fn=generate_documentation,
    inputs=[
        gr.Textbox(lines=10, placeholder="Paste your code here."),
        gr.Dropdown(['Python','JavaScript','Java','C++'], label="Select Language")
    ],
    outputs=gr.Textbox(label="AI-Generated Documentation"),
    title="AI-Powered Documentation Generator",
    description="Paste your code and AI will generate detailed documentation."
)


if __name__ == "__main__":
    interface.launch()

# # Text AI documentation Generator
# if __name__ == "__main__":
#     test_code = "def add(a,b): return a+b"
#     print("### AI-Generated Documentation ###")
#     print(generate_documentation(test_code))
    