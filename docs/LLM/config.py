import os
from dotenv import load_dotenv

s = 3

class Config:

    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
