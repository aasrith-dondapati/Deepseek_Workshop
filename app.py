# pip install --upgarde langchain langchain-community
# pip install -U langchain-ollama
# pip install streamlit



from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """question: {question} Answer: Generate the answer step by step"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="deepseek-r1")

chain = prompt | model

question = input("Enter your question here: ")

if question:
    try:
        fornatted_prompt = prompt.format(question=question)

        response = chain.invoke({"question": question})

        print("Response:", response)

    except Exception as e:
        print(f"Error: {e}")