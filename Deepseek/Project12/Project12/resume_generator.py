import requests
import gradio as gr
from fpdf import FPDF

OLLAMA_API = 'http://localhost:11434/api/generate'

def resume_generator(name, job_role, experience, skills, education, summary):
    """
    Uses DeepSeek AI to generate a structured professional resume.
    """
    prompt = f"Generate a professional resume based on the following details:\n\n"\
        f"Name: {name}\nJob Role: {job_role}\nExperience: {experience} years\n"\
        f"Skills: {skills}\nEducation: {education}\nSummary: {summary}\n\n"\
        f"Ensure the resume in ATS-friendly, well-formatted, and professional."
    # Enhance prompt to generate the resume in particular language
    payload = {
        'model':'deepseek-r1',
        'prompt':prompt,
        'stream':False
    }
    response = requests.post(OLLAMA_API, json=payload)

    if response.status_code == 200:
        return response.json().get('requests',"Can't Generate Resume")
    else:
        return f"Error: {response.text}"


def generate_pdf_resume(resume_text, filename="resume.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in resume_text.split("\n"):
        pdf.cell(200, 100, txt=line, ln=True)
    
    pdf.output(filename)
    return filename

interface = gr.Interface(
    fn=resume_generator,
    inputs=[
        gr.Textbox(label="Full Name"),
        gr.Textbox(label="Job Role"),
        gr.Slider(0,50, label="Years of Experience"),
        gr.Textbox(label="Skills (comma-seperated)"),
        gr.Textbox(label="Education"),
        gr.Textbox(label="Summary (Optional)"),
    ],
    outputs=gr.Textbox(label="Generated Resume"),
    title="AI-Powered Resume Generator",
    description="Enter your details to generate a professional resume."
)

if __name__=="__main__":
    interface.launch()


# if __name__=="__main__":
#     test_resume = resume_generator("John Doe","Software Engineer","3",
#                                    "Python, AI, Web Development","B.Tech. ECE", "Experienced in AI and cloud computing.")
    
#     print("### AI-Generated Resume ###")
#     print(test_resume)