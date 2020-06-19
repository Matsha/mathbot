import os
import discord
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
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount+1)

#stuff
client.activity = discord.Game(name=".ping") 

client.run(TOKEN)