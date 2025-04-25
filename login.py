import streamlit as st

# Set page configuration
st.set_page_config(page_title="Resume_Based_Job_Classifier", layout="centered")

# Set the text color to black using markdown
st.markdown("<h1 style='color:white;'>Resume_Based_Job_Classifier</h1>", unsafe_allow_html=True)

# Background Image (Unsplash example)
page_bg_img = """
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
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Logo (Top Right)
st.markdown(
    """
    <div style='position: absolute; top: 10px; right: 30px;'>
        <img src='https://static.vecteezy.com/system/resources/previews/016/134/475/non_2x/letter-r-logo-design-logo-template-creative-r-logo-symbol-vector.jpg' width='80'>
    </div>
    """,
    unsafe_allow_html=True
)

# Login Card
st.markdown("<h3 style='color: white;'>🔐 Login</h3>", unsafe_allow_html=True)

username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", type="password", placeholder="Enter your password")

# Session state for login status
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Login button
if st.button("Login"):
    if username == "user" and password == "123":
        st.session_state.logged_in = True
        st.success("Login successful!")
        st.experimental_rerun()  # Reload the page to switch to file upload page
    else:
        st.error("Invalid username or password")

if st.session_state.logged_in:
    st.experimental_rerun()  # Automatically rerun to switch to the next page (file.py)
