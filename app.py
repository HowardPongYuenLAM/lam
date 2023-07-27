import streamlit as st
import os
from mytoken import *
from dotenv import load_dotenv
from pathlib import Path

def main():
    st.set_page_config(page_title="Ask pdf")
    st.header("test key")
#    response="lampongyuen"
    response=GCP_PROJECT_ID
    st.write(response)
    
if __name__ == '__main__':
    dotenv_path = Path('path/to/.env')
    load_dotenv(dotenv_path=dotenv_path,verbose=True)
    GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
    SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
    STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')
    working_key = os.environ.get("mykey2")
    from dotenv import dotenv_values
    print(dotenv_values)
    main()
