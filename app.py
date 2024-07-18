import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv

# Set page config at the very beginning (only once)
st.set_page_config(page_title="Q&A DEMO")

# Load environment variables from .env file
load_dotenv()

# Verify that the API key is loaded correctly
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    st.error("OPENAI_API_KEY environment variable is not set.")
else:
    st.success(f"API Key loaded: {api_key[:4]}****")

# Function to load OpenAI model and get response
def get_openai_response(question):
    llm = ChatOpenAI(openai_api_key=api_key, model_name="gpt-3.5-turbo", temperature=0.5)
    messages = [HumanMessage(content=question)]
    response = llm(messages)
    return response.content

# Streamlit app layout
st.header("Langchain Application")

# Take the input from the user for the chat
input_text = st.text_input("Input", key="input")
submit = st.button("Ask the question")

# If ask button is clicked
if submit and input_text:
    response = get_openai_response(input_text)
    st.subheader("The response is")
    st.write(response)