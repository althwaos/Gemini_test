import streamlit as st
import google.generativeai as genai

# ────────────────────────────
# configure
# ────────────────────────────
genai.configure(api_key="AIzaSyDy_17Hn9m6Zd3CAeOxvLdJjTlLZizdttk")

st.title("Gemini Sanity Check")

user_input = st.text_input("Ask Gemini:", "Hello, Gemini!")
if st.button("Send"):
    resp = genai.chat.create(
        model="gemini-pro",
        temperature=0.5,
        messages=[
            {"author":"system", "content":"You are a helpful assistant."},
            {"author":"user",   "content":user_input},
        ],
    )
    answer = resp.choices[0].message.content
    st.write(answer)
