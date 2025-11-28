import discord
from discord import app_commands
import config
from utils import is_admin, toggle_admin_commands

class SetupCommands:
    def __init__(self, bot: discord.Client):
        self.bot = bot
        self.tree = bot.tree
        self.register()
        
    def register(self):
        @self.tree.command(name="check_admin", description="Check if you are an admin.")
        async def check_admin(interaction: discord.Interaction):
            if interaction.user.id in config.ADMIN_IDS:
                await interaction.response.send_message("✅ You are an admin.", ephemeral=True)
            else:
                await interaction.response.send_message("❌ You are not an admin.", ephemeral=True)
                
        @self.tree.command(name="enable_admin_commands", description="Enable admin commands for bot.")
        @app_commands.check(is_admin)
        async def enable_admin_commands(interaction: discord.Interaction):
            toggle_admin_commands(True)
            await interaction.response.send_message("✅ Admin commands enabled.", ephemeral=True)
            
        @self.tree.command(name="disable_admin_commands", description="Disable admin commands for bot.")
        @app_commands.check(is_admin)
        async def disable_admin_commands(interaction: discord.Interaction):
            toggle_admin_commands(False)
            await interaction.response.send_message("✅ Admin commands disabled.", ephemeral=True)