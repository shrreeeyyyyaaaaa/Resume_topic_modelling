import streamlit as st


st.set_page_config(page_title="Resume Classifier", layout="centered")

# Background + Logo Styling
st.markdown("""
    <style>
        .stApp {
            background-image: url('back.png');
            background-size: cover;
        }
        .login-box {
            background-color: rgba(255,255,255,0.85);
            padding: 2rem;
            border-radius: 10px;
            max-width: 400px;
            margin: auto;
            margin-top: 100px;
        }
        .logo {
            position: absolute;
            top: 10px;
            right: 10px;
            width: 50px;
        }
    </style>
""", unsafe_allow_html=True)


st.image("logo.png", width=50)

# Login Form
def login():
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.header("🔐 Login")
    username = st.text_input("👨‍💻Username")
    password = st.text_input("🗝️Password", type="password")
    if st.button("Submit", type="primary"):
        if username == "user" and password == "123":
            st.session_state.authenticated = True
            st.switch_page("file.py")
        else:
            st.error("Invalid username or password")
    st.markdown('</div>', unsafe_allow_html=True)

# Session Control
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login()
else:
    st.switch_page("file.py")
