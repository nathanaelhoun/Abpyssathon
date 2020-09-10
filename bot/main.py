import os
from dotenv import load_dotenv
from abpyssathon import Abpyssathon as Abpyssathon
import PostgresqlManager

print("Loading environment variables... ", end="")
load_dotenv()
print("done !")

print("Connecting to database... ", end="")
try:
    db = PostgresqlManager.PostgresqlManager()
    db.connect(os.getenv("DATABASE_URL"))
    print("done !")
except Exception as e:
    print("Failed :(")
    print(e)
    exit(1)

client = Abpyssathon(command_prefix="&", db=db)

print("Loading extensions... ", end="")
client.load_extension("cogs.events")
client.load_extension("cogs.fun")
client.load_extension("cogs.score")
client.load_extension("cogs.utilities")
print("done !")

print("Ready to launch client... ", end="")
print("Running client")
try:
    client.run(os.getenv("BOT_TOKEN"))
finally:
    print("Disconnecting from database... ", end="")
    db.disconnect()
    print("done ! ")
    client.logout()