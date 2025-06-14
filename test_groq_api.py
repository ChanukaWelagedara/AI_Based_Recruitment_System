from groq import Groq

# Paste your brand new API key here
api_key = "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"  # Replace with your new key

print(f"Using API key: {api_key[:10]}... (length={len(api_key)})")

client = Groq(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="llama3-70b-8192",  # Full model name
        messages=[{"role": "user", "content": "Hello Groq!"}],
        max_tokens=10,
    )
    print("✅ Success:", response.choices[0].message.content)
except Exception as e:
    print("❌ Error:", e)
