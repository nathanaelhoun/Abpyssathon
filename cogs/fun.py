from discord.ext import commands
from strings import *
from strings import Strings as STR
import discord


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Answer pong to ping"""

        await ctx.send(STR.PING)

    @commands.command()
    async def activity(self, ctx, *, newActivity: str):
        """Set a new activity for the bot"""

        # TODO : Check if admin
        game = discord.Game(newActivity)
        await self.bot.change_presence(status=discord.Status.online, activity=game)

    @commands.group()
    async def score(self, ctx):
        if ctx.invoked_subcommand is None:
            await bot.send(STR.ERR_NO_SUBCOMMAND)

    @score.command()
    async def show(self, ctx, categories: str):
        """Show the score of each member of the server"""

        # TODO
        pass

    @score.command()
    async def add(self, ctx, quantity: str, category: str):
        """Add points to a server member"""

        # TODO
        pass


def setup(bot):
    bot.add_cog(Fun(bot))
