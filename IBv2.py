import base64
import random
import binascii
import asyncio
import aiohttp
import json
import discord
#import requests
import pytz
import datetime
import youtube_dl
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot

BOT_PREFIX = ("~", "&")

client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def load(ctx, extension)
    client.load_extension(f"cogs.{extension}"")

@client.command()
async def unload(ctx, extension)
    client.unload_extension(f"cogs.{extension}"")

@client.command(pass_context=True)
async def hello(ctx):
    msg = 'Hello <@{}>. Welcome to the server! ~~Prepare to die.~~'.format(ctx.message.author.id)
    await ctx.send(msg)

@client.command()
async def caesar(ctx, text, s):
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
      else:
         result += chr((ord(char) + int(s) - 97) % 26 + 97)
    embeded = discord.Embed(
        title='Caesar Encrypted',
        colour=discord.Colour.default()
    )
    embeded.add_field(name="Plain Text:", value=text, inline=False)
    embeded.add_field(name="Shift Number:", value=s, inline=False)
    embeded.add_field(name="Cipher:", value=result, inline=False)
    await ctx.send(embed=embeded)

@client.command()
async def caesarbf(ctx, text):
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
                result+= chr((ord(char) + int(s)-65) % 26 + 65)
            elif (char.isspace()):
                result += ' '
            else:
                result += chr((ord(char) + int(s) - 97) % 26 + 97)
        embeded.add_field(name="Shift #" + i, value=result, inline=False)
    await ctx.send(embed=embeded)


@client.command(name='htt',
                description="Converts hexadecimal code into text.",
                brief="Hex to Text")
async def hex_to_text(ctx, *hex_data):
    if ctx.message.author.id == 345993541643665410:
        msg = "No <@345993541643665410>..."
        await ctx.send(msg)
    else:
        ascii_string = str(base64.b16decode(''.join(hex_data), casefold=True))[2:-1]
        embeded = discord.Embed(
            title='Hex Decrypted',
            colour=discord.Colour.default()
        )
        embeded.add_field(name="Decrypted Text:", value=ascii_string, inline=False)
        await ctx.send(embed=embeded)

@client.command(name='tth',
                description="Converts text into hexadecimal code.",
                brief="Text to Hex")
async def text_to_hex(ctx,  *ascii_string):
   ascii_string2 = str.encode(' '.join(ascii_string))
   hex_data = str(base64.b16encode(ascii_string2))[2:-1]
   embeded = discord.Embed(
        title='Hex Encrypted',
        colour=discord.Colour.default()
   )
   embeded.add_field(name="Encrypted Text:", value=hex_data, inline=False)
   await ctx.send(embed=embeded)

@client.command(name='b64tt',
                description="Converts base 64 into text.",
                brief="Base64 to Text")
async def base_to_text(ctx, base_data):
    if ctx.message.author.id == 345993541643665410:
        msg = "No <@345993541643665410>..."
        await ctx.send(msg)
    else:
         ascii_string = str(base64.b64decode(base_data))[2:-1]
         embeded = discord.Embed(
              title='Base64 Decrypted',
              colour=discord.Colour.default()
         )
         embeded.add_field(name="Decrypted Text:", value=ascii_string, inline=False)
         await ctx.send(embed=embeded)

@client.command(name='ttb64',
                description="Converts text into base64",
                brief="Text to Base64")
async def text_to_base(ctx, *ascii_string):
   ascii_string2 = str.encode(' '.join(ascii_string))
   base_data = str(base64.b64encode(ascii_string2))[2:-1]
   embeded = discord.Embed(
        title='Base64 Encrypted',
        colour=discord.Colour.default()
   )
   embeded.add_field(name="Encrypted Text:", value=base_data, inline=False)
   await ctx.send(embed=embeded)

@client.command(name='b32tt',
                description="Converts base 32 into text.",
                brief="Base32 to Text")
async def base_to_text(ctx, base_data):
    if ctx.message.author.id == 345993541643665410:
        msg = "No <@345993541643665410>..."
        await ctx.send(msg)
    else:
        ascii_string = str(base64.b32decode(base_data))[2:-1]
        embeded = discord.Embed(
             title='Base32 Decrypted',
             colour=discord.Colour.default()
        )
        embeded.add_field(name="Decrypted Text:", value=ascii_string, inline=False)
        await ctx.send(embed=embeded)

@client.command(name='ttb32',
                description="Converts text into base32",
                brief="Text to Base32")
async def text_to_base(ctx, *ascii_string):
   ascii_string2 = str.encode(' '.join(ascii_string))
   base_data = str(base64.b32encode(ascii_string2))[2:-1]
   embeded = discord.Embed(
        title='Base32 Encrypted',
        colour=discord.Colour.default()
   )
   embeded.add_field(name="Encrypted Text:", value=base_data, inline=False)
   await ctx.send(embed=embeded)

@client.command(name='bintext',
                description="Converts binary code into text",
                brief='Binary to Text'
)
async def binary_to_text(ctx, s):
    if ctx.message.author.id == 345993541643665410:
        msg = "No <@345993541643665410>..."
        await ctx.send(msg)
    else:
        output = ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
        embeded = discord.Embed(
             title='Binary Decrypted',
             colour=discord.Colour.default()
        )
        embeded.add_field(name="Decrypted Text:", value=output, inline=False)
        await ctx.send(embed=embeded)

@client.command(name='textbin',
                description="Converts text into binary code",
                brief='Text to Binary'
)
async def text_to_binary(ctx, *text):
    output = ''.join([bin(ord(c))[2:].rjust(8, '0') for c in """ """.join(text)])
    embeded = discord.Embed(
         title='Binary Encrypted',
         colour=discord.Colour.default()
    )
    embeded.add_field(name="Encrypted Text:", value=output, inline=False)
    await ctx.send(embed=embeded)

@client.command(pass_context=True)
async def praise(ctx, *ascii_string):
    if ctx.message.author.id == 345993541643665410:
        msg = "No <@345993541643665410>..."
        await ctx.send(msg)
    else:
        string = ' '.join(ascii_string)
        str = ""
        for i in string:
            str = i + str
        msg = '*' + str + '*'
        await ctx.message.delete()
        await ctx.send(msg)


@client.command()
async def olegga(ctx):
    msg = 'The meme team. The dream team.'
    await ctx.send(msg)

@client.command()
async def omega(ctx):
    msg = "¯\ \_(Ω)_/¯"
    await ctx.send(msg)

@client.command()
async def nou(ctx):
    msg = """```
  _   _         _    _
 | \ | |       | |  | |
 |  \| | ___   | |  | |
 | . ` |/ _ \  | |  | |
 | |\  | (_) | | |__| |
 |_| \_|\___/   \____/
                       ```"""
    await ctx.send(msg)

@client.command()
async def olega(ctx):
    msg = "soon :tm: :tm:"
    await ctx.send(msg)

@client.command(name='hail',
                aliases=['wub', 'ash'])
async def wub(ctx):
    possible_responses = [
        "*hails*",
        "*snows*",
        "*sliah*",
        "*adds another layer of ice to hail balls*",
        #";-;",

    ]
    await ctx.send(random.choice(possible_responses))

@client.command()
async def think(ctx):
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

@client.command()
async def sma(ctx):
    msg = 'ALL HAIL SMA'
    await ctx.send(msg)

@client.command()
async def sma2(ctx):
    msg = '*swing?*'
    await ctx.send(msg)

@client.command()
async def ra_men(ctx):
    msg = 'https://bit.ly/theoneandonlytruegod'
    await ctx.send(msg)

@client.command()
async def ra_women(ctx):
    msg = 'https://bit.ly/hitthemnotes'
    await ctx.send(msg)

@client.command()
async def ra_people(ctx):
    msg = 'https://cdn.discordapp.com/attachments/495715051454464000/542040478988894217/ra.gif'
    await ctx.send(msg)

@client.command()
async def love(ctx):
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

@client.command()
async def goodbot(ctx):
    possible_responses = [
        'YEET!!',
        "`\^-^/`",
        'ヽ(^◇^*)/',
       # 'It is quite possible',
        '(◠‿◠)',
    ]
    await ctx.send(random.choice(possible_responses))

@client.command()
async def badbot(ctx):
    possible_responses = [
        ":(",
        "How dare you...",
        "Why are you so mean?",
        "*feelsbadpeople*",
        ";-;",

    ]
    await ctx.send(random.choice(possible_responses))

@client.command()
async def whatsthis(ctx):
    possible_responses = [
        'o.O',
        "O.o",
        'o.o',
        'O.O',
        'OwO',
    ]
    await ctx.send(random.choice(possible_responses))

#@client.command()
#async def justdoit():
#    await client.send_file(channel, 'just_do_it.png')

@client.command()
async def sleep(ctx):
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

@client.command()
async def sleepnow(ctx):
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

@client.command()
async def patd(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/542117908852113427/612969194778001448/Capture_2019-08-19-08-17-44.png")

@client.command()
async def vhug(ctx):
    msg = "https://cdn.discordapp.com/attachments/537869721639452692/545299782999212032/giphy.gif"
    await ctx.send(msg)

@client.command()
async def vhug2(ctx):
    msg = "https://cdn.discordapp.com/attachments/549328917220163611/556302299358560257/Virtual_Hug.gif"
    await ctx.send(msg)

@client.command()
async def omemega(ctx):
    msg = "https://cdn.discordapp.com/attachments/547986603830935572/547987976005877791/2u7x88.png"
    await ctx.send(msg)

@client.command(name='uap',
                pass_context=True,
                brief="Do Not Use")
async def announceuap(ctx, *msg):
    if ctx.message.channel.id == "453561669021597704":
      await client.send_message(client.get_channel("535411504707534856"), """ """.join(msg))
    else:
      await ctx.send("You don't have permission to perform this command.")


@client.command(name='ra',
                pass_context=True,
                brief="Do Not Use")
async def announcera(ctx, *msg):
    if ctx.message.channel.id == "453561669021597704":
      await client.send_message(client.get_channel("538570662487523342"), """ """.join(msg))
    else:
      await ctx.send("You don't have permission to perform this command.")

@client.command(name='iris',
                pass_context=True,
                brief="Do Not Use")
async def announceiris(ctx, *msg):
    if ctx.message.channel.id == "453561669021597704":
      await client.send_message(client.get_channel("536398366582636546"), """ """.join(msg))
    else:
      await ctx.send("You don't have permission to perform this command.")

@client.command(name='tna',
                pass_context=True,
                brief="Do Not Use")
async def announcetna(ctx, *msg):
    if ctx.message.channel.id == "453561669021597704":
      await client.send_message(client.get_channel("538969463131996161"), """ """.join(msg))
    else:
      await ctx.send("You don't have permission to perform this command.")

@client.command(name='oleg',
                pass_context=True,
                brief="Do Not Use")
async def announceolegga(ctx, *msg):
    if ctx.message.channel.id == "453561669021597704":
      await client.send_message(client.get_channel("530504530882985997"), """ """.join(msg))
    else:
      await ctx.send("You don't have permission to perform this command.")

@client.command(name='olegg',
                pass_context=True,
                brief="Do Not Use")
async def announceoleggga(ctx, *msg):
    if ctx.message.channel.id == "453561669021597704":
      await client.send_message(client.get_channel("554008348564127765"), """ """.join(msg))
    else:
      await ctx.send("You don't have permission to perform this command.")

@client.command(name='tfc',
                pass_context=True,
                brief="Do Not Use")
async def announcefriendship(ctx, *msg):
    if ctx.message.channel.id == 453561669021597704:
      await client.get_channel(585484704900186112).send(""" """.join(msg))
    else:
      await ctx.send("You don't have permission to perform this command.")


@client.command(name='ba',
                pass_context=True,
                brief="Do Not Use")
async def announcebanana(ctx, *msg):
    if ctx.message.channel.id == "453561669021597704":
      await client.send_message(client.get_channel("518193641186131992"), """ """.join(msg))
    else:
      await ctx.send("You don't have permission to perform this command.")

#@client.command(pass_context=True)
#async def hug(ctx):
#    await ctx.send("*hugs <@{}>*".format(ctx.message.author.id))

@client.command(name='hug',
                aliases=['hugs'],
                brief="Hugs mentioned user")
async def hug(ctx, member : discord.Member):
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

@client.command()
async def pat(ctx, member : discord.Member):
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

@client.command()
async def story(ctx):
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

@client.event
async def on_ready():
    await client.change_presence(activity=Game(name="bit.ly/IP1_start"))
    print("Logged in as " + client.user.name)

@client.event
async def on_member_join(ctx):
    if ctx.guild.name == "The Tavern":
        for channel in ctx.guild.channels:
            if str(channel) == "the-bar":
                await client.get_channel(612524089730531348).send(f"""Hello and Welcome {ctx.mention}! To The Tavern!""")

@client.command(brief="Only for use in the tavern")
async def sethex(ctx, val: str):
    value = discord.Colour(value=int(val, 16))
    embeded = discord.Embed(
        title='Colour Changed',
        colour=value
    )
    embeded.set_thumbnail(url="https://www.colorhexa.com/" + val + ".png")
    embeded.add_field(name='Role Colour Changed', value='Successfully changed' + ctx.message.author.display_name + '\'s role colour to **' + str(value) + "**")
    for role in ctx.guild.roles:
        if role.name == "Ivy" and ctx.message.author.id == 202428607610486786:
            await role.edit(colour=value)
            await ctx.send(embed=embeded)
        elif role.name == "timtams" and ctx.message.author.id == 344984109833256961:
            await role.edit(colour=value)
            await ctx.send(embed=embeded)
        elif role.name == "Chickaen" and ctx.message.author.id == 517853706817896460:
            await role.edit(colour=value)
            await ctx.send(embed=embeded)
        elif role.name == "Red" and ctx.message.author.id == 505109455982034944:
            await role.edit(colour=value)
            await ctx.send(embed=embeded)
        elif role.name == "Mental" and ctx.message.author.id == 424959492606656522:
            await role.edit(colour=value)
            await ctx.send(embed=embeded)
        elif role.name == "Jay" and ctx.message.author.id == 518198365272539147:
            await role.edit(colour=value)
            await ctx.send(embed=embeded)
        elif role.name == "Carl" and ctx.message.author.id == 393827547873280000:
            await role.edit(colour=value)
            await ctx.send(embed=embeded)
        elif role.name == "idoncare" and ctx.message.author.id == 117046427837792256:
            await role.edit(colour=value)
            await ctx.send(embed=embeded)
        elif role.name == "Brush" and ctx.message.author.id == 585171748060659752:
            await role.edit(colour=value)
            await ctx.send(embed=embeded)


# @client.command()
# async def echo(*msg):
#     await ctx.send(' '.join(msg))

#@client.command(pass_context=True)
#async def potato(ctx):
#    area=ctx.message.channel
#    await client.send_file(area, r"C:\Users\User\Downloads\potato.jpg",filename="Potato",content="When I grow up, I wanna be a potato!")

@client.command()
async def time(ctx, name=""):
    check = 1
    if name == "lime" or name == "carl" or name == "mental" or name == "wale" or name == "wubba" or name == "rubik":
        tz = pytz.timezone('US/Eastern')
    elif name == "satan" or name == "red" or name == "jay" or name == "idc" or name == "brush":
        tz = pytz.timezone('US/Central')
    elif name == "ivy" or name == "tt":
        tz = pytz.timezone('Australia/NSW')
    elif name == "tomer":
        tz = pytz.timezone('Israel')
    elif name == "memes" or name == "twg":
        tz = pytz.timezone('PST8PDT')
    elif name == "sma":
        tz = pytz.timezone('Asia/Singapore')
    elif name == "mlg":
        tz = pytz.timezone('WET')
    elif name == "rigin":
        tz = pytz.timzone('America/Fortaleza')
    elif name =="green":
        tz = pytz.timezone('Europe/Amsterdam')
    else:
        await ctx.send("Invalid Name")
        check = 0
    if check == 1:
        today = datetime.datetime.now(tz)
        await ctx.send(today.strftime("%d-%m-%Y | %I:%M:%S %p"))

@client.command()
async def kynktwitch(ctx):
    await ctx.send("https://www.twitch.tv/kynk_")
    await ctx.send("Come and hang with Kynk!")

@client.command()
async def kynkyt(ctx):
    await ctx.send("https://www.youtube.com/user/MrKink13/")

@client.command()
async def carl(ctx):
    possible_responses = [
        'SCREEEEEEEEE',
    #    'pingus',
    #    'pongus',
    #    'nO',
    #    'ùwú',
    #    'neat',
    ]
    await ctx.send(random.choice(possible_responses))

@client.command()
async def mental(ctx):
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

@client.command()
async def randcolour(ctx):
    hexval = [ '0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',]
    msg = ''.join(random.choices(hexval, k=6))
    await ctx.send('#' + msg)

@client.command()
async def pingus(ctx):
    await ctx.send("Pongus")
    await ctx.send("Lemme see that")

@client.command()
async def addrole(ctx, rolename=""):
    user = ctx.message.author
    check = 1
    role = ""
    embeded = discord.Embed(
        title='Adding Role',
        colour=discord.Colour.default()
    )
    embeded.set_thumbnail(url=user.avatar_url)
    if rolename == "birb":
        role = "Birb"
    elif rolename == "mudae":
        role = "MudaeBot"
    elif rolename == "pokecord":
        role = "Pok3cord"
    elif rolename == "nsfw":
        role = "Bathroom Key (NSFW)"
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

@client.command()
async def removerole(ctx, rolename=""):
    user = ctx.message.author
    check = 1
    role = ""
    embeded = discord.Embed(
        title='Removing Role',
        colour=discord.Colour.default()
    )
    embeded.set_thumbnail(url=user.avatar_url)
    if rolename == "birb":
        role = "Birb"
    elif rolename == "mudae":
        role = "MudaeBot"
    elif rolename == "pokecord":
        role = "Pok3cord"
    elif rolename == "nsfw":
        role = "Bathroom Key (NSFW)"
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
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#
#    if message.author.id == 345993541643665410:
#        await message.channel.send('Hello <@345993541643665410> o/')
#        url = "https://discordapp.com/api/webhooks/609943520622411796/IoV84MAO7EbdVt8HAWOn1uwgAsjLM4j-YkR7NQa2lCi2V-_FoPJnde_waBN0VtKQ8mA-"
#
#        data = {}
#        data["content"] = "Hello <@345993541643665410> o/"
#        data["username"] = "Tooth Pinger 9000"
#
#        result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
#
#        try:
#            result.raise_for_status()
#        except requests.exceptions.HTTPError as err:
#            print(err)
#        else:
#            print("Payload delivered successfully, code {}.".format(result.status_code))

client.run('NTM2OTA3MTMxNDcxNzkwMDg3.Dyd0VQ.BED0UqPiQffV0ig7kdVy3BoykfM')
