🧠 IntelliSQL: Intelligent SQL Querying with LLMs (Gemini Pro)
📌 Overview
IntelliSQL is a cloud-based application that converts natural language queries into SQL statements using Google's Gemini Pro Large Language Model (LLM).

The system allows users to interact with databases using plain English instead of writing complex SQL queries manually.

This project demonstrates the integration of:

Large Language Models (LLMs)
SQLite Database
Streamlit Web Interface
Secure API Management
🚀 Key Features
✅ Natural Language → SQL Conversion
✅ Intelligent Query Assistance
✅ SQLite Database Integration
✅ Secure Google API Key Handling (.env)
✅ Streamlit-Based User Interface
✅ Modular Project Architecture

🏗️ System Architecture
User → Streamlit UI → Gemini API → SQL Query Generation → SQLite Database → Results Display

The Gemini Pro model interprets user queries and generates optimized SQL statements which are executed against a local SQLite database.

🛠️ Tech Stack
Python
Streamlit
Google Gemini Pro (google-generativeai)
SQLite3
Pandas
python-dotenv
