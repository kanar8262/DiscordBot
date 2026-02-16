import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Bot ist online als {bot.user}")

bot.run("DEIN_BOT_TOKEN_HIER")

