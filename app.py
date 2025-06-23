# app.py
import streamlit as st
from openai import AzureOpenAI

# ───────────────────────────────────────
# 0) AZURE OPENAI CONFIGURATION
# ───────────────────────────────────────
AZURE_OPENAI_API_KEY = "7CqvJEXBe6eFMK18yVr9jB811IyfIGbw2FqxCZREkMmqwJWQNj4JJQQJ99BEACYeBjFXJ3w3AAAAACOGSx58"
AZURE_OPENAI_ENDPOINT = "https://group7project.openai.azure.com/"
AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"          # your deployment name
AZURE_OPENAI_API_VERSION = "2024-05-01-preview"  # keep as installed

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION,
)

# ───────────────────────────────────────
# 1) SIMPLE UI
# ───────────────────────────────────────
st.title("Azure-OpenAI Sanity Check")

prompt = st.text_input("Say something to your Azure model:", "Hello world!")
if st.button("Send to Azure"):
    with st.spinner("Waiting for response…"):
        resp = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=[
                {"role":"system", "content":"You are a helpful assistant."},
                {"role":"user",   "content":prompt},
            ],
            temperature=0.7,
            max_tokens=200,
        )
        answer = resp.choices[0].message.content
    st.subheader("Azure says:")
    st.write(answer)
