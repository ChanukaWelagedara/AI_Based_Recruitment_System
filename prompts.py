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
You are a technical interviewer.

Generate exactly 25 **technical multiple-choice questions** (MCQs) based ONLY on the technologies, programming languages, tools, and frameworks mentioned in the following CV summary.

Each question should test the candidate's knowledge of these tools and skills — e.g., if the CV mentions React, ask a React question; if it mentions AWS or Terraform, ask about those.

Return ONLY a valid JSON list where each item has:
- question (string)
- options (list of 4 strings)
- correct (integer, 0–3)

DO NOT include explanations or any text outside the JSON.

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
