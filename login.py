import streamlit as st

# Set page config FIRST
st.set_page_config(page_title="Login", layout="centered")

# Background image styling
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://pin.it/pgIysJBGJ");  
    background-size: cover;
}
.login-container {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 2rem;
    border-radius: 10px;
    max-width: 400px;
    margin: auto;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Logo top right
st.markdown(
    """
    <div style='position: absolute; top: 10px; right: 10px;'>
        <img src='https://pin.it/3UomMHruJ' width='100'>
    </div>
    """,
    unsafe_allow_html=True
)

# Login form
with st.container():
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "user" and password == "123":
            st.success("Login successful!")
            st.switch_page("pages/file.py")
        else:
            st.error("Invalid username or password")
    st.markdown("</div>", unsafe_allow_html=True)
