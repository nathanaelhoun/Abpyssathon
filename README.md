# Abpyssathon

A Discordbot written in Python.

# Features

(list is coming...)

# Installation and deploying

TODO

# Contributing

## Dependencies

- Python3

```bash
sudo apt install python3 python3-pip virtual-env
```

- discord.py
- Psycopg2 for the database connection

```bash
python3 -m pip install -U discord.py python-dotenv
python3 -m pip install psycopg2-binary
```

## Configure

Create a `.env` file with these tokens:

```
BOT_TOKEN=<bot-token-here>
DATABASE_URL=postgres://<full-postgresql-database-url-here>
```

## Launch the bot

```bash
python3 bot/main.py
```