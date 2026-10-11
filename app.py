import streamlit as st

st.title("PrisMate AI")

user_input = st.text_area("Paste your CV or describe your situation")

if st.button("Generate Plan"):
    st.write("AI response will appear here")
