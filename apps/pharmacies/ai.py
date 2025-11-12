import google.generativeai as genai
from django.conf import settings
import os
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def analyze_symptoms(symptoms_text):
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    The user will describe symptoms. 
    Your job is NOT to diagnose diseases. 
    ONLY suggest **safe, common, over-the-counter medicines**.
    If symptoms are severe, tell them to visit a doctor.

    Return your result in this JSON format only:
    {{
      "suggested_condition": "...",
      "suggested_medicines": ["...", "..."],
      "advice": "..."
    }}

    Symptoms: {symptoms_text}
    """

    response = model.generate_content(prompt)
    return response.text
