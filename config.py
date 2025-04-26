from dotenv import load_dotenv
import os

load_dotenv(override=True)

OPENAI_KEY = str(os.getenv('OPENAI_API_KEY')) 
