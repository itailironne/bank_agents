import os
import streamlit as st
from langchain.llms import OpenAI
from langchain_experimental.agents import create_csv_agent

# Set page configuration and CSS styles
st.set_page_config(page_title="CSV Data Query Tool", layout="wide")
st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    font-weight: bold;
    color: #FF4B4B;
}
body {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    background-color: #f0f2f6;
}
.stButton>button {
    color: white;
    background-color: #FF4B4B;
    border-radius: 8px;
    border: none;
    padding: 10px 24px;
    margin: 10px 0;
    font-size: 16px;
}
.stTextInput>div>div>input {
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<p class="big-font">CSV Data Query Tool</p>', unsafe_allow_html=True)
st.write("This tool allows you to upload a CSV file and ask questions about its contents. Please upload your file and enter your question below.")

# Retrieve the API key securely from environment variables
api_key = ""
if not api_key:
    st.error("API key not found. Please ensure the OPENAI_API_KEY environment variable is set.")
    st.stop()

# Initialize the OpenAI model with the API key
llm = OpenAI(temperature=0, openai_api_key=api_key)

# Layout: Use columns for uploader and input
col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv", help="Only CSV files are accepted")
with col2:
    user_question = st.text_input("Enter your question:", help="Type your question regarding the CSV data here")

if uploaded_file is not None and user_question:
    if st.button('Answer Question', on_click=None, help="Click to process your query"):
        csv_file_path = "temp.csv"
        with open(csv_file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())

        try:
            agent = create_csv_agent(
                llm,
                csv_file_path,
                verbose=True,
                allow_dangerous_code=True,
                pandas_kwargs={'delimiter': ';', 'encoding': 'latin1'}
            )
            with st.spinner('Processing...'):
                answer = agent.run(user_question)
            st.success('Processed successfully!')
            st.info("Answer: " + answer)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")






















