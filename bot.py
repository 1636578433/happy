import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=',')

@bot.event
async def on_ready():
    print("Bot started")

bot.run('ODUyNjA1MjMzMTQ5MjQ3NTQ4.YMJQgA.EPZ9YB5bSy2H7rPWD5zTwnm0yRc')