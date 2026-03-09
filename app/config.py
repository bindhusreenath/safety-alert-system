import os
from dotenv import load_dotenv
from pathlib import Path

# 🔥 Force absolute path to project root .env
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"

load_dotenv(dotenv_path=env_path)

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
AUDIO_URL = os.getenv("AUDIO_URL")

print("TWILIO SID:", TWILIO_ACCOUNT_SID)