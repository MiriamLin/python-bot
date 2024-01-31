# A todo list that can add, delete, display, and clear tasks.
import discord
from discord.ext import commands
import re
import os
import pickle

class Todo:
    def __init__(self, date, label, item):
        d = re.compile("[0-9]{1,2}/[0-9]{1,2}")
        assert d.match(date)
        self.date = date
        self.label = label
        self.item = item

    def __lt__(self, other):
        a=self.date.split('/')
        b=other.date.split('/')
        if(int(a[0])<int(b[0])):
            return True
        elif(int(a[0])==int(b[0]) and int(a[1])<int(b[1])):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.date==other.date and self.label==other.label and self.item==other.item

    def __repr__(self):
        return f"{self.date} {self.label} {self.item}"

class Todo_list(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('todo.pickle', 'rb') as f:
            self.todo_list = pickle.load(f)

    @commands.command(
        help = '''
        Add TODO.
        For example:
        $add 06/24 Sprout Discord Bot HW
        ''', 
        brief = "Add TODO."
    )
    async def add(self, ctx, date, label, *, item):
        try:
            t = Todo(date, label, item)
        except Exception as e:
            print(e)
            await ctx.send("Invalid input ><")
            return
        self.todo_list.append(t)
        self.todo_list.sort()
        with open('todo.pickle', 'wb') as f:
            pickle.dump(self.todo_list, f)
            f.close()
        await ctx.send('"{}" added to TODO list'.format(item))

    @commands.command(
        help = '''
        Done TODO.
        For example:
        $done 6/24 Sprout Discord Bot HW
        ''', 
        brief = "Done TODO." 
    )
    async def done(self, ctx, date, label, *, item): 
        try:
            t = Todo(date, label, item)
        except Exception as e:
            print(e)
            await ctx.send("Invalid input ><")
            return
        if t in self.todo_list:
            self.todo_list.remove(t)
            await ctx.send('"{}" removed from TODO list'.format(item))
            with open('todo.pickle', 'wb') as f:
                pickle.dump(self.todo_list, f)
                f.close()
        else:
            await ctx.send('"{}" is not in TODO list'.format(item))

    @commands.command(
        help = '''
        Show all TODO with the label if specified sorted by date.
        For example:
        $show Sprout
        $show
        ''',
        brief = "Show all TODO with the label if specified sorted by date." # 輸入 $help 時顯示
    )
    async def show(self, ctx, label=None):
        try:
            p=0
            if not self.todo_list:
                await ctx.send("There are nothing in your todo list.")
            elif label is None:
                for i in self.todo_list:
                    await ctx.send(i)
            else:
                for i in self.todo_list:
                    if i.label==label:
                        await ctx.send(i)
                        p=1
                if p==0:
                    await ctx.send("There are nothing in this label.")
        except Exception as e:
            await ctx.send('Query error: ' + str(e))

    @commands.command(help = "Clear TODO list.", brief = "Clear TODO list.")
    async def clear(self, ctx):
        self.todo_list.clear()
        await ctx.send('Success to clear the TODO list.')
        with open('todo.pickle', 'wb') as f:
            pickle.dump(self.todo_list, f)
            f.close()

def setup(bot):
    bot.add_cog(Todo_list(bot))
