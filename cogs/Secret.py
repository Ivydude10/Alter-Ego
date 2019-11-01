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

class Secret(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='November',
                    aliases=['nov'],
                    brief="Nothing to see here...")
    async def november(self, ctx):
        message = "Nxwr89mT"
        await ctx.message.author.send(message)


def setup(client):
    client.add_cog(Secret(client))
