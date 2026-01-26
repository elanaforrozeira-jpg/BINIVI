# BINIVI Advanced Version - Technical Documentation

## Overview

The BINIVI Advanced Version is a complete refactor of the original Telegram Music Bot, introducing a modular architecture, robust queue management, and improved configuration handling. This document provides a detailed technical overview of the implementation.

## Architecture

### Directory Structure

```
BINIVI/
├── main.py                          # Entry point and bot initialization
├── config.py                        # Configuration management
├── requirements.txt                 # Python dependencies
├── handlers/                        # Command handlers (modular)
│   ├── __init__.py
│   ├── start_help.py               # /start, /help, /ping, /id commands
│   └── play_queue.py               # /play, /queue, /skip commands
├── core/                           # Core utilities
│   └── queue_manager.py            # Music queue management
├── README.md                       # User-facing documentation
├── UPGRADE_PLAN.md                 # Upgrade plan and rationale
└── TECHNICAL_DOCUMENTATION.md      # This file
```

### Key Components

#### 1. **main.py** - Core Bot Initialization

This file serves as the entry point for the bot. It handles:

*   **Health Check Server:** An aiohttp-based HTTP server that runs on port 8080 (configurable) for deployment platforms like Render.
*   **Bot Initialization:** Creates a Pyrogram Client instance with proper configuration.
*   **Plugin Loading:** Automatically loads all handler modules from the `handlers/` directory.
*   **Logging:** Implements structured logging for better error tracking.

**Key Functions:**
- `health_handler()`: Responds to health check requests with a styled HTML response.
- `start_server()`: Starts the aiohttp server.
- `main()`: Orchestrates bot startup and keeps it running.

#### 2. **config.py** - Configuration Management

This file manages all configuration variables and enforces the use of environment variables for sensitive data.

**Key Variables:**
- `BOT_TOKEN`: Telegram bot token (required).
- `OWNER_ID`: Telegram ID of the bot owner (required).
- `API_ID`, `API_HASH`: Telegram API credentials (optional, defaults to public test credentials).
- `BOT_NAME`: Display name for the bot.
- `PORT`: Port for the health check server.
- `SUPPORT_CHANNEL`, `SUPPORT_CHAT`: Links to support resources.

**Improvement:** All sensitive credentials are now read from environment variables, with sensible defaults for non-sensitive values.

#### 3. **handlers/start_help.py** - Command Handlers

This module contains handlers for basic commands:

*   **`/start`**: Displays a welcome message with inline keyboard buttons for adding the bot to groups and accessing support.
*   **`/help`**: Shows a comprehensive list of available commands.
*   **`/ping`**: Measures and displays the bot's response time.
*   **`/id`**: Returns the user's Telegram ID and chat ID (if in a group).

**Features:**
- Separate handlers for private and group chats.
- Inline keyboard buttons for easy navigation.
- Auto-deletion of messages in groups after 10 seconds.

#### 4. **handlers/play_queue.py** - Music Queue and Playback

This module is the core of the advanced feature set:

*   **`/play` and `/song`**: Adds a song request to the queue and initiates playback if no song is currently being processed.
*   **`/queue`**: Displays the current list of songs in the queue.
*   **`/skip`**: Allows group administrators to skip the currently playing song.

**Key Functions:**
- `process_next_song()`: Asynchronously processes the next song in the queue.
  - Downloads the song using yt-dlp.
  - Converts to MP3 format.
  - Uploads to Telegram.
  - Cleans up temporary files.
  - Recursively processes the next song in the queue.

**Features:**
- Queue-based song processing for group chats.
- Per-chat queue management.
- Admin-only skip functionality.
- Graceful error handling with user-friendly error messages.

#### 5. **core/queue_manager.py** - Queue Management

This module provides a centralized queue management system:

**Key Class: `MusicQueueManager`**

| Method | Purpose |
| :--- | :--- |
| `add_to_queue()` | Adds a song request to a chat's queue. |
| `get_next_in_queue()` | Retrieves and removes the next song from the queue. |
| `is_queue_empty()` | Checks if a chat's queue is empty. |
| `get_queue_list()` | Returns a list of all songs in the queue. |
| `set_processing_status()` | Sets whether a song is currently being processed. |
| `is_currently_processing()` | Checks if a song is being processed. |

**Features:**
- Per-chat queue isolation (each group has its own queue).
- Thread-safe operations using a global instance.
- Simple and efficient queue operations using Python's `deque`.

