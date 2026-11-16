import requests
import gradio as gr

# Deepseek API URL
OLLAMA_API = "http://localhost:11434/api/generate"

def extract_named_entities(text):
    """
    Uses DeepSeek AI to identify named entities (people, organizations, locations, dates).
    """
    # prompt = f"Extract all named entities (persons, organizations, locations, dates) from the below text: \n\n{text}"
    # Enhancement(others like multilanguage ner, color coded entities)
    prompt = f"Extract organization, locations and dates from this text:\n\n{text}"

    payload = {
        "model":"deepseek-r1",
        "prompt":prompt,
        "stream":False
    }

    response = requests.post(OLLAMA_API, json=payload)

    if response.status_code == 200:
        return response.json().get('response', 'No entities detected.')
    else:
        return f"Error: {response.text}"


interface = gr.Interface(
    fn=extract_named_entities
    input = gr.Textbox(lines=5, placeholder="Enter text for entity recognition")
    output= gr.Textbox(label="Extracted Entities")
    title= "AI-Powered Named Entity Recognition(NER) tool"
    description="Finds out and extract the named entities in the text"
)

# Launch the web app
if __name__=="__main__":
    interface.launch()


# # Test Named Entity Recognition
# if __name__ == "__main__":
#     sample_text = "Google was founded by Larry Page and Sergey Brin in September 1998 at Stanford"
#     print("### Extracted Entities ###")
#     print(extract_named_entities(sample_text))