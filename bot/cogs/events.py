from discord.ext import commands
import discord

from strings import Strings as STR


class Events(commands.Cog):
    """Define the actions ran on events, especially for common errors"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Restore bot activity"""

        print("I'm alive! Connected as {}.".format(self.bot.user))

        print("Restoring bot activity... ", end="")
        rows = self.bot.database.execute(
            """
            SELECT value
            FROM system
            WHERE key = 'activity';
            """
        )

        if len(rows) == 0:
            print("No bot activity found.")
        else:
            game = discord.Game(rows[0][0])
            await self.bot.change_presence(status=discord.Status.online, activity=game)
            print("Restored '{}'.".format(rows[0][0]))

    @commands.Cog.listener()
    async def on_message(self, ctx: commands.Context):
        """Check that we are not in a DM Channel"""
        if isinstance(ctx.channel, discord.DMChannel) and not ctx.author.bot:
            await ctx.channel.send(STR.ERR_PRIVATE_CHANNEL)

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        """Send a message when a common command error is detected"""

        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send(STR.ERR_PRIVATE_CHANNEL)

        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(STR.ERR_BOT_MISSING_PERMISSIONS)

        if isinstance(error, commands.CommandNotFound):
            await ctx.send(STR.ERR_NO_COMMAND)

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(STR.ERR_MISSING_REQUIRED_ARGUMENT)

        if isinstance(
            error,
            (
                commands.BadArgument,
                commands.ConversionError,
                commands.UnexpectedQuoteError,
                commands.ArgumentParsingError,
            ),
        ):
            await ctx.send(STR.ERR_BAD_ARGUMENTS)


def setup(bot):
    """Add this class to the bot"""
    bot.add_cog(Events(bot))
