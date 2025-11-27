from mc.rcon_client import RconClient

from mc.log_parser import follow_log
import re
import DiscordChatBridge

CHAT_REGEX = re.compile(
    r"<(?P<name>\w+)> (?P<msg>.+)"
)

async def send_message_to_mc(name: str,message: str):
    try:
        with RconClient() as rcon:
            rcon.command(f"say {name}: {message}")
    except Exception as e:
        print(f"Failed to send message: {e}")
        
async def read_message_from_mc(log_path, chat_bridge: DiscordChatBridge):
    async for line in follow_log(log_path):
        match = CHAT_REGEX.search(line)
        if not match:
            return None
        username = match.group("name")
        message = match.group("msg")
        await chat_bridge.send(username, message)