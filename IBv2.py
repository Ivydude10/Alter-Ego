import base64
import random
import binascii
import asyncio
import aiohttp
import json
import discord
import os
#import requests
import pytz
import datetime
import youtube_dl
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot

BOT_PREFIX = ("~", "&")

client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

# @client.command()
# async def echo(*msg):
#     await ctx.send(' '.join(msg))

#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#
#    if message.author.id == 345993541643665410:
#        await message.channel.send('Hello <@345993541643665410> o/')
#        url = "https://discordapp.com/api/webhooks/609943520622411796/IoV84MAO7EbdVt8HAWOn1uwgAsjLM4j-YkR7NQa2lCi2V-_FoPJnde_waBN0VtKQ8mA-"
#
#        data = {}
#        data["content"] = "Hello <@345993541643665410> o/"
#        data["username"] = "Tooth Pinger 9000"
#
#        result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
#
#        try:
#            result.raise_for_status()
#        except requests.exceptions.HTTPError as err:
#            print(err)
#        else:
#            print("Payload delivered successfully, code {}.".format(result.status_code))
@client.event
async def on_ready():
    await client.change_presence(activity=Game(name="bit.ly/IP2_SystemStart"))
    print("Logged in as " + client.user.name)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NTM2OTA3MTMxNDcxNzkwMDg3.Dyd0VQ.BED0UqPiQffV0ig7kdVy3BoykfM')
