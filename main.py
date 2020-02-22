import os
from dotenv import load_dotenv
from discord.ext import commands
import psycopg2

load_dotenv()

client = commands.Bot(command_prefix="&")

client.load_extension("cogs.events")
client.load_extension("cogs.fun")
client.load_extension("cogs.utilities")

db_connection = psycopg2.connect(os.getenv('DATABASE_URL'), sslmode='require')
db_cursor = db_connection.cursor()

client.run(os.getenv('BOT_TOKEN'))