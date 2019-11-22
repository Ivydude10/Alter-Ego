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
            resp = """
So uhh... Hello, and Welcome! To Ivy Puzzle 1!
This is my first real attempt at a short but fun puzzle.
Hopefully you enjoy this, and please give me some feedback.
Anyways, go to bit.ly/IP1\_start to begin.

P.S. All links are in the form of bit.ly/IP1\_(password)"""
        elif msg == "2":
            resp = """
It's that time once again!
Ivy's Puzzle 2 is officially released.
Go to bit.ly/IP2\_SystemStart to begin.
And once again, all links are of the form bit.ly/IP2\_(insert pass here).
"""
        elif msg == "3":
            resp = """
Ah shoot, here we go again!
It's time for the third instalment of Ivy's Puzzles.
You should know the drill by now, all links are of the form bit.ly/IP\3_(insertphrasehere).
The link to start is down below:
bit.ly/IP3\_InitiateTesting
"""
        elif msg == "4":
            resp = """
It's time. The moment you've all been waiting for.
The release of IP4 is now.
Passwords are the same as usual, bit.ly/IP\4_???
However, this time there's a secret.
An alternate start to the puzzle, that only few will find.
First one to dm me the secret image gets a special reward.
Ready or not? Here. We. Go.
bit.ly/IP4\_ReadyOrNot
"""
        elif msg =="4secret":
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
        elif msg == "5":
            resp = """
And we are back! With another *beautiful* Ivy Puzzle.
This time, we are on number 5! And for that, we have a special edition.
This time, it's less about the ciphers, and more about your music knowledge.
That's right! This, is a Guess That Song Challenge!

For this, four different routes have been created, based on different genres:
        Video Game - music from various Video Game OSTs
        Anime - opening songs to different anime series
        TV Shows - the opening track to a variety of TV Shows
        Mainstream - any other type of music that doesn't fit in the above categories

To start, head over to bit.ly/IP5\_GuessThat(Insert your route of choice here)
As usual, all links are of the form bit.ly/IP5\_(Password).
First one to DM me with any of the 4 ending images, wins.
And the first one to DM me the bonus phrase, gets a special bonus, TBA.
Good luck, and have fun!

"""

        else:
            resp = "Invalid Number"
        await ctx.send(resp)


def setup(client):
    client.add_cog(IvyPuzzles(client))
