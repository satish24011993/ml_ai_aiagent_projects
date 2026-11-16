import requests
import fitz #PyMuPDF
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a research paper PDF.
    """
    text = ""
    with fitz.open(pdf_file.name) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text if text.strip() else "No text found in the PDF."


def summarize_research_paper(paper_text):
    """
    Uses DeepSeek AI to summarize an academic research paper.
    """

    prompt = f"Summarize the following academic research paper:\n\n{paper_text}\n\n" \
             "Extract key sections (abstract, introduction, methodology, results, conclusion)"
    
    payload = {
        "model":"deepseek-r1",
        "prompt":prompt,
        "stream":False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code==200:
        return response.json().get("response", "No summary generated.")
    
    else:
        return f"Error: {response.text}"
    

interface = gr.Interface(
    fn=summarize_research_paper,
    inputs=[
        gr.Textbox(lines=10, label="Research Paper"),
    ],
    outputs=gr.Textbox(label='AI-Generated Research Summary'),
    title="AI powered Research Paper Summarizer",
    description="Upload a research paper, and AI will generate a structured summary."
)

if __name__ == "__main__":
    interface.launch()

# # Test AI Research Paper Summarizer
# if __name__ =="__main__":
#     test_paper = "Text of Paper add here...." #Add text of paper here
#     print("### AI-Generated Research Paper Summary ###")
#     print(summarize_research_paper(test_paper))
