# main fuction
import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='$')
with open(os.path.join("..", "info", "token.txt"), 'r') as f:
    token = f.read().strip("\n")
with open(os.path.join("..", "info", "extensions.txt"), 'r') as f:
    for extension in f:
        bot.load_extension(extension.strip('\n')) 

@bot.event
async def on_ready():
    print("Ready!")
    print("User name:", bot.user.name)
    print("User ID:", bot.user.id)

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    if "hello" in message.content.lower():
        await message.channel.send("Hello~ Nice to meet you.") 
    if message.content.lower().startswith("help"):
        await message.channel.send("Enter commands starting with $ or enter $help for more information:)")
    await bot.process_commands(message)

# load extension
@bot.command(help = "Load extension.", brief = "Load extension.")
async def load(ctx, extension): 
    try:
        bot.load_extension(extension.lower()) 
        await ctx.send(f"{extension} loaded.") 
    except Exception as e:
        await ctx.send(e) 

# unload extension 
@bot.command(help = "Un-load extension.", brief = "Un-load extension.")
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension.lower()) 
        await ctx.send(f"{extension} unloaded.") 
    except Exception as e:
        await ctx.send(e) 

# reload extension 
@bot.command(help = "Re-load extension.", brief = "Re-load extension.")
async def reload(ctx, extension):
    try:
        bot.reload_extension(extension.lower()) 
        await ctx.send(f"{extension} reloaded.") 
    except Exception as e:
        await ctx.send(e)

bot.run(token) 
