import streamlit as st
from google import genai

# ───────────────────────────────────────
# CONFIGURE GEMINI
# ───────────────────────────────────────
# Hard-code your key here just to validate the flow:
client = genai.Client(api_key="AIzaSyDy_17Hn9m6Zd3CAeOxvLdJjTlLZizdttk")

# ───────────────────────────────────────
# BUILD A TINY UI
# ───────────────────────────────────────
st.title("🤖 Gemini Sanity‐Check")

user_input = st.text_input("Ask Gemini something:", value="Hello, Gemini!")
if st.button("Send"):
    # ───────────────────────────────────────
    # CALL Gemini
    # ───────────────────────────────────────
    response = client.chat.completions.create(
        model="gemini-pro",
        temperature=0.5,
        messages=[
            {"author": "system", "content": "You are a helpful assistant."},
            {"author": "user",   "content": user_input},
        ],
    )
    reply = response.choices[0].message.content

    # ───────────────────────────────────────
    # DISPLAY
    # ───────────────────────────────────────
    st.subheader("Gemini says:")
    st.write(reply)
