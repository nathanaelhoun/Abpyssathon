from discord.ext import commands
from discord import Embed as DiscordEmbed
from psycopg2 import Error as psycopg2Error

from strings import Strings as STR
from strings import Pluralizer
from methods import parse_mentions


class Score(commands.Cog):
    """Count and store in the database the score of members of each Guild"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def score(self, ctx: commands.Context):
        """Manage scores for the members of the guild"""

        if ctx.invoked_subcommand is None:
            await ctx.send(STR.ERR_NO_SUBCOMMAND)

    @score.command()
    async def show(self, ctx: commands.Context):
        """Show the score of each member of the guild"""

        try:
            rows = self.bot.database.execute(
                """
                SELECT *
                FROM score
                WHERE sco_guild_id = {}
                ORDER BY sco_value DESC
                """.format(
                    ctx.guild.id
                )
            )

            if len(rows) == 0:
                await ctx.send(STR.SCORE_SHOW_NO_POINTS)
                return

            result_string = ""
            i = 0
            rank = 0
            previous_value = 0
            for row in rows:
                i += 1
                # guild_id = row[0]
                member_id = row[1]
                value = row[2]

                member_name = ""
                for member in ctx.guild.members:
                    if member.id == member_id:
                        member_name = member.display_name

                if member_name == "":
                    member_name = STR.SCORE_SHOW_MEMBER_HAS_LEFT

                if previous_value != value:
                    previous_value = value
                    rank = i

                result_string += "\n" + STR.SCORE_SHOW_RANKING_ITEM.format(
                    rank, member_name, Pluralizer(value)
                )

            embed = DiscordEmbed(
                title=STR.SCORE_SHOW_RANKING_INTRO,
                description="```\n{}\n```".format(result_string),
            )
            await ctx.send(STR.SCORE_SHOW_RANKING_INTRO, embed=embed)

        except psycopg2Error as err:
            print(err)
            await ctx.send(STR.ERR_DATABASE)

    async def modify_points(self, ctx: commands.Context, value: int):
        """Add or remove points to guild members in the database"""

        members = parse_mentions(ctx.message)
        if len(members) == 0:
            await ctx.send(STR.ERR_MISSING_REQUIRED_ARGUMENT)
            return

        sql = """
        INSERT INTO score VALUES
        """
        data_sql = []
        members_name = ""

        for member in members:
            if members_name != "":
                sql += ", "
                members_name += ", "

            sql += "(%s, %s, %s) "
            data_sql.append(ctx.guild.id)
            data_sql.append(member.id)
            data_sql.append(value)
            members_name += member.display_name

        sql += """
        ON CONFLICT (sco_guild_id, sco_member_id) 
        DO UPDATE SET sco_value = score.sco_value + EXCLUDED.sco_value;
        """

        try:
            self.bot.database.insert(sql, data_sql)

            message = STR.SCORE_ADD_SUCCESSFULLY.format(
                Pluralizer(value), members_name, ctx.author.display_name
            )
            if value < 0:
                message = STR.SCORE_REMOVE_SUCCESSFULLY.format(
                    Pluralizer(-value), members_name, ctx.author.display_name
                )

            await ctx.send(message)

        except psycopg2Error as err:
            print(err)
            await ctx.send(STR.ERR_DATABASE)

    @score.command()
    async def add(
        self, ctx: commands.Context, quantity: str, mentions: str
    ):  # pylint: disable=unused-argument
        """Add points to a guild members

        You can add points to several guild members or the members of a role
        by tagging them in the command
        """
        # mentions argument is used to the &help generation

        try:
            value = int(quantity)
        except ValueError:
            await ctx.send(STR.SCORE_ADD_ERR_NAN)
            return

        if value < 0:
            await ctx.send(STR.SCORE_ADD_ERR_NEGATIVE)
            return

        await self.modify_points(ctx, value)

    @score.command()
    async def remove(self, ctx: commands.Context, quantity: str):
        """Remove points to a guild members

        Works the same way as add function
        """

        try:
            value = int(quantity)
        except ValueError:
            await ctx.send(STR.SCORE_ADD_ERR_NAN)
            return

        if value < 0:
            await ctx.send(STR.SCORE_ADD_ERR_NEGATIVE)
            return

        await self.modify_points(ctx, (-value))


def setup(bot):
    """Add this class to the bot"""
    bot.add_cog(Score(bot))
