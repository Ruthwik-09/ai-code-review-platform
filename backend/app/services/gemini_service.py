import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("API Key Loaded:", api_key is not None)

genai.configure(api_key=api_key)

# Use a stable model
model = genai.GenerativeModel("gemini-2.0-flash")


def review_code(code: str):
    prompt = f"""
You are an expert software engineer.

Review the following code.

Provide:
1. Bugs
2. Code Quality Suggestions
3. Time Complexity
4. Space Complexity
5. Improved Code

Code:
{code}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"ERROR: {str(e)}"