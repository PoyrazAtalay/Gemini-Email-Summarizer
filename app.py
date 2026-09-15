import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load environment variables
load_dotenv(override=True)

# 2. Initialize the client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

def analyze_email(email_text):
    ai_message = [
        {
            "role": "system",
            "content": "You are an email assistant. Extract a concise Subject Line and a 3-bullet action summary from the provided email."
        },
        {
            "role": "user",
            "content": email_text
        }
    ]
    
    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=ai_message
    )
    
    return response.choices[0].message.content

email = """
YOUR_EMAIL_HERE
"""

print(analyze_email(email))
