import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

MCRCON_HOST = os.getenv("MCRCON_HOST")
MCRCON_PORT = int(os.getenv("MCRCON_PORT"))
MCRCON_PASSWORD = os.getenv("MCRCON_PASSWORD")

raw_admins = os.getenv("ADMIN_DISCORD_IDS", "")
ADMIN_IDS = {int(x.strip()) for x in raw_admins.split(",") if x.strip().isdigit()}

SERVER_SCRIPT_DIRECTORY = os.getenv("SERVER_SCRIPT_DIRECTORY")