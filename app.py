import streamlit as st
import sqlite3
import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Model
model = genai.GenerativeModel("gemini-pro")


# Function to convert NL to SQL
def generate_sql_query(user_input):
    prompt = f"""
    You are an expert SQL developer.
    Convert the following natural language query into a valid SQLite SQL query.

    Database Schema:
    Table: sales
    Columns:
    id (INTEGER)
    product_name (TEXT)
    region (TEXT)
    sales_amount (INTEGER)

    Rules:
    - Only generate SELECT queries.
    - Do not generate DELETE, DROP, UPDATE, or INSERT queries.
    - Do not explain anything.
    - Return only the SQL query.

    User Query: {user_input}
    """

    response = model.generate_content(prompt)
    return response.text.strip()


# Function to execute SQL
def execute_query(sql_query):
    conn = sqlite3.connect("data.db")
    try:
        df = pd.read_sql_query(sql_query, conn)
        return df
    except Exception as e:
        return str(e)
    finally:
        conn.close()


# Streamlit UI
st.set_page_config(page_title="IntelliSQL", layout="wide")

st.title("🧠 IntelliSQL - Intelligent SQL Querying with Gemini Pro")

user_input = st.text_input("Enter your question in natural language:")

if st.button("Generate SQL"):
    if user_input:
        sql_query = generate_sql_query(user_input)

        st.subheader("Generated SQL Query:")
        st.code(sql_query, language="sql")

        if st.button("Execute Query"):
            result = execute_query(sql_query)

            st.subheader("Query Result:")
            if isinstance(result, pd.DataFrame):
                st.dataframe(result)
            else:
                st.error(result)
    else:
        st.warning("Please enter a query.")
