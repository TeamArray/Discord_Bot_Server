import discord
import asyncio
#import random
from discord import embed
from discord.ext import commands
from discord.ext.commands import client

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')    

client.run("통큰")
