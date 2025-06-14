import glob
from agents.central_managing_ai import run_task
from utils.pdf_utils import extract_text_from_pdf
from vector import add_text_to_vector_db, search_similar_texts 

def main():
    # Load all CVs and job ads
    cv_paths = glob.glob("data/cv_pdfs/*.pdf")
    job_paths = glob.glob("data/job_ads/*.pdf")

    if not job_paths:
        print("No job ads found in data/job_ads/")
        return

    # Pick first job ad
    job_path = job_paths[0]
    job_text = extract_text_from_pdf(job_path)

    # Store job ad in vector DB
    add_text_to_vector_db(f"job_{job_path}", job_text) 

    # Summarize job ad
    job_summary = run_task("summarize_cv", cv_path=job_path)
    print(f"Job Summary:\n{job_summary}\n")

    for cv_path in cv_paths:
        print(f"Processing CV: {cv_path}")

        # Summarize CV
        cv_summary = run_task("summarize_cv", cv_path=cv_path)

        add_text_to_vector_db(cv_path, cv_summary)

        #print(f"Candidate Summary:\n{cv_summary}\n")

        # Match candidate to job
        match_result = run_task("match_cv", cv_summary=cv_summary, job_summary=job_summary)
        #print(f"Match Result:\n{match_result}\n")

        # Conduct MCQ Interview
                # Conduct MCQ Interview
        interview = run_task("mcq_interview", cv_summary=cv_summary)

        print("\n--- 25 MCQ Questions ---")
        for idx, q in enumerate(interview["questions"], start=1):
            print(f"{idx}. {q['question']}")
            for i, opt in enumerate(q["options"]):
                print(f"   {chr(65+i)}. {opt}")
            print()



        # Interview analysis
        transcript = "Candidate answered all questions confidently."
        analysis = run_task("analyze_interview", interview_transcript=transcript)
       # print(f"Interview Analysis:\n{analysis}\n")

        # Generate follow-up email
        email = run_task("send_email", cv_summary=cv_summary, job_summary=job_summary, score=interview["score"])
       # print(f"Generated Email:\n{email}\n")

        print("=" * 40)

if __name__ == "__main__":
    main()


# import glob
# from agents.central_managing_ai import run_task
# #from vector import add_text_to_vector_db, search_similar_texts
# from utils.pdf_utils import extract_text_from_pdf

# def main():
#     # Load all CVs and job ads
#     cv_paths = glob.glob("data/cv_pdfs/*.pdf")
#     job_paths = glob.glob("data/job_ads/*.pdf")

#     if not job_paths:
#         print("No job ads found in data/job_ads/")
#         return

#     # For demo, just pick the first job ad
#     job_path = job_paths[0]
#     job_text = extract_text_from_pdf(job_path)

#     # Store job ad in vector DB
#     add_text_to_vector_db(f"job_{job_path}", job_text)

#     # Summarize job ad with AI
#     job_summary = run_task("summarize_cv", cv_path=job_path)

#     print(f"Job Summary:\n{job_summary}\n")

#     for cv_path in cv_paths:
#         print(f"Processing CV: {cv_path}")

#         # Summarize CV and add to vector DB
#         cv_summary = run_task("summarize_cv", cv_path=cv_path)
#        # add_text_to_vector_db(cv_path, cv_summary)

#         print(f"Candidate Summary:\n{cv_summary}\n")

#         # Match candidate to job
#         match_result = run_task("match_cv", cv_summary=cv_summary, job_summary=job_summary)
#         print(f"Match Result:\n{match_result}\n")

#         # Conduct MCQ Interview
#         interview = run_task("mcq_interview", cv_summary=cv_summary)
#         print(f"MCQ Interview Score: {interview['score']}")
#         for q in interview["questions"][:3]:  # print first 3 questions as sample
#             print(f"Q: {q['question']}")
#             print(f"Options: {q['options']}")
#             print(f"Selected: {q['selected']} Correct: {q['correct']}")
#             print()

#         # Interview analysis (simulate transcript)
#         transcript = "Candidate answered all questions confidently."
#         analysis = run_task("analyze_interview", interview_transcript=transcript)
#         print(f"Interview Analysis:\n{analysis}\n")

#         # Generate email
#         email = run_task("send_email", cv_summary=cv_summary, job_summary=job_summary, score=interview["score"])
#         print(f"Generated Email:\n{email}\n")

#         print("="*40)

# if __name__ == "__main__":
#     main()

