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
token = os.environ["TOKEN"]

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
    argembed.add_field(name='~bintext [binary data]', value="Converts the given string from binary to text. Note: Don\'t include spaces.", inline=False)
    argembed.add_field(name='~textbin [text]', value='Converts the given string from text to binary.', inline=False)
    argembed.add_field(name='~htt [hex data]', value='Converts the given string from hex to text.', inline=False)
    argembed.add_field(name='~tth [text]', value='Converts the given string from text to hex.', inline=False)
    argembed.add_field(name='~b32tt [base32 data]', value='Converts the given string from base32 to text.', inline=False)
    argembed.add_field(name='~ttb32 [text]', value='Converts the given string from text to base32.', inline=False)
    argembed.add_field(name='~b64tt [base64 data]', value='Converts the given string from base64 to text.', inline=False)
    argembed.add_field(name='~ttb64 [text]', value='Converts the given string from text to base64.', inline=False)

    respembed = discord.Embed(
        colour = discord.Colour.green()
    )
    respembed.set_author(name="Help - Miscellaneous")
    respembed.add_field(name='~hello', value="Hello and welcome!", inline=False)
    respembed.add_field(name='~omega', value="[Insert Shrug Here]", inline=False)
    respembed.add_field(name='~nou', value="No you.", inline=False)
    respembed.add_field(name='~olega', value="How soon?", inline=False)
    respembed.add_field(name='~hail', value="Hails.", inline=False)
    respembed.add_field(name='~think', value="Hmm...", inline=False)
    respembed.add_field(name='~ra_men', value="Never gonna give you up.", inline=False)
    respembed.add_field(name='~ra_women', value="Never gonna let you down.", inline=False)
    respembed.add_field(name='~ra_people', value="Never gonna run around and desert you.", inline=False)
    respembed.add_field(name='~love', value="Love Love!", inline=False)
    respembed.add_field(name='~goodbot', value="Aww, thank you!", inline=False)
    respembed.add_field(name='~badbot', value="Why would you be so cruel!", inline=False)
    respembed.add_field(name='~whatsthis', value="Huh? What's this?", inline=False)
    respembed.add_field(name='~sleep', value="Influence people to sleep.", inline=False)
    respembed.add_field(name='~sleepnow', value="Influence people to sleep now!", inline=False)
    respembed.add_field(name='~patd', value="Pat the D", inline=False)
    respembed.add_field(name='~vhug', value="A virtual hug!", inline=False)
    respembed.add_field(name='~vhug2', value="Another virtual hug!", inline=False)
    respembed.add_field(name='~vhug3', value="Yet another virtual hug!", inline=False)
    respembed.add_field(name='~chocolatemilk', value="Never underestimate the power of chocolate milk!", inline=False)
    respembed.add_field(name="~omemega", value="I heard you like memes?", inline=False)
    respembed.add_field(name="~kynktwitch", value="A link to Kynk's twitch channel", inline=False)
    respembed.add_field(name="~kynkyt", value="A link to Kynk's youtube channel", inline=False)
    respembed.add_field(name='~death', value="You know the rules.", inline=False)
    respembed.add_field(name="~self-deprecation", value="and so do I.", inline=False)


    await ctx.send("I have dmed you my instructions.")
    await ctx.message.author.send(embed=argembed)
    await ctx.message.author.send(embed=respembed)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.event
async def on_ready():
    await client.change_presence(activity=Game(name="with the idea of Hope"))
    print("Logged in as " + client.user.name)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
