# 功能：顯示dcard、ptt等論壇熱門文章

import discord
from discord.ext import commands
# import asyncio
import requests
from bs4 import BeautifulSoup
# import random
from datetime import datetime, timedelta

def get_dcard(a):
    r = requests.get('https://www.dcard.tw/f')
    dcsoup = BeautifulSoup(r.text, "html.parser")
    results = dcsoup.find_all(class_="tgn9uw-3 cUGTXH")
    return results[int(a)].text
def get_dcc(a):
    r = requests.get('https://www.dcard.tw/forum/popular')
    dcc = BeautifulSoup(r.text, "html.parser")
    results = dcc.find_all(class_="nvtgdu-5 ixDZiU")
    return results[int(a)].text
def get_ptt(a):
    r = requests.get('https://www.ptt.cc/bbs/index.html')
    dcc = BeautifulSoup(r.text, "html.parser")
    results = dcc.find_all('div',class_='board-name')
    return results[int(a)].text
def get_ettoday(a):
    r = requests.get('https://www.ettoday.net/news/hot-news.htm')
    etsoup = BeautifulSoup(r.text, "html.parser")
    etso=etsoup.select(".part_pictxt_3")
    for e in etso:
        title_list = [title.text for title in e.select("a")]
    return title_list[int(a)].replace('\u3000','  ')

class Dc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help = "印出dcard及時熱門文章",
        brief = "Print dcard's popular article"
    )
    async def dcard(self, ctx,rank):
        await ctx.send("dcard目前第"+str(rank)+"熱門的文章標題:")
        try:
            dcar=get_dcard(int(rank)-1)
        except Exception as e:
            await ctx.send('Query error: ' + str(e))

        await ctx.send(dcar)

    @commands.command(
        help = "印出dcard及時熱門看板",
        brief = "Print dcard's popular board"
    )
    async def dcc(self, ctx, rank):
        await ctx.send("dcard目前第"+str(rank)+"熱門的文章看板為:")
        try:
            dcar=get_dcc(int(rank)-1)
        except Exception as e:
            await ctx.send('Query error: ' + str(e))

        await ctx.send(dcar)

    @commands.command(
        help = "印出ptt及時熱門看板",
        brief = "Print ptt's popular article"
    )
    async def ptt(self, ctx,rank):
        await ctx.send("ptt目前第"+str(rank)+"熱門的文章看板:")
        try:
            pt=get_ptt(int(rank)-1)
        except Exception as e:
            await ctx.send('Query error: ' + str(e))

        await ctx.send(pt)
    
    @commands.command(
        help = "印出ettoday及時熱門新聞",
        brief = "Print Ettoday's popular news"
    )
    async def ettoday(self, ctx, rank):
        await ctx.send("Ettoday 目前第"+str(rank)+"熱門的新聞標題:")
        try:
            et=get_ettoday(2*int(rank)-1)
        except Exception as e:
            await ctx.send('Query error: ' + str(e))

        await ctx.send(et)


def setup(bot):
    bot.add_cog(Dc(bot))
