import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Create a .env file to store the api key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def process_text(text):
    # Generates sentiment analysis for the text provided by the user.
    content = model.generate_content(f"Provide sentiment analysis for the following text:\n{text}")
    return content.candidates[0].content.parts[0].text
    # print(content)
