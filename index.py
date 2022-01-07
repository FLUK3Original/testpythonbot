import discord
import time
from discord.ext import commands

TOKEN = 'Bot tokene'

bot = commands.Bot(command_prefix='h!')

@bot.event
async def on_ready():
    print('A bot elindult!')

@bot.command()
async def hello(ctx):
    await ctx.send("Szia! :D")
    
bot.run(TOKEN)
