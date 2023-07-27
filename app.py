import streamlit as st
import os
from mytoken import *

def main():
    st.set_page_config(page_title="Ask")
    st.header("test key")
#    response=os.environ['test']
    response=mykey
    st.write(response)
    
if __name__ == '__main__':
    main()
