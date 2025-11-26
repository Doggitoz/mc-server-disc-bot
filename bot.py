import discord
import config
from commands.whitelist_cmds import WhitelistCommands
from commands.server_cmds import ServerCommands

class McBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)
        
    async def setup_hook(self):
        WhitelistCommands(self)
        ServerCommands(self)
        await self.tree.sync()
        
client = McBot()
client.run(config.DISCORD_BOT_TOKEN)