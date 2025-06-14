import json
import random
from groq_client import generate_completion
from prompts import MCQ_INTERVIEW_PROMPT

def conduct_mcq_interview(cv_summary):
    prompt = MCQ_INTERVIEW_PROMPT.format(cv_summary=cv_summary)
    response = generate_completion(prompt)
    raw_output = response.choices[0].message.content

    print("DEBUG - Raw LLM output for MCQs:")
    print(raw_output)
    print("-----")

    try:
        questions = json.loads(raw_output)
    except json.JSONDecodeError:
        print("JSON decode error, returning empty question list.")
        questions = []

    # Simulate candidate answers and scoring
    score = 0
    for q in questions:
        selected = random.randint(0, 3)
        q["selected"] = selected
        if selected == q["correct"]:
            score += 4  # 4 marks per correct

    return {"questions": questions, "score": score}
