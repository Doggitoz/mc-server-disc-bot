import discord
from mc import whitelist

class WhitelistCommands:
    def __init__(self, bot: discord.Client):
        self.bot = bot
        self.tree = bot.tree
        self.register()

    def register(self):
        @self.tree.command(name="whitelist_add", description="Add a player to the Minecraft whitelist")
        async def whitelist_add(interaction: discord.Interaction, username: str):
            try:
                response = whitelist.add_player(username)
                await interaction.response.send_message(f"✅ {response}")
            except Exception as e:
                await interaction.response.send_message(f"❌ Failed to add player to whitelist: {e}")
