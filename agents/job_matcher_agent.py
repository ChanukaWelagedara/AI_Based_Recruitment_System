from groq_client import generate_completion
from prompts import JOB_MATCH_PROMPT

def match_cv_to_job(cv_summary, job_summary):
    prompt = JOB_MATCH_PROMPT.format(job_ad=job_summary, cv_summary=cv_summary)
    response = generate_completion(prompt)
    return response.choices[0].message.content
