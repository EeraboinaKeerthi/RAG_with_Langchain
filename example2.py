# app.py
import os
import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from constants import openai_key

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_key

# UI
st.title("Scientists Search Results")

input_text = st.text_input("Enter your prompt:")

first_input_prompt = PromptTemplate(
    input_variables = ['name'],
    template = "Tell me about Scientist Research {name}"
)

llm = OpenAI(temperature=0.7)
chain=LLMChain(llm=llm,prompt= first_input_prompt,verbose = True)

if input_text:
    st.write(chain.run(input_text))

