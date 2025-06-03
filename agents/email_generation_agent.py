from groq_client import generate_completion
from prompts import EMAIL_GENERATION_PROMPT

def generate_email(cv_summary, job_summary, score):
    prompt = EMAIL_GENERATION_PROMPT.format(cv_summary=cv_summary, job_summary=job_summary, score=score)
    response = generate_completion(prompt)
    return response.choices[0].message.content
