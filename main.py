from dotenv import load_dotenv
load_dotenv()
import os

from discord.ext import commands

client = commands.Bot(command_prefix='&')

client.load_extension("cogs.events")
client.load_extension("cogs.fun")
client.load_extension("cogs.utilities")

client.run(os.getenv('BOT_TOKEN'))