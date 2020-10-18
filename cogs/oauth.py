import gettext
import discord
from discord.ext import commands
from discord.ext.commands import Bot

localedir = 'locales'
_ = gettext.gettext

class OauthCog(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx):
        # TODO: logging

        user_lang = 'fi'
        # TODO: user_lang = getUserLanguage(ctx.member.id)
        lang = gettext.translation('oauth', localedir, fallback=False, languages=[user_lang])
        global _
        lang.install()
        _ = lang.gettext


        return

    @commands.command(name='auth', hidden=True)
    async def auth(self, ctx):
        """
        Authorize bot to access Hattrick data

        This command gives user the authorization link where they find a verifier

        :param ctx:
        """
        global _
        # TODO: log new user auth
        # author_id = ctx.author.id
        # resources = oauth.initiate()
        # if resources is None:
        #     embed_error = discord.Embed(color=0xff0000,
        #                                 description=_('Authorization failed'))
        #     await log("Authorization failed for user: " + str(ctx.author), color=0xff0000)
        #     await ctx.author.send(embed=embed_error)
        #     return
        #
        # await sqlite_utils.write_keys(author_id, resources[0], resources[1], username=str(ctx.author))

        embed_auth = discord.Embed(title="👉  {}  👈"
                                   .format(_('Click here and sign in with your Hattrick credentials')),
                                   url='https://www.hattrick.org/', description=
                                   _("Finalize authorization by typing `!verify <auth token>`,"
                                     " for example `!verify 1234567890`"))

        await ctx.author.send(embed=embed_auth)

    # @commands.command(name='verify', hidden=True)
    # async def verify(ctx, verifier):
    #     """
    #     :param ctx:
    #
    #     :param verifier: The "pin" user gets when loggin in with their Hattrick credentials to the auth page
    #     """
    #
    #     verifier = verifier.strip('<>')
    #
    #     keys = await sqlite_utils.get_keys(ctx.author.id)
    #     resources = oauth.verify(keys[0], keys[1], verifier)
    #
    #     if resources is None:
    #         embed_error = discord.Embed(color=0xff0000,
    #                                     description=
    #                                     'Valtuutus epäonnistui! Varmista, että kirjoitit vahvistuskoodin oikein')
    #         await log("Verification failed for user: " + str(ctx.author), color=0xff0000)
    #         await ctx.author.send(embed=embed_error)
    #         return
    #
    #     await sqlite_utils.write_keys(ctx.author.id, resources[0], resources[1], username=str(ctx.author))
    #
    #     data = await init_command(ctx, 'teamdetails', {"version": 3.4})
    #     await sqlite_utils.write_user_info(ctx.author.id, data.get('HattrickData').get('User'))
    #
    #     await help_me(ctx)
    #
    #     await log("New verified user: " + str(ctx.author))
