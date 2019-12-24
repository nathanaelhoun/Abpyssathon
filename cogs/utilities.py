from discord.ext import commands
from datetime import datetime
import os
import discord

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def recordchat(self, ctx):
        '''Record all the chat into a .txt file'''
        message = ctx.message
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
            try:
                discord_file = discord.File(log_file, filename)
            except Exception:
                print("ERROR : Impossible d'attacher le fichier")
            try:
                await message.author.send(content=content, file=discord_file)
                print('Archive of #{0.channel.name} (guild : {0.guild.name}) send to {0.author}'.format(message))
            except:
                await message.author.send("Impossible d'envoyer l'archive :sob:")
                print('ERROR : Archive of #{0.channel.name} (guild : {0.guild.name}) not sent to {0.author}'.format(message))

        except:
            await message.author.send("Impossible de créer l'archive :sob:")
            print('ERROR : impossible to archive #{0.channel.name} (guild : {0.guild.name}) asked by {0.author}'.format(message))

        os.remove(log_file)

def setup(bot):
    bot.add_cog(Utilities(bot))