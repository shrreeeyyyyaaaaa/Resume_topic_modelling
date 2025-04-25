import os
import re
import PyPDF2
import docx2txt
import streamlit as st
import numpy as np
import nltk
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

nltk.download('stopwords')

# Basic page setup
st.set_page_config(page_title="Resume Based Job Classifier", layout="wide")

# --- Session management ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- Page 1: Login Page ---
if not st.session_state.logged_in:
  import streamlit as st


# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    st.image("login_page.png", use_column_width=True)

with col2:
    st.markdown("<h1 style='text-align: center;'>Resume Based Job Classifier</h1>", unsafe_allow_html=True)
    st.write("---")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "user" and password == "1234":
            st.success("Login successful! 🎉")
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid credentials. Please try again.")


# --- Page 2: Resume Upload Page ---
else:
    st.markdown("<h1 style='text-align: center;'>Resume Based Job Classifier</h1>", unsafe_allow_html=True)
    st.write("---")
    st.markdown('<h3>Upload your resume(s)</h3>', unsafe_allow_html=True)

    @st.cache_resource
    def load_model():
        return SentenceTransformer('all-MiniLM-L6-v2')
    
    model = load_model()

    job_roles = {
        "Software Engineer": "programming, development, testing, software, backend, frontend, cloud, APIs",
        "Data Scientist": "machine learning, data analysis, Python, statistics, model building, visualization",
        "Data Analyst": "SQL, data analysis, Python, PowerBI, analytics, Tableau, visualization",
        "Marketing Specialist": "marketing, branding, campaigns, content creation, digital marketing, SEO",
        "Financial Analyst": "finance, investment, risk analysis, budgeting, accounting, financial modeling",
        "Sales Executive": "sales, targets, customer acquisition, CRM, relationship management",
        "Public Relations Officer": "PR, media, reputation management, communication, public speaking",
        "IT Administrator": "networks, servers, IT support, system admin, cybersecurity, hardware",
        "UI/UX Designer": "design, Figma, user interface, user experience, wireframes, prototyping",
        "Civil Engineer": "construction, infrastructure, site management, AutoCAD, structural design",
        "Business Consultant": "strategy, consulting, business analysis, problem solving, client meetings",
        "Business Development Manager": "growth, partnerships, revenue, business strategy, stakeholder engagement",
        "Chef / Culinary Expert": "cooking, kitchen, recipes, cuisine, food preparation, menu planning",
        "Bank Officer": "banking, loans, customer service, financial products, compliance",
        "Creative Arts Professional": "art, painting, music, drama, storytelling, creativity"
    }

    @st.cache_data
    def embed_job_roles():
        return {role: model.encode(desc) for role, desc in job_roles.items()}
    
    job_embeddings = embed_job_roles()

    def extract_text(uploaded_file):
        if uploaded_file.type == "application/pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            return " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
        elif uploaded_file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/msword"]:
            return docx2txt.process(uploaded_file)
        elif uploaded_file.type == "text/plain":
            return uploaded_file.read().decode("utf-8")
        else:
            return ""

    def clean_text(text):
        text = text.lower()
        return re.sub(r'[^a-zA-Z\s]', '', text)

    uploaded_files = st.file_uploader("Upload Resumes (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"], accept_multiple_files=True)

    if uploaded_files and st.button("Classify Resumes"):
        for uploaded_file in uploaded_files:
            st.divider()
            st.subheader(f"📄 {uploaded_file.name}")

            raw_text = extract_text(uploaded_file)
            cleaned = clean_text(raw_text)
            embedding = model.encode(cleaned)

            similarities = {
                role: cosine_similarity([embedding], [emb])[0][0]
                for role, emb in job_embeddings.items()
            }

            top_roles = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:3]

            st.markdown("### 🔍 Top 3 Job Matches:")
            for role, score in top_roles:
                st.markdown(f"- **{role}** — Similarity Score: `{score:.4f}`")
