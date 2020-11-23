from discord.ext import commands
import discord

from strings import Strings as STR


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Answer pong to ping"""

        await ctx.send(STR.PING)

    @commands.command()
    async def ping2(self, ctx: commands.Context):
        """Answer pong to ping and tag the best user of the server (Medhi)"""

        await ctx.send(STR.PING2)

    @commands.command()
    async def activity(self, ctx: commands.Context, newActivity: str):
        """Set a new activity for the bot"""

        # TODO : Check if admin
        game = discord.Game(newActivity)
        await self.bot.change_presence(status=discord.Status.online, activity=game)
        await ctx.send(STR.ACTIVITY_NEW.format(newActivity, ctx.message.author))


def setup(bot):
    bot.add_cog(Fun(bot))
