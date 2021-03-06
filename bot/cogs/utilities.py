from datetime import datetime
import os
import random
import discord
from discord.ext import commands
from discord.errors import Forbidden, HTTPException, InvalidArgument

from strings import Strings as STR
from strings import Pluralizer
from utils import parse_mentions


class Utilities(commands.Cog):
    """Utility bot commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def archivechat(self, ctx: commands.Context):
        """Archive a channel into a .txt file and sends it to the user in a DM"""

        message = ctx.message
        log_file = "output-{0.id}.txt".format(message)

        async with ctx.channel.typing():
            with open(log_file, "w", encoding="UTF-8") as file:
                print(
                    STR.ARCHIVE_BEGIN.format(message.channel.name, message.guild.name)
                )
                await ctx.send(STR.ARCHIVE_NOTIF_BEGIN)

                file.write(
                    STR.ARCHIVE_FILE_HEADER.format(
                        message.guild.name,
                        message.channel.name,
                        datetime.now().strftime("%Y/%m/%d, %H:%M:%S"),
                    )
                )

                async for msg in message.channel.history(limit=1000000000):
                    time_string = msg.created_at.strftime("%Y-%m-%d %H:%M")
                    try:
                        author = msg.author
                    except NameError:
                        author = "invalid"

                    content = msg.clean_content
                    try:
                        attachment = "[Attachment : {0.attachments[0].url}]".format(msg)
                    except IndexError:
                        attachment = ""

                    template = "[{time_str}] <{author}> {content} {attachment}\n"
                    file.write(
                        template.format(
                            time_str=time_string,
                            author=author,
                            content=content,
                            attachment=attachment,
                        )
                    )

                file.write(STR.ARCHIVE_FILE_FOOTER)
                print(
                    STR.ARCHIVE_COMPLETED.format(
                        message.channel.name, message.guild.name
                    )
                )

            filename = STR.ARCHIVE_FILENAME.format(
                message.channel.name, message.guild.name
            )

            discord_file = discord.File(log_file, filename)
            try:
                await message.author.send(
                    content=STR.ARCHIVE_MESSAGE.format(
                        message.channel.name, message.guild.name
                    ),
                    file=discord_file,
                )
                await ctx.send(STR.ARCHIVE_SUCCESS.format(ctx.author.mention))
            except (Forbidden, HTTPException, InvalidArgument):
                await message.author.send(STR.ARCHIVE_ERR_SENDING)

        os.remove(log_file)

    # Command group -----------------------------------------------------------
    # Randomize team or picking someone
    @commands.group()
    async def random(self, ctx: commands.Context):
        """Choose a random member or randomize teams"""
        if ctx.invoked_subcommand is None:
            await ctx.send(STR.ERR_NO_SUBCOMMAND)

    @random.command()
    async def teams(self, ctx: commands.Context, number_per_team: int, mentions: str):
        """Randomize teams with the mentionned users or roles"""
        # mentions argument is used to the &help generation

        if number_per_team < 2:
            await ctx.send(
                STR.RANDOM_ERR_WRONG_NB_PER_TEAM.format(Pluralizer(number_per_team))
            )
            return

        members_to_pick = parse_mentions(ctx.message)
        if len(members_to_pick) == 0:
            await ctx.send(STR.ERR_MISSING_REQUIRED_ARGUMENT)
            return

        teams = list()

        while len(members_to_pick) > 0:
            new_team = list()
            while len(new_team) < number_per_team and len(members_to_pick) > 0:
                chosen_member = random.sample(members_to_pick, 1)[0]
                members_to_pick.remove(chosen_member)
                new_team.append(chosen_member)

            teams.append(new_team)

        embed = discord.Embed()

        for i, team in enumerate(teams):
            embed.add_field(
                name=STR.RANDOM_TEAMS_TEAM_LABEL.format(i + 1),
                value="\n".join(
                    STR.RANDOM_TEAMS_MEMBER_LABEL.format(m.display_name) for m in team
                ),
            )

        mentions = " ".join(
            u.mention for u in ctx.message.mentions + ctx.message.role_mentions
        )

        await ctx.send(
            STR.RANDOM_TEAMS_PERFECT.format(
                number_per_team,
                mentions,
            ),
            embed=embed,
        )

    @random.command()
    async def pickone(self, ctx: commands.Context):
        """Pick randomly a member in a list of mentions"""

        members = parse_mentions(ctx.message)
        if len(members) == 0:
            await ctx.send(STR.ERR_MISSING_REQUIRED_ARGUMENT)
            return

        chosen_member = random.sample(members, 1)[0]
        await ctx.send(STR.RANDOM_PICKONE_SUCCESS.format(chosen_member.mention))


def setup(bot):
    """Add this class to the bot"""
    bot.add_cog(Utilities(bot))
