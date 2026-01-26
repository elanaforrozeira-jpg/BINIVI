import asyncio
import logging
from aiohttp import web
from pyrogram import Client
from config import BOT_TOKEN, OWNER_ID, PORT, BOT_NAME, API_ID, API_HASH

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s"
)
LOG = logging.getLogger(__name__)

# ═══════════════════════════════════════════════════════════
#                    HEALTH CHECK SERVER
# ═══════════════════════════════════════════════════════════

async def health_handler(request):
    return web.Response(
        text=f"""
<!DOCTYPE html>
<html>
<head>
    <title>{BOT_NAME} - Status</title>
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
        <h1>🎵 {BOT_NAME}</h1>
        <p class="status">✅ Bot is Running!</p>
        <p>Advanced Version</p>
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
    LOG.info(f"✅ Health server running on port {PORT}")

# ═══════════════════════════════════════════════════════════
#                       BOT CLIENT
# ═══════════════════════════════════════════════════════════

if not BOT_TOKEN:
    LOG.error("❌ ERROR: BOT_TOKEN is required!")
    exit(1)

# Enforce proper API credentials
if API_ID == 27829712 or API_HASH == "fb590fb04369d740e742a0198aa66e0a":
    LOG.warning("⚠️ WARNING: Using default public test API_ID/API_HASH. Please set your own in environment variables for production use.")

app = Client(
    name="VivekMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="handlers") # Load all handlers from the 'handlers' directory
)

# ═══════════════════════════════════════════════════════════
#                         MAIN
# ═══════════════════════════════════════════════════════════

async def main():
    LOG.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    LOG.info(f"  🎵 {BOT_NAME} - Advanced Version")
    LOG.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    # Start health server
    await start_server()
    
    # Start bot
    await app.start()
    me = await app.get_me()
    LOG.info(f"  ✅ Bot Started: @{me.username}")
    LOG.info(f"  👤 Owner ID: {OWNER_ID}")
    LOG.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    # Keep running
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        LOG.info("Bot stopped by user.")
    except Exception as e:
        LOG.error(f"An unexpected error occurred: {e}")
