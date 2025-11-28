import discord

class DiscordChatBridge:
    def __init__(self, bot: discord.Client):
        self.bot = bot
        self.channel_id = None

    async def setup(self, channel_id: int):
        channel = self.bot.get_channel(channel_id)
        if channel:
            print(f"Channel found: {channel.name}, Type: {channel.type}")
        else:
            print("Channel not found.")
            return
        self.channel = channel
        if not self.channel:
            print("Chat channel with id not found.")
        
    async def send(self, username: str, message: str):
        if self.channel is None:
            await self.setup()
        if self.channel:
            await self.channel.send(f"**{username}**: {message}")