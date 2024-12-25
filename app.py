import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai 

load_dotenv() #load all environment variables from .env file

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## Initialize the app
st.set_page_config(page_title='LLM Project')

st.header('LLM Gemini Application 🤖')

input = st.text_input('Please ask question',key='input', height=400)
submit = st.button('Submit')


#function to load the LLM model 
def get_model_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

if submit:
    model_response = get_model_response(input)
    st.write(model_response)
