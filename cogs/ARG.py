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

class ARG(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def caesar(self, ctx, text, s):
        result = ""
       # transverse the plain text
        for i in range(len(text)):
          char = text[i]
          # Encrypt uppercase characters in plain text

          if (char.isupper()):
             result += chr((ord(char) + int(s)-65) % 26 + 65)
          # Encrypt lowercase characters in plain text
          elif (char.isspace()):
              result += ' '
          elif (char.islower()):
             result += chr((ord(char) + int(s) - 97) % 26 + 97)
          else:
             result += char
        embeded = discord.Embed(
            title='Caesar Encrypted',
            colour=discord.Colour.default()
        )
        embeded.add_field(name="Plain Text:", value=text, inline=False)
        embeded.add_field(name="Shift Number:", value=s, inline=False)
        embeded.add_field(name="Cipher:", value=result, inline=False)
        await ctx.send(embed=embeded)

    @commands.command()
    async def caesarbf(self, ctx, text):
        embeded = discord.Embed(
            title='Caesar Decrypted',
            colour=discord.Colour.default()
        )
        embeded.add_field(name="Plain Text:", value=text, inline=False)
        for i in range(25):
            result = ""
            for j in range(len(text)):
                char = text[j]
                if (char.isupper()):
                    result+= chr((ord(char) - i-65) % 26 + 65)
                elif (char.isspace()):
                    result += ' '
                elif (char.islower()):
                    result += chr((ord(char) - i - 97) % 26 + 97)
                else:
                    result += char
            embeded.add_field(name="Shift #" + str(i), value=result, inline=False)
        await ctx.send(embed=embeded)

    @commands.command(name='htt',
                    description="Converts hexadecimal code into text.",
                    brief="Hex to Text")
    async def hex_to_text(self, ctx, *hex_data):
        ascii_string = str(base64.b16decode(''.join(hex_data), casefold=True))[2:-1]
        embeded = discord.Embed(
            title='Hex Decrypted',
            colour=discord.Colour.default()
        )
        embeded.add_field(name="Decrypted Text:", value=ascii_string, inline=False)
        await ctx.send(embed=embeded)

    @commands.command(name='tth',
                    description="Converts text into hexadecimal code.",
                    brief="Text to Hex")
    async def text_to_hex(self, ctx,  *ascii_string):
       ascii_string2 = str.encode(' '.join(ascii_string))
       hex_data = str(base64.b16encode(ascii_string2))[2:-1]
       embeded = discord.Embed(
            title='Hex Encrypted',
            colour=discord.Colour.default()
       )
       embeded.add_field(name="Encrypted Text:", value=hex_data, inline=False)
       await ctx.send(embed=embeded)

    @commands.command(name='b32tt',
                    description="Converts base 32 into text.",
                    brief="Base32 to Text")
    async def base32_to_text(self, ctx, base_data):
        ascii_string = str(base64.b32decode(base_data))[2:-1]
        embeded = discord.Embed(
             title='Base32 Decrypted',
             colour=discord.Colour.default()
        )
        embeded.add_field(name="Decrypted Text:", value=ascii_string, inline=False)
        await ctx.send(embed=embeded)

    @commands.command(name='ttb32',
                    description="Converts text into base32",
                    brief="Text to Base32")
    async def text_to_base32(self, ctx, *ascii_string):
       ascii_string2 = str.encode(' '.join(ascii_string))
       base_data = str(base64.b32encode(ascii_string2))[2:-1]
       embeded = discord.Embed(
            title='Base32 Encrypted',
            colour=discord.Colour.default()
       )
       embeded.add_field(name="Encrypted Text:", value=base_data, inline=False)
       await ctx.send(embed=embeded)

    @commands.command(name='bintext',
                    description="Converts binary code into text",
                    brief='Binary to Text'
    )
    async def binary_to_text(self, ctx, s):
        output = ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
        embeded = discord.Embed(
             title='Binary Decrypted',
             colour=discord.Colour.default()
        )
        embeded.add_field(name="Decrypted Text:", value=output, inline=False)
        await ctx.send(embed=embeded)

    @commands.command(name='textbin',
                    description="Converts text into binary code",
                    brief='Text to Binary'
    )
    async def text_to_binary(self, ctx, *text):
        output = ''.join([bin(ord(c))[2:].rjust(8, '0') for c in """ """.join(text)])
        embeded = discord.Embed(
             title='Binary Encrypted',
             colour=discord.Colour.default()
        )
        embeded.add_field(name="Encrypted Text:", value=output, inline=False)
        await ctx.send(embed=embeded)

    @commands.command(name='btt',
                  description="Converts base 64 into text.",
                  brief="Base64 to Text")
    async def base64_to_text(self, ctx, base_data):
        ascii_string = str(base64.b64decode(base_data))[2:-1]
        embeded = discord.Embed(
            title='Base64 Decrypted',
            colour=discord.Colour.default()
        )
        embeded.add_field(name="Decrypted Text:", value=ascii_string, inline=False)
        await ctx.send(embed=embeded)

    @commands.command(name='ttb',
                  description="Converts text into base64",
                  brief="Text to Base64")
    async def text_to_base64(self, ctx, *ascii_string):
        ascii_string2 = str.encode(' '.join(ascii_string))
        base_data = str(base64.b64encode(ascii_string2))[2:-1]
        embeded = discord.Embed(
            title='Base64 Encrypted',
            colour=discord.Colour.default()
        )
        embeded.add_field(name="Encrypted Text:", value=base_data, inline=False)
        await ctx.send(embed=embeded)


def setup(client):
    client.add_cog(ARG(client))
