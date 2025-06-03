from .cv_summary_agent import summarize_cv
from .job_matcher_agent import match_cv_to_job
from .chatbot_interview_agent import conduct_mcq_interview
from .interview_analysis_agent import analyze_interview
from .email_generation_agent import generate_email

def run_task(task_type, **kwargs):
    if task_type == "summarize_cv":
        return summarize_cv(kwargs["cv_path"], kwargs.get("linkedin_url"))
    elif task_type == "match_cv":
        return match_cv_to_job(kwargs["cv_summary"], kwargs["job_summary"])
    elif task_type == "mcq_interview":
        return conduct_mcq_interview(kwargs["cv_summary"])
    elif task_type == "analyze_interview":
        return analyze_interview(kwargs["interview_transcript"])
    elif task_type == "send_email":
        return generate_email(kwargs["cv_summary"], kwargs["job_summary"], kwargs["score"])
    else:
        raise ValueError(f"Unknown task type: {task_type}")
