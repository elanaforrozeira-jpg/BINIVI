import os
import asyncio
from aiohttp import web
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import yt_dlp

from config import (
    BOT_TOKEN, OWNER_ID, API_ID, API_HASH, 
    BOT_NAME, PORT, START_IMG, 
    SUPPORT_CHANNEL, SUPPORT_CHAT
)

# ═══════════════════════════════════════════════════════════
#                    HEALTH CHECK SERVER
# ═══════════════════════════════════════════════════════════

async def health_handler(request):
    return web.Response(
        text=f"""
<!DOCTYPE html>
<html>
<head>
    <title>VIVEK MUSIC BOT</title>
    <style>
        body {{ font-family: Arial; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
        .container {{ text-align: center; padding: 40px; background: rgba(0,0,0,0.3); border-radius: 20px; }}
        h1 {{ font-size: 3em; margin-bottom: 10px; }}
        p {{ font-size: 1.2em; }}
        .status {{ color: #00ff88; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎵 VIVEK MUSIC BOT</h1>
        <p class="status">✅ Bot is Running!</p>
        <p>Made with ❤️ by Vivek</p>
    </div>
</body>
</html>
        """,
        content_type="text/html"
    )

async def start_server():
    app = web.Application()
    app.router.add_get("/", health_handler)
    app.router.add_get("/health", health_handler)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"✅ Health server running on port {PORT}")

# ═══════════════════════════════════════════════════════════
#                       BOT CLIENT
# ═══════════════════════════════════════════════════════════

# Validate BOT_TOKEN
if not BOT_TOKEN:
    print("❌ ERROR: BOT_TOKEN is required!")
    print("👉 Get it from @BotFather on Telegram")
    exit(1)

app = Client(
    name="VivekMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

# ═══════════════════════════════════════════════════════════
#                       COMMANDS
# ═══════════════════════════════════════════════════════════

# /start Command
@app.on_message(filters.command("start") & filters.private)
async def start_private(client, message: Message):
    user = message.from_user
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Me To Group", url=f"https://t.me/{(await client.get_me()).username}?startgroup=true")],
        [
            InlineKeyboardButton("📢 Channel", url=SUPPORT_CHANNEL),
            InlineKeyboardButton("💬 Support", url=SUPPORT_CHAT)
        ],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ])
    
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""
**━━━━━━━━━━━━━━━━━━━━━**
🎵 **Welcome to {BOT_NAME}!**
**━━━━━━━━━━━━━━━━━━━━━**

Hey **{user.first_name}**! 👋

I'm a powerful music bot that can download and send songs for you!

**🎧 What I can do:**
• Download songs from YouTube
• Send high quality audio files
• Works in groups & private chat

**📝 Quick Start:**
Just send `/play song name` to get started!

**━━━━━━━━━━━━━━━━━━━━━**
        """,
        reply_markup=keyboard
    )

@app.on_message(filters.command("start") & filters.group)
async def start_group(client, message: Message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Channel", url=SUPPORT_CHANNEL),
         InlineKeyboardButton("💬 Support", url=SUPPORT_CHAT)]
    ])
    
    sent = await message.reply(
        f"**🎵 {BOT_NAME} is Active!**\n\n"
        f"Send `/play song name` to download music!\n\n"
        f"Made with ❤️ by Vivek",
        reply_markup=keyboard
    )
    
    # Auto delete after 10 seconds
    await asyncio.sleep(10)
    try:
        await sent.delete()
        await message.delete()
    except:
        pass

# /help Command
@app.on_message(filters.command("help"))
async def help_command(client, message: Message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Channel", url=SUPPORT_CHANNEL),
         InlineKeyboardButton("💬 Support", url=SUPPORT_CHAT)]
    ])
    
    await message.reply(
        f"""
**━━━━━━━━━━━━━━━━━━━━━**
📚 **{BOT_NAME} - HELP**
**━━━━━━━━━━━━━━━━━━━━━**

**🎵 Music Commands:**
• `/play [song name]` - Download a song
• `/song [song name]` - Same as play

