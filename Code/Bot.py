# Imports
from discord import channel, colour
from discord.ext import commands
from pprint import pprint
import linecache
import discord
import aiohttp
import random
import json
import os

from discord.ext.commands.core import command

# API Url's
giphyURL = "http://api.giphy.com/v1/gifs/search"

# Command Initialization
bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# Test Case
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

# Giphy Implementation
giphyKey = linecache.getline('Fonzie-Bot\Authentication Keys\Authentication.txt', 17)
giphyKey.rstrip()

@bot.command(pass_context=True)
async def giphy(ctx, *, search):
    embed = discord.Embed(colour=discord.Colour.blue())
    session = aiohttp.ClientSession()

    # If the search is empty return a random gif
    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=' + 'IY7W2PRaObx8r8N5LJO4Y3zFGL3MgaBJ')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else: # If the search is not empty then implement it into the search url
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=' + 'IY7W2PRaObx8r8N5LJO4Y3zFGL3MgaBJ' + '&limit=10')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:  # skip bot messages
        return

    # write all possible words in lower case. 
    if message.content.lower() in ['wall']:
        await message.channel.send('https://cdn.discordapp.com/attachments/767899814402326559/854588332247744572/1596575456116-1.png')

    await bot.process_commands(message)  # to allow other commands

# Code to get token for bot
token = linecache.getline('Fonzie-Bot\Authentication Keys\Authentication.txt', 8)

# Clean up token so it has no trailing newline
token.rstrip()

bot.run(token)