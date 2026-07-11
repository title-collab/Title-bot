import discord
from discord.ext import commands
import socket
import os

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

MC_IP = "147.185.221.212"
MC_PORT = 25301

def check_server():
    """Check if server is online"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((MC_IP, MC_PORT))
        sock.close()
        return result == 0
    except:
        return False

@bot.event
async def on_ready():
    print(f'Bot online: {bot.user}')

@bot.command()
async def server(ctx):
    """Check server status"""
    status = check_server()
    if status:
        embed = discord.Embed(title="🟢 Server ONLINE", color=discord.Color.green())
    else:
        embed = discord.Embed(title="🔴 Server OFFLINE", color=discord.Color.red())
    
    embed.add_field(name="IP", value=MC_IP, inline=False)
    embed.add_field(name="Port", value=MC_PORT, inline=False)
    await ctx.send(embed=embed)

bot.run(os.getenv("BOT_TOKEN"))
