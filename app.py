# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qCRvSeF9lJpO3Mpb0mPNvaxGQ4KAunZC
"""


import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBcWXn8BnzvbwQsxKcQuz30clByoNEJXJM")

def review_code(code):
    response = genai.GenerativeModel("gemini-pro").generate_content(code)
    return response.text if response else "No response received."

st.title("AI Code Reviewer")
code_input = st.text_area("Enter your Python code:")
if st.button("Review Code") and code_input.strip():
    st.write(review_code(code_input))