import os
import asyncio
from sys import exit as sysExit
from psycopg2 import Error as psycopg2Error
from dotenv import load_dotenv
from discord import __version__ as discord_version_info

from postgresql_manager import PostgresqlManager
from abpyssathon import Abpyssathon

print("Running with discordpy " + discord_version_info)
print("Loading environment variables... ", end="")
load_dotenv()
print("done!")

print("Connecting to database... ", end="")
try:
    db = PostgresqlManager()
    db.connect(os.getenv("DATABASE_URL"))
    print("done!")
except psycopg2Error as err:
    print("Failed :(", err)
    sysExit(1)

client = Abpyssathon(command_prefix="&", database=db)

print("Loading extensions... ", end="")
client.load_extension("cogs.events")
client.load_extension("cogs.fun")
client.load_extension("cogs.score")
client.load_extension("cogs.utilities")
print("done!")

print("Ready to launch client. ", end="")
print("Running client...")

try:
    client.run(os.getenv("BOT_TOKEN"))
finally:
    print("\nLogging out client... ", end="")
    asyncio.run(client.logout())
    print("done! ")

    print("Disconnecting from database... ", end="")
    db.disconnect()
    print("done! ")

    print("Goodbye!")