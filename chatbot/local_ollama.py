from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

#prompt template

prompt = ChatPromptTemplate.from_messages( 
    [ 
        ("system","You are a helpful assistant. Please respond to the user queries"),
        ("user","Quiestion:{question}")
    ]
)

#streamlit framework
st.title("Langchain Demo with ollama")
input_text = st.text_input("Drop your query")

#ollama llama2 llm
llm = Ollama(model="phi3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))