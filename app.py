import streamlit as st
import os
import mytoken as *

def main():
    mytoken
#    os.environ['test']='pqrst'
    st.set_page_config(page_title="Ask")
    st.header("Ask your PDF testing")
    response=os.environ['test']
    st.write(response)
if __name__ == '__main__':
    main()
