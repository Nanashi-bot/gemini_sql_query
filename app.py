from dotenv import load_dotenv
import os
import streamlit as st
import sqlite3
import google.generativeai as genai

load_dotenv()  # loading environment variables
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to load Gemini model and provide sql query as respone


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt[0], question])
    return response.text


def execute_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name STUDENT and has the following columns -
    NAME, CLASS, SECTION, MARKS \n
    For example,
    Example 1 = How many entries of record are present?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    Example 2 = Tell me all the students studying in Data Science class?, the SQL command will be something like this SELECT * FROM STUDENT whee CLASS="Data Science";
    also the sql code should not have ''' in beginning or end and sql word in the output

    """
]

# Streamlit app

st.set_page_config(page_title="SQL query retriever")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

# If submit is clicked
if st.button("Ask the question"):
    response = get_gemini_response(question, prompt)
    # print(response)
    data = execute_sql_query(response, "student.db")
    st.success("The Response is")
    for row in data:
        print(row)
        st.header(row)
