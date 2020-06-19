import os
import discord
import random
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

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


#commands
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)


@client.command()
async def add(ctx, time=10.0):
    inta = random.choice(range(1, 100))
    intb = random.choice(range(1, 100))
    result = int(inta) + int(intb)
    await ctx.send(f'**{inta}** + **{intb}**')

    def check(m):
        return m.author == ctx.author

    try:
        userAnswer = await client.wait_for('message',
                                           timeout=float(time),
                                           check=check)
    except asyncio.TimeoutError:
        await ctx.send(
            '**You didnt enter an answer. The right answer is {}**'.format(
                result))
    else:
        if (userAnswer.content.isnumeric()):
            if str(result) == userAnswer.content:
                await ctx.send("**You got it right!**")
            else:
                await ctx.send(
                    "**You are wrong! The right answer is {}**".format(result))
        else:
            await ctx.send("**Please enter a number.**")


#stuff
client.activity = discord.Game(name=".ping")

client.run(TOKEN)