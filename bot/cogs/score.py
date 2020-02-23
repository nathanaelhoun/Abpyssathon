from discord.ext import commands
from strings import Strings as STR


class Score(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def score(self, ctx):
        if ctx.invoked_subcommand is None:
            await bot.send(STR.ERR_NO_SUBCOMMAND)

    @score.command()
    async def show(self, ctx, categories: str):
        """Show the score of each member of the server"""
        try:
            rows = self.bot.db.select("*", "homework", "", "")
            for row in rows:
                print(row)
        except Exception as e:
            print(e)

        # TODO
        pass

    @score.command()
    async def add(self, ctx, quantity: str, category: str):
        """Add points to a server member"""

        # TODO
        pass


def setup(bot):
    bot.add_cog(Score(bot))
