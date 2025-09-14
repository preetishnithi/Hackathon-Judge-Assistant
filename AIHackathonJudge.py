import gradio as gr
import google.generativeai as genai
import os
import fitz
from PIL import Image
from io import BytesIO

genai.configure(api_key="AIzaSyA3lT6eHJRkGcEAbntepciCY659HRXB0iQ")

model = genai.GenerativeModel('gemini-2.5-flash')

def extract_text_from_pdf(pdf_file):

    document = fitz.open(pdf_file)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def analyze_submission(project_description, project_screenshot, project_pdf):

    pdf_text = extract_text_from_pdf(project_pdf.name)
    prompt_text = (
        "You are a hackathon judge. "
        "Analyze the following project based on its description, a screenshot, and a detailed PDF document. "
        "Provide a score from 1-10 for 'Innovation' and 'Technical Execution'. "
        "Then, write a short, constructive feedback paragraph based on all three inputs. "
        "Project Description: " + project_description + "\n\n" +
        "PDF Document Content: " + pdf_text
    )

    try:
        response = model.generate_content([prompt_text, project_screenshot])
        return response.text
    except Exception as e:
        return f"Error: {e}"

with gr.Blocks(title="AI Hackathon Judge Assistant", theme=gr.themes.Default()) as demo:
    gr.Markdown(
        """
        # 🤖 AI Hackathon Judge Assistant
        Upload a project's description, screenshot, and a supporting PDF to get an AI-generated evaluation report.
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            project_description_input = gr.Textbox(lines=8, label="Project Description")
            project_screenshot_input = gr.Image(type="pil", label="Project Screenshot")
            project_pdf_input = gr.File(label="Project PDF (e.g., business plan, whitepaper)")
            
            analyze_button = gr.Button("Analyze Project")

        with gr.Column(scale=2):
            judge_report_output = gr.Textbox(
                label="Judge's Report",
                lines=30,  
                show_copy_button=True,
                autoscroll=True
            )

    analyze_button.click(
        fn=analyze_submission,
        inputs=[project_description_input, project_screenshot_input, project_pdf_input],
        outputs=judge_report_output
    )

if _name_ == "_main_":
    demo.launch()