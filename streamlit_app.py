import streamlit as st
import os
from crewai.crews.crew_output import CrewOutput
from ai_agent_using_clarifai import (
    extract_text_from_resume,
    Crew,
    resume_feedback_task,
    resume_advisor_task,
    research_task,
)

st.set_page_config(page_title="AI Resume Advisor & Job Finder", layout="centered")

st.title("AI Resume Advisor & Job Finder")
st.markdown("""
This app uses advanced AI agents to:
- **Analyze your resume** and provide professional feedback
- **Rewrite your resume** to make it stand out
- **Find 5 relevant, recent job postings** based on your improved resume and location

**How it works:**
1. Upload your resume (PDF or DOCX)
2. Enter your preferred job location
3. Click 'A
nalyze & Find Jobs' to get feedback, an improved resume, and job recommendations
""")


uploaded_file = st.file_uploader(
    "Upload your resume (PDF or DOCX)", type=["pdf", "docx"]
)
location = st.text_input("Preferred job location", "")

if st.button("Analyze & Find Jobs"):
    if not uploaded_file or not location:
        st.error("Please upload a resume and enter a location.")
    else:
        # Save uploaded file temporarily
        with open("temp_resume", "wb") as f:
            f.write(uploaded_file.getbuffer())
        resume_text = extract_text_from_resume("temp_resume")
        os.remove("temp_resume")

        # Inject resume and location into tasks
        resume_feedback_task.description = resume_feedback_task.description.format(
            resume=resume_text
        )
        resume_advisor_task.description = resume_advisor_task.description.format(
            resume=resume_text
        )
        research_task.description = research_task.description.format(location=location)

        # Run the Crew
        crew = Crew(
            agents=[
                resume_feedback_task.agent,
                resume_advisor_task.agent,
                research_task.agent,
            ],
            tasks=[resume_feedback_task, resume_advisor_task, research_task],
            verbose=True,
        )
        results = crew.kickoff()

        def clean_markdown(md):
            if not isinstance(md, str):
                return md
            cleaned = md.strip()
            if cleaned.startswith("```markdown"):
                cleaned = cleaned[len("```markdown") :].strip()
            if cleaned.startswith("```"):
                cleaned = cleaned[3:].strip()
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3].strip()
            return cleaned

        if isinstance(results, CrewOutput):
            outputs = [getattr(task, "raw", "") for task in results.tasks_output]
            section_titles = [
                "Resume Feedback",
                "Improved Resume",
                "Job Recommendations",
            ]
            for title, md in zip(section_titles, outputs):
                st.subheader(title)
                st.markdown(clean_markdown(md), unsafe_allow_html=True)
        else:
            st.error("Unexpected result format from Crew execution.")
