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

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def praise(self, ctx, *ascii_string):
        string = ' '.join(ascii_string)
        str = ""
        for i in string:
            str = i + str
        msg = '*' + str + '*'
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command(name='hug',
                    aliases=['hugs'],
                    brief="Hugs mentioned user")
    async def hug(self, ctx, member : discord.Member):
         author = ctx.message.author
    #    if member.id == "359217949246226434":
    #        await ctx.send(f"*hugs {member}*")
         if member.id == ctx.message.author.id:
            await ctx.send(f"*<@{member.id}> hugs themselves and starts crying ;-;*")
         else:
             if member.id == 424959492606656522 or author.id == 424959492606656522:
                  await ctx.send(f"UwU *<@{author.id}> hugs <@{member.id}>* UwU")
             else:
                  await ctx.send(f"*<@{author.id}> hugs <@{member.id}>*")

    @commands.command()
    async def pat(self, ctx, member : discord.Member):
         author = ctx.message.author
    #    if member.id == "359217949246226434":
    #        await ctx.send(f"*hugs {member}*")
         if member.id == ctx.message.author.id:
            await ctx.send(f"<@{member.id}> pats themselves? uwu? ")
         elif member.id == 424959492606656522 or author.id == 424959492606656522:
            await ctx.send(f"UwU <@{author.id}> pats <@{member.id}> UwU")
            await ctx.send("-pat- -pat-")
         else:
            await ctx.send(f"<@{author.id}> pats <@{member.id}>")
            await ctx.send("-pat- -pat-")

    @commands.command()
    async def story(self, ctx):
        channel = ctx.message.channel
        author = ctx.message.author
        def check(m):
            return m.channel == channel and m.author == author
        await ctx.send("Enter a body organ")
        Organ = await client.wait_for('message', check=check)
        await ctx.send("Enter an adjective")
        Adj1 = await client.wait_for('message', check=check)
        await ctx.send("Enter a verb")
        Verb1 = await client.wait_for('message', check=check)
        await ctx.send("Enter a plural noun")
        plNoun1 = await client.wait_for('message', check=check)
        await ctx.send("Enter another plural noun")
        plNoun2 = await client.wait_for('message', check=check)
        await ctx.send("Enter another plural noun")
        plNoun3 = await client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj2 = await client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj3 = await client.wait_for('message', check=check)
        await ctx.send("Enter another plural noun")
        plNoun4 = await client.wait_for('message', check=check)
        await ctx.send("Enter a container")
        Container = await client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj4 = await client.wait_for('message', check=check)
        await ctx.send("Enter a noun")
        Noun1 = await client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj5 = await client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj6 = await client.wait_for('message', check=check)
        await ctx.send("Enter a number")
        Number = await client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj7 = await client.wait_for('message', check=check)
        await ctx.send("Enter an adverb")
        Adverb = await client.wait_for('message', check=check)
        await ctx.send("Enter another noun")
        Noun2 = await client.wait_for('message', check=check)
        await ctx.send("Enter another verb")
        Verb2 = await client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj8 = await client.wait_for('message', check=check)
        await ctx.send("Enter an event")
        Event = await client.wait_for('message', check=check)
        await ctx.send("Enter another verb")
        Verb3 = await client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj9 = await client.wait_for('message', check=check)
        await ctx.send("Enter an exclamation")
        Excl = await client.wait_for('message', check=check)
        mainStory = "Many say that " + str(Organ.clean_content) + " storming is " + str(Adj1.clean_content) + " and does not "\
                    + str(Verb1.clean_content) + ". However, with the combination of the right " + str(plNoun1.clean_content) + \
                    ", " + str(plNoun2.clean_content) + " and " + str(plNoun3.clean_content) + " anyone can lead a " + \
                    str(Adj2.clean_content) + " session. When you have pulled together a " + str(Adj3.clean_content) + " group of " +\
                    str(plNoun4.clean_content) + " brought together in a " + str(Container.clean_content) + " that is " + \
                    str(Adj4.clean_content) + " and have a " + str(Noun1.clean_content) + " that is " + str(Adj5.clean_content) \
                    + " for the participants to suggest " + str(Adj6.clean_content) + " ideas, you will yield " +\
                    str(Number.clean_content) + " more " + str(Adj7.clean_content) + " ideas. Next time you need " + \
                    str(Adverb.clean_content) + " thought-up ideas for a " + str(Noun2.clean_content) + ", a way to " + \
                    str(Verb2.clean_content) + " sales for your business, or even " + str(Adj8.clean_content) + " ideas for activities for the company "\
                    + str(Event.clean_content) + ", put these suggestions to work and let the ideas " + str(Verb3.clean_content)\
                    + ". With so many " + str(Adj9.clean_content) + " ideas you'll have the boss declaring " + \
                    str(Excl.clean_content) + " in no time!"
    
        await ctx.send(mainStory)

def setup(client):
    client.add_cog(Fun(client))
