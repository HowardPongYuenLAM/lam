# https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management




#CREATE DATABASE pets;
#USE pets;
#CREATE TABLE mytable (
#    name            varchar(80),
#    pet             varchar(80)
#);

#INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');

# import streamlit as st
# conn = st.experimental_connection('pets.db', type='sql')
# pet_owners = conn.query('select * from mytable')
# st.write("abc")


import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return mysql.connector.connect(**st.secrets.db_credentials)
#    return mysql.connector.connect(**st.secrets["pets"])

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

