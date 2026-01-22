import os
from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH, BOT_NAME

# Use default API credentials if not provided
api_id = API_ID if API_ID else 27829712
api_hash = API_HASH if API_HASH else "a3a3a3a3a3a3a3a3a3a3a3a3a3a3a3a3"

app = Client(
    "VivekMusicBot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

# Create downloads folder
if not os.path.exists("downloads"):
    os.makedirs("downloads")

if __name__ == "__main__":
    print(f"Starting {BOT_NAME}...")
    app.run()
