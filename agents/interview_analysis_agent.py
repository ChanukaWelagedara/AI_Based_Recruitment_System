from groq_client import generate_completion
from prompts import INTERVIEW_ANALYSIS_PROMPT

def analyze_interview(interview_transcript):
    prompt = INTERVIEW_ANALYSIS_PROMPT.format(interview_transcript=interview_transcript)
    response = generate_completion(prompt)
    return response.choices[0].message.content
