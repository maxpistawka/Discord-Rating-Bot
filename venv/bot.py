import discord


from discord.ext import commands
import uuid
import requests
import shutil
import tokenAbstractor

import discordImage
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)
images = []


def run_discord_bot():


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!!')



    client.run(str(tokenAbstractor.getKey()))

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send('hey')
    if message.content.startswith("tony is"):
        await message.channel.send('a bit of a beast')
    else:
        await client.process_commands(message)


@client.command()
async def save(ctx):
    try:
        url = ctx.message.attachments[0].url
    except IndexError:
        print("Error: no attachments")
        await ctx.send("Error: no attachments")
    else:
        if url[0:26] == "https://cdn.discordapp.com":
            newDI = discordImage.DiscordImage(url)
            images.append(newDI)

@client.command()
async def range(ctx):
    await ctx.send("There are currently" + len(images) + "added images")

@client.command()
async def seeImage(ctx, arg):
    try:
        index = int(arg) - 1
    except ValueError:
        print("Error: please enter a number")
        await ctx.send("Error: invalid number")
    else:
        try:
            currentImage = images[index]
            await ctx.send(currentImage.getURL())
            await ctx.send(currentImage.getRatings())
        except IndexError:
            print("Error: invalid index")







