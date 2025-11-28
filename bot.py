import discord
import config
import asyncio
from DiscordChatBridge import DiscordChatBridge

from commands.whitelist_cmds import WhitelistCommands
from commands.server_cmds import ServerCommands
from commands.setup_cmds import SetupCommands
from mc.chat import read_message_from_mc, send_message_to_mc

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

class McBot(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)
        self.chat_bridge = DiscordChatBridge(self)
        

    async def on_ready(self):
        print(f"Bot is ready. Logged in as {self.user}")
    
    async def setup_hook(self):
        WhitelistCommands(self)
        ServerCommands(self)
        SetupCommands(self)
        await self.chat_bridge.setup(config.CHAT_CHANNEL_ID)
        await self.tree.sync()
        asyncio.create_task(
            read_message_from_mc(config.MC_LOG_PATH, self.chat_bridge)
        )
        
    async def on_discord_message(self, message: discord.Message):
        if message.author.bot:
            return
        if message.channel.id == config.CHAT_CHANNEL_ID:
            await send_message_to_mc(message.author.display_name, message.content)
        
client = McBot(intents=intents)
client.run(config.DISCORD_BOT_TOKEN)