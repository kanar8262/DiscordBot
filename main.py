import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Bot ist online als {bot.user}")

bot.run("MTQ3MjcxMzc3ODUzNjc3NTc2MA.GTdfM1.Hl4ZRBxM2qGO7wGsepWz4OSzXigre29QC8wy8o")

