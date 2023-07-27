import streamlit as st
import os
from mytoken import *
from dotenv import load_dotenv

def main():
    st.set_page_config(page_title="Ask pdf")
    st.header("test key3")
    response=HUGGINGFACEHUB_API_TOKEN
    st.write(response)
    
if __name__ == '__main__':
    load_dotenv(verbose=True)
    HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')
    main()
