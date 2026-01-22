from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_NAME

@Client.on_message(filters.command("help"))
async def help_command(client, message: Message):
    try:
        await message.delete()
    except:
        pass
        
    await message.reply(f"""
🎵 **{BOT_NAME} - Commands**

**Music Commands:**
• /play [song] - Play/Download a song
• /song [name] - Download song as audio

**Utility Commands:**
• /start - Start the bot
• /help - Show this message
• /ping - Check bot latency

**Made with ❤️ by Vivek**
    """)
