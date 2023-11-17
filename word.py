# 檔名：word.py
# 功能：對詞語輸出各種操作

import discord
from discord.ext import commands
# import asyncio
import requests
from bs4 import BeautifulSoup
# import random
import os
import io

def pic(word):
    r = requests.get(f"https://unsplash.com/s/photos/{word}")
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find("img", {"class": "_2UpQX"})
    link = results.get("src")
    final=requests.get(link)
    if final.status_code == 200:
        return final.content
    else:
        raise Exception(f'{final.status_code} {final.reason}')
def urban(word):
    r = requests.get(f"https://www.urbandictionary.com/define.php?term={word}")
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find(class_='meaning')
    return results.text
def syn(word):
    r=requests.get(f"https://www.thesaurus.com/browse/{word}")
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find_all(class_='css-1kg1yv8 eh475bn0')
    return results
class Word(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(help = "輸入詞語輸出相關圖片", brief = "word's picture")
    async def pic(self, ctx, word):
        try:
            picture = io.BytesIO(pic(word))
            picture = discord.File(picture, filename='pic.png')
            await ctx.send(file = picture)
        except Exception as e:
            await ctx.send("There are no pictures for "+str(word))

    @commands.command(help = "查詢字詞在Urban票選最精闢的解釋", brief = "word's top definition")
    async def definition(self, ctx, word):
        try:
            trans=urban(word)
            await ctx.send(f"{word}'s top definition: ")
            await ctx.send(trans)
        except Exception as e:
            await ctx.send("There are no definition for "+str(word))

    @commands.command(help = "查詢字詞的同義字", brief = "print word's synonyms")
    async def synonyms(self, ctx, word):
        try:
            results=syn(word)
            if(len(results)==0):
                await ctx.send(f"There are no synonyms for {word}.")
            else:
                for i in range(len(results)):
                    await ctx.send(results[i].text)
        except Exception as e:
            await ctx.send('Error: ' + str(e))


def setup(bot):
    bot.add_cog(Word(bot))
    