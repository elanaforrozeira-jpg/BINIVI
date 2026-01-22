from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME

@Client.on_message(filters.command("start"))
async def start_command(client, message: Message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Me To Group", url=f"https://t.me/{(await client.get_me()).username}?startgroup=true")],
        [InlineKeyboardButton("📢 Channel", url="https://t.me/VivekMusicOfficial"),
         InlineKeyboardButton("💬 Support", url="https://t.me/VivekMusicChat")]
    ])
    
    await message.reply_photo(
        photo="https://telegra.ph/file/89fce177916645cf09b52.jpg",
        caption=f"""
🎵 **Welcome to {BOT_NAME}!**

I can play music in your group voice chats!

**Commands:**
• /play [song name] - Play a song
• /help - Show all commands
• /ping - Check if I'm alive

Made with ❤️ by Vivek
        """,
        reply_markup=keyboard
    )
    
    # Auto-delete user command
    try:
        await message.delete()
    except:
        pass
