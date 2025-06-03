CV_SUMMARY_PROMPT = """
You are a professional CV summarizer. Use the CV text and LinkedIn content below to create a concise summary.

CV Text:
{cv_text}

LinkedIn:
{linkedin_text}

Summarize the candidate’s strengths, skills, experience, and achievements in 5–7 lines.
"""

JOB_MATCH_PROMPT = """
Evaluate how well the candidate matches the job description.

Job Description:
{job_ad}

Candidate Summary:
{cv_summary}

1. Provide a short justification.
2. Give a score from 0 to 100.
"""

MCQ_INTERVIEW_PROMPT = """
Based on the following candidate CV summary, generate 25 MCQ-style interview questions with 4 answer choices each.
Clearly indicate the correct answer.

Return the result as a JSON list with fields:
- question
- options (list of 4)
- correct (index starting from 0)

CV Summary:
{cv_summary}
"""

INTERVIEW_ANALYSIS_PROMPT = """
You are an interview evaluator.

Here is the interview transcript:
{interview_transcript}

Evaluate candidate's clarity, communication, and technical skill in 5–7 lines.
"""

EMAIL_GENERATION_PROMPT = """
Write a professional email to the candidate based on the job description and their evaluation.

Candidate Summary:
{cv_summary}

Job Description:
{job_summary}

Matching Score: {score}

Compose a short, friendly email indicating next steps.
"""
