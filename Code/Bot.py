# Imports
from aiohttp.client import request
from discord import channel, colour
from discord.ext import commands
from pprint import pprint
from github import Github
from numpy import random as rand
import random
import linecache
import requests
import discord
import aiohttp
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

# Sandbox -----------------------------------------------------------------------------------------------------------------------------------------
@bot.command()
async def test(ctx, user: discord.Member, arg2):
    if arg2:
        await ctx.send(user.mention + ' ' + arg2)
    else:
        await ctx.send('You dumbass, this command requires two arguments')


# Random meme responses ---------------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_message(message):
    if message.author == bot.user:  # skip bot messages
        return

    # write all possible words in lower case. 
    if message.content.lower() in ['wall']:
        await message.channel.send('https://cdn.discordapp.com/attachments/767899814402326559/854588332247744572/1596575456116-1.png')
        
    if message.content.lower() in ['bradley']:
        await message.channel.send('https://cdn.discordapp.com/attachments/630596126344609793/854344671279054908/VID_20200622_191526_839.mp4')
        
    if message.content.lower() in ['rekt']:
        await message.channel.send('https://cdn.discordapp.com/attachments/630596126344609793/854004996801298433/iqlr99et24571.jpg')
        
    if message.content.lower() in ['response to kai']:
        await message.channel.send('https://tenor.com/view/cry-about-it-cat-hoverboard-cat-on-hoverboard-cry-gif-21748938')

    await bot.process_commands(message)  # to allow other commands
    

# Giphy Implementation ----------------------------------------------------------------------------------------------------------------------------
giphyKey = linecache.getline('Fonzie-Bot\Authentication Keys\Authentication.txt', 17).rstrip()

@bot.command(pass_context=True)
async def giphy(ctx, *, search):
    embed = discord.Embed(colour=discord.Colour.blue())
    session = aiohttp.ClientSession()

    # If the search is empty return a random gif
    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=' + giphyKey)
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    elif search != '': # If the search is not empty then implement it into the search url
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=' + giphyKey + '&limit=10')
        data = json.loads(await response.text())
        gif_choice = rand.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()
    await ctx.send(embed=embed)


# Detector ----------------------------------------------------------------------------------------------------------------------------------------
detectorAnswers = ['ITS OFF THE SCALE!!!', 'Its getting a bit sus my guy.', 'None Detected.']

@bot.command()
async def detect(ctx, user: discord.Member, arg):
    randNum = rand.randint(3)
    if user:
        if randNum == 0:
            # await ctx.send("hello, {}".format(user.mention))
            await ctx.send('{}\'s {}: {}'.format(user.mention, arg, detectorAnswers[0]))
        elif randNum == 1:
            # await ctx.send("goodbye, {}".format(user.mention))
            await ctx.send('{}\'s {}: {}'.format(user.mention, arg, detectorAnswers[1]))
        elif randNum == 2:
            # await ctx.send("goodbye, {}".format(user.mention))
            await ctx.send('{}\'s {}: {}'.format(user.mention, arg, detectorAnswers[2]))
    else:
        await ctx.send('You have to mention someone numnutz')
    

# GitHub API --------------------------------------------------------------------------------------------------------------------------------------
githubAPIToken = linecache.getline('Fonzie-Bot\Authentication Keys\Authentication.txt', 20).rstrip()
github = Github(githubAPIToken)

@bot.command()
async def botstatus(ctx):
    await ctx.send("https://github.com/Shrewkin/Fonzie-Bot/commit/main")

@bot.command()
async def git(ctx, keyword):
    for repo in github.search_repositories(keyword):
        await ctx.send('I found a repo that matches your keyword: https://github.com/{}'.format(repo.full_name))
        break
    
@bot.command()
async def gituser(ctx, keyword):
    url = 'https://api.github.com/users/{}'.format(keyword)
    urlData = requests.get(url).json()
    if ('html_url' not in urlData):
        await ctx.send('Github has no record of the username ' + keyword)
    else:
        await ctx.send('{}'.format(urlData['html_url']))


# Joke Commands -----------------------------------------------------------------------------------------------------------------------------------

#Credit: AustinJacob
@bot.command()
async def penis(ctx, *users: discord.Member):
    dongs = {}
    msg = ""
    state = random.getstate()

    for user in users:
        random.seed(user.id)
        dongs[user] = "8{}D".format("=" * random.randint(0, 30))

    random.setstate(state)
    dongs = sorted(dongs.items(), key=lambda x: x[1])

    for user, dong in dongs:
        msg += "**{}'s size:**\n{}\n".format(user.display_name, dong)
    await ctx.send(msg)

# Code to get token for bot -----------------------------------------------------------------------------------------------------------------------
token = linecache.getline('Fonzie-Bot\Authentication Keys\Authentication.txt', 8).rstrip()

bot.run(token)