from groq_client import generate_completion
from prompts import CV_SUMMARY_PROMPT
from utils.pdf_utils import extract_text_from_pdf
from utils.linkedin_scraper import scrape_linkedin

def summarize_cv(cv_path, linkedin_url=None):
    cv_text = extract_text_from_pdf(cv_path)
    linkedin_text = scrape_linkedin(linkedin_url) if linkedin_url else "No LinkedIn provided"

    prompt = CV_SUMMARY_PROMPT.format(cv_text=cv_text, linkedin_text=linkedin_text)
    response = generate_completion(prompt)
    return response.choices[0].message.content
