from discord.ext import commands
import discord
from discord.errors import Forbidden, HTTPException, InvalidArgument

from strings import Pluralizer, Strings as STR
from utils import parse_mentions


class Roles(commands.Cog):
    """Manage the roles for the current guild"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def roles(self, ctx: commands.Context):
        """Manage roles for this guild"""

        if ctx.invoked_subcommand is None:
            await ctx.send(STR.ERR_NO_SUBCOMMAND)

    @roles.command()
    async def add(
        self, ctx: commands.Context, role_name: str, mentions: str
    ):  # pylint: disable=unused-argument
        """Create a role in the current guild and add it to the given people"""
        # mentions argument is used to the &help generation

        members = parse_mentions(ctx.message)
        if len(members) == 0:
            await ctx.send(STR.ERR_MISSING_REQUIRED_ARGUMENT)
            return

        role = discord.utils.get(ctx.message.author.guild.roles, name=role_name)
        if role is not None:
            await ctx.send(STR.ROLE_CREATE_ERR_EXISTING.format(role.mention))
            return

        try:
            role = await ctx.guild.create_role(
                name=role_name,
                mentionable=True,
                hoist=True,
                colour=discord.Colour.random(),
            )
        except Forbidden as err:
            await ctx.send(STR.ROLE_CREATE_ERR_PERMISSION)
            print(err)
        except HTTPException as err:
            await ctx.send(STR.ROLE_CREATE_ERR_HTTP)
            print(err)
        except InvalidArgument as err:
            await ctx.send(STR.ROLE_CREATE_INVALID_ARG)
            print(err)

        if role is None:
            return

        # The role has been created
        member_names = []
        try:
            for member in members:
                await member.add_roles(role, atomic=True)
                member_names.append(member.display_name)
        except Forbidden as err:
            await ctx.send(STR.ROLE_CREATE_ERR_PERMISSION)
            print(err)
        except HTTPException as err:
            await ctx.send(STR.ROLE_CREATE_ERR_HTTP)
            print(err)

        await ctx.send(
            STR.ROLE_CREATE_SUCCESS.format(
                role.mention, ctx.author.display_name, ", ".join(member_names)
            )
        )

        if len(member_names) != len(members):
            await ctx.send(STR.ROLE_CREATE_ERR_ADDED)

    @roles.command()
    async def show(self, ctx: commands.Context):
        """Show the number of roles of each member of the guild"""

        members = sorted(ctx.guild.members, key=lambda x: len(x.roles), reverse=True)

        description = STR.ROLE_SHOW_INTRO
        for member in members:
            unique_roles_nb = sum(len(r.members) == 1 for r in member.roles)

            description += (
                STR.ROLE_SHOW_ITEM.format(
                    member.display_name,
                    len(member.roles) - 1,
                    unique_roles_nb,
                )
                + "\n"
            )

        embed = discord.Embed(
            description="```\n" + description + "\n```",
        )

        await ctx.send(
            STR.ROLE_SHOW_TEXT.format(Pluralizer(len(ctx.guild.roles))),
            embed=embed,
        )


def setup(bot):
    """Add this class to the bot"""
    bot.add_cog(Roles(bot))
