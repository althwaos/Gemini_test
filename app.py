import streamlit as st
import google.generativeai as genai

# ────────────────────────────────
# CONFIGURE GEMINI
# ────────────────────────────────
# For quick testing, we hard-code the key here.
# (On Streamlit Cloud you can also set it as a Secret.)
genai.configure(api_key="AIzaSyDy_17Hn9m6Zd3CAeOxvLdJjTlLZizdttk")

# ────────────────────────────────
# 1) UI: prompt input
# ────────────────────────────────
st.title("🤖 Gemini Sanity-Check")
user_input = st.text_input("Ask Gemini something:", "Hello, Gemini!")

if st.button("Send"):
    # ────────────────────────────────
    # 2) CALL the chat completions API
    # ────────────────────────────────
    response = genai.chat.completions.create(
        model="gemini-pro",
        temperature=0.5,
        messages=[
            {"author": "system", "content": "You are a helpful assistant."},
            {"author": "user",   "content": user_input},
        ],
    )
    # ────────────────────────────────
    # 3) DISPLAY the reply
    # ────────────────────────────────
    reply = response.choices[0].message.content
    st.subheader("Gemini says:")
    st.write(reply)
