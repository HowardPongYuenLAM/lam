import streamlit as st
import os
from mytoken import *
from dotenv import load_dotenv

def main():
    st.set_page_config(page_title="Ask pdf")
    st.header("test key")
#    response="lampongyuen"
    response=working_key
    st.write(response)
    
if __name__ == '__main__':
    load_dotenv(verbose=True)
    working_key = os.environ.get("mykey2")
    main()
