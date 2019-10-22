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

class IvyPuzzles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='ivypuzzle',
                    aliases=['ip'],
                    brief="The Hub of the Ivy Puzzles")
    async def ivypuzzle(self, ctx, msg=""):
        resp = ""
        if msg == "":
            resp = "Please enter a number and try again."
        elif msg == "1";
            resp = "https://bit.ly/IP1_start"
        elif msg == "2";
            resp = "https://bit.ly/IP2_SystemStart"
        elif msg == "3";
            resp = "https://bit.ly/IP3_InitiateTesting"
        else
            resp = "Invalid number"
        ctx.send(resp)


def setup(client):
    client.add_cog(IvyPuzzles(client))
