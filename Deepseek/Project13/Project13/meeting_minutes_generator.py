import requests
import gradio as gr
import speech_recognition as sr

# DeepSeek API URL
OLLAMA_API = 'http://localhost:11434/api/generate'


def generate_meeting_minutes(transcript):
    """
    Uses DeepSeek AI to generate a structured meeting summary.
    """
    prompt = f"Summarize the following meeting transcript into structured meeting minutes:\n\n{transcript}"\
            "Extrack key discussion, decisions made, and action items."
    # Enhance
    # prompt = f"Summarize this meeting transcript in {language}:\n\n{transcript}"

    payload = {
        "model":"deepseek-r1",
        "prompt":prompt,
        "stream":False
    }

    response = requests.post(OLLAMA_API, json=payload)

    if response.status_code == 200:
        return response.json().get('request','No Meeting minutes generated')
    else:
        return f"Error: {response.text}"

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)

# Create Gradio interface
interface = gr.Interface(
    fn=generate_meeting_minutes,
    inputs=gr.Textbox(lines=5, placeholder="Paste your meeting transcript here"),
    outputs=gr.Textbox(label='Generated Meeting Minutes'),
    title="AI-Powered Meeting Minutes Generator",
    description="Paste a meeting transcript, and AI will generate a structured summary with key points and action items."
)

if __name__=="__main__":
    interface.launch()

# if __name__=="__main__":
#     test_transcript = "John: Q4 sales increased by 15%. Sarah: We need to increase the marketing budget. Descision is approve higher budget."
#     print("### AI-Generated Meeting Minutes ###")
#     print(generate_meeting_minutes(test_transcript))