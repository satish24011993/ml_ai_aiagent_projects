import requests
import gradio as gr

OLLAMA_API = 'http://localhost:11434/api/generate'

def analyze_sentiment(text, language='English'):
    """
    Uses DeepSeek AI to classify sentiment as positive, negative, or neutral based on given text.
    """
    # prompt = f"Classify the sentiment of the following text:\n\n{text}"
    # Enhanced 
    # prompt = f"Analyze th sentiment of this text. Provide a sentiment score from -1 (very negative) to +1 (very positive)"
    # prompt = f"Classify the sentiment of this text (in {language} as Positive, Negative or Neutral)"
    prompt = f'Identify the sentiment in the following text and highlight words that contribute to it:\n\n{text}'

    payload = {
        'model':'deepseek-r1',
        'prompt':prompt,
        'stream':False
    }

    response = requests.post(OLLAMA_API, json=payload)
    if response.status_code == 200:
        return response.json().get('request','No Sentiment detected')
    else:
        return f"Error Response: {response}"


interface = gr.Interface(
    fn=analyze_sentiment
    input=gr.Textbox(lines=3, placeholder="Enter a sentence for sentiment analysis"),
    output=gr.Textbox(label="Sentiment Result"),
    title="AI-Powered Sentiment Analysis",
    description="Enter a sentence, and DeepSeek AI will classify its sentiment as Positive, Negative or Neutral"
)

if __name__=="__main__":
    interface.launch()

# if __name__=='__main__':
#     sample_text = 'I\'m feeling good today'
#     print("Sentiment Analysis report:") 
#     print(analyze_sentiment(sample_text))