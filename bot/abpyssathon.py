import psycopg2
from discord.ext import commands
from discord import Intents
from strings import Strings as STR

intents = Intents(messages=True, guilds=True, members=True)


class Abpyssathon(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            command_prefix=kwargs.pop("command_prefix"),
            intents=intents,
        )

        self.db = kwargs.pop("db")
