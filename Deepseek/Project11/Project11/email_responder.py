import requests
import gradio as gr

OLLAMA_API = "http://localhost:11434/api/generate"


def generate_email_response(email_content, tone="Formal"):
    """
    Uses DeepSeek AI to generate an appropriate email response
    """
    prompt = f"Generate an {tone} email response to the following email:\n\n{email_content}\n"\
    "Ensure the response is polite, clear and professional."
    # Enhance the prompt to get the response based on language. 

    payload = {
        "model":"deepseek-r1",
        "prompt":prompt,
        "stream":False
    }

    response = requests.post(OLLAMA_API, json=payload)

    if response.status_code == 200:
        return response.json().get('response', 'No response generated.')
    else:
        return f"Error: {response.text}"

interface = gr.Interface(
    fn=generate_email_response,
    inputs=[gr.Textbox(lines=6,placeholder="Paste the email content here"),
    gr.Radio(['Formal','Casual','Friendly'],label='Tone'),
    ],
    outputs=gr.Textbox(label="AI-Generated Email Response"),
    title="AI-Powered Email Responder",
    description="Paste an email and let AI generate a professional response."
)


# # Test AI Email Responder
# if __name__ == "__main__":
#     test_email = "Dear Support, I am facing issues with my order. Can you assist me?"
#     print("### AI-Generated Email Response ###")
#     print(generate_email_response(test_email))