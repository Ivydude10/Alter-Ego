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
        await ctx.send(str)

    @commands.command(name='eightball',
                      aliases=['8ball'])
    async def eightball(self, ctx):
        possible_responses = [
            'Duh',
            'Is the sky blue?',
            'Is grass green?',
            'Who do you think you are? A Nigerian prince?',
            'Not a chance bossypants.',
            #'neat',
            #'-pat-',
        ]
        await ctx.send(random.choice(possible_responses))

    @commands.command(name='hug',
                    aliases=['hugs'],
                    brief="Hugs mentioned user")
    async def hug(self, ctx, member : discord.Member):
         author = ctx.message.author
    #    if member.id == "359217949246226434":
    #        await ctx.send(f"*hugs {member}*")
         if member.id == ctx.message.author.id:
              msg = "**" + author.display_name + "** hugs themselves and starts crying ;-;"
         elif member.id == 424959492606656522 or author.id == 424959492606656522:
              msg = "UwU **" + author.display_name + "** hugs **" + member.display_name + "** UwU"
         else:
              msg = "**" + author.display_name + "** hugs **" + member.display_name + "**"
         embeded = discord.Embed(
             title=msg,
             colour=discord.Colour.default()
         )
         possible_responses = [
             "https://media1.tenor.com/images/11b756289eec236b3cd8522986bc23dd/tenor.gif?itemid=10592083",
             "https://media1.tenor.com/images/fd47e55dfb49ae1d39675d6eff34a729/tenor.gif?itemid=12687187",
             "https://tenor.com/view/milk-and-mocha-hug-cute-kawaii-love-gif-12535134",
             "https://tenor.com/view/hug-peachcat-cat-cute-gif-13985247",
             "https://tenor.com/view/virtual-hug-gif-5026057",
             "https://tenor.com/view/wyatt-logan-timeless-matt-lanter-lucy-preston-abigail-spencer-gif-12254044",
             "https://tenor.com/view/big-hero6-baymax-feel-better-hug-hugging-gif-4782499",
             "https://tenor.com/view/warm-hug-gif-10592083",
             "https://tenor.com/view/hugs-hug-ghost-hug-gif-4451998",
             "https://tenor.com/view/dog-hug-bff-bestfriend-friend-gif-9512793",
             "https://tenor.com/view/cuddle-party-finding-dory-disney-hug-gif-7278312",
             "https://tenor.com/view/friends-joey-chandler-hug-gif-3877439",
             "https://tenor.com/view/hugs-gif-9322908",
             "https://tenor.com/view/hug-gif-5026053",
             "https://tenor.com/view/cat-hug-back-hug-notice-me-attention-to-me-gif-14227401",
             "https://tenor.com/view/hugs-notmine-kpop-korea-gif-4593622",
             "https://tenor.com/view/cat-hug-love-cuddle-snuggle-gif-8656017",
             "https://tenor.com/view/minions-hug-gif-4127473",
             "https://tenor.com/view/polar-bears-hug-hugging-cuddle-comfortable-gif-3904776",
             "https://tenor.com/view/virtual-hug-random-hug-gif-7939558",
             "https://tenor.com/view/puuung-puung-love-you-hug-comfort-gif-13883173",
             "https://tenor.com/view/monika-hug-doki-doki-literature-club-gif-14883661",
             "https://tenor.com/view/puuung-love-puung-cuddle-morning-gif-13889660",
             "https://tenor.com/view/cheer-up-comfort-hug-couple-love-gif-4215407",
             "https://tenor.com/view/hug-gibbons-hugging-monies-hugs-gif-7693050",
             "https://tenor.com/view/hug-cuddle-comfort-love-friends-gif-5166500",
             "https://tenor.com/view/hug-anime-gif-7552075",
             "https://tenor.com/view/anime-jump-small-gif-11098589",
             "https://tenor.com/view/hug-anime-gif-11074788",
             "https://tenor.com/view/hug-anime-gif-7552093",
             "https://tenor.com/view/noragami-yato-yukine-hug-squeeze-gif-13576354",
             "https://tenor.com/view/hug-cry-sad-anime-tackle-gif-5634582",
             "https://tenor.com/view/kanna-kobayashi-anime-hug-love-gif-7883854",
             "https://tenor.com/view/kanna-kobayashi-anime-hug-love-gif-7883854",
             "https://tenor.com/view/seraph-love-hug-hugging-anime-gif-4900166",
         ]
         hug = random.choice(possible_responses)
         await ctx.send(embed=embeded)
         await ctx.send(hug)

    @commands.command(name='hugtest',
                    aliases=['hugstest'],
                    brief="Hugs mentioned user")
    async def hugtest(self, ctx, member : discord.Member):
         author = ctx.message.author
    #    if member.id == "359217949246226434":
    #        await ctx.send(f"*hugs {member}*")
         if member.id == ctx.message.author.id:
              msg = "**" + author.display_name + "** hugs themselves and starts crying ;-;"
         elif member.id == 424959492606656522 or author.id == 424959492606656522:
              msg = "UwU **" + author.display_name + "** hugs **" + member.display_name + "** UwU"
         else:
              msg = "**" + author.display_name + "** hugs **" + member.display_name + "**"
         embeded = discord.Embed(
             colour=discord.Colour.default()
         )
         possible_responses = [
            "https://media1.tenor.com/images/11b756289eec236b3cd8522986bc23dd/tenor.gif?itemid=10592083",
            "https://media.discordapp.net/attachments/625127221505425428/644323044512366602/Chiaki_Hug.gif",
         ]
         hug = random.choice(possible_responses)
         embeded.set_author(name=msg)
         embeded.set_image(url=hug)
         await ctx.send(embed=embeded)

    @commands.command()
    async def chihug(self, ctx):
        embeded = discord.Embed()
        embeded.set_image(url="https://media.discordapp.net/attachments/625127221505425428/644323044512366602/Chiaki_Hug.gif")
        await ctx.send(embed=embeded)

    @commands.command()
    async def heart(self, ctx, name):
        heart = ""
        flag = 0
        name = name.lower()
        if name == "aro":
            heart = ":black_heart::white_heart::green_heart:"
        elif name == "ace":
            heart = ":black_heart::white_heart::purple_heart:"
        elif name == "pan":
            heart = ":heartpulse::yellow_heart::blue_heart:"
        elif name == "bi":
            heart = ":heart::purple_heart::blue_heart: "
        else:
            await ctx.send("Invalid flag (or I just haven't added it yet)")
            flag = 1
        if flag == 0:
            await ctx.send(heart)


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
    async def slap(self, ctx, member : discord.Member):
         author = ctx.message.author
    #    if member.id == "359217949246226434":
    #        await ctx.send(f"*hugs {member}*")
         if member.id == ctx.message.author.id:
            await ctx.send(f"No. I'm sorry, but I will not allow you to hurt yourself. *hugs <@{author.id}>*")
    #     elif member.id == 424959492606656522 or author.id == 424959492606656522:
    #        await ctx.send(f"UwU <@{author.id}> pats <@{member.id}> UwU")
    #        await ctx.send("-pat- -pat-")
         else:
            await ctx.send(f"<@{author.id}> slaps <@{member.id}>!")
            await ctx.send("Ouch!")

    @commands.command()
    async def story(self, ctx):
        channel = ctx.message.channel
        author = ctx.message.author
        def check(m):
            return m.channel == channel and m.author == author
        await ctx.send("Enter a body organ")
        Organ = await self.client.wait_for('message', check=check)
        await ctx.send("Enter an adjective")
        Adj1 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter a verb")
        Verb1 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter a plural noun")
        plNoun1 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another plural noun")
        plNoun2 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another plural noun")
        plNoun3 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj2 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj3 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another plural noun")
        plNoun4 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter a container")
        Container = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj4 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter a noun")
        Noun1 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj5 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj6 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter a number")
        Number = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj7 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter an adverb")
        Adverb = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another noun")
        Noun2 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another verb")
        Verb2 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj8 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter an event")
        Event = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another verb")
        Verb3 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter another adjective")
        Adj9 = await self.client.wait_for('message', check=check)
        await ctx.send("Enter an exclamation")
        Excl = await self.client.wait_for('message', check=check)
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
