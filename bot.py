import os
import asyncio
from aiohttp import web
from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH, BOT_NAME

# ============== HEALTH CHECK SERVER ==============
async def health_check(request):
    """Health check endpoint for Render"""
    return web.Response(text="VIVEK MUSIC BOT is running! ✅")

async def start_health_server():
    """Start HTTP server for health checks"""
    app = web.Application()
    app.router.add_get("/", health_check)
    app.router.add_get("/health", health_check)
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Health server running on port {port}")

# ============== BOT CONFIGURATION ==============

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

# ============== MAIN ==============
async def main():
    """Main function to run health server and bot together"""
    # Start health check server first
    await start_health_server()
    
    # Start bot
    print(f"Starting {BOT_NAME}...")
    await app.start()
    print(f"{BOT_NAME} is now running!")
    
    # Keep running
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
