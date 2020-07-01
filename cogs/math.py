import discord
from discord.ext import commands
from discord.ext.commands import cooldown
import random
import asyncio
import time

class Math(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("**Command is on cooldown**")

    #add
    @commands.command(aliases=["addition"])
    @commands.cooldown(1, 100, commands.BucketType.channel)
    async def add(self, ctx, time=15):
        inta = random.choice(range(1, 100))
        intb = random.choice(range(1, 100))
        result = int(inta) + int(intb)
        await ctx.send(f'**{inta}** + **{intb}**')
        if (time > 60):
            await ctx.send("The maximum time allowed is 60 seconds.")
            time = 60
        if (time < 0):
            await ctx.send("Please enter a positive value")
            time = 15

        def check(m):
            return m.content.isnumeric(
            ) and ctx.channel == m.channel and m.author != self.bot.user

        try:
            userAnswer = await self.bot.wait_for('message',
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
        ctx.command.reset_cooldown(ctx)


    #subtract
    @commands.command(aliases=["subtract", "subtraction"])
    @commands.cooldown(1, 100, commands.BucketType.channel)
    async def sub(self, ctx, time=15):
        inta = random.choice(range(1, 100))
        intb = random.choice(range(1, 100))
        result = int(inta) - int(intb)
        await ctx.send(f'**{inta}** - **{intb}**')
        if (time > 60):
            await ctx.send("The maximum time allowed is 60 seconds.")
            time = 60
        if (time < 0):
            await ctx.send("Please enter a positive value")
            time = 15

        def checkpositive(m):
            return m.content.isnumeric(
            ) and ctx.channel == m.channel and m.author != self.bot.user

        def checknegative(m):
            return ctx.channel == m.channel and m.author != self.bot.user and m.content.startswith(
                '-') and m.content[1:].isnumeric()

        try:
            userAnswer = await self.bot.wait_for(
                'message',
                timeout=int(time),
                check=checkpositive if result >= 0 else checknegative)
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
        ctx.command.reset_cooldown(ctx)


    #multiply
    @commands.command()
    @commands.cooldown(1, 100, commands.BucketType.channel)
    async def multiply(self, ctx, time=30):
        inta = random.choice(range(1, 100))
        intb = random.choice(range(1, 20))
        result = int(inta) * int(intb)
        await ctx.send(f'**{inta}** x **{intb}**')
        if (time > 60):
            await ctx.send("The maximum time allowed is 60 seconds.")
            time = 60
        if (time < 0):
            await ctx.send("Please enter a positive value")
            time = 15

        def check(m):
            return m.content.isnumeric(
            ) and ctx.channel == m.channel and m.author != self.bot.user

        try:
            userAnswer = await self.bot.wait_for('message',
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
        ctx.command.reset_cooldown(ctx)


    #divide
    @commands.command()
    @commands.cooldown(1, 100, commands.BucketType.channel)
    async def divide(self, ctx, time=30):
        inta = random.choice(range(1, 20))
        result = random.choice(range(1, 20))
        intb = inta * result
        await ctx.send(f'**{intb}**:**{inta}**')
        if (time > 60):
            await ctx.send("The maximum time allowed is 60 seconds.")
            time = 60
        if (time < 0):
            await ctx.send("Please enter a positive value")
            time = 15

        def check(m):
            return m.content.isnumeric(
            ) and ctx.channel == m.channel and m.author != self.bot.user

        try:
            userAnswer = await self.bot.wait_for('message',
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
        ctx.command.reset_cooldown(ctx)
    

def setup(bot):
    bot.add_cog(Math(bot))
    
