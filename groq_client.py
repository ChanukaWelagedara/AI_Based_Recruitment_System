import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is missing in your environment variables.")

client = Groq(api_key=api_key)

def generate_completion(prompt, model="llama-3.3-70b-versatile", max_tokens=1024, temperature=1.0, stream=False):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature,
        stream=stream,
        top_p=1,
        stop=None,
    )
    return response
