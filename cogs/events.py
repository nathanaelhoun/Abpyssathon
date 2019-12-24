from discord.ext import commands
import discord

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Je suis vivant !')
        print('Connecté en tant que {0.bot.user}'.format(self))

    # Does not work : activate infinite number of time when a message is sent. Don't know why 
    # @commands.Cog.listener()
    # async def on_message(self, ctx):
    #     if isinstance(ctx.channel, discord.DMChannel):
    #         await ctx.channel.send(":x: Désolé, mais je n'accepte pas les commandes depuis les messages privés ! Contacte-moi sur un serveur :wink:")

def setup(bot):
    bot.add_cog(Events(bot))