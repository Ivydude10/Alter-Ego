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

BOT_PREFIX = ("~", "&")
client = Bot(command_prefix=BOT_PREFIX)

class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        number = ctx.guild.member_count
        if ctx.guild.name == "Banana Army":
            for channel in ctx.guild.channels:
                if str(channel) == "hellos-and-goodbyes":
                    await self.client.get_channel(518457529727057951).send(f"""Hi {ctx.mention}! Welcome to **Banana Army**. Please make sure to read through <#528411370337599488> before using this server. Head over to <#533515934149640192> and follow the instructions there if you haven't done so already. Otherwise, we hope you have a great time in our group <:mudkip:528569347426222081>

                    We are now currently at **{number}** members. Rock on, gamers ;))""")
        if ctx.guild.name == "The Festive Crew":
            for channel in ctx.guild.channels:
                if str(channel) == "welcomes":
                    await self.client.get_channel(570851644107915269).send(f"""Hello, and welcome {ctx.mention} to The Festive Crew!

Please make them feel welcomed!""")

    @commands.Cog.listener()
    async def on_member_remove(self, ctx):
        number = ctx.guild.member_count
        if ctx.guild.name == "Banana Army":
            for channel in ctx.guild.channels:
                if str(channel) == "hellos-and-goodbyes":
                    await self.client.get_channel(518457529727057951).send(f"""**{ctx.display_name}** has left **Banana Army**. Cheers, mate. It was nice having you in our server.

                    We are now currently at **{number}** members. Rock on, gamers ;))""")
        if ctx.guild.name == "The Festive Crew":
            for channel in ctx.guild.channels:
                if str(channel) == "welcomes":
                    await self.client.get_channel(570851644107915269).send(f"""Oh no! {ctx.display_name} has left The Festive Crew.

What the hell did you guys do?""")

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.guild.name == "Banana Army":
            if str(ctx.channel) == "suggestions-and-voting":
                await ctx.add_reaction('✅')
                await ctx.add_reaction('❌')


    @commands.command(brief="Only for use in the tavern")
    async def sethex(self, ctx, val: str):
        value = discord.Colour(value=int(val, 16))
        check = 0
        embeded = discord.Embed(
            title='Change Colour',
            colour=value
        )
        embeded.set_thumbnail(url="https://www.colorhexa.com/" + val + ".png")
        embeded.add_field(name='Role Colour Changed', value='Successfully changed ' + ctx.message.author.display_name + '\'s role colour to **' + str(value) + "**")
        for role in ctx.guild.roles:
            if role.name == "Ivy" and ctx.message.author.id == 202428607610486786:
                await role.edit(colour=value)
            elif role.name == "timtams" and ctx.message.author.id == 344984109833256961:
                await role.edit(colour=value)
            elif role.name == "Chickaen" and ctx.message.author.id == 517853706817896460:
                await role.edit(colour=value)
            elif role.name == "Red" and ctx.message.author.id == 505109455982034944:
                await role.edit(colour=value)
            elif role.name == "Mental" and ctx.message.author.id == 424959492606656522:
                await role.edit(colour=value)
            elif role.name == "Jay" and ctx.message.author.id == 518198365272539147 or ctx.message.author.id == 633793859645734912:
                await role.edit(colour=value)
            elif role.name == "Carl" and ctx.message.author.id == 393827547873280000:
                await role.edit(colour=value)
            elif role.name == "idoncare" and ctx.message.author.id == 117046427837792256:
                await role.edit(colour=value)
            elif role.name == "Brush" and ctx.message.author.id == 585171748060659752:
                await role.edit(colour=value)
            elif role.name == "Tomer" and ctx.message.author.id == 212974870869311489:
                await role.edit(colour=value)
            elif role.name == "Memes" and ctx.message.author.id == 480913237664071680:
                await role.edit(colour=value)
        await ctx.send(embed=embeded)

    @commands.command(brief="Only for use in the tavern",
                      name='setcolor',
                      aliases=['setcolour'])
    @commands.has_permissions(manage_guild=True)
    async def setcolor(self, ctx, name, val: str):
        value = discord.Colour(value=int(val, 16))
        check = 0
        embeded = discord.Embed(
            title='Change Colour',
            colour=value
        )
        embeded.set_thumbnail(url="https://www.colorhexa.com/" + val + ".png")
        for role in ctx.guild.roles:
            if role.name == name:
                await role.edit(colour=value)
                check = 1
        if check == 1:
            embeded.add_field(name='Role Colour Changed', value='Successfully changed colour of **' + name + '** to **' + str(value) + "**")
        else:
            embeded.add_field(name='Role Colour Changed', value='Failed to change colour of **' + name + '** as that role does not exist')
        await ctx.send(embed=embeded)

    @commands.command()
    async def time(self, ctx, name=""):
        check = 1
        name = name.lower()
        if name == "lime" or name == "carl" or name == "mental" or name == "wale" or name == "wubba" or name == "rubik" or name == "shin'a" or name == "shina" or name == "yasu" or name == "fluffy" or name == "bb" or name == "batsy" or name == "pumpkin" or name == "deb" or name == "est":
            tz = pytz.timezone('US/Eastern')
        elif name == "satan" or name == "red" or name == "jay" or name == "idc" or name == "brush" or name == "haiku" or name =="chickaen" or name == "septa" or name == "cst" or name == "arc" or name == "rac" or name == "ayia":
            tz = pytz.timezone('US/Central')
        elif name == "ivy" or name == "tt" or name == "equus" or name == "aest":
            tz = pytz.timezone('Australia/NSW')
        elif name == "tomer":
            tz = pytz.timezone('Israel')
        elif name == "memes" or name == "twg" or name == "zamas" or name == "ded" or name == "merc" or name == "pst":
            tz = pytz.timezone('PST8PDT')
        elif name == "octo":
            tz = pytz.timezone('MST7MDT')
        elif name == "acoustic":
            tz = pytz.timezone('Singapore')
        elif name == "jake":
            tz = pytz.timezone("Pacific/Auckland")
        elif name == "sma":
            tz = pytz.timezone('Asia/Singapore')
        elif name == "mlg":
            tz = pytz.timezone('WET')
        elif name == "rigin":
            tz = pytz.timezone('America/Fortaleza')
        elif name =="green":
            tz = pytz.timezone('Europe/Amsterdam')
        elif name == "marco":
            tz = pytz.timezone('Asia/Novosibirsk')
        elif name == "ash":
            tz = pytz.timezone('US/Hawaii')
        elif name == "steven":
            tz = pytz.timezone("Asia/Seoul")
        else:
            await ctx.send("Invalid Name")
            check = 0
        if check == 1:
            today = datetime.datetime.now(tz)
            await ctx.send(today.strftime("%d-%m-%Y | %I:%M:%S %p"))

    @commands.command(name='randcolour',
                      aliases=['randcolor'])
    async def randcolour(self, ctx):
        hexval = [ '0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',]
        msg = ''.join(random.choices(hexval, k=6))
        await ctx.send('#' + msg)

    @commands.command()
    async def addrole(self, ctx, rolename=""):
        user = ctx.message.author
        check = 1
        role = ""
        embeded = discord.Embed(
            title='Adding Role',
            colour=discord.Colour.default()
        )
        embeded.set_thumbnail(url=user.avatar_url)
        if user.id == 202428607610486786 or user.id == 639801918381752340 or user.id == 458964261738250263:
            role = rolename
        else:
            if rolename == "birb":
                role = "Birb"
            elif rolename == "mudae":
                role = "MudaeBot"
            elif rolename == "pokecord":
                role = "Pok3cord"
            elif rolename == "nsfw":
                role = "Bathroom Key (NSFW)"
            elif rolename == "IP":
                role = "IP Notification"
            else:
                await ctx.send("Invalid Role")
                check = 0
        if check == 1:
            role1 = discord.utils.get(ctx.guild.roles, name=role)
            if role1 in user.roles:
                embeded.add_field(name=role, value="Failed to add role to " + user.display_name + " as they already have it.", inline=False)
                await ctx.send(embed=embeded)
            else:
                embeded.add_field(name=role, value="Successfully added role to " + user.display_name, inline=False)
                await ctx.send(embed=embeded)
                await user.add_roles(role1)

    @commands.command()
    async def pfp(self, ctx, user: discord.Member=None):
        if user == None:
            user = ctx.message.author
        embeded = discord.Embed(
            title = user.display_name + "\'s profile picture."
        )
        embeded.set_image(url=user.avatar_url)
        await ctx.send(embed=embeded)

    @commands.command()
    async def serverpic(self, ctx):
        embeded = discord.Embed(
            title = ctx.guild.name + "\'s server image."
        )
        embeded.set_image(url=ctx.guild.icon_url_as(format=None,static_format='png',size=4096))
        await ctx.send(embed=embeded)

    @commands.command()
    async def removerole(self, ctx, rolename=""):
        user = ctx.message.author
        check = 1
        role = ""
        embeded = discord.Embed(
            title='Removing Role',
            colour=discord.Colour.default()
        )
        embeded.set_thumbnail(url=user.avatar_url)
        if user.id == 202428607610486786:
            role = rolename
        else:
            if rolename == "birb":
                role = "Birb"
            elif rolename == "mudae":
                role = "MudaeBot"
            elif rolename == "pokecord":
                role = "Pok3cord"
            elif rolename == "nsfw":
                role = "Bathroom Key (NSFW)"
            elif rolename == "IP":
                role = "IP Notification"
            else:
                await ctx.send("Invalid Role")
                check = 0
        if check == 1:
            role1 = discord.utils.get(ctx.guild.roles, name=role)
            if role1 not in user.roles:
                embeded.add_field(name=role, value="Failed to remove role to " + user.display_name + " as they do not have it.", inline=False)
                await ctx.send(embed=embeded)
            else:
                embeded.add_field(name=role, value="Successfully removed role from " + user.display_name, inline=False)
                await ctx.send(embed=embeded)
                await user.remove_roles(role1)

    @commands.command()
    async def userinfo(self, ctx, member:discord.Member = None):
        if member == None:
            member = ctx.author
        roles = [role for role in member.roles]
        embeded = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)
        embeded.set_author(name=f"User Info - {member}")
        embeded.set_thumbnail(url=member.avatar_url)
        embeded.add_field(name="ID: ", value=member.id)
        embeded.add_field(name="Server Name: ", value=member.display_name)
        embeded.add_field(name="Created at: ", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embeded.add_field(name="Joined at: ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embeded.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
        await ctx.send(embed=embeded)

def setup(client):
    client.add_cog(Utility(client))
