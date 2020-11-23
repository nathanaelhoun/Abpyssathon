from discord.ext import commands
from discord import Intents

intents = Intents(messages=True, guilds=True, members=True)


class Abpyssathon(commands.Bot):
    """An instance of a discordbot, with the database connection"""

    def __init__(self, **kwargs):
        super().__init__(
            command_prefix=kwargs.pop("command_prefix"),
            intents=intents,
        )

        self.database = kwargs.pop("database")
