import streamlit as st
import fitz
import os
import time
from dotenv import load_dotenv
from google import genai


# ---------------- API SETUP ----------------
load_dotenv()
api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)

# ---------------- PDF FUNCTION ----------------
def extract_text(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# ---------------- AI FUNCTION ----------------
#def ask_ai(prompt):
    #response = client.models.generate_content(
        #model="gemini-flash-latest",
      #  contents=prompt
   # )
    #return response.text

def ask_ai(prompt):
    for i in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )
            return response.text
        except Exception as e:
            print("Retrying...", i+1)
            time.sleep(2)

    return "AI is busy. Please try again later."

# ---------------- STREAMLIT UI ----------------
st.title("📚 AI Study Buddy")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    text = extract_text(uploaded_file)

    st.subheader("📄 Extracted Text (Preview)")
    st.write(text[:1000])

    option = st.selectbox(
        "Choose Action",
        ["Explain", "Summarize", "Quiz", "Flashcards"]
    )

    if st.button("Generate"):
        if option == "Explain":
            result = ask_ai(f"Explain simply:\n{text}")
        elif option == "Summarize":
            result = ask_ai(f"Summarize in bullet points:\n{text}")
        elif option == "Quiz":
            result = ask_ai(f"Create 5 MCQs with answers:\n{text}")
        else:
            result = ask_ai(f"Create flashcards Q&A:\n{text}")

        st.subheader("🤖 AI Output")
        st.write(result)