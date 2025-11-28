import discord
import config

global admin_commands_enabled
admin_commands_enabled = True

def toggle_admin_commands(enabled: bool):
    global admin_commands_enabled
    admin_commands_enabled = enabled

def is_admin(interaction: discord.Interaction) -> bool:
    if (not admin_commands_enabled):
        return False
    return interaction.user.id in config.ADMIN_IDS