# 功能：猜數字遊戲
import discord
from discord.ext import commands
import random
def calculate(l,vg):
    a_count=0
    b_count=0
    for i in range(len(l)):
        if l[i]==vg[i]:
            a_count+=1
        if vg[i] in l:
            b_count+=1
    b_count-=a_count
    return(a_count,b_count)

class Guess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.command(help = "啟動猜數字遊戲", brief = "Guess nAnB.")
    async def guessnumber(self, ctx):
        def is_valid(m):
            return m.author==ctx.author
        await ctx.send("Guess a 4-digits number that doesn't contain 0.")
        ans=''.join(random.sample("123456789",4))
        print("answer:",ans)
        for s in range(30):
            g=await self.bot.wait_for('message',check=is_valid,timeout=300.0)
            guess=g.content.strip()
            
            if guess.lower()=="quit":
                await ctx.send("已退出遊戲")
                return

            elif guess.lower()!="quit" and (guess.isdigit()==False or len(str(guess))!=4 or '0' in str(guess)):
                await ctx.send("輸入不合法，請重新輸入")
                continue
            else:
                aa,bb=calculate(ans,guess)
                if aa==4:
                    await ctx.send("恭喜答對!")
                    return
                else:
                    await ctx.send(f"{aa}A{bb}B")
        await ctx.send(f"Game over! Correct answer: {ans}")
def setup(bot):
    bot.add_cog(Guess(bot))
