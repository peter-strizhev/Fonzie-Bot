import discord
import os
import linecache

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(';hello'):
        await message.channel.send('Hello!')


# Code to get token for bot
token = linecache.getline('Fonzie-Bot\Authentication Keys\Authentication.txt', 8)

# Clean up token so it has no trailing newline
token.rstrip()
print(token)

client.run(token)