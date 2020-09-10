import psycopg2
from discord.ext import commands
from strings import Strings as STR


class Abpyssathon(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=kwargs.pop("command_prefix"))

        self.db = kwargs.pop("db")
