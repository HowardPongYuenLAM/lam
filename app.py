import streamlit as st
import os

def main():
    st.set_page_config(page_title="Ask your PDF there ")
    st.header("Ask your PDF there")
    response=os.environ['HUGGINGFACEHUB_API_TOKEN']
    st.write(response)
   

if __name__ == '__main__':
    main()
