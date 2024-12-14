## Integrate our code with OpenAI API

import os
import streamlit as st
from langchain_community.llms import OpenAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

## streamlit framework
st.title('Langchain Demo')
input_text=st.text_input('Search')

## OpenAI LLMs
llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))

