from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_NAME
import yt_dlp
import os

@Client.on_message(filters.command(["play", "p"]))
async def play_command(client, message: Message):
    # Auto-delete user command
    try:
        await message.delete()
    except:
        pass
    
    if len(message.command) < 2:
        return await message.reply("❌ Please provide a song name!\n\nExample: `/play Arijit Singh`")
    
    query = " ".join(message.command[1:])
    status_msg = await message.reply(f"🔍 Searching for **{query}**...")
    
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)
            if 'entries' in info:
                info = info['entries'][0]
            
            title = info.get('title', 'Unknown')
            duration = info.get('duration', 0)
            thumb = info.get('thumbnail', '')
            file_path = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
        
        await status_msg.edit("📤 Uploading audio...")
        
        await message.reply_audio(
            audio=file_path,
            title=title,
            caption=f"🎵 **{title}**\n\n• Duration: {duration//60}:{duration%60:02d}\n• Requested by: {message.from_user.mention}\n\n🎧 **{BOT_NAME}**",
            thumb=thumb if thumb else None
        )
        
        await status_msg.delete()
        
        # Cleanup
        if os.path.exists(file_path):
            os.remove(file_path)
            
    except Exception as e:
        await status_msg.edit(f"❌ Error: {str(e)}")
