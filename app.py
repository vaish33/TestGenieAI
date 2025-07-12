import os
from dotenv import load_dotenv
import streamlit as st
import openai

# Load environment variables from .env file
load_dotenv()

# Fetch OpenAI API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    st.error("OpenAI API key is not set. Please add it to the .env file.")

# Streamlit app configuration
st.set_page_config(page_title="🧞 TestGenieAI", page_icon="✨", layout="centered")

# Add a custom CSS style
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom right, #f4f4f9, #ffe4e1);
        font-family: 'Arial', sans-serif;
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
    }
    .header {
        text-align: center;
        margin-top: 30px;
    }
    .header img {
        height: 120px;
    }
    .header h1 {
        font-size: 28px;
        margin-bottom: 5px;
        color: #ff4500;
    }
    .header p {
        font-size: 14px;
        color: #555;
    }
    .response-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        margin-top: 20px;
        border-radius: 10px;
        overflow-x: scroll;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    }
    .input-container {
        display: flex;
        gap: 10px;
        align-items: center;
        justify-content: center;
        margin-top: 20px;
    }
    .input-container textarea {
        width: calc(100% - 60px);
        max-width: 600px;
        height: 100px;
        padding: 10px;
        border: 2px solid #ff4500;
        border-radius: 10px;
        font-size: 16px;
        resize: none;
    }
    .send-button {
        background-color: #ff4500;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
        font-size: 16px;
        cursor: pointer;
    }
    .send-button:hover {
        background-color: #ff6347;
    }
    </style>
    """,
    #unsafe_allow_html=True,
)

# Header Section
st.markdown(
    """
    <div class="container">
        <div class="header">
            <img src="https://i.postimg.cc/J0hdZsys/genie-with-lamp-logo-designs-vector-genie-lam-logo-concept-828162-270.avif" alt="Genie Logo">
            <h1>✨ TestGenieAI - Your Magical Test Case Generator ✨</h1>
            <p>Generate Functional, API, and Data Test Cases in Real-Time</p>
        </div>
    </div>
    """,
    #unsafe_allow_html=True,
)

# Helper function to generate test cases
def generate_test_cases(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an assistant specializing in generating detailed and structured test cases."},
                {"role": "user", "content": query}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

# State management for input and responses
if "response" not in st.session_state:
    st.session_state.response = ""

# Input box and send button
with st.container():
    st.markdown("<div class='input-container'>", unsafe_allow_html=True)
    user_input = st.text_area("Type your prompt:", height=100)
    send_button = st.button("Send", key="send_button")
    st.markdown("</div>", unsafe_allow_html=True)

if send_button and user_input:
    # Show loading spinner
    with st.spinner("TestGenie is thinking..."):
        st.session_state.response = generate_test_cases(user_input)

# Display response
if st.session_state.response:
    st.markdown(
        f"""
        <div class="container">
            <div class="response-box">
                <h3 style="color: #ff4500;">Response:</h3>
                <p>{st.session_state.response}</p>
            </div>
        </div>
        """,
        #unsafe_allow_html=True,
    )