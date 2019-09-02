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

class Announce(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='ra',
                    pass_context=True,
                    brief="Do Not Use")
    async def announcera(self, ctx, *msg):
        if ctx.message.channel.id == 453561669021597704:
          await client.get_channel(538570662487523342).send(""" """.join(msg))
        else:
          await ctx.send("You don't have permission to perform this command.")

    @commands.command(name='tfc',
                    pass_context=True,
                    brief="Do Not Use")
    async def announcefriendship(self, ctx, *msg):
        if ctx.message.channel.id == 453561669021597704:
          await client.get_channel(585484704900186112).send(""" """.join(msg))
        else:
          await ctx.send("You don't have permission to perform this command.")


    @commands.command(name='ba',
                    pass_context=True,
                    brief="Do Not Use")
    async def announcebanana(self, ctx, *msg):
        if ctx.message.channel.id == 453561669021597704:
          await client.get_channel(518193641186131992).send(""" """.join(msg))

def setup(client):
    client.add_cog(Announce(client))
