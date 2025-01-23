import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# Langsmit Tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')
os.environ['LANGCHAIN_TRACING_V2']="true"

# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","Your are a helpful AI assistant"),("user","Question:{question}")
    ]
)

## Ollama model
llm = Ollama(model="gemma:2b")
output = StrOutputParser()
chain = prompt|llm|output

# streamlit frame
st.title("Langchain Demo with Gemma2 model")
input_text = st.text_input("Enter your query?")

if input_text:
    st.write(chain.invoke({'question':input_text}))
    
