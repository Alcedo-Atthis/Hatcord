from discord.ext import commands


class OauthCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
