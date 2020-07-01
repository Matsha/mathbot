import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='.')

cred = credentials.Certificate("./firebasekey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def enable(ctx, extension):
    bot.load_extension(f'cogs.{extension.lower()}')
    await ctx.send(f'The category **{extension}** has been enabled.')

@bot.command()
async def disable(ctx, extension):
    bot.unload_extension(f'cogs.{extension.lower()}')
    await ctx.send(f'The category **{extension}** has been disabled.')
    
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)

