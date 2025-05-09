# app.py
import os
import streamlit as st
from langchain.llms import OpenAI
from constants import openai_key

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_key

# UI
st.title("LangChain with OpenAI API")

prompt = st.text_input("Enter your prompt:")

if prompt:
    llm = OpenAI(temperature=0.7)
    response = llm(prompt)
    st.write("### Response:")
    st.write(response)
