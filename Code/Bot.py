# Imports
# Discord
from asyncio import queues
from discord.ext.commands.core import command
from discord import activity, channel, colour, voice_client
from aiohttp.client import request
from discord.ext import commands, tasks
from discord.player import FFmpegPCMAudio
import requests
import discord

# Github
from github import Github

# Youtube
from youtubesearchpython.internal.constants import VideoDurationFilter
import youtubesearchpython as ytsearch
from pytube import YouTube
from bs4 import BeautifulSoup
from lxml import etree
import youtube_dl
import asyncio
import urllib
import sys

# Other
from multiprocessing import Process
from numpy import random as rand
from pprint import pprint
import linecache
import aiohttp
import asyncio
import logging
import random
import json
import time
import os


# API Url's
giphyURL = "http://api.giphy.com/v1/gifs/search"

# Command Initialization
intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=';', intents=intents)
logging.basicConfig(level=logging.INFO)

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
        
    if message.content.lower() in ['yes']:
        await message.channel.send('https://tenor.com/view/yes-chad-gif-18386674')
        
    if message.content.lower() in ['rage']:
        await message.channel.send('https://tenor.com/view/rage-dog-smash-keyboard-gaming-gif-21319862')
        
    if message.content.lower() in ['coom']:
        await message.channel.send('https://tenor.com/view/ketchup-mustard-condiments-squirt-weird-gif-16235402')
        
    if message.content.lower() in ['based', 'chad']:
        await message.channel.send('https://tenor.com/view/giga-chad-gigachad-big-gif-21053844')
        
    if message.content.lower() in ['iran']:
        await message.channel.send('https://cdn.discordapp.com/attachments/680928395399266314/767130121777709086/video0.mov')
        
    if message.content.lower() in ['monkey']:
        await message.channel.send('https://cdn.discordapp.com/attachments/650743322192773206/875122761129922580/video0.mp4')
        
    if message.content.lower() in ['tim', 'timothy']:
        start = 0
        end = 51
        randomNum = random.randint(start, end)
        option = {0 : 'https://cdn.discordapp.com/attachments/742954139805548614/882666000988897350/clown_car_meme.mp4',
                  1 : 'https://cdn.discordapp.com/attachments/508877167812149249/836266385763205130/176939772_976240653146457_2307467322338258938_n.mp4',
                  2 : 'https://cdn.discordapp.com/attachments/508877167812149249/836269804557172756/-_gta_5_car_drip.mp4',
                  3 : 'https://cdn.discordapp.com/attachments/508877167812149249/836273422815592528/DtBsZu4R5N26s6lH.mp4',
                  4 : 'https://cdn.discordapp.com/attachments/508877167812149249/836273495658463282/GTA_DRIP_CAR.mp4',
                  5 : 'https://cdn.discordapp.com/attachments/508877167812149249/836264156419325972/FNAF_car.mp4',
                  6 : 'https://cdn.discordapp.com/attachments/332532353668743169/837323278536278066/0CAxfx2BJmoY6uOi.mp4',
                  7 : 'https://cdn.discordapp.com/attachments/443859138754117643/837355428286824448/sarywapo_on_Instagram___Imaginate_ser_de_calama_y__1MP42.mp4',
                  8 : 'https://cdn.discordapp.com/attachments/448475898803519509/837374073419333652/Car_Drip_Skype.mp4',
                  9 : 'https://cdn.discordapp.com/attachments/448475898803519509/837374737202020453/Geometry_Dash_Car.mp4',
                  10 : 'https://cdn.discordapp.com/attachments/448475898803519509/837374761884713000/Angry_Birds_Car.mp4',
                  11 : 'https://cdn.discordapp.com/attachments/448475898803519509/837374781795467324/Bad_Piggys_Car.mp4',
                  12 : 'https://cdn.discordapp.com/attachments/448475898803519509/837374795669962763/Kahoot_Car.mp4',
                  13 : 'https://cdn.discordapp.com/attachments/448475898803519509/837466647891279922/snapchat_car.mp4',
                  14 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471644406251550/xbox_360_car_meme.mp4',
                  15 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471644674555914/Blackberry_Car.mp4',
                  16 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471646121197568/Garrys_Mod_Car.mp4',
                  17 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471650366357524/Roblox_Car.mp4',
                  18 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471650244591626/League_of_Legends_Car_drip.mp4',
                  19 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471651388981308/Wii_U_Car_Drip.mp4',
                  20 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471651314532402/postal_2_car_drip.mp4',
                  21 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471652311990322/numberblocks_car_drip.mp4',
                  22 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471653147181076/Forza_Italia_Car_Drip.mp4',
                  23 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471744599785512/America_Drip_Car.mp4',
                  24 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471745413611530/Minecraft_Car_Drip.mp4',
                  25 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471815458357278/6ed6e.mp4',
                  26 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471747800170567/Car_Drip_Big_Small.mp4',
                  27 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471748835770409/rsxstgwset.mp4',
                  28 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471751948468244/tedzhyszyh.mp4',
                  29 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471752245346314/Car_Drip_Facebook_Messenger.mp4',
                  30 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471753897771008/Car_Drip_Xiaomi.mp4',
                  31 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471757311934514/Car_Drip_Windows_Phone_Nokia.mp4',
                  32 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471808709328936/Car_Drip_Polish.mp4',
                  33 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471810979102791/Car_Drip_TMobile.mp4',
                  34 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471813536710666/Car_Drip_Polsat_TV.mp4',
                  35 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471813663195146/Car_Drip_Avast_Antivirus_Super_useless_fucking_antivirus.mp4',
                  36 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471813743017984/Car_Drip_Tango_Live_App.mp4',
                  37 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471816875638784/Car_Drip_Huawei.mp4',
                  38 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471818679451729/Reds_Among_Drip_Car_-_Drip_Car_Meme.mp4',
                  39 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471854221590558/undertale_car.mp4',
                  40 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471856033267752/Troll_face_car.mp4',
                  41 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471858927861790/kfc_car.mp4',
                  42 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471860147880006/clash_of_clans_car.mp4',
                  43 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471861486387253/home_depot_car.mp4',
                  44 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471863772938270/dsi_car.mp4',
                  45 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471865999458316/3ds_car.mp4',
                  46 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471907137847336/gamecube_car.mp4',
                  47 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471908634034186/nokia_car_meme.mp4',
                  48 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471911213924402/kitten.mp4',
                  49 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471912807890944/Apple_Car_Meme.mp4',
                  50 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471914385080323/twitter_car.mp4',
                  51 : 'https://cdn.discordapp.com/attachments/448475898803519509/837471915147788299/telegram_car_meme.mp4'}
        await message.channel.send(option[randomNum])
        
    if message.content.lower() in ['who']:
        await message.channel.send('cares')
    
    if message.content.lower() in ['rat']:
        await message.channel.send('https://tenor.com/view/rats-gif-19501976')
        
    if message.content.lower() in ['sonic']:
        await message.channel.send('https://cdn.discordapp.com/attachments/653101016014651399/881002933641170964/video0-1200.mp4')
        
    if message.content.lower() in ['credit score']:
        await message.channel.send('https://cdn.discordapp.com/attachments/630596126344609793/877522790138392587/video0.mp4')
        
    if message.content.lower() in ['stupid bot']:
        await message.channel.send('no you')
    
    if message.content.lower() in ['floppa']:
        await message.channel.send('https://cdn.discordapp.com/attachments/874447411144171610/882110009306124319/video0.mp4')
    
    if message.content.lower() in ['bloodborne']:
        await message.channel.send('https://cdn.discordapp.com/attachments/883288801781379122/883339438183284766/1630672781909.png')
        
    if message.content.lower() in ['goodnight', 'gn']:
        await message.channel.send('https://cdn.discordapp.com/attachments/586797838458028034/855737692334850068/Snapchat-1984710211.jpg')
        
    if message.content.lower() in ['queen']:
        await message.channel.send('https://cdn.discordapp.com/attachments/446468958309318656/828797976268636180/image0-44.png https://cdn.discordapp.com/attachments/446468958309318656/828797976691736617/image1-3.png https://cdn.discordapp.com/attachments/446468958309318656/828797976914296872/image2-2.png https://cdn.discordapp.com/attachments/446468958309318656/828797977094127636/image3-1.png')
        
    if message.content.lower() in ['weed']:
        await message.channel.send('https://cdn.discordapp.com/attachments/628658329899499563/825228862198644758/eeeTHALLISc4ra1_1275649121454624768480P_1.mp4')

    if message.content.lower() in ['no']:
        await message.channel.send('https://cdn.discordapp.com/attachments/506863443165577217/651565046404612116/1575351380698.png')
        
    if message.content.lower() in ['social credit']:
        await message.channel.send('ATTENTION CITIZEN. THIS IS THE MINISTRY OF STATE SECURITY. \n' +
                                   'YOUR INTERNET ACTIVITY HAS ATTRACTED OUR ATTENTION. \n' +
                                   'DUE TO YOUR INTERNET CRIMES YOU WILL BE BROUGHT DOWN TO -70 SOCIAL CREDIT SCORE. (-70)\n' + 
                                   'DO NOT DO THIS AGAIN. \n' +
                                   'GLORY TO THE CHINESE COMMUNIST PARTY.\n' +
                                   'https://cdn.discordapp.com/attachments/802281935308849192/868053509545791498/CCP.mp4')

    await bot.process_commands(message)  # to allow other commands
    

