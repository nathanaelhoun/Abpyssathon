from discord.ext import commands
from strings import Strings as STR
from discord import Embed as DiscordEmbed
import math


class Score(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def score(self, ctx):
        """Manage scores for the members of the guild"""
        if ctx.invoked_subcommand is None:
            await ctx.send(STR.ERR_NO_SUBCOMMAND)

    @score.command()
    async def show(self, ctx):
        """Show the score of each member of the guild"""

        try:
            rows = self.bot.db.execute(
                """
                SELECT * 
                FROM score 
                WHERE sco_guild_id = {} 
                """.format(
                    ctx.guild.id
                )
            )

            if len(rows) == 0:
                await ctx.send(STR.SCORE_SHOW_NO_POINTS)
                return

            result_string = ""
            i = 0
            previous_value = 0
            for row in rows:
                # row[0] is guild id
                # row[1] is member id
                # row[2] is value
                member_name = ""
                for member in ctx.guild.members:
                    if member.id == row[1]:
                        member_name = member.display_name

                if member_name == "":
                    member_name = STR.SCORE_SHOW_MEMBER_HAS_LEFT

                if previous_value != row[2]:
                    previous_value = row[2]
                    i += 1

                result_string += "\n" + STR.SCORE_SHOW_RANKING_ITEM.format(
                    i, member_name, row[2]
                )

            embed = DiscordEmbed(
                title=STR.SCORE_SHOW_RANKING_INTRO,
                description="```\n{}\n```".format(result_string),
            )
            await ctx.send(STR.SCORE_SHOW_RANKING_INTRO, embed=embed)

        except Exception as e:
            print(e)

    async def modify_points(self, ctx, value: int):
        """Add or remove points to guild members in the database"""

        members = set()
        if len(ctx.message.mentions) == 0 and len(ctx.message.role_mentions) == 0:
            await ctx.send(STR.ERR_MISSING_REQUIRED_ARGUMENT)
            return

        for member in ctx.message.mentions:
            members.add(member)

        for role in ctx.message.role_mentions:
            for member in role.members:
                members.add(member)

        values_sql = ""
        members_name = ""
        for member in members:
            if members_name != "":
                values_sql += ", "
                members_name += ", "

            values_sql += "({}, {}, {})".format(ctx.guild.id, member.id, value)
            members_name += member.display_name

        sql = """
        INSERT INTO score VALUES
        {}
        ON CONFLICT (sco_guild_id, sco_member_id) 
        DO UPDATE SET sco_value = score.sco_value + EXCLUDED.sco_value;
        """.format(
            values_sql
        )

        try:
            self.bot.db.insert(sql)

            message = STR.SCORE_ADD_SUCCESSFULLY.format(
                value, members_name, ctx.author.display_name
            )
            if value < 0:
                message = STR.SCORE_REMOVE_SUCCESSFULLY.format(
                    -value, members_name, ctx.author.display_name
                )

            await ctx.send(message)
        except Exception as e:
            print(e)
            await ctx.send(STR.ERR_DATABASE)

    @score.command()
    async def add(self, ctx, quantity: str):
        """Add points to a guild members

        You can add points to several guild members or the members of a role by tagging them in the command
        """

        try:
            value = int(quantity)
        except Exception as e:
            await ctx.send(STR.SCORE_ADD_ERR_NAN)

        if value < 0:
            await ctx.send(STR.SCORE_ADD_ERR_NEGATIVE)
            return

        await self.modify_points(ctx, value)

    @score.command()
    async def remove(self, ctx, quantity: str):
        """Remove points to a guild members

        Works the same way as add functions
        """

        try:
            value = int(quantity)
        except Exception as e:
            await ctx.send(STR.SCORE_ADD_ERR_NAN)

        if value < 0:
            await ctx.send(STR.SCORE_ADD_ERR_NEGATIVE)
            return

        try:
            await self.modify_points(ctx, (-value))
            pass
        except Exception as e:
            print(e)


def setup(bot):
    bot.add_cog(Score(bot))
