from dotenv import load_dotenv
from os import getenv

load_dotenv()

class Config:
    app_name = "<APP_NAME>"
    api_key = getenv("API_KEY")