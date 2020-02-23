from discord.ext import commands
from strings import Strings as STR
import math


class Score(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def score(self, ctx):
        if ctx.invoked_subcommand is None:
            await bot.send(STR.ERR_NO_SUBCOMMAND)

    @score.command()
    async def show(self, ctx):
        """Show the score of each member of the guild"""

        category = 1  # categories are not implemented yet

        try:
            rows = self.bot.db.execute(
                "SELECT * FROM score WHERE sco_guild_id = {} AND sco_category_id = {}".format(
                    ctx.guild.id, category
                )
            )

            if len(rows) == 0:
                await ctx.send(STR.SCORE_SHOW_NO_POINTS)
                return

            result_string = ""
            i = 0
            for row in rows:
                i += 1
                # row[0] is guild id
                # row[1] is member id
                # row[2] is category id
                # row[3] is value
                member_name = ""
                for member in ctx.guild.members:
                    if member.id == row[1]:
                        member_name = member.display_name

                if member_name == "":
                    member_name = STR.SCORE_SHOW_MEMBER_HAS_LEFT

                result_string += "\n" + STR.SCORE_SHOW_RANKING_ITEM.format(
                    i, member_name, row[3]
                )

            await ctx.send(STR.SCORE_SHOW_RANKING_INTRO + "```" + result_string + "```")

        except Exception as e:
            print(e)

    async def modify_points(self, ctx, value: int, category):
        """Add or remove points to guild members in the database"""

        # TODO implement categories (search for the id with the name in the db and output an error if the id doesn't exist)

        members = set()
        if len(ctx.message.mentions) == 0 and len(ctx.message.role_mentions) == 0:
            await ctx.send(STR.ERR_MISSING_REQUIRED_ARGUMENT)
            return

        for member in ctx.message.mentions:
            members.add(member)

        for role in ctx.message.role_mentions:
            for member in role.members:
                members.add(member)

        sql = """INSERT INTO score VALUES """
        members_name = ""
        for member in members:
            if members_name != "":
                sql += ", "
                members_name += ", "

            sql += "({},{},{},{})".format(ctx.guild.id, member.id, category, value)
            members_name += member.display_name

        sql += """
            ON CONFLICT (sco_guild_id, sco_member_id, sco_category_id) 
            DO UPDATE SET sco_value = score.sco_value + EXCLUDED.sco_value;"""

        try:
            self.bot.db.insert(sql)
            await ctx.send(
                STR.SCORE_ADD_SUCCESSFULLY.format(
                    value, members_name, ctx.author.display_name
                )
            )
        except Exception as e:
            print(e)
            await ctx.send(STR.SCORE_ERR_DATABASE)

    @score.command()
    async def add(self, ctx, quantity: str):  # , category: str):
        """Add points to a guild members
        
        You can add points to several guild members or the members of a role by tagging them in the command
        """

        category = 1  # TODO categories are not implemented yet

        try:
            value = int(quantity)
        except Exception as e:
            await ctx.send(STR.SCORE_ADD_ERR_NAN)

        if value < 0:
            await ctx.send(STR.SCORE_ADD_ERR_NEGATIVE)
            return

        await self.modify_points(ctx, value, category)

    @score.command()
    async def remove(self, ctx, quantity: str):  # , category: str):
        """Remove points to a guild members
        
        Works the same way as add functions
        """

        category = 1  # TODO categories are not implemented yet

        try:
            value = int(quantity)
        except Exception as e:
            await ctx.send(STR.SCORE_ADD_ERR_NAN)

        if value < 0:
            await ctx.send(STR.SCORE_ADD_ERR_NEGATIVE)
            return
        try:
            await self.modify_points(ctx, (-value), category)
            pass
        except Exception as e:
            print(e)


def setup(bot):
    bot.add_cog(Score(bot))
