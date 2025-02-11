# pip install --upgarde langchain langchain-community
# pip install -U langchain-ollama
# pip install streamlit

from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

import streamlit as st

st.title("AD Chatbot using Deepseek-R1")

template = """question: {question} Answer: Generate the answer step by step"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="deepseek-r1")

chain = prompt | model

question = st.text_input("Enter your question here: ")

if question:
    try:
        fornatted_prompt = prompt.format(question=question)

        response = chain.invoke({"question": question})

        #print("Response:", response)
        st.write("Response:", response)

    except Exception as e:
        #print(f"Error: {e}")
        st.write(f"Error: {e}")