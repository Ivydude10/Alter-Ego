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
        elif msg == "1":
            resp = "https://bit.ly/IP1_start"
        elif msg == "2":
            resp = "https://bit.ly/IP2_SystemStart"
        elif msg == "3":
            resp = "https://bit.ly/IP3_InitiateTesting"
        elif msg == "4":
            resp = "Invalid Number"
            message = """
            So, you tried to be clever huh?
            Thought you could gain early access to IP4?
            Well too bad, since it isnt available yet.
            However, I'll give you a little something for trying this out....
            6 links have been created for IP4.
            5 are just for fun, whereas one of them is a hint towards a secret.
            I'm not gonna tell you which is which, and the secret will not be active until the puzzle is released.
            So, have fun searching!! :)



            What? You want a hint of some kind?
            Ugh, fine. You might wanna revist the links of the previous puzzles... ;)

            P.S. You might wanna keep this to yourself. Only one person can claim the secret."""
            await ctx.message.author.send(message)
        else:
            resp = "Invalid Number"
        await ctx.send(resp)


def setup(client):
    client.add_cog(IvyPuzzles(client))
