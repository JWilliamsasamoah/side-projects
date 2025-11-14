# LinkedIn Resume Helper (AI-Powered)

This project is a **Streamlit web app** that:

- Logs into LinkedIn with your credentials (via Selenium)
- Scrapes your **profile, experience, education, licenses, projects, and skills**
- Sends that data to a **Groq LLM (llama3-8b-8192)** to generate a clean, structured resume
- Builds a formatted **Word document (`.docx`)** using `python-docx`
- Lets you **download your resume** directly from the app

It’s designed to turn a LinkedIn profile into a professional resume with minimal manual work.

---

## 🔍 Main Features

- **LinkedIn scraping with Selenium**
  - Logs in using the email/password you provide
  - Visits your profile URL
  - Extracts:
    - Basic info (name, headline, location)
    - Experience
    - Education
    - Licenses & Certifications
    - Projects
    - Skills (from `/details/skills/`)

- **Resume generation with Groq LLM**
  - Sends all scraped data as JSON to a Groq model (`llama3-8b-8192`)
  - Asks the model to format everything into a resume with sections:
    - PERSONAL INFORMATION  
    - OBJECTIVE  
    - EXPERIENCE  
    - EDUCATION  
    - SKILLS  
    - PROJECTS  

- **Formatted `.docx` resume**
  - Uses `python-docx` to:
    - Add section headings (OBJECTIVE, EXPERIENCE, etc.)
    - Add bullet points for experience and education details
    - Style section titles (color, bold, size)
  - Saves the final file as `Final_Resume.docx`
  - Streamlit offers a **Download Resume** button

- **Streamlit UI**
  - Inputs for:
    - LinkedIn Email
    - LinkedIn Password
    - LinkedIn Profile URL
  - Visual **progress bar** during scraping and generation
  - Displays the scraped JSON and the generated resume text

---

## 🛠 Tech Stack

**Language**
- Python

**Libraries & Tools**
- **Streamlit** – Web UI
- **Selenium** – Browser automation for LinkedIn login + scraping
- **webdriver-manager** – Manages ChromeDriver
- **Groq Python SDK** – Calls the LLM (`llama3-8b-8192`)
- **python-docx** – Generates the Word resume file
- **dotenv** – Loads environment variables from `.env`
- **Pandas / JSON / time / re** – Data handling and utilities

---

## 🔐 Environment Variables

This project uses a `.env` file for the Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
