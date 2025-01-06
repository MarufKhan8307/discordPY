import discord
from discord.ext import commands

# Intents setup
intents = discord.Intents.default()
intents.message_content = True  # Enable this for reading message content

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)

# Events
@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

# Commands
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(f"The sum of {a} and {b} is {a + b}")

# Run the bot
TOKEN = "MTA3NjE3MjAwODQxODcxMzczMQ.G9wFgX.xaUmyUF-Og4i7wqmhbcaLneqDf2j9qwukhxNyQ"
bot.run(TOKEN)
