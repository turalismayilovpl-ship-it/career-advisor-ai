import streamlit as st
import os
from groq import Groq

st.title("PrisMate AI")

user_input = st.text_area("Paste your CV or describe your situation")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_plan(text):
    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a senior career advisor. Provide clear, structured, actionable guidance."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

if st.button("Generate Plan"):
    if user_input.strip():
        output = generate_plan(user_input)
        st.write(output)
    else:
        st.write("Please enter your CV or description.")
