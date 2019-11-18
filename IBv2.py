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
from discord.utils import get

BOT_PREFIX = ("~", "&", "alterego ", "alter ego ", "ae ", "lvybot ")

client = Bot(command_prefix=BOT_PREFIX)
client.remove_command('help')

@client.check
async def globally_blacklist_roles(ctx):
    blacklist = ["bean of all beans", "blacklist"]  # Role names
    return not any(get(ctx.guild.roles, name=name) in ctx.author.roles for name in blacklist)

@client.command()
async def help(ctx):
    argembed = discord.Embed(
        colour = discord.Colour.green()
    )
    argembed.set_author(name="Help - ARG")
    argembed.add_field(name='~caesar [text] [number]', value='Encodes the given string, using Caesar shift.', inline=False)
    argembed.add_field(name='~caesarbf [text]', value='Decodes the given string, using Caesar shift bruteforce.', inline=False)
    argembed.add_field(name='~bintext [binary data]', value='Converts the given string from binary to text. Note: Don\'t include spaces.'', inline=False)
    argembed.add_field(name='~textbin [text]', value='Converts the given string from text to binary.', inline=False)
    argembed.add_field(name='~htt [hex data]', value='Converts the given string from hex to text.', inline=False)
    argembed.add_field(name='~tth [text]', value='Converts the given string from text to hex.', inline=False)
    argembed.add_field(name='~b32tt [base32 data]', value='Converts the given string from base32 to text.', inline=False)
    argembed.add_field(name='~ttb32 [text]', value='Converts the given string from text to base32.', inline=False)
    argembed.add_field(name='~b64tt [base64 data]', value='Converts the given string from base64 to text.', inline=False)
    argembed.add_field(name='~ttb64 [text]', value='Converts the given string from text to base64.', inline=False)

    await ctx.send("I have dmed you my instructions.")
    await ctx.message.author.send(embed=argembed)

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
    await client.change_presence(activity=Game(name="with the idea of Hope"))
    print("Logged in as " + client.user.name)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NTM2OTA3MTMxNDcxNzkwMDg3.Dyd0VQ.BED0UqPiQffV0ig7kdVy3BoykfM')
