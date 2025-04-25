import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="Login", layout="centered")

# Use uploaded background image
uploaded_bg = "b53c83f0-8563-4778-9685-6aa0f8ffadcb.png"

# Inject CSS
st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{open(uploaded_bg, 'rb').read().encode('base64').decode()}");
        background-size: cover;
        background-position: center;
    }}

    .login-card {{
        background-color: rgba(255, 255, 255, 0.9);
        padding: 3rem 2rem;
        border-radius: 25px;
        max-width: 420px;
        margin: 120px auto;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(8px);
    }}

    h1, h2, h3, h4 {{
        color: black !important;
        text-align: center;
        font-weight: bold;
    }}

    input, .stTextInput, .stPasswordInput {{
        border-radius: 15px !important;
        padding: 12px !important;
        font-size: 16px !important;
        background-color: #f8f9fa !important;
        border: 1px solid #ced4da !important;
    }}

    button[kind="primary"] {{
        border-radius: 12px;
        font-weight: bold;
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Logo (optional, hide if not needed)
st.markdown(
    """
    <div style='position: absolute; top: 10px; right: 10px;'>
        <img src='https://i.imgur.com/N1n3zVj.png' width='80'>
    </div>
    """,
    unsafe_allow_html=True
)

# Login form layout
st.markdown("<div class='login-card'>", unsafe_allow_html=True)
st.title("🔐 Login")

username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", type="password", placeholder="Enter your password")

if st.button("Login"):
    if username == "user" and password == "123":
        st.success("Login successful!")
        st.switch_page("pages/file.py")
    else:
        st.error("Invalid username or password")

st.markdown("</div>", unsafe_allow_html=True)
