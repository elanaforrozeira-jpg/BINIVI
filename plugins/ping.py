from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("ping"))
async def ping_command(client, message: Message):
    try:
        await message.delete()
    except:
        pass
    await message.reply("🏓 **Pong!**\n\nBot is alive and working!")
