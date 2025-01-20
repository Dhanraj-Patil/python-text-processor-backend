import google.generativeai as genai

genai.configure(api_key="AIzaSyBSgVTCi_3nUqHE9v5leIeqB3mBMeSwwQI")
model = genai.GenerativeModel("gemini-1.5-flash")

def process_text(text):
    content = model.generate_content(f"Provide sentiment analysis for the following text:\n{text}")
    return content.candidates[0].content.parts[0].text
    # print(content)
