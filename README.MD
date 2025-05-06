# 🤖 AI- Job Matcher - Resume-Job Matcher & Cover Letter Generator

An intelligent tool that analyzes a candidate's resume and a job description to evaluate compatibility and automatically generate a tailored cover letter. Ideal for 
personal use to check whether you fit a particular role and easily get a tailored cover letter.

---
![Demo](demo.gif)
## 🚀 Features

- 🔍 **Resume Parsing**: Extracts skills, experience, education, and achievements from the uploaded resume.
- 🧠 **Job Matching**: Compares parsed resume data against a job description to assess relevance.
- ✍️ **Cover Letter Generation**: Produces a personalized cover letter using AI based on the user's qualifications and the job role.
- 📊 **Skill & Domain Analysis**: Highlights key technical skills and domain expertise.
- 🧾 **Streamlit Interface**: Simple web UI to interactively upload resumes, input job descriptions, and get results instantly.

---
## 🛠️ Tech Stack


- **Ollama** : Advanced language model for natural language processing and AI-driven analysis.
- **Streamlit** : Modern web framework for building interactive user interfaces.
- **Swarm Framework** : Coordination of specialized AI agents for modular task execution.
- **Python** : Core programming language for backend logic and AI integration.

---
## 🧩 Architecture Overview

**Frontend** :

Built with Streamlit, allowing users to upload resumes and input job descriptions.
Displays results in a tabbed interface, including analysis, job matches, screening scores, and recommendations.

**Backend**:

Orchestrator Agent: Coordinates the workflow by delegating tasks to specialized agents.
Extractor Agent: Extracts structured data from resumes.
Analyzer Agent: Analyzes the extracted data for skills, experience, and qualifications.
Matcher Agent: Matches the candidate's profile with the provided job description using Ollama.
Recommender Agent: Generates the tailored cover letter

**AI Integration**:

Uses Ollama to process natural language inputs and generate results such as job matching analysis and cover letters.

---

## 📂 Folder Structure
app.py: Main Streamlit application file.
agents: Contains specialized AI agents for extraction, analysis, matching, and recommendation.
utils: Utility modules for logging, error handling, and file management.
uploads: Directory for storing uploaded resumes.
results: Directory for saving analysis outputs.

---

##📝 How It Works
Upload Resume: Users upload a PDF resume via the Streamlit interface.
Input Job Description: Users paste a job description into the provided text area.

**AI Processing**:
The resume is parsed, and the job description is analyzed.

**View Results** :
Users can view skills analysis, job matches, screening scores, and a tailored cover letter.
Save Results: Analysis outputs are saved in the results directory for future reference.

---
## 🚀 Getting Started
Clone the repository.
Install dependencies using pip install -r requirements.txt.
Run the application with streamlit run app.py.
Upload a resume and input a job description to get started!

---

## 📌 Future Enhancements
Improve job matching accuracy with advanced NLP techniques.
Allow editing of given resume in latex to fit job description for better chances
Let me know if you need further details or modifications!
