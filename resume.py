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

# Set page config
st.set_page_config(page_title="Resume_Based_Job_Classifier", layout="centered")

# Set background and logo
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://img.freepik.com/premium-photo/black-office-interior_1029476-21663.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
input, .stTextInput, .stPasswordInput {
    border-radius: 15px !important;
    padding: 10px !important;
    font-size: 16px !important;
    background-color: #f8f9fa !important;
    border: 1px solid #ced4da !important;
}
button[kind="primary"] {
    border-radius: 12px;
    font-weight: bold;
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
}
.stApp {
    background-color: #3e2723; /* dark brown */
    color: white;
}
.title-style {
    text-align: center;
    font-size: 40px;
    color: #ffccbc;
    font-weight: bold;
}
.subtitle-style {
    color: #ffe0b2;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div style='position: absolute; top: 10px; right: 30px;'>
        <img src='https://static.vecteezy.com/system/resources/previews/016/134/475/non_2x/letter-r-logo-design-logo-template-creative-r-logo-symbol-vector.jpg' width='80'>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Session management ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- Page 1: Login Page ---
if not st.session_state.logged_in:
    st.markdown("<h1 style='color:white;'>Resume_Based_Job_Classifier</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>🔐 Login</h3>", unsafe_allow_html=True)
    
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    if st.button("Login"):
        if username == "user" and password == "123":
            st.session_state.logged_in = True
            st.success("Login successful! Redirecting...")
            st.experimental_rerun()  # Force rerun to load next page
        else:
            st.error("Invalid username or password")

# --- Page 2: Resume Classifier Page ---
else:
    st.markdown('<div class="title-style">📂 Resume Job Role Classifier</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-style">Upload your resumes below to find the top matching job roles.</div>', unsafe_allow_html=True)

    # Load model
    @st.cache_resource
    def load_model():
        return SentenceTransformer('all-MiniLM-L6-v2')
    model = load_model()

    job_roles = {
        "Software Engineer": "programming, development, testing, software, backend, frontend, cloud, APIs",
        "Data Scientist": "machine learning, data analysis, Python, statistics, model building, visualization",
        "Data Analyst": "Sql, data analysis, Python, powerBI,analytics,tableau,visualization",
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

    uploaded_files = st.file_uploader("📄 Upload Resumes", type=["pdf", "docx", "txt"], accept_multiple_files=True)

    if uploaded_files and st.button("🔍 Classify Resumes"):
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
