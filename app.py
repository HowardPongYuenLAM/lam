import streamlit as st
import os


def main():
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")
    response=MY_HUGGINGFACEHUB_API_TOKEN = "abc"
    st.write(response)
   

if __name__ == '__main__':
    main()
