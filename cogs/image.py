import os
import discord
from utils.data import getJSON

from discord.ext import commands
from datetime import datetime

from utils.web_api import ImageAPI

class Image(commands.Cog):  
    def __init__(self, bot):
        self.bot = bot
        self.config = getJSON("config.json")
        self.API_Handler = ImageAPI()
    
    @commands.command(
        name='deadchat',
        description='Deadchat',
        aliases=['dead', 'chatdead']
    )
    async def deadchat(self, ctx):
        e = discord.Embed(colour=0x2ECC71)
        e.set_image(url="https://i.imgur.com/0WjrVUN.png")
        e.set_footer(text="Made with ❤️ by Roxiun")

        await ctx.send(embed=e)

    @commands.command(
        name='distractedboyfriend',
        description='Distracted Boyfriend meme',
        aliases=['boyfriend', 'distractedbf', 'dbf']
    )
    async def distractedboyfriend(self, ctx):
        msg = ctx.message.content

        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        args = msg[len(prefix_used) + len(alias_used):].split(',')

        
        if len(args) > 3:
            await ctx.send(":x: Too many arguments (Max 3)")
            return
        elif len(args) == 1 and args[0] == '':
            await ctx.send("You must specify some text dummy")
            return
        
        image = self.API_Handler.getImgflip("112126428", args)
        
        e = discord.Embed(colour=0x2ECC71)
        e.set_image(url=image)
        e.set_footer(text="Made with ❤️ by Roxiun & Imgflip")

        await ctx.send(embed=e)
    
    @commands.command(
        name='drake',
        description='Drake Choice meme',
        aliases=['drakeposting', 'hotline', 'hotlinebling', 'drakehotlinebling']
    )
    async def drake(self, ctx):
        msg = ctx.message.content

        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        args = msg[len(prefix_used) + len(alias_used):].split(',')

        
        if len(args) > 2:
            await ctx.send(":x: Too many arguments (Max 2)")
            return
        elif len(args) == 1 and args[0] == '':
            await ctx.send("You must specify some text dummy")
            return
        
        image = self.API_Handler.getImgflip("181913649", args)
        
        e = discord.Embed(colour=0x2ECC71)
        e.set_image(url=image)
        e.set_footer(text="Made with ❤️ by Roxiun & Imgflip")

        await ctx.send(embed=e)
    @commands.command(
        name='changemymind',
        description='Steven Crowder\'s sign, prove me wrong',
    )
    async def changemymind(self, ctx):
        msg = ctx.message.content

        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        args = msg[len(prefix_used) + len(alias_used):].split(',')

        
        if len(args) > 2:
            await ctx.send(":x: Too many arguments (Max 2)")
            return
        elif len(args) == 1 and args[0] == '':
            await ctx.send("You must specify some text dummy")
            return
        
        image = self.API_Handler.getImgflip("129242436", args)
        
        e = discord.Embed(colour=0x2ECC71)
        e.set_image(url=image)
        e.set_footer(text="Made with ❤️ by Roxiun & Imgflip")

        await ctx.send(embed=e)
    
    @commands.command(
        name='expandingbrain',
        description='3 brain meme',
        aliases=['brains', 'bigbrain']
    )
    async def expandingbrain(self, ctx):
        msg = ctx.message.content

        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        args = msg[len(prefix_used) + len(alias_used):].split(',')

        
        if len(args) > 2:
            await ctx.send(":x: Too many arguments (Max 2)")
            return
        elif len(args) == 1 and args[0] == '':
            await ctx.send("You must specify some text dummy")
            return
        
        image = self.API_Handler.getImgflip("93895088", args)
        
        e = discord.Embed(colour=0x2ECC71)
        e.set_image(url=image)
        e.set_footer(text="Made with ❤️ by Roxiun & Imgflip")

        await ctx.send(embed=e)
    
    @commands.command(
        name='carswerve',
        description='Car drifts off highway, sharp turn on road',
        aliases=['distractedcar', 'carexit']
    )
    async def carswerve(self, ctx):
        msg = ctx.message.content

        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        args = msg[len(prefix_used) + len(alias_used):].split(',')


        
        if len(args) > 3:
            await ctx.send(":x: Too many arguments (Max 3)")
            return
        elif len(args) == 1 and args[0] == '':
            await ctx.send("You must specify some text dummy")
            return
        
        image = self.API_Handler.getImgflip("124822590", args)
        
        e = discord.Embed(colour=0x2ECC71)
        e.set_image(url=image)
        e.set_footer(text="Made with ❤️ by Roxiun & Imgflip")

        await ctx.send(embed=e)
    
    @commands.command(
        name='uno',
        description='Draw 25 cards or do something you dont like meme',
        aliases=['unodraw', 'drawcards', 'draw25']
    )
    async def uno(self, ctx):
        msg = ctx.message.content

        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        args = msg[len(prefix_used) + len(alias_used):].split(',')

        
        if len(args) > 3:
            await ctx.send(":x: Too many arguments (Max 2)")
            return
        elif len(args) == 1 and args[0] == '':
            await ctx.send("You must specify some text dummy")
            return

        image = self.API_Handler.getImgflip("93895088", args)
        
        e = discord.Embed(colour=0x2ECC71)
        e.set_image(url=image)
        e.set_footer(text="Made with ❤️ by Roxiun & Imgflip")

    @commands.command(
        name='spank',
        description='Spanks a user',
        aliases=[]
    )
    async def spank(self, ctx, user: discord.User):
        e = discord.Embed(colour=0x2ECC71)
        e.description = f"{user.mention} has been spanked by {ctx.message.author.mention} 😳"

        await ctx.send(embed=e)
        '''
        if len(args) > 3:
            await ctx.send(":x: Too many arguments (Max 2)")
            return
        elif len(args) == 1 and args[0] == '':
            await ctx.send("You must specify some text dummy")
            return

        image = self.API_Handler.getImgflip("93895088", args)
        
        e = discord.Embed(colour=0x2ECC71)
        e.set_image(url=image)
        e.set_footer(text="Made with ❤️ by Roxiun & Imgflip")
        '''

    @commands.command(
        name='meme',
        description='Sends a random meme',
        aliases=['memes','randomeme', 'subreddit']
    )
    async def meme(self, ctx, subreddit: str = None, amount: int = None, time: str = None):
        if not time:
            time = 'month'
        possibletime = ['day','week','month','year']
        time = time.replace("ly", "")
        if not time in possibletime:
            return
        if not subreddit:
            if not amount:
                async with ctx.typing():
                    meme = self.API_Handler.getMeme("dankmemes")
                    e = discord.Embed(colour=0x2ECC71)
                    e.title = f"{meme['title']}"
                    e.set_image(url=meme['url'])
                    e.set_footer(text=f"👍 {meme['upvotes']} | Made with ❤️ by Roxiun")
                    await ctx.send(embed=e)
                    return
            elif amount:
                async with ctx.typing():
                    meme = self.API_Handler.getMeme("dankmemes", amount, time)
                    e = discord.Embed(colour=0x2ECC71)
                    e.title = f"{meme['title']}"
                    e.set_image(url=meme['url'])
                    e.set_footer(text=f"👍 {meme['upvotes']} | Made with ❤️ by Roxiun")
                    await ctx.send(embed=e)
                    return
        elif subreddit:
            if amount:
                async with ctx.typing():
                    meme = self.API_Handler.getMeme(subreddit, amount, time)
                    e = discord.Embed(colour=0x2ECC71)
                    e.title = f"{meme['title']}"
                    e.set_image(url=meme['url'])
                    e.set_footer(text=f"👍 {meme['upvotes']} | Made with ❤️ by Roxiun")
                    await ctx.send(embed=e)
                    return
            else:
                async with ctx.typing():
                    amount = 50
                    meme = self.API_Handler.getMeme(subreddit, amount, time)
                    e = discord.Embed(colour=0x2ECC71)
                    e.title = f"{meme['title']}"
                    e.set_image(url=meme['url'])
                    e.set_footer(text=f"👍 {meme['upvotes']} | Made with ❤️ by Roxiun")
                    await ctx.send(embed=e)
                    return

        e = discord.Embed(description=":no_entry_sign: Something went wrong", colour=0xE74C3C)
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Image(bot))