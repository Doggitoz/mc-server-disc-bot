import discord
from mc import whitelist
import re

class WhitelistCommands:
    def __init__(self, bot: discord.Client):
        self.bot = bot
        self.tree = bot.tree
        self.register()

    def register(self):
        @self.tree.command(name="whitelist_add", description="Add a player to the Minecraft whitelist")
        async def whitelist_add(interaction: discord.Interaction, username: str):
            # Check if the username is valid
            if not re.match(r'^[a-zA-Z0-9_-]+$', username) and len(username) > 16:
                await interaction.response.send_message("❌ Invalid username.")
                return
            try:
                whitelist.add_player(username)
                await interaction.response.send_message(f"✅ User '{username}' added to whitelist.")
            except Exception as e:
                await interaction.response.send_message(f"❌ Failed to add player to whitelist: {e}")
