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
        await ctx.send("Image Saved")
    except IndexError:
        print("Error: no attachments")
        await ctx.send("Error: no attachments")
    else:
        if url[0:26] == "https://cdn.discordapp.com":
            newDI = discordImage.DiscordImage(url)
            images.append(newDI)

@client.command()
async def range(ctx):
    await ctx.send("There are currently " + str(len(images)) + " added images")

@client.command("")
async def helper(ctx):
    helpStr = "Current Commands: \n"
    helpStr = helpStr + "$save (img): saves image to next index (starting at 1) \n"
    helpStr = helpStr + "$seeImage (index): displays image at index with it's assigned ratings \n"
    helpStr = helpStr + "$rate (index) (rater name) (rating out of 10): assigns rating to image in slot index \n"
    helpStr = helpStr + "$range : returns how many images have been added \n"
    await ctx.send("`" + helpStr + "`")

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
            ratings = currentImage.getRatings()
            await ctx.send("Current ratings for this image:")
            for x in ratings:
                await ctx.send(x)
        except IndexError:
            print("Error: invalid index")

@client.command()
async def rate(ctx, number, username, ratingVal):
    try:
        index = int(number) - 1
        currentImage = images[index]
        newRating = discordImage.Rating(username, int(ratingVal))
        currentImage.addRating(newRating)
        await ctx.send("Rating Added")
    except IndexError:
        print("Error: please enter a number")
        await ctx.send("Error: invalid index")