**⚡ Utility Commands:**
• `/start` - Start the bot
• `/help` - Show this message
• `/ping` - Check bot status
• `/id` - Get your Telegram ID

**💡 Example:**
`/play Tum Hi Ho`
`/play Arijit Singh songs`

**━━━━━━━━━━━━━━━━━━━━━**
Made with ❤️ by Vivek
        """,
        reply_markup=keyboard
    )

# /ping Command
@app.on_message(filters.command("ping"))
async def ping_command(client, message: Message):
    import time
    start = time.time()
    msg = await message.reply("🏓 **Pinging...**")
    end = time.time()
    
    await msg.edit(
        f"🏓 **Pong!**\n\n"
        f"**⚡ Response:** `{round((end - start) * 1000, 2)}ms`\n"
        f"**✅ Status:** Bot is alive!"
    )

# /id Command
@app.on_message(filters.command("id"))
async def id_command(client, message: Message):
    user = message.from_user
    text = f"**👤 Your Info:**\n\n"
    text += f"**🆔 ID:** `{user.id}`\n"
    text += f"**📛 Name:** {user.first_name}\n"
    
    if message.chat.type != "private":
        text += f"\n**👥 Chat Info:**\n"
        text += f"**🆔 Chat ID:** `{message.chat.id}`\n"
        text += f"**📛 Title:** {message.chat.title}\n"
    
    await message.reply(text)

# /play Command
@app.on_message(filters.command(["play", "p", "song"]))
async def play_command(client, message: Message):
    if len(message.command) < 2:
        return await message.reply(
            "❌ **Please provide a song name!**\n\n"
            "**Example:**\n"
            "`/play Tum Hi Ho`\n"
            "`/play Arijit Singh`"
        )
    
    query = " ".join(message.command[1:])
    status = await message.reply(f"🔍 **Searching:** `{query}`...")
    
    # Create downloads folder
    os.makedirs("downloads", exist_ok=True)
    
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'downloads/%(id)s.%(ext)s',
            'noplaylist': True,
            'quiet': True,
            'no_warnings': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        
        await status.edit("⬇️ **Downloading...**")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)
            if 'entries' in info:
                info = info['entries'][0]
            
            title = info.get('title', 'Unknown')
            duration = info.get('duration', 0)
            video_id = info.get('id', 'audio')
            thumb_url = info.get('thumbnail', '')
            channel = info.get('channel', 'Unknown')
            
            file_path = f"downloads/{video_id}.mp3"
        
        await status.edit("📤 **Uploading...**")
        
        # Format duration
        mins, secs = divmod(duration, 60)
        duration_str = f"{mins}:{secs:02d}"
        
        caption = f"""
**━━━━━━━━━━━━━━━━━━━━━**
🎵 **{title}**
**━━━━━━━━━━━━━━━━━━━━━**

**⏱️ Duration:** {duration_str}
**🎤 Channel:** {channel}
**👤 Requested by:** {message.from_user.mention}

**━━━━━━━━━━━━━━━━━━━━━**
🎧 **{BOT_NAME}**
        """
        
        await message.reply_audio(
            audio=file_path,
            caption=caption,
            title=title,
            performer=channel
        )
        
        await status.delete()
        
        # Cleanup
        if os.path.exists(file_path):
            os.remove(file_path)
            
    except Exception as e:
        await status.edit(f"❌ **Error:** `{str(e)}`\n\nPlease try again!")

# Callback for help button
@app.on_callback_query(filters.regex("help"))
async def help_callback(client, callback):
    await callback.answer()
    await help_command(client, callback.message)

# ═══════════════════════════════════════════════════════════
#                         MAIN
# ═══════════════════════════════════════════════════════════

async def main():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"  🎵 {BOT_NAME}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    # Start health server for Render
    await start_server()
    
    # Start bot
    await app.start()
    me = await app.get_me()
    print(f"  ✅ Bot Started: @{me.username}")
    print(f"  👤 Owner ID: {OWNER_ID}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    # Keep running
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
