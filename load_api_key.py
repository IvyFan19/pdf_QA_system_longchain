import os
from dotenv import load_dotenv
"""
S1: Load the API Key
"""
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("Missing OpenAI API Key! Make sure to set it in the .env file.")

