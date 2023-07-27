import streamlit as st
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")
    response=os.environ['HUGGINGFACEHUB_API_TOKEN']
    st.write(response)
   

if __name__ == '__main__':
    main()
