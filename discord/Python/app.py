import discord
from discord import Embed
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------') 

@bot.command()
async def ping(ctx):
    latancy = bot.latency
    await ctx.send(embed = Embed(description=f'Ping! {round(latancy*1000)}ms'))


bot.run("통큰")
