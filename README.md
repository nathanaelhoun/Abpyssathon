# Abpyssathon

A Discordbot for my class group, written in Python with [discordpy](https://discordpy.readthedocs.io/en/latest/).

> **Warning**
> Abpyssathon was living in Heroku, and since they [stopped their free plan in November 2022](https://help.heroku.com/RSBRUH58/removal-of-heroku-free-product-plans-faq), near the end of our cursus, we decided that is was time for Abpyssathon to retire after 4 years of loyal service. Goodbye, dear friend.

# Features

- 🏆 Count the points for all members and output a ranking. A point equals to an absence during one lesson
- 🎲 Pick a random member, he/she will have to do _this_ task no one wants to do
- 🎲 Make random teams with the members of a discord role, to gain time for our class projects
- 🏷️ Create roles in the guild (because we create a lot of roles)
- 🏓 Last but not least, answers "Pong" to "&ping" (plus a special Medhi version with `&ping2`)

See all commands with the `&help` bot command.

# Deployment

If you wish to use my bot, you can email me ([see my profile](https://github.com/nathanaelhoun)).
Otherwise you can deploy it by yourself:

1. Clone the repository

   ```bash
   $ git clone https://github.com/nathanaelhoun/Abpyssathon
   $ cd Abpyssathon
   ```

2. Create a `.env` file with these tokens:

   ```
   BOT_TOKEN=<bot-token-here>
   DATABASE_URL=postgres://<full-postgresql-database-url-here>
   ```

3. Create the database tables with the script `database_creation.sql` in a postgresql database

4. Then launch the bot

   ```bash
   $ python3 bot/main.py
   ```

# Contributing

## Install dependencies

- Python3

  ```bash
  $ sudo apt install python3 python3-pip virtual-env
  # or
  $ sudo pacman -S python python-pip python-virtualenv
  ```

- Python requirements ([discordpy](discordpy.readthedocs.io/) and [psycopg2](https://pypi.org/project/psycopg2/))
  ```bash
  $ pip install -r requirements.txt
  ```

## Configure and launch the bot

See [deployment instructions](#deployment)
