import asyncio
import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME, SUPPORT_CHANNEL, SUPPORT_CHAT, START_IMG

# ═══════════════════════════════════════════════════════════
#                       COMMANDS
# ═══════════════════════════════════════════════════════════

# /start Command
@Client.on_message(filters.command("start") & filters.private)
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

I'm an **Advanced Music Bot** that can download and send songs for you, now with a **Music Queue System** for groups!

**🎧 What I can do:**
• Download songs from YouTube
• Send high quality audio files
• Works in groups & private chat
• **Advanced Music Queue (Group)**

**📝 Quick Start:**
Just send `/play song name` to get started!

**━━━━━━━━━━━━━━━━━━━━━**
        """,
        reply_markup=keyboard
    )

@Client.on_message(filters.command("start") & filters.group)
async def start_group(client, message: Message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Channel", url=SUPPORT_CHANNEL),
         InlineKeyboardButton("💬 Support", url=SUPPORT_CHAT)]
    ])
    
    sent = await message.reply(
        f"**🎵 {BOT_NAME} is Active!**\n\n"
        f"Send `/play song name` to download music!\n"
        f"Use `/queue` to see the current song list."
        f"Advanced Version Active!"
        f"",
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
@Client.on_message(filters.command("help"))
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
• `/play [song name]` - Download a song and add it to the queue.
• `/song [song name]` - Same as play.
• `/queue` - Show the current music queue (Group only).
• `/skip` - Skip the current song (Admin only in Group).

**⚡ Utility Commands:**
• `/start` - Start the bot.
• `/help` - Show this message.
• `/ping` - Check bot status.
• `/id` - Get your Telegram ID.

**💡 Example:**
`/play Tum Hi Ho`
`/play Arijit Singh songs`

**━━━━━━━━━━━━━━━━━━━━━**
        """,
        reply_markup=keyboard
    )

# /ping Command
@Client.on_message(filters.command("ping"))
async def ping_command(client, message: Message):
    start = time.time()
    msg = await message.reply("🏓 **Pinging...**")
    end = time.time()
    
    await msg.edit(
        f"🏓 **Pong!**\n\n"
        f"**⚡ Response:** `{round((end - start) * 1000, 2)}ms`\n"
        f"**✅ Status:** Bot is alive! (Advanced Version)"
    )

# /id Command
@Client.on_message(filters.command("id"))
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

# Callback for help button
@Client.on_callback_query(filters.regex("help"))
async def help_callback(client, callback):
    await callback.answer()
    await help_command(client, callback.message)
