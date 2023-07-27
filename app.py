import streamlit as st
import os
from mytoken import *
from dotenv import load_dotenv

def main():
    st.set_page_config(page_title="Ask pdf")
    st.header("test key")
#    response=os.environ('mykey2')
    response="api"
    st.write(response)
    
if __name__ == '__main__':
    main()
