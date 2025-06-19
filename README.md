# build_ai_agent_with_clarifai
Build an AI Agent with Clarifai Build an AI agent using models deployed on the Clarifai platform. You can use any agentic framework and create a simple Streamlit app (or similar UI) that connects to your agent and demonstrates it in action.  This challenge focuses on building an AI agent from concept to deployment.


## AI Resume Advisor & Job Finder
### Project Overview
This project demonstrates an end-to-end AI-powered workflow for resume analysis, improvement, and job search using advanced language models deployed on the Clarifai platform. The solution leverages an agentic framework (CrewAI) to coordinate multiple specialized agents, and provides a user-friendly interface via Streamlit.

### Key Features:

* Resume Analysis: Upload your resume (PDF or DOCX) and receive professional feedback on how to improve it.
* Resume Enhancement: The AI rewrites your resume based on the feedback, making it more attractive to recruiters.
* Job Search: The improved resume is used to find 5 relevant, recent job postings based on your preferred location.
## Workflow & Code Structure
### Resume Upload & Extraction

* Users upload their resume through the Streamlit UI.
* The app supports PDF and DOCX formats.
* The extract_text_from_resume function reads and extracts text from the uploaded file.
## Agentic Pipeline (CrewAI)
### Agent 1: Resume Advisor
Reviews the resume and provides detailed feedback and a score out of 10.
### Agent 2: Resume Writer
Uses the feedback to rewrite and enhance the resume (without fabricating information).
### Agent 3: Job Researcher
* Uses the improved resume and user-specified location to search for 5 relevant, recent job postings using the Serper search tool.
* The agents are orchestrated in sequence using the CrewAI framework.
Results Display

### The Streamlit UI presents:
* The feedback and score
* The improved resume (in markdown format)
* The list of job recommendations with links and descriptions

## File Structure
* ai_agent_using_clarifai.py: Core logic for agent/task definitions, resume extraction, and workflow setup.
* streamlit_app.py: Streamlit UI for user interaction and workflow execution.
* requirements.txt: All required dependencies for the project.
* README.md: Project documentation.
## Setup & Installation
### 1.Clone the repository
```
git clone https://github.com/yourusername/build_ai_agent_with_clarifai.git
cd build_ai_agent_with_clarifai
```

### 2.Install dependencies
```
pip install -r requirements.txt
```
### Set up API Keys
Set the following environment variables with your credentials:

* CLARIFAI_PAT: Your Clarifai Personal Access Token
* SERPER_API_KEY: Your Serper.dev API key
On Windows (PowerShell): or set it in .env
```
$env:CLARIFAI_PAT="your_clarifai_pat"
$env:SERPER_API_KEY="your_serper_api_key"
```

Run the Streamlit App
## Dependencies
All dependencies are listed in requirements.txt:

* streamlit
* crewai
* crewai_tools
* pymupdf
* python-docx
* IPython

## How the AI Workflow Operates
1. User uploads a resume and enters a location.
2. Resume text is extracted and passed to the agentic pipeline.
3. Agent 1 analyzes and scores the resume.
4. Agent 2 rewrites the resume based on feedback.
5. Agent 3 finds 5 relevant jobs using the improved resume and location.
6.Results are displayed in the Streamlit UI.
## Notes
* Ensure your API keys are valid and have sufficient quota.
* The app does not store your resume or personal data.
* For best results, use a well-formatted resume in PDF or DOCX format.
* License

## The output format in streamlit in display the Educatioin is working as it should will welcome anyone to contribute to it.