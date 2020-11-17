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

- Python requirements
```bash
pip install -r requirements.txt
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