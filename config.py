import os
from dotenv import load_dotenv

load_dotenv()

# Required
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# Optional
API_ID = int(os.getenv("API_ID", "0")) 
API_HASH = os.getenv("API_HASH", "")
STRING_SESSION = os.getenv("STRING_SESSION", "")
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

# Bot Info
BOT_NAME = "VIVEK MUSIC"
SUPPORT_CHANNEL = "https://t.me/VivekMusicOfficial"
