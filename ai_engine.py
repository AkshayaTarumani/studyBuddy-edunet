import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_ai(prompt):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )
    return response.text


def explain_topic(text):
    return ask_ai(f"Explain this simply for students:\n{text}")

def summarize_text(text):
    return ask_ai(f"Summarize in bullet points:\n{text}")

def generate_quiz(text):
    return ask_ai(f"Create 5 MCQs with answers:\n{text}")

def generate_flashcards(text):
    return ask_ai(f"Create flashcards Q&A format:\n{text}")