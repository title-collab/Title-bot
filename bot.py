import discord
from discord.ext import commands
from google import genai

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())
genai.configure(api_key="YOUR_GEMINI_API_KEY")

@bot.event
async def on_ready():
    print(f'Bot online: {bot.user}')

@bot.command()
async def joke(ctx):
    response = genai.generate_text(prompt="Tell me a funny joke")
    await ctx.send(response.result)

@bot.command()
async def ask(ctx, *, question):
    response = genai.generate_text(prompt=question)
    await ctx.send(response.text[:1950])  # Discord limit

bot.run("YOUR_DISCORD_TOKEN")
