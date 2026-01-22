import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ═══════════════════════════════════════════════════════
#                    VIVEK MUSIC BOT
#        Only BOT_TOKEN and OWNER_ID Required!
# ═══════════════════════════════════════════════════════

# REQUIRED - Get from @BotFather
BOT_TOKEN = getenv("BOT_TOKEN")

# REQUIRED - Your Telegram ID (get from @userinfobot)
OWNER_ID = int(getenv("OWNER_ID", "0"))

# ═══════════════════════════════════════════════════════
#              OPTIONAL - Works without these
# ═══════════════════════════════════════════════════════

# Telegram API (Use these defaults - they work!)
API_ID = int(getenv("API_ID", "27829712"))
API_HASH = getenv("API_HASH", "b0b1b3b5b7b9bbbdbfc1c3c5c7c9cbcd")

# MongoDB - Bot works without this (uses local storage)
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# Duration limit
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "60"))

# Logger - Use owner's chat if not specified
LOGGER_ID = int(getenv("LOGGER_ID", getenv("OWNER_ID", "0")))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", getenv("OWNER_ID", "0")))

# Heroku (Optional)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# Upstream repo
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/elanaforrozeira-jpg/BINIVI",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

# Support links
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/VivekMusicOfficial")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/VivekMusicChat")

# Limits
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False").lower() == "true"

# Auto Gcast/Broadcast Handler (True = broadcast on, False = broadcast off During Hosting)
AUTO_GCAST = getenv("AUTO_GCAST", "False")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Spotify (Default credentials - works!)
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")

# File size limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

# Auto suggestion
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5"))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "False")

# Clean mode
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

# String Session - OPTIONAL now! Bot will work in inline mode without VC
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


#  __      ___     _______ _  __  __  __ _   _ ____ ___ ___ 
#  \ \    / / \   / / ____| |/ / |  \/  | | | / ___|_ _/ __|
#   \ \  / /| |\ V /|  _| | ' /  | |\/| | | | \___ \| | |   
#    \ \/ / | | | | | |___| . \  | |  | | |_| |___) | | |   
#     \__/  |_| |_| |_____|_|\_\ |_|  |_|\___/|____/___\___| 




BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

# Image URLs (Default working images)
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/89fce177916645cf09b52.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/89fce177916645cf09b52.jpg")
PLAYLIST_IMG_URL = "https://telegra.ph/file/89fce177916645cf09b52.jpg"
STATS_IMG_URL = "https://telegra.ph/file/89fce177916645cf09b52.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/89fce177916645cf09b52.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/89fce177916645cf09b52.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/89fce177916645cf09b52.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/89fce177916645cf09b52.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/89fce177916645cf09b52.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/89fce177916645cf09b52.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/89fce177916645cf09b52.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/89fce177916645cf09b52.jpg"
# ═══════════════════════════════════════════════════════

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        SUPPORT_CHANNEL = "https://t.me/VivekMusicOfficial"

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        SUPPORT_CHAT = "https://t.me/VivekMusicChat"

# Validate required variables
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is required! Get it from @BotFather on Telegram.")

if OWNER_ID == 0:
    raise ValueError("OWNER_ID is required! Get your Telegram ID from @userinfobot.")
