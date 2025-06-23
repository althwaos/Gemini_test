import streamlit as st
import google.generativeai as genai

# ────────────────────────────────
# CONFIGURE GEMINI
# ────────────────────────────────
# (Hard-code for now; you can move into secrets later)
genai.configure(api_key="AIzaSyDy_17Hn9m6Zd3CAeOxvLdJjTlLZizdttk")

# ────────────────────────────────
# UI
# ────────────────────────────────
st.title("🤖 Gemini Sanity-Check")

prompt = st.text_input("Ask Gemini something:", "Hello, Gemini!")
if st.button("Send"):
    # ────────────────────────────────
    # CALL Gemini
    # ────────────────────────────────
    resp = genai.chat.completions.create(
        model="gemini-pro",
        temperature=0.5,
        messages=[
            {"author": "system", "content": "You are a helpful assistant."},
            {"author": "user",   "content": prompt},
        ],
    )
    reply = resp.choices[0].message.content

    # ────────────────────────────────
    # DISPLAY
    # ────────────────────────────────
    st.subheader("Gemini says:")
    st.write(reply)
