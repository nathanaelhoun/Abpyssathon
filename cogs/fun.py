from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        '''Answer pong to ping'''
        await ctx.send('Pong ! :ping_pong:')


def setup(bot):
    bot.add_cog(Fun(bot))