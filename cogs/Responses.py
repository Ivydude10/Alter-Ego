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

class Responses(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def hello(self, ctx):
        msg = 'Hello <@{}>. Welcome to the server! ~~Prepare to die.~~'.format(ctx.message.author.id)
        await ctx.send(msg)

    @commands.command()
    async def olegga(self, ctx):
        msg = 'The meme team. The dream team.'
        await ctx.send(msg)

    @commands.command()
    async def omega(self, ctx):
        msg = "¯\ \_(Ω)_/¯"
        await ctx.send(msg)

    @commands.command()
    async def nou(self, ctx):
        msg = """```
      _   _         _    _
     | \ | |       | |  | |
     |  \| | ___   | |  | |
     | . ` |/ _ \  | |  | |
     | |\  | (_) | | |__| |
     |_| \_|\___/   \____/
                           ```"""
        await ctx.send(msg)

    @commands.command()
    async def olega(self, ctx):
        msg = "soon :tm: :tm:"
        await ctx.send(msg)

    @commands.command(name='hail',
                    aliases=['wub', 'ash'])
    async def wub(self, ctx):
        possible_responses = [
            "*hails*",
            "*snows*",
            "*sliah*",
            "*adds another layer of ice to hail balls*",
            #";-;",

        ]
        await ctx.send(random.choice(possible_responses))

    @commands.command()
    async def think(self, ctx):
        msg = """
    ▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▄█▀▀░░░░░░▀▀█▄▒▒▒▒▒
    ▒▒▒▄█▀▄██▄░░░░░░░░▀█▄▒▒▒
    ▒▒█▀░▀░░▄▀░░░░▄▀▀▀▀░▀█▒▒
    ▒█▀░░░░███░░░░▄█▄░░░░▀█▒
    ▒█░░░░░░▀░░░░░▀█▀░░░░░█▒
    ▒█░░░░░░░░░░░░░░░░░░░░█▒
    ▒█░░██▄░░▀▀▀▀▄▄░░░░░░░█▒
    ▒▀█░█░█░░░▄▄▄▄▄░░░░░░█▀▒
    ▒▒▀█▀░▀▀▀▀░▄▄▄▀░░░░▄█▀▒▒
    ▒▒▒█░░░░░░▀█░░░░░▄█▀▒▒▒▒
    ▒▒▒█▄░░░░░▀█▄▄▄█▀▀▒▒▒▒▒▒
    ▒▒▒▒▀▀▀▀▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒"""
        await ctx.send(msg)

    @commands.command()
    async def sma(self, ctx):
        msg = 'ALL HAIL SMA'
        await ctx.send(msg)

    @commands.command()
    async def sma2(self, ctx):
        msg = '*swing?*'
        await ctx.send(msg)

    @commands.command()
    async def ra_men(self, ctx):
        msg = 'https://bit.ly/theoneandonlytruegod'
        await ctx.send(msg)

    @commands.command()
    async def ra_women(self, ctx):
        msg = 'https://bit.ly/hitthemnotes'
        await ctx.send(msg)

    @commands.command()
    async def ra_people(self, ctx):
        msg = 'https://cdn.discordapp.com/attachments/495715051454464000/542040478988894217/ra.gif'
        await ctx.send(msg)

    @commands.command()
    async def love(self, ctx):
        possible_responses = [
            ':two_hearts:',
            ':heart:',
            ':sparkling_heart:',
            ':purple_heart:',
            ':heartpulse:',
            ':gift_heart:'
            ':heartbeat:',
            ':revolving_hearts:',
            ':cupid:',
            ':blue_heart:',
            ':yellow_heart:',
            ':green_heart:',
            ':hearts:',
            ':heart:',
            ':black_heart:',
            ':heart_decoration:',
        ]
        await ctx.send(random.choice(possible_responses))

    @commands.command()
    async def goodbot(self, ctx):
        possible_responses = [
            'YEET!!',
            "`\^-^/`",
            'ヽ(^◇^*)/',
           # 'It is quite possible',
            '(◠‿◠)',
        ]
        await ctx.send(random.choice(possible_responses))

    @commands.command()
    async def badbot(self, ctx):
        possible_responses = [
            ":(",
            "How dare you...",
            "Why are you so mean?",
            "*feelsbadpeople*",
            ";-;",

        ]
        await ctx.send(random.choice(possible_responses))

    @commands.command()
    async def whatsthis(self, ctx):
        possible_responses = [
            'o.O',
            "O.o",
            'o.o',
            'O.O',
            'OwO',
        ]
        await ctx.send(random.choice(possible_responses))

    @commands.command()
    async def sleep(self, ctx):
        possible_responses = [
            "https://tenor.com/view/pokemon-eevee-sleepy-gif-7347193",
            "https://tenor.com/view/bunnyplay-petplay-pet-play-ddlg-gif-8940758",
            "https://cdn.discordapp.com/attachments/296644675769466882/506195016822161409/sleep.gif",
            "https://tenor.com/view/milk-and-mocha-bear-couple-sleepy-texting-cute-gif-12498624",
            "https://tenor.com/view/cat-kitten-sleep-yawn-sweet-dreams-gif-4475998"
            "https://tenor.com/view/sleep-sleeping-gif-5978220",
            "https://media1.tenor.com/images/f3aecb2fe3311803a81dab1e0d2a1645/tenor.gif?itemid=4716141",
            "http://i.imgur.com/pvA2QBg.gif",
            "https://cdn.discordapp.com/attachments/453561669021597704/611891983257960489/t9wj0wukeby01.png",
        ]
        await ctx.send(random.choice(possible_responses))

    @commands.command()
    async def sleepnow(self, ctx):
        possible_responses = [
         #   "https://tenor.com/view/pokemon-eevee-sleepy-gif-7347193",
         #   "https://tenor.com/view/bunnyplay-petplay-pet-play-ddlg-gif-8940758",
            "https://cdn.discordapp.com/attachments/296644675769466882/506195016822161409/sleep.gif",
         #   "https://tenor.com/view/milk-and-mocha-bear-couple-sleepy-texting-cute-gif-12498624",
         #   "https://tenor.com/view/cat-kitten-sleep-yawn-sweet-dreams-gif-4475998"
         #   "https://tenor.com/view/sleep-sleeping-gif-5978220",
         #   "https://media1.tenor.com/images/f3aecb2fe3311803a81dab1e0d2a1645/tenor.gif?itemid=4716141",
            "https://cdn.discordapp.com/attachments/453561669021597704/611891983257960489/t9wj0wukeby01.png",
        ]
        await ctx.send(random.choice(possible_responses))

    @commands.command()
    async def patd(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/542117908852113427/612969194778001448/Capture_2019-08-19-08-17-44.png")

    @commands.command()
    async def vhug(self, ctx):
        msg = "https://cdn.discordapp.com/attachments/537869721639452692/545299782999212032/giphy.gif"
        await ctx.send(msg)

    @commands.command()
    async def vhug2(self, ctx):
        msg = "https://cdn.discordapp.com/attachments/549328917220163611/556302299358560257/Virtual_Hug.gif"
        await ctx.send(msg)

    @commands.command()
    async def omemega(self, ctx):
        msg = "https://cdn.discordapp.com/attachments/547986603830935572/547987976005877791/2u7x88.png"
        await ctx.send(msg)

    @commands.command()
    async def kynktwitch(self, ctx):
        await ctx.send("https://www.twitch.tv/kynk_")
        await ctx.send("Come and hang with Kynk!")

    @commands.command()
    async def kynkyt(self, ctx):
        await ctx.send("https://www.youtube.com/user/MrKink13/")

    @commands.command()
    async def carl(self, ctx):
        possible_responses = [
            'SCREEEEEEEEE',
        #    'pingus',
        #    'pongus',
        #    'nO',
        #    'ùwú',
        #    'neat',
        ]
        await ctx.send(random.choice(possible_responses))

    @commands.command()
    async def mental(self, ctx):
        possible_responses = [
            'whooza',
            'sad',
            'Magical',
            'nO',
            'ùwú',
            'neat',
            '-pat-',
        ]
        await ctx.send(random.choice(possible_responses))

    @commands.command()
    async def pingus(self, ctx):
        await ctx.send("Pongus")
        await ctx.send("Lemme see that")

    @commands.command()
    async def death(self, ctx):
        embeded = discord.Embed(
            title="Death is Banned Here!",
            colour=discord.Colour.default()
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/353766146115371009/614279320864555019/image0.png')
        await ctx.send(embed=embeded)

def setup(client):
    client.add_cog(Responses(client))
