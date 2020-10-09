import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Bot

bot = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------') 


@bot.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith('!ping'):
        latancy = bot.latency
        await ctx.send(f'Ping! {round(latancy*1000)}ms')


bot.run("NzYyMjkzNTAzOTI1MDI2ODQ2.X3nDJg.r6e6TtHklcSf-JIEJ6WUa97ez9M")
