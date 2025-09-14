#  AI Hackathon Judge Assistant

An AI-powered project evaluator built with **Google Gemini API**, **Gradio**, and **PyMuPDF**.  
It analyzes hackathon submissions (project description, screenshots, and supporting PDFs) and generates evaluation scores with constructive feedback.

---

##  Features
- Extracts text from uploaded PDF documents.
- Accepts project descriptions + screenshots.
- Evaluates projects on:
  - **Innovation (1–10)**
  - **Technical Execution (1–10)**
- Provides **AI-generated constructive feedback**.

---

##  Tech Stack
- Python 3.10+
- [Gradio](https://www.gradio.app/) – UI framework
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [PyMuPDF](https://pymupdf.readthedocs.io/) – PDF parsing
- [PIL](https://pillow.readthedocs.io/) – image handling

---

## Installation
1. **Clone this repository:**
   ```bash
   git clone https://github.com/preetishnithi/AI-Hackathon-Judge.git
   cd AI-Hackathon-Judge
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your Gemini API key in AIHackathonJudge.py:**
   ```bash
   genai.configure(api_key="YOUR_API_KEY")
   ```
4. **Run the app:**
   ```bash
   python AIHackathonJudge.py
   ```

## Usage
- Upload your project description(text).
- Upload a screenshot(optional).
- Upload your PDF document.
- Click **Analyze Project** to get AI-generated scores and feedback.

---
