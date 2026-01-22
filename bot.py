import os
from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH, BOT_NAME

# Use default API credentials only if not provided
# Note: These are public test credentials. For production, get your own from https://my.telegram.org
api_id = API_ID if API_ID else 27829712
api_hash = API_HASH if API_HASH else "a3a3a3a3a3a3a3a3a3a3a3a3a3a3a3a3"

if not api_id or not api_hash:
    raise ValueError("API_ID and API_HASH are required! Get them from https://my.telegram.org")

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
