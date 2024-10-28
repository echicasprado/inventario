from dotenv import load_dotenv
import os

class Settings:
    load_dotenv()
    DATABASE_URL = os.getenv("DATA_URL")

settings = Settings()