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

bot.run("통큰")
