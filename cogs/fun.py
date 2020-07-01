import discord
from discord.ext import commands
import random

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def owo(self, ctx, *, str=""):
        if (str != ""):
            str = str.lower()
            #delete these
            owostr = str.replace("o", "owo")
            owostr = owostr.replace("u", "uwu")
            #word replacements
            owostr = owostr.replace("you", "chu")
            owostr = owostr.replace("ove", "uv")
            owostr = owostr.replace("no", "nu")
            #letter replacements
            owostr = owostr.replace("r", "w")
            owostr = owostr.replace("l", "w")
            owostr = owostr.replace("th", "ff")
            #append
            owoappend = ["òwó", "owo", "UwU", "uwu", "d-daddy", "qwq"]
            owoemotes = ["(≧∀≦)", "(⋟﹏⋞)", "(＾▽＾)", "<3", "（*＾3＾）"]
            #stutter
            s = owostr[0]
            owostr = owostr.replace(s, (s + "-" + s), 1)
            #final
            owostr = random.choice(owoappend) + " " + owostr + " " + random.choice(
                owoemotes) + " ~"
            await ctx.send(owostr)
        else:
            await ctx.send("pwease entew a sentence owo (⋟﹏⋞)~")

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if("gay" in ctx.content.lower()):
            await ctx.add_reaction('🌈')

    @commands.command()
    async def dab(self, ctx):
        dablist = [
            "<:dabsans:724932370956025906>", "<:dabroblox:724932349669802104>",
            "<:dabpepe:724932328811528203>", "<:dab:724932300462358588>"
        ]
        await ctx.send(random.choice(dablist))

def setup (bot):
    bot.add_cog(Fun(bot))