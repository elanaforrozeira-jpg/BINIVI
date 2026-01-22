# VIVEK MUSIC - Setup Guide

## Configuration Documentation

This guide explains exactly where to put your API keys and tokens to set up VIVEK MUSIC bot.

### Required Configuration Variables

#### 1. BOT_TOKEN
**What it is:** Your Telegram bot token  
**How to get it:** 
1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` command
3. Follow the prompts to create your bot
4. Copy the token provided

**Where to put it:**
- **Option 1:** In `config.py` file at **line 13**
  ```python
  BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
  ```
- **Option 2:** Set as environment variable `BOT_TOKEN`

---

#### 2. API_ID & API_HASH
**What it is:** Your Telegram API credentials  
**How to get it:**
1. Visit [my.telegram.org/apps](https://my.telegram.org/apps)
2. Log in with your phone number
3. Create a new application
4. Copy the `api_id` and `api_hash`

**Where to put it:**
- **Option 1:** In `config.py` file at **lines 10-11**
  ```python
  API_ID = 12345678
  API_HASH = "abcdef1234567890abcdef1234567890"
  ```
- **Option 2:** Set as environment variables `API_ID` and `API_HASH`

---

#### 3. MONGO_DB_URI
**What it is:** MongoDB database connection string  
**How to get it:**
1. Visit [cloud.mongodb.com](https://cloud.mongodb.com)
2. Sign up or log in
3. Create a new cluster (free tier available)
4. Click "Connect" -> "Connect your application"
5. Copy the connection string
6. Replace `<password>` with your database password

**Where to put it:**
- **Option 1:** In `config.py` file at **line 16**
  ```python
  MONGO_DB_URI = "mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
  ```
- **Option 2:** Set as environment variable `MONGO_DB_URI`

---

#### 4. STRING_SESSION
**What it is:** Pyrogram session string for the assistant account  
**How to get it:**
1. Message [@StringSessionBot](https://t.me/StringSessionBot) on Telegram
2. Send `/start` command
3. Select "Pyrogram v2"
4. Enter your phone number, OTP, and 2FA password (if enabled)
5. Copy the session string provided

**Where to put it:**
- **Option 1:** In `config.py` file at **line 86**
  ```python
  STRING1 = "BQAabcdef..."  # Your long session string
  ```
- **Option 2:** Set as environment variable `STRING_SESSION`

**Note:** You can add up to 5 assistant accounts using STRING1, STRING2, STRING3, STRING4, STRING5

---

#### 5. OWNER_ID
**What it is:** Your Telegram user ID  
**How to get it:**
1. Message [@userinfobot](https://t.me/userinfobot) on Telegram
2. It will reply with your user ID

**Where to put it:**
- **Option 1:** In `config.py` file at **line 25**
  ```python
  OWNER_ID = 123456789
  ```
- **Option 2:** Set as environment variable `OWNER_ID`

---

#### 6. LOGGER_ID
**What it is:** Group ID where bot will send logs  
**How to get it:**
1. Create a new Telegram group
2. Add your bot to the group
3. Add [@MissRose_bot](https://t.me/MissRose_bot) to the group
4. Send `/id` command
5. Copy the group ID (starts with -100...)

**Where to put it:**
- **Option 1:** In `config.py` file at **line 21**
  ```python
  LOGGER_ID = -1001234567890
  ```
- **Option 2:** Set as environment variable `LOGGER_ID`

**Important:** Make sure your bot is admin in the logger group!

---

### Optional Configuration

#### Support Channel & Chat Links
Edit these in `config.py` at lines 42-43:
```python
SUPPORT_CHANNEL = "https://t.me/YourChannel"
SUPPORT_CHAT = "https://t.me/YourGroup"
```

#### Image URLs
Edit image URLs in `config.py` starting from line 115:
```python
START_IMG_URL = "https://te.legra.ph/file/your-image.jpg"
PING_IMG_URL = "https://te.legra.ph/file/your-image.jpg"
# ... and more
```

---

### Quick Setup Checklist

- [ ] Get BOT_TOKEN from @BotFather
- [ ] Get API_ID and API_HASH from my.telegram.org/apps
- [ ] Get MONGO_DB_URI from cloud.mongodb.com
- [ ] Get STRING_SESSION from @StringSessionBot
- [ ] Get your OWNER_ID from @userinfobot
- [ ] Create a logger group and get LOGGER_ID
- [ ] Add all values to config.py or set as environment variables
- [ ] Make bot admin in logger group
- [ ] Run the bot!

---

### Environment Variables (for Heroku/VPS)

If deploying on Heroku or VPS, you can set these as environment variables instead of editing config.py:

```bash
export BOT_TOKEN="your_bot_token"
export API_ID="your_api_id"
export API_HASH="your_api_hash"
export MONGO_DB_URI="your_mongo_uri"
export STRING_SESSION="your_session_string"
export OWNER_ID="your_user_id"
export LOGGER_ID="your_logger_group_id"
```

---

## Need Help?

If you encounter any issues:
1. Double-check all your credentials are correct
2. Ensure LOGGER_ID starts with -100 (supergroup ID)
3. Make sure bot is admin in logger group
4. Contact support at [@VivekMusicSupport](https://t.me/VivekMusicSupport)

---

**Powered by VIVEK MUSIC**
