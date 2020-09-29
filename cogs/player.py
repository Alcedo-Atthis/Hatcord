from discord.ext import commands


class PlayerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def youthplayer(self, ctx, youth_player_id: int):
        await ctx.send(content='Test')

    @commands.command()
    async def player(self, ctx, player_id: int):
        await ctx.send(content='Test')
