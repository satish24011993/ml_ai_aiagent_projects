import requests
import gradio as gr

# Deepseek API URL
OLLAMA_API = "http://localhost:11434/api/generate"


def analyze_symptoms(symptoms):
    """
    Uses DeepSeek AI to analyze symptoms and provide possible conditions.
    """
    prompt = f"Analyze the following symptoms and suggest possible health conditions:\n\nSymptoms\
        Prove a short list of possible causes and general advice (no treatment recommendations)"
    
    # prompt =f"Analyze the following symptoms and classify them as mild, moderate, or severe:\n\nSymptoms: {symptoms}"
    # prompt = f"Analyze symptoms in {language} and provide a response: \n\n Symptoms: {symptoms}

    payload = {
        'model':'deepseek-r1',
        'prompt':prompt,
        'stream': False
    }

    response = requests.post(OLLAMA_API, json=payload)

    if response.status_code == 200:
        return response.json().get('response', "No information available.")
    else:
        return f"Error: {response.text}"
    

# Create Gradio interface
interface = gr.Interface(
    fn = analyze_symptoms,
    inputs=gr.Textbox(lines=2, placeholder="Enter your symptoms (e.g., fever, cough, sore throat)"),
    outputs=gr.Textbox(label="Possible Conditions and Advice"),
    title="AI-Powered Medical Symptoms checker!",
    description="Enter your symptoms, and the AI will suggest possible causes and general advice."
)


if __name__ == "__main__":
    interface.launch()


# # Test Medical Symptom Checker
# if __name__ == "__main__":
#     test_symptoms = "Fever, cough, body aches"
#     print("### AI Medical Analysis ###")
#     print(analyze_symptoms(test_symptoms))