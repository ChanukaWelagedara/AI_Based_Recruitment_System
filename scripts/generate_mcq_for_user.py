# scripts/generate_mcq_for_user.py

from vector import get_document_by_id
from agents.chatbot_interview_agent import conduct_mcq_interview

def print_mcq_questions_for_user(doc_id: str):
    cv_summary = get_document_by_id(doc_id)
    if not cv_summary:
        print(f"No CV summary found for ID: {doc_id}")
        return

    result = conduct_mcq_interview(cv_summary)
    
    print(f"\n--- 25 MCQ Questions for CV: {doc_id} ---\n")
    for idx, q in enumerate(result["questions"], start=1):
        print(f"{idx}. {q['question']}")
        for i, opt in enumerate(q["options"]):
            print(f"   {chr(65+i)}. {opt}")
        print()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python generate_mcq_for_user.py <cv_doc_id>")
    else:
        print_mcq_questions_for_user(sys.argv[1])
