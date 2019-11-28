from dotenv import load_dotenv
load_dotenv()
from datetime import datetime
import os

import discord
# from discord.ext import commands

client = discord.Client()

async def recordchat(message):
    log_file = "output-{0.id}.txt".format(message)

    try:
        with open(log_file, 'w', encoding="UTF-8") as file: 
                print("--- Archive beginning of channel {0.channel.name} (guild : {0.guild.name})".format(message))
                
                file.write("Guild : {0.guild.name}\n".format(message))
                file.write("Channel : #{0.channel.name}\n".format(message))
                file.write("Archive created on {}\n".format(datetime.now().strftime("%Y/%m/%d, %H:%M:%S")))
                
                async for msg in message.channel.history(limit=1000000000):
                    time_string = msg.created_at.strftime("%Y-%m-%d %H:%M")                
                    try:
                        author = msg.author
                    except:
                        author = 'invalid'
                    content = msg.clean_content
                    try:
                        attachment = '[Attachment : {0.attachments[0].url}]'.format(msg)
                    except IndexError:
                        attachment = ''
                    
                    template = '[{time_str}] <{author}> {content} {attachment}\n'
                    file.write(template.format(time_str=time_string, author=author, content=content, attachment=attachment))

                file.write("Archive ended\n")
                print("--- Archive completed of #{0.channel.name} (guild : {0.guild.name})".format(message))

        content = ":ok: Archive du channel #{0.channel.name}".format(message)
        filename = "Archive-channel-{0.channel.name}.txt".format(message)
        discord_file = discord.File(log_file, filename)
        try:
            await message.author.send(content=content, file=discord_file)
            print('Archive of #{0.channel.name} (guild : {0.guild.name}) send to {0.author}'.format(message))
        except:
            await message.author.send("Impossible d'envoyer l'archive :sob:")
            print('ERROR : Archive of #{message.channel.name} (guild : {message.guild.name}) not sent to {message.author}')

    except:
        await message.author.send("Impossible de créer l'archive :sob:")
        print('ERROR : impossible to archive #{message.channel.name} (guild : {message.guild.name}) asked by {message.author}')

    os.remove(log_file)

@client.event
async def on_ready():
    print('Je suis vivant !')
    print('Connecté en tant que {0.user}'.format(client))


@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        await message.author.send(":x: Désolé, mais je n'accepte pas les commandes depuis les messages privés ! Contacte-moi sur un serveur :wink:")
        return

    if message.author == client.user:
        return

    if message.content.lower().startswith('ping'):
        await message.channel.send('Pong ! :ping_pong:')
        return

    if message.content.startswith('&'):
        content = str.split(message.content, ' ')
        command = str.lower(content.pop(0).strip('&'))
        
        subcommands = []
        arguments = []

        for word in content:
            if(word.startswith('&')):
                subcommands.append(str.lower(word.strip('&')))
            else:
                arguments.append(str.lower(word))

        if (command == 'recordchat'):
            await recordchat(message)

client.run(os.getenv('BOT_TOKEN'))