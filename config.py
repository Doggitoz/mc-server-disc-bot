import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

MCRCON_HOST = os.getenv("MCRCON_HOST")
MCRCON_PORT = int(os.getenv("MCRCON_PORT"))
MCRCON_PASSWORD = os.getenv("MCRCON_PASSWORD")

ADMIN_IDS = {int(x.strip()) for x in os.getenv("ADMIN_DISCORD_IDS", "").split(",") if x.strip().isdigit()}

SERVER_SCRIPT_DIRECTORY = os.getenv("SERVER_SCRIPT_DIRECTORY")

CHAT_CHANNEL_ID = int(os.getenv("CHAT_CHANNEL_ID"))
MC_LOG_PATH = os.getenv("MC_LOG_PATH")