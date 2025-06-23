import streamlit as st
import google.generativeai as genai

# ────────────────────────────
# CONFIGURE GEMINI
# ────────────────────────────
# Paste your API key here (for quick testing only):
genai.configure(api_key="AIzaSyDy_17Hn9m6Zd3CAeOxvLdJjTlLZizdttk")

# ────────────────────────────
# UI
# ────────────────────────────
st.title("🤖 Gemini Sanity-Check")

user_input = st.text_input("Ask Gemini something:", "Hello, Gemini!")
if st.button("Send"):
    # ────────────────────────────
    # CALL Gemini
    # ────────────────────────────
    response = genai.chat.create(
        model="gemini-pro",
        temperature=0.5,
        messages=[
            {"author": "system", "content": "You are a helpful assistant."},
            {"author": "user",   "content": user_input},
        ],
    )
    # Extract and show the reply
    reply = response.choices[0].message.content
    st.subheader("Gemini says:")
    st.write(reply)
