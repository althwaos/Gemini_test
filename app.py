# test_gemini.py

from google import genai

# 1) configure with your Gemini API key
client = genai.Client(api_key="AIzaSyDy_17Hn9m6Zd3CAeOxvLdJjTlLZizdttk")

# 2) call a trivial chat completion
response = client.chat.completions.create(
    model="gemini-pro",            # or "gemini-ultra"
    temperature=0.5,
    messages=[
        {"author": "system", "content": "You are a helpful assistant."},
        {"author": "user",   "content": "Hello, Gemini! How are you today?"}
    ],
)

# 3) print out Gemini’s reply
print("Gemini says:", response.choices[0].message.content)
