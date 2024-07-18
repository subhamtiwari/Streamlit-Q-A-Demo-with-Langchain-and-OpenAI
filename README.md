### Project: Streamlit Q&A Demo with Langchain and OpenAI

This repository contains a project that demonstrates how to build a simple question-and-answer web application using Streamlit, Langchain, and OpenAI. The app allows users to input questions and receive responses generated by OpenAI's language model.

#### Key Features
- **Interactive Web Interface**: Built using Streamlit to provide an interactive user experience.
- **OpenAI Integration**: Utilizes OpenAI's GPT-3.5-turbo model for generating responses.
- **Environment Variable Management**: Loads API keys securely using `dotenv`.

#### Dependencies
- `streamlit`
- `langchain_community`
- `dotenv`

#### Setup

1. **Install the required packages**:
    ```bash
    pip install streamlit langchain_community python-dotenv
    ```

2. **Set up environment variables**:
    - Create a `.env` file in the project root and add your OpenAI API key:
      ```plaintext
      OPENAI_API_KEY=your_openai_api_key_here
      ```

#### Code Overview

1. **Imports and Setup**:
    ```python
    import streamlit as st
    from langchain_community.chat_models import ChatOpenAI
    from langchain.schema import HumanMessage
    import os
    from dotenv import load_dotenv
    ```

2. **Streamlit Page Configuration**:
    ```python
    # Set page config at the very beginning (only once)
    st.set_page_config(page_title="Q&A DEMO")
    ```

3. **Load Environment Variables**:
    ```python
    # Load environment variables from .env file
    load_dotenv()

    # Verify that the API key is loaded correctly
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        st.error("OPENAI_API_KEY environment variable is not set.")
    else:
        st.success(f"API Key loaded: {api_key[:4]}****")
    ```

4. **Function to Get OpenAI Response**:
    ```python
    # Function to load OpenAI model and get response
    def get_openai_response(question):
        llm = ChatOpenAI(openai_api_key=api_key, model_name="gpt-3.5-turbo", temperature=0.5)
        messages = [HumanMessage(content=question)]
        response = llm(messages)
        return response.content
    ```

5. **Streamlit App Layout**:
    ```python
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
    ```

#### Usage

1. Run the Streamlit app:
    ```bash
    streamlit run your_script_name.py
    ```

2. Open your browser and go to the URL provided by Streamlit.

3. Enter your question in the input field and click "Ask the question" to see the response generated by OpenAI.

This project showcases how to create a simple yet powerful Q&A application using Streamlit, Langchain, and OpenAI's language model. Feel free to customize and extend this code to fit your specific use case.
