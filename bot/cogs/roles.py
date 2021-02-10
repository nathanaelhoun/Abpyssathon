from discord.ext import commands
import discord
from discord.errors import Forbidden, HTTPException, InvalidArgument

from strings import Strings as STR
from methods import parse_mentions


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
            await ctx.send(STR.CREATEROLE_ERR_EXISTING.format(role.mention))
            return

        try:
            role = await ctx.guild.create_role(
                name=role_name,
                mentionable=True,
                hoist=True,
                colour=discord.Colour.random(),
            )
        except Forbidden as err:
            await ctx.send(STR.CREATEROLE_ERR_PERMISSION)
            print(err)
        except HTTPException as err:
            await ctx.send(STR.CREATEROLE_ERR_HTTP)
            print(err)
        except InvalidArgument as err:
            await ctx.send(STR.CREATEROLE_INVALID_ARG)
            print(err)
        except err:
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
            await ctx.send(STR.CREATEROLE_ERR_PERMISSION)
            print(err)
        except HTTPException as err:
            await ctx.send(STR.CREATEROLE_ERR_HTTP)
            print(err)
        except err:
            print(err)

        await ctx.send(
            STR.CREATEROLE_SUCCESS.format(
                role.mention, ctx.author.display_name, ", ".join(member_names)
            )
        )

        if len(member_names) != len(members):
            await ctx.send(STR.CREATEROLE_ERR_ADDED)


def setup(bot):
    """Add this class to the bot"""
    bot.add_cog(Roles(bot))
