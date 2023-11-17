# 功能：顯示月曆上的各種資訊
from asyncio import DefaultEventLoopPolicy
import discord
from discord.ext import commands
import math
import datetime

def whichday(y,m,d):
    p = [ 0, 3, 2, 5, 0, 3, 5, 1,4, 6, 2, 4 ]
    y=int(y)
    m=int(m)
    d=int(d)
    if m<3:
        y-=1
    nn=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    return nn[(d+p[m-1]+y+(y//4)-(y//100)+(y//400))%7]
def whichdayint(y,m,d):
    p = [ 0, 3, 2, 5, 0, 3, 5, 1,4, 6, 2, 4 ]
    y=int(y)
    m=int(m)
    d=int(d)
    if m<3:
        y-=1
    return (d+p[m-1]+y+(y//4)-(y//100)+(y//400))%7
def nam(m):
    m=int(m)
    mon= ["January","February","March","April","May","June","July", "August","September","October","November","December"]
    return mon[m-1]
def monthnumber(y,m):
    y=int(y)
    m=int(m)
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        return 31
    elif m==4 or m==6 or m==9 or m==11:
        return 30
    elif m==2:
       if(y%400==0 or (y%4==0 and y%100!=0)):
            return 29
       else:
            return 28
def tsa(y1,m1,d1,y2,m2,d2):
    y1=int(y1)
    y2=int(y2)
    m1=int(m1)
    m2=int(m2)
    d1=int(d1)
    d2=int(d2)
    day1 = datetime.datetime(y1,m1,d1)
    day2 = datetime.datetime(y2,m2,d2)
    return str(day2-day1).replace(", 0:00:00","")
class date(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "查詢當日為星期幾", brief = "What day")
    async def day(self, ctx, year, month, date):
        try:
            t=whichday(year,month,date)
        except Exception as e:
            await ctx.send('Query error: ' + str(e))
        await ctx.send(str(year)+"/"+str(month)+"/"+str(date)+" is "+str(t)+".")

    @commands.command(help = "查詢當月有幾天", brief = "How many days in the month")
    async def howmany(self, ctx, year, month):
        try:
            t=monthnumber(year,month)
        except Exception as e:
            await ctx.send('Query error: ' + str(e))
        await ctx.send("There are "+str(t)+" days in "+str(nam(month))+", "+str(year)+".")

    @commands.command(help = "計算兩日期相差", brief = "相差幾日")
    async def days(self, ctx, year1, month1,date1,year2,month2,date2):
        try:
            t=tsa(year1,month1,date1,year2,month2,date2)
            await ctx.send('There are ' + str(t)+" between "+str(year1)+"/"+str(month1)+"/"+str(date1)+" and "+str(year2)+"/"+str(month2)+"/"+str(date2))
        except Exception as e:
            await ctx.send('Query error: ' + str(e))
def setup(bot):
    bot.add_cog(date(bot))
