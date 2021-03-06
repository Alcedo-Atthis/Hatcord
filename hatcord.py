import gettext
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from cogs import player, match, team, oauth, help

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='ht-', case_insensitive=True)
bot.remove_command('help')

bot.add_cog(player.PlayerCog(bot))
bot.add_cog(match.MatchCog(bot))
bot.add_cog(team.TeamCog(bot))
bot.add_cog(oauth.OauthCog(bot))
bot.add_cog(help.HelpCog(bot))


@bot.event
async def on_ready():
    """
    Print guilds to console when bot is operational
    """

    await bot.wait_until_ready()
    print(bot.user.name + " connected to guilds:")
    for guild in bot.guilds:
        print(guild.name)

    # Set bot status to 'Listening to !help'
    activity = discord.Activity(name='!help', type=discord.ActivityType.listening)
    await bot.change_presence(activity=activity)


@bot.event
async def on_message(message):
    # Disregard messages sent by the bot
    if message.author.id == bot.user.id:
        return
    # Process commands
    await bot.process_commands(message)


@bot.event
async def on_command(ctx):
    # TODO: logging
    # TODO: switch to user language, default to EN

    return


bot.run(TOKEN)
