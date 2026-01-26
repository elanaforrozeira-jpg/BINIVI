# 🎵 BINIVI - Advanced Music Bot

This is the advanced version of the BINIVI Telegram Music Bot, built on \`pyrogram\` and \`yt-dlp\`.

## ✨ Advanced Features

*   **Modular Architecture:** The codebase has been refactored into a modular structure (\`handlers/\`, \`core/\`) for better maintainability and scalability.
*   **Music Queue System:** Implemented a robust queue system for group chats, allowing multiple song requests to be processed sequentially.
    *   \`/play [song name]\` - Adds the song to the queue.
    *   \`/queue\` - Shows the current list of songs in the queue.
    *   \`/skip\` - Allows group admins to skip the currently playing song.
*   **Improved Configuration:** Enhanced configuration to strictly use environment variables for sensitive credentials (\`API_ID\`, \`API_HASH\`, \`BOT_TOKEN\`).
*   **Structured Logging:** Integrated Python's \`logging\` module for better error tracking and monitoring.

## 🚀 Quick Start

### 1. Setup

1.  **Clone the repository:**
    \`\`\`bash
    git clone https://github.com/elanaforrozeira-jpg/BINIVI.git
    cd BINIVI
    \`\`\`

2.  **Install dependencies:**
    \`\`\`bash
    sudo pip3 install -r requirements.txt
    \`\`\`

3.  **Configuration:**
    Create a \`.env\` file in the root directory and fill in your credentials.

    \`\`\`
    # Get from @BotFather
    BOT_TOKEN="YOUR_BOT_TOKEN"

    # Your Telegram ID (get from @userinfobot)
    OWNER_ID="YOUR_OWNER_ID"

    # Get from my.telegram.org
    API_ID="YOUR_API_ID"
    API_HASH="YOUR_API_HASH"

    # Optional
    BOT_NAME="My Advanced Music Bot"
    PORT=8080
    \`\`\`

### 2. Run the Bot

Run the main file:

\`\`\`bash
python3 main.py
\`\`\`

## 📚 Commands

| Command | Description | Usage |
| :--- | :--- | :--- |
| \`/start\` | Starts the bot and shows the welcome message. | Private & Group |
| \`/help\` | Shows the list of available commands. | Private & Group |
| \`/play\` | Downloads and plays the requested song. Adds to queue in groups. | Private & Group |
| \`/song\` | Alias for \`/play\`. | Private & Group |
| \`/queue\` | Shows the list of songs currently in the queue. | Group |
| \`/skip\` | Skips the currently playing song. | Group (Admin Only) |
| \`/ping\` | Checks the bot's response time and status. | Private & Group |
| \`/id\` | Gets your user ID and chat ID. | Private & Group |

---
*Advanced Version by Manus AI*
