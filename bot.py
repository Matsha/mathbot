import os
import discord
import random
import time
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import cooldown


#initialization with hidden token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='.')


#events
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("**Command is on cooldown**")
    else:
        raise error


#commands
@client.command()
async def dab(ctx):
    dablist = ["<:dabsans:724932370956025906>","<:dabroblox:724932349669802104>","<:dabpepe:724932328811528203>","<:dab:724932300462358588>"]
    await ctx.send(random.choice(dablist))


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)


@client.command()
async def cherry(ctx):
    await ctx.send("Cherry is a nice person <:concern:719557784764416081>")


#add
@client.command(aliases=["addition"])
@commands.cooldown(1, 100, commands.BucketType.channel)
async def add(ctx, time=15):
    inta = random.choice(range(1, 100))
    intb = random.choice(range(1, 100))
    result = int(inta) + int(intb)
    await ctx.send(f'**{inta}** + **{intb}**')
    if(time>60):
        await ctx.send("The maximum time allowed is 60 seconds.")
        time = 60
    if(time<0):
        await ctx.send("Please enter a positive value")
        time = 15

    def check(m):
        return m.content.isnumeric(
        ) and ctx.channel == m.channel and m.author != client.user

    try:
        userAnswer = await client.wait_for('message',
                                           timeout=int(time),
                                           check=check)
    except asyncio.TimeoutError:
        await ctx.send(
            '**You didnt enter an answer. The right answer is {}**'.format(
                result))
    else:
        if str(result) == userAnswer.content:
            await ctx.send("**You got it right!**")
        else:
            await ctx.send(
                "**You are wrong! The right answer is {}**".format(result))
    add.reset_cooldown(ctx)


#subtract
@client.command(aliases=["subtract","subtraction"])
@commands.cooldown(1, 100, commands.BucketType.channel)
async def sub(ctx, time=15):
    inta = random.choice(range(1, 100))
    intb = random.choice(range(1, 100))
    result = int(inta) - int(intb)
    await ctx.send(f'**{inta}** - **{intb}**')
    if(time>60):
        await ctx.send("The maximum time allowed is 60 seconds.")
        time = 60
    if(time<0):
        await ctx.send("Please enter a positive value")
        time = 15

    def check(m):
        return m.content.isnumeric(
        ) and ctx.channel == m.channel and m.author != client.user

    try:
        userAnswer = await client.wait_for('message',
                                           timeout=int(time),
                                           check=check)
    except asyncio.TimeoutError:
        await ctx.send(
            '**You didnt enter an answer. The right answer is {}**'.format(
                result))
    else:
        if str(result) == userAnswer.content:
            await ctx.send("**You got it right!**")
        else:
            await ctx.send(
                "**You are wrong! The right answer is {}**".format(result))
    sub.reset_cooldown(ctx)

#multiply
@client.command()
@commands.cooldown(1, 100, commands.BucketType.channel)
async def multiply(ctx, time=30):
    inta = random.choice(range(1, 100))
    intb = random.choice(range(1, 20))
    result = int(inta) * int(intb)
    await ctx.send(f'**{inta}** x **{intb}**')
    if(time>60):
        await ctx.send("The maximum time allowed is 60 seconds.")
        time = 60
    if(time<0):
        await ctx.send("Please enter a positive value")
        time = 15

    def check(m):
        return m.content.isnumeric(
        ) and ctx.channel == m.channel and m.author != client.user

    try:
        userAnswer = await client.wait_for('message',
                                           timeout=int(time),
                                           check=check)
    except asyncio.TimeoutError:
        await ctx.send(
            '**You didnt enter an answer. The right answer is {}**'.format(
                result))
    else:
        if str(result) == userAnswer.content:
            await ctx.send("**You got it right!**")
        else:
            await ctx.send(
                "**You are wrong! The right answer is {}**".format(result))
    multiply.reset_cooldown(ctx)

#divide
@client.command()
@commands.cooldown(1, 100, commands.BucketType.channel)
async def divide(ctx, time=30):
    inta = random.choice(range(1,20))
    result =random.choice(range(1,20))
    intb = inta * result
    await ctx.send(f'**{intb}**:**{inta}**')
    if(time>60):
        await ctx.send("The maximum time allowed is 60 seconds.")
        time = 60
    if(time<0):
        await ctx.send("Please enter a positive value")
        time = 15

    def check(m):
        return m.content.isnumeric(
        ) and ctx.channel == m.channel and m.author != client.user

    try:
        userAnswer = await client.wait_for('message',
                                           timeout=int(time),
                                           check=check)
    except asyncio.TimeoutError:
        await ctx.send(
            '**You didnt enter an answer. The right answer is {}**'.format(
                result))
    else:
        if str(result) == userAnswer.content:
            await ctx.send("**You got it right!**")
        else:
            await ctx.send(
                "**You are wrong! The right answer is {}**".format(result))
    divide.reset_cooldown(ctx)
    

 
@client.command()
async def owo(ctx, *, str=""):
    if (str!=""):
        str = str.lower()
        #delete these
        owostr = str.replace("o","owo")
        owostr = owostr.replace("u","uwu")
        #word replacements
        owostr = owostr.replace("you","chu")
        owostr = owostr.replace("ove","uv")
        owostr = owostr.replace("no","nu")
        #letter replacements
        owostr = owostr.replace("r","w")
        owostr = owostr.replace("l","w")
        owostr = owostr.replace("th","ff")
        #append
        owoappend = ["òwó","owo","UwU","uwu","d-daddy","qwq"]
        owoemotes = ["(≧∀≦)","(⋟﹏⋞)","(＾▽＾)","<3","（*＾3＾）"]
        #stutter
        s = owostr[0]
        owostr = owostr.replace(s, (s+"-"+s),1)
        #final
        owostr= random.choice(owoappend)+" "+owostr+" "+random.choice(owoemotes)+" ~"
        await ctx.send(owostr)
    else:
        await ctx.send("pwease entew a sentence owo (⋟﹏⋞)~")

#stuff
client.activity = discord.Game(name="with someone's patience")

client.run(TOKEN)