# Giphy Implementation ----------------------------------------------------------------------------------------------------------------------------
giphyKey = linecache.getline('/DiscordBot/Fonzie-Bot/AuthenticationKeys/Authentication.txt', 17).rstrip()

@bot.command(pass_context=True)
async def giphy(ctx, *, search):
    embed = discord.Embed(colour=discord.Colour.blue())
    session = aiohttp.ClientSession()

    # If the search is empty return a random gif
    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=' + giphyKey)
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else: # If the search is not empty then implement it into the search url
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=' + giphyKey + '&limit=10')
        data = json.loads(await response.text())
        print(data)
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
        random.seed(user.id)
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
githubAPIToken = linecache.getline('/DiscordBot/Fonzie-Bot/AuthenticationKeys/Authentication.txt', 20).rstrip()
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

# TODO: Music Player -------------------------------------------------------------------------------------------------------------------------------
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0', # bind to ipv4 since ipv6 addresses cause issues sometimes
    'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
}

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

songQueue = []

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')
    
@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()
    
@bot.command(name='leave', help='Command to make the bot leave teh voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send('Fonzie currently isnt in a voice channel')

@bot.command(name='play', help='This will play or queue a new song')
async def play(ctx, *, url):
    server = ctx.message.guild
    voice_channel = server.voice_client
    channel = ctx.message.author.voice.channel
    
    if voice_channel and voice_channel.is_connected():
        pass
    else:
        voice_channel = await channel.connect()
        await ctx.send('Successfully joined `{}`'.format(channel))
    
    def search(query):
        with ytdl:
            try:
                request.get(query)
            except:
                info = ytdl.extract_info('ytsearch: {}'.format(query), download=False)['entries'][0]
            else:
                info = ytdl.extract_info(query, download=False)
        return (info, info['formats'][0]['url'])
    
    await ctx.send('Searching for: {} :mag_right:'.format(url))
    
    video, source = search(url)
    voice_channel.play(FFmpegPCMAudio(source, **ffmpeg_options), after=lambda e: print('done', e))
    voice_channel.is_playing()
    await ctx.send('Playing: :notes: `{}` - Now!'.format(url))
    
@bot.command(name='pause', help='This command pauses teh song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.pause():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything you big goober.")

@bot.command(name='resume', help='Resumes the current song.')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot wasnt playing anything, you should try to use the play command num nutz.")
        
@bot.command(name='stop', help='Stops the currently playing song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot wasn't playing anything.")

# TODO: Youtube API --------------------------------------------------------------------------------------------------------------------------------
# @bot.command()
# async def searchvideo(ctx, keyword):
#     videosSearch = ytsearch.VideosSearch('NoCopyrightSounds', limit = 2)
#     print(videosSearch.result())
#     await ctx.send('https://www.youtube.com/watch?v={}'.format(videosSearch.result['id']))
#     
# def fetch_titles(url):
#     video_titles = []
#     html = requests.get(url)
#     soup = BeautifulSoup(html.text, "html5lib")
#     # print(soup.find_all('script'))
#     counter = 0
#     for scripts in soup.find_all('script'):
#         counter += 1
#         if counter == 33:
#             testString = str(scripts.text)
#             print(testString.find("videoId"))
#             # jsonFile = json.loads(scripts)
#             # print(jsonFile)
#             #for titles in jsonFile.find_all('text'):
#                 #print(titles)
#             #print(jsonFile["responseContext"]["contents"]["twoColumnBrowseResultsRenderer"]["tabs"]["tabRenderer"]["endpoint"]["content"]["sectionListRenderer"]["contents"]["sectionListRenderer"]["contents"]["itemSectionRenderer"]["contents"]["gridRenderer"]["videoId"])
#     
#     # # What the fuck even is this, trying to parse youtube data I ripped is a nightmare
#     # print("beginning")
#     # for ytInitialData in soup.find_all("ytInitialData"):
#     #     print("pretest")
#     #     for responseContext in soup.find_all("responseContext"):
#     #         print("test")
#     #         for contents in soup.find_all("contents"):
#     #             print("test1")
#     #             for twoColumnBrowseResultsRenderer in soup.find_all("twoColumnBrowseResultsRenderer"):
#     #                 print("test2")
#     #                 for tabs in soup.find_all("tabs"):
#     #                     print("test3")
#     #                     for tabRenderer in soup.find_all("tabRenderer"):
#     #                         print("test4")
#     #                         for endpoint in soup.find_all("endpoint"):
#     #                             print("test5")
#     #                             for content in soup.find_all("content"):
#     #                                 print("test6")
#     #                                 for sectionListRenderer in soup.find_all("sectionListRenderer"):
#     #                                     print("test7")
#     #                                     for contents in soup.find_all("contents"):
#     #                                         print("test8")
#     #                                         for itemSectionRenderer in soup.find_all("itemSectionRenderer"):
#     #                                             print("test9")
#     #                                             for contents in soup.find_all("contents"):
#     #                                                 print("test10")
#     #                                                 for gridRenderer in soup.find_all("gridRenderer"):
#     #                                                     print("test11")
#     #                                                     for videoId in soup.find_all("videoId"):
#     #                                                         print(videoId)
# 
#     for entry in soup.find_all("videoId"):
#         for link in entry.find_all("videoId"):
#             youtube = etree.HTML(urllib.request.urlopen(link["href"]).read()) 
#             video_title = youtube.xpath("//span[@id='eow-title']/@title") 
#             if len(video_title) > 0:
#                 video_titles.append({"title":video_title[0], "url":link.attrs["href"]})
#     return video_titles

# Joke Commands -----------------------------------------------------------------------------------------------------------------------------------

#Credit: Whoever AustinJacob Stole this from (modified by me)
@bot.command()
async def penis(ctx, *users: discord.Member):
    dongs = {}
    msg = ""
    state = random.getstate()

    for user in users:
        random.seed(user.id)
        if user.id == 245063782924156929:
            dongs[user] = "8{}D".format("=" * 40)
        else:
            dongs[user] = "8{}D".format("=" * random.randint(0, 30))

    random.setstate(state)
    dongs = sorted(dongs.items(), key=lambda x: x[1])

    for user, dong in dongs:
        msg += "**{}'s size:**\n{}\n".format(user.display_name, dong)
    await ctx.send(msg)

# Code to get token for bot -----------------------------------------------------------------------------------------------------------------------
def launch():
    token = linecache.getline('/DiscordBot/Fonzie-Bot/AuthenticationKeys/Authentication.txt', 8).rstrip()
    bot.run(token)