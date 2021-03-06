from discord.ext import commands
import discord

from strings import Strings as STR


class Fun(commands.Cog):
    """Fun and general commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Answer pong to ping"""

        await ctx.send(STR.PING)

    @commands.command()
    async def ping2(self, ctx: commands.Context):
        """Answer pong to ping and tag the best user of Discord (Medhi)"""

        await ctx.send(STR.PING2)

    @commands.command()
    async def activity(self, ctx: commands.Context, new_activity: str):
        """Set a new activity for the bot"""

        game = discord.Game(new_activity)
        await self.bot.change_presence(status=discord.Status.online, activity=game)
        await ctx.send(STR.ACTIVITY_NEW.format(new_activity, ctx.message.author))

        sql = """
        INSERT INTO system VALUES
        ('activity', %s)
        ON CONFLICT (key) 
        DO UPDATE SET value = EXCLUDED.value;
        """
        self.bot.database.insert(sql, (new_activity,))


def setup(bot):
    """Add this class to the bot"""

    bot.add_cog(Fun(bot))
