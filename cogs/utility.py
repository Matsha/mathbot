import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(administrator=True)
    async def clear(self, ctx, amount=1):
        if amount > 50:
            await ctx.send("you can only purge 50 messages at a time")
        else:
            await ctx.channel.purge(limit=amount + 1)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command(aliases=['calculate','eval','evaluate','math'])
    async def calc(self, ctx, *, expression):
        expression = expression.replace("x","*")
        expression = expression.replace("^","**")
        expression = expression.replace(":","/")
        answer = eval(expression)
        await ctx.send(f'The answer is: **{round(answer,4)}**')

def setup(bot):
    bot.add_cog(Utility(bot))
    
