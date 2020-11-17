from discord.ext import commands
from datetime import datetime
import os
import discord
import random
from strings import Strings as STR


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def archivechat(self, ctx):
        """Archive a channel into a .txt file"""

        message = ctx.message
        log_file = "output-{0.id}.txt".format(message)

        async with ctx.channel.typing():
            try:
                with open(log_file, "w", encoding="UTF-8") as file:
                    print(
                        STR.ARCHIVE_BEGIN.format(
                            message.channel.name, message.guild.name
                        )
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
                        except:
                            author = "invalid"
                        content = msg.clean_content
                        try:
                            attachment = "[Attachment : {0.attachments[0].url}]".format(
                                msg
                            )
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

                filename = STR.ARCHIVE_SEND_FILENAME.format(
                    message.channel.name, message.guild.name
                )

                try:
                    discord_file = discord.File(log_file, filename)
                except Exception:
                    message.author.send(
                        STR.ARCHIVE_ERR_ATTACHMENT.format(message.channel.name)
                    )
                    return

                try:
                    await message.author.send(
                        content=STR.ARCHIVE_SEND_SUCCESSFUL.format(
                            message.channel.name, message.guild.name
                        ),
                        file=discord_file,
                    )
                    await ctx.send(
                        STR.ARCHIVE_SUCESSFULLY_SENT.format(ctx.author.mention)
                    )
                except:
                    await message.author.send(STR.ARCHIVE_ERR_SENDING)
            except:
                await message.author.send(STR.ARCHIVE_ERR)

        os.remove(log_file)

    # Command group -----------------------------------------------------------
    # Randomize team or picking someone
    @commands.group()
    async def random(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(STR.ERR_NO_SUBCOMMAND)

    @random.command()
    async def teams(self, ctx, numberPerTeam: int, role: discord.Role):
        """Randomize teams with the members of a discordrole"""

        if numberPerTeam < 2:
            await ctx.send(STR.RANDOM_ERR_WRONG_NUMBER_IN_TEAM.format(numberPerTeam))
            return

        members_to_pick = role.members.copy()
        teams = list()

        while len(members_to_pick) > 0:
            new_team = list()
            while len(new_team) < numberPerTeam and len(members_to_pick) > 0:
                new_team.append(
                    members_to_pick.pop(random.randrange(len(members_to_pick)))
                )

            teams.append(new_team)

        embed = discord.Embed()

        team_number = 0
        for team in teams:
            team_number = team_number + 1
            team_string = ""
            for member in team:
                team_string += "\n"
                team_string += STR.RANDOM_TEAMS_MEMBER_LABEL.format(member.display_name)

            embed.add_field(
                name=STR.RANDOM_TEAMS_TEAM_LABEL.format(team_number),
                value=team_string,
            )

        await ctx.send(
            STR.RANDOM_TEAMS_PERFECT.format(numberPerTeam, role.mention), embed=embed
        )

    @random.command()
    async def pickone(self, ctx, role: discord.Role):
        """Pick randomly a member of a role"""

        chosen_member = role.members[random.randrange(len(role.members))]
        await ctx.send(STR.RANDOM_PICKONE_SUCCESS.format(chosen_member.mention))


def setup(bot):
    bot.add_cog(Utilities(bot))
