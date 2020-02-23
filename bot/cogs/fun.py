from discord.ext import commands
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
    async def activity(self, ctx, newActivity: str):
        """Set a new activity for the bot"""

        # TODO : Check if admin
        game = discord.Game(newActivity)
        await self.bot.change_presence(status=discord.Status.online, activity=game)


def setup(bot):
    bot.add_cog(Fun(bot))
