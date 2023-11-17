# 檔名：todo_list.py
# 功能：TODO list (新增、刪除、顯示)
# TODO：刪除、顯示、排序、清空、儲存記錄至檔案 

import discord
from discord.ext import commands
import re
import os
import pickle

# 一項 Todo 的 class
class Todo:
    # 初始化
    def __init__(self, date, label, item):
        # 判斷是否為合法的日期 (不是很完整的判斷)
        d = re.compile("[0-9]{1,2}/[0-9]{1,2}")
        assert d.match(date)
        self.date = date
        self.label = label
        self.item = item

    # 小於 < (定義兩個 Todo 之間的「小於」，sort 時會用到)
    def __lt__(self, other):
        a=self.date.split('/')
        b=other.date.split('/')
        if(int(a[0])<int(b[0])):
            return True
        elif(int(a[0])==int(b[0]) and int(a[1])<int(b[1])):
            return True
        else:
            return False


    # 等於 = (判斷兩個 Todo 是否相等)
    def __eq__(self, other):
        return self.date==other.date and self.label==other.label and self.item==other.item

    # 回傳一個代表這個 Todo 的 string
    def __repr__(self):
        return f"{self.date} {self.label} {self.item}"


# Todo list 相關 commands
class Todo_list(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # 儲存 TODO list
        with open('todo.pickle', 'rb') as f:
            self.todo_list = pickle.load(f)

    # $add date label item
    @commands.command(
        help = '''
        Add TODO.
        For example:
        $add 06/24 Sprout Discord Bot HW
        ''', # 輸入 $help add 時顯示
        brief = "Add TODO." # 輸入 $help 時顯示
    )
    async def add(self, ctx, date, label, *, item):
        try:
            # 依照輸入建立一個 Todo object
            t = Todo(date, label, item)
        except Exception as e:
            # 建立失敗
            print(e)
            await ctx.send("Invalid input ><")
            return
        # 把 Todo 加進 list
        self.todo_list.append(t)
        # 按照日期排序，若實作了 Todo 的 __lt__ 則可以直接用 sort() 排序
        self.todo_list.sort()
        with open('todo.pickle', 'wb') as f:
            pickle.dump(self.todo_list, f)
            f.close()

        # 印出加入成功的訊息
        await ctx.send('"{}" added to TODO list'.format(item))

    # $done date label item
    @commands.command(
        help = '''
        Done TODO.
        For example:
        $done 6/24 Sprout Discord Bot HW
        ''', # 輸入 $help add 時顯示
        brief = "Done TODO." # 輸入 $help 時顯示
    )
    async def done(self, ctx, date, label, *, item): # * 代表 label 後面所有的字都會放到 item 內
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


    # $show [label]
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


    # $clear
    @commands.command(help = "Clear TODO list.", brief = "Clear TODO list.")
    async def clear(self, ctx):
        self.todo_list.clear()
        await ctx.send('Success to clear the TODO list.')
        with open('todo.pickle', 'wb') as f:
            pickle.dump(self.todo_list, f)
            f.close()

def setup(bot):
    bot.add_cog(Todo_list(bot))