## Data Flow

### Song Request Flow

1.  **User sends `/play [song name]`**
2.  **Handler validates input** and extracts the song query.
3.  **Queue Manager adds the song** to the chat's queue.
4.  **If no song is currently processing:**
    - Set processing status to `True`.
    - Call `process_next_song()`.
5.  **`process_next_song()` executes:**
    - Sends "Searching..." message.
    - Downloads the song using yt-dlp.
    - Sends "Uploading..." message.
    - Uploads the audio file to Telegram.
    - Cleans up temporary files.
    - Sets processing status to `False`.
    - Recursively calls itself to process the next song in the queue.
6.  **If the queue is empty,** the function exits gracefully.

### Queue State Diagram

```
User Request
    ↓
Is Queue Empty?
    ├─ Yes → Add to Queue → Is Processing? → No → Start Processing
    │                                        ↓
    │                                       Yes → Wait
    └─ No → Add to Queue → Wait for Current Song to Finish
```

## Configuration Best Practices

### Environment Variables

Create a `.env` file in the root directory:

```bash
# Required
BOT_TOKEN="123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh"
OWNER_ID="1234567890"

# Optional (with defaults)
API_ID="27829712"
API_HASH="fb590fb04369d740e742a0198aa66e0a"
BOT_NAME="🎵 My Music Bot"
PORT="8080"
```

### Security Considerations

*   Never hardcode sensitive credentials in the source code.
*   Use environment variables for all secrets.
*   For production, use a secrets management system (e.g., AWS Secrets Manager, HashiCorp Vault).
*   Regularly rotate API tokens and credentials.

## Logging

The bot uses Python's built-in `logging` module for structured logging:

```python
import logging
LOG = logging.getLogger(__name__)
```

**Log Levels:**
- `INFO`: General information (bot startup, song added to queue).
- `WARNING`: Potential issues (using default API credentials).
- `ERROR`: Error conditions (failed downloads, API errors).
- `DEBUG`: Detailed diagnostic information.

**Example Log Output:**
```
[2026-01-26 10:30:45,123 - INFO] - main - ✅ Health server running on port 8080
[2026-01-26 10:30:46,456 - INFO] - main - ✅ Bot Started: @VivekMusicBot
[2026-01-26 10:30:50,789 - INFO] - core.queue_manager - Added 'Tum Hi Ho' to queue for chat -1001234567890. Queue size: 1
```

## Deployment

### Render.com (Recommended)

1.  Fork the repository on GitHub.
2.  Go to [render.com](https://render.com) and sign in.
3.  Create a new Web Service and connect your GitHub repository.
4.  Set the following environment variables:
    - `BOT_TOKEN`
    - `OWNER_ID`
    - `API_ID` (optional)
    - `API_HASH` (optional)
5.  Deploy!

### Local Development

```bash
# Install dependencies
sudo pip3 install -r requirements.txt

# Run the bot
python3 main.py
```

## Future Enhancements

Potential improvements for future versions:

1.  **Database Integration:** Store user preferences, song history, and statistics.
2.  **Playlist Support:** Allow users to create and manage playlists.
3.  **Search Filtering:** Provide multiple search results and let users choose.
4.  **Rate Limiting:** Implement rate limiting to prevent abuse.
5.  **Admin Dashboard:** Web-based dashboard for bot management.
6.  **Internationalization:** Support for multiple languages.
7.  **Spotify Integration:** Download songs from Spotify playlists.
8.  **Caching:** Cache frequently requested songs to reduce download time.

## Troubleshooting

### Bot doesn't start

- Ensure `BOT_TOKEN` is set correctly.
- Check that all dependencies are installed: `sudo pip3 install -r requirements.txt`.
- Verify that port 8080 (or your configured port) is not in use.

### Songs not downloading

- Ensure `yt-dlp` is installed and up-to-date.
- Check that FFmpeg is installed on the system: `sudo apt-get install ffmpeg`.
- Verify that the song is available on YouTube.

### Queue not working in groups

- Ensure the bot has the necessary permissions in the group.
- Verify that the chat ID is being captured correctly.

## Contributing

To contribute to this project:

1.  Fork the repository.
2.  Create a new branch for your feature.
3.  Make your changes and commit them with clear messages.
4.  Push your changes and create a pull request.

---

*Advanced Version by Manus AI*
