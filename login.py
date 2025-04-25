import streamlit as st

# Page config
st.set_page_config(page_title="Login", layout="centered")

# Background Image (Unsplash example)
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1531497865144-0464ef8fb9a9");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

.login-card {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 3rem 2rem;
    border-radius: 20px;
    max-width: 400px;
    margin: 100px auto;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(10px);
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
    <div style='position: absolute; top: 10px; right: 10px;'>
        <img src='https://i.imgur.com/N1n3zVj.png' width='80'>
    </div>
    """,
    unsafe_allow_html=True
)

# Login Card
st.markdown("<div class='login-card'>", unsafe_allow_html=True)
st.markdown("### 🔐 Login")

username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", type="password", placeholder="Enter your password")

if st.button("Login"):
    if username == "user" and password == "123":
        st.success("Login successful!")
        st.switch_page("pages/file.py")
    else:
        st.error("Invalid username or password")

st.markdown("</div>", unsafe_allow_html=True)
