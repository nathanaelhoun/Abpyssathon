from discord.ext import commands
import discord
from strings import Strings as STR

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(STR.LAUNCH_SUCCESSFUL)
        print(STR.CONNECTION_SUCCESSFUL.format(self.bot.user))

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if isinstance(ctx.channel, discord.DMChannel) and not ctx.author.bot:
            await ctx.channel.send(STR.ERR_PRIVATE_CHANNEL)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send(STR.ERR_PRIVATE_CHANNEL)

        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(STR.ERR_BOT_MISSING_PERMISSIONS)

        if isinstance(error, commands.CommandNotFound):
            await ctx.send(STR.HELP)

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(STR.ERR_MISSING_REQUIRED_ARGUMENT)

        if (
            isinstance(error, commands.BadArgument)
            or isinstance(error, commands.ConversionError)
            or isinstance(error, commands.UnexpectedQuoteError)
            or isinstance(error, commands.ArgumentParsingError)
        ):
            await ctx.send(STR.ERR_BAD_ARGUMENTS)


def setup(bot):
    bot.add_cog(Events(bot))
