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

def setup(bot):
    bot.add_cog(Events(bot))