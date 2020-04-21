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
        switcher = {
            "": "Please enter a number and try again.",
            "1": """
So uhh... Hello, and Welcome! To Ivy Puzzle 1!
This is my first real attempt at a short but fun puzzle.
Hopefully you enjoy this, and please give me some feedback.
Anyways, go to bit.ly/IP1\_start to begin.

P.S. All links are in the form of bit.ly/IP1\_(password)""",
            "2": """
It's that time once again!
Ivy's Puzzle 2 is officially released.
Go to bit.ly/IP2\_SystemStart to begin.
And once again, all links are of the form bit.ly/IP2\_(insert pass here).
""",
            "3": """
Ah shoot, here we go again!
It's time for the third instalment of Ivy's Puzzles.
You should know the drill by now, all links are of the form bit.ly/IP\3_(insertphrasehere).
The link to start is down below:
bit.ly/IP3\_InitiateTesting
""",
            "4": """
It's time. The moment you've all been waiting for.
The release of IP4 is now.
Passwords are the same as usual, bit.ly/IP\4_???
However, this time there's a secret.
An alternate start to the puzzle, that only few will find.
First one to dm me the secret image gets a special reward.
Ready or not? Here. We. Go.
bit.ly/IP4\_ReadyOrNot
""",
            "4secret": """
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

    P.S. You might wanna keep this to yourself. Only one person can claim the secret.""",
            "5": """
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

""",
            "6": """
Have we already made 6 of these? Why do I lack a life?
Anyways, it’s time for instalment number 6 of the Ivy Puzzles.
6 “small” puzzles of varying difficulty. Can you solve them all?
As usual, passwords are of the form bit.ly/IP6\_(password).
DM the final image as proof that you have finished.
Top 3 people will receive xp for this, and the first person will get something extra.
Good luck, and have fun.

The link to start is bit.ly/IP6\_ReadySteadyGo
""",
            "7": """Nothing to see here, move along..."""

        }
        resp = switcher.get(msg, "Invalid Number")
        await ctx.send(resp)


def setup(client):
    client.add_cog(IvyPuzzles(client))
