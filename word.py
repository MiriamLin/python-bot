# assist users with various word-related queries
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup 
import os
import io

# Enter a word and get images from Unsplash.
def pic(word):
    r = requests.get(f"https://unsplash.com/s/photos/{word}")
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find("img", {"class": "_2UpQX"})
    link = results.get("src")
    final = requests.get(link)
    if final.status_code == 200:
        return final.content
    else:
        raise Exception(f'{final.status_code} {final.reason}')

# Enter a word and get definition from Urban Dictionary.
def urban(word):
    r = requests.get(f"https://www.urbandictionary.com/define.php?term={word}")
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find(class_='meaning')
    return results

class Word(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(help = "輸入詞語輸出相關圖片", brief = "word's pictures")
    async def pic(self, ctx, word):
        try:
            picture = io.BytesIO(pic(word))
            picture = discord.File(picture, filename='pic.png')
            await ctx.send(file = picture)
        except Exception as e:
            await ctx.send("There are no pictures for " + str(word))

    @commands.command(help = "查詢字詞在 Urban Dictionary 的解釋", brief = "word's definition")
    async def definition(self, ctx, word):
        try:
            trans = urban(word)
            await ctx.send(f"{word}'s top definition: ")
            await ctx.send(trans)
        except Exception as e:
            await ctx.send("There is no definition for " + str(word))

def setup(bot):
    bot.add_cog(Word(bot))
