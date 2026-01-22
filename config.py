import os
from dotenv import load_dotenv

load_dotenv()

# ═══════════════════════════════════════════════════════════
#              🎵 VIVEK MUSIC BOT - CONFIGURATION
# ═══════════════════════════════════════════════════════════
#                ONLY 2 VARIABLES REQUIRED!
# ═══════════════════════════════════════════════════════════

# ✅ REQUIRED - Get from @BotFather on Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# ✅ REQUIRED - Your Telegram ID (get from @userinfobot)
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# ═══════════════════════════════════════════════════════════
#              DEFAULT VALUES - DON'T CHANGE!
# ═══════════════════════════════════════════════════════════

# Telegram API Credentials (Public Test Credentials - Works!)
API_ID = 27829712
API_HASH = "fb590fb04369d740e742a0198aa66e0a"

# Bot Info
BOT_NAME = "🎵 VIVEK MUSIC"
BOT_USERNAME = ""  # Will be set automatically

# Port for Render
PORT = int(os.getenv("PORT", 8080))

# Support Links
SUPPORT_CHANNEL = "https://t.me/VivekMusicOfficial"
SUPPORT_CHAT = "https://t.me/VivekMusicChat"

# Images
START_IMG = "https://telegra.ph/file/89fce177916645cf09b52.jpg"
PING_IMG = "https://telegra.ph/file/89fce177916645cf09b52.jpg"
