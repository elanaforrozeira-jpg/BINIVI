import os
import asyncio
import logging
import yt_dlp
from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_NAME
from core.queue_manager import queue_manager

LOG = logging.getLogger(__name__)

# Helper function to process the next song in the queue
async def process_next_song(client, chat_id: int):
    """Pops the next song from the queue and starts processing it."""
    
    # Check if another song is already being processed
    if queue_manager.is_currently_processing(chat_id):
        return

    next_item = queue_manager.get_next_in_queue(chat_id)
    
    if not next_item:
        queue_manager.set_processing_status(chat_id, False)
        LOG.info(f"Queue for chat {chat_id} is empty. Stopping processing.")
        return

    queue_manager.set_processing_status(chat_id, True)
    query = next_item['query']
    message = next_item['message']
    
    status = await message.reply(f"🎶 **Now Playing (From Queue):** `{query}`...")
    
    # --- Download and Upload Logic (Copied and adapted from original bot.py) ---
    
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
        LOG.error(f"Error processing song for chat {chat_id}: {e}")
        await status.edit(f"❌ **Error:** `{str(e)}`\n\nPlease try again!")
    finally:
        # After processing, set status to False and check for the next song
        queue_manager.set_processing_status(chat_id, False)
        # Recursively call to process the next song if the queue is not empty
        asyncio.create_task(process_next_song(client, chat_id))


# /play and /song Command
@Client.on_message(filters.command(["play", "p", "song"]))
async def play_command(client, message: Message):
    if len(message.command) < 2:
        return await message.reply(
            "❌ **Please provide a song name!**\n\n"
            "**Example:**\n"
            "`/play Tum Hi Ho`\n"
            "`/play Arijit Singh`"
        )
    
    query = " ".join(message.command[1:])
    chat_id = message.chat.id
    
    # Add to queue
    queue_size = queue_manager.add_to_queue(chat_id, query, message)
    
    if queue_size > 1:
        await message.reply(f"✅ **Added to Queue!**\n\n"
                            f"Your request is at position **#{queue_size - 1}** in the queue.")
    else:
        # Start processing if this is the first item
        await message.reply(f"🔍 **Searching and Starting:** `{query}`...")
        asyncio.create_task(process_next_song(client, chat_id))

# /queue Command
@Client.on_message(filters.command("queue"))
async def queue_command(client, message: Message):
    chat_id = message.chat.id
    queue_list = queue_manager.get_queue_list(chat_id)
    
    if not queue_list:
        return await message.reply("🎶 **The music queue is currently empty!**")
    
    queue_text = "**🎶 Current Music Queue:**\n\n"
    for i, query in enumerate(queue_list):
        queue_text += f"**{i+1}.** `{query}`\n"
        
    await message.reply(queue_text)

# /skip Command (Admin only)
@Client.on_message(filters.command("skip") & filters.group)
async def skip_command(client, message: Message):
    chat_id = message.chat.id
    
    # Basic admin check (can be improved with get_chat_member)
    member = await client.get_chat_member(chat_id, message.from_user.id)
    if not (member.can_manage_chat or member.status in ["creator", "administrator"]):
        return await message.reply("❌ **Only group administrators can skip songs!**")

    if not queue_manager.is_currently_processing(chat_id):
        return await message.reply("❌ **No song is currently being processed to skip!**")

    # Stop the current processing by setting status to False and immediately calling process_next_song
    # The current download/upload task will finish, but the next song will start immediately after.
    # For a true skip, we would need to stop the running yt-dlp process, which is complex.
    # For this advanced version, we will simply start the next song immediately after the current one finishes.
    
    # A simpler, more immediate skip for this context:
    queue_manager.set_processing_status(chat_id, False)
    await message.reply("⏭️ **Skipping current song...**")
    asyncio.create_task(process_next_song(client, chat_id))
