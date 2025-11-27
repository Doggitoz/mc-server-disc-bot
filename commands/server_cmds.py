import discord
from discord import app_commands
from mc import server

from config import ADMIN_IDS

def is_admin(interaction: discord.Interaction) -> bool:
    return interaction.user.id in ADMIN_IDS

class ServerCommands:
    def __init__(self, bot: discord.Client):
        self.bot = bot
        self.tree = bot.tree
        self.register()

    def register(self):
        @self.tree.command(name="status", description="Get the server status, TPS, and player list.")
        async def status(interaction: discord.Interaction):
            try:
                info = server.general_status()
                await interaction.response.send_message(f"```\n{info}\n```")
            except Exception as e:
                await interaction.response.send_message(f"❌ Failed to get server status: {e}")

        @self.tree.command(name="start", description="Start the Minecraft server.")
        async def start(interaction: discord.Interaction):
            try:
                msg = server.start_server()
                await interaction.response.send_message(msg)
            except Exception as e:
                await interaction.response.send_message(f"❌ Failed to start server or server is already running: {e}")

        # @self.tree.command(name="stop", description="Stop the Minecraft server.")
        # @app_commands.check(is_admin)
        # async def stop(interaction: discord.Interaction):
        #     try:
        #         msg = server.stop_server()
        #         await interaction.response.send_message(msg)
        #     except Exception as e:
        #         await interaction.response.send_message(f"❌ Failed to stop server: {e}")

        # @self.tree.command(name="restart", description="Restart the Minecraft server.")
        # @app_commands.check(is_admin)
        # async def restart(interaction: discord.Interaction):
        #     try:
        #         stop_msg = server.stop_server()
        #         start_msg = server.start_server()
        #         await interaction.response.send_message(f"{stop_msg}\n{start_msg}")
        #     except Exception as e:
        #         await interaction.response.send_message(f"❌ Failed to restart server: {e}")

        async def check_error(interaction, error):
            if isinstance(error, app_commands.CheckFailure):
                await interaction.response.send_message("❌ You are not authorized.", ephemeral=True)

        start.error = check_error
        # stop.error = check_error
        # restart.error = check_error
