import streamlit as st
import os
from groq import Groq

st.title("PrisMate AI")

user_input = st.text_area("Paste your CV or describe your situation")

# Initialize Groq client using Streamlit Secrets
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_plan(text):
    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a senior career advisor. Provide clear, structured, "
                    "actionable guidance tailored to the user's background."
                )
            },
            {"role": "user", "content": text}
        ]
    )

    # Extract message content safely across all Groq versions
    msg = response.choices[0].message

    if isinstance(msg, dict):
        return msg.get("content", "No content returned.")
    return msg

if st.button("Generate Plan"):
    if user_input.strip():
        st.write("Generating your personalized career plan...")
        output = generate_plan(user_input)
        st.write(output)
    else:
        st.write("Please enter your CV or description.")
