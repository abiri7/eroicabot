import discord
from discord.ext import commands

class info(commands.Cog):
    
    def __init__(self,client):
        self.client = client

    @client.command(aliases=['1-23'])
    async def storya1ch23(self, ctx):
        await ctx.send(file=discord.File('projects\guides\story1-23guide.png'))

    @client.command()
    async def drge(self, ctx):
        await ctx.send(file=discord.File('projects\guides\drge.png'))

    @client.command()
    async def gift(self, ctx):
        await ctx.send(file=discord.File('projects\guides\afty.png'))

    @client.command()
    async def pport(ctx):
        await ctx.send(file=discord.File('projects\guides\passport.png'))

    @client.command()
    async def carl(ctx):
        await ctx.send(file=discord.File('projects\guides\carriagelist.png'))

    

def setup(client):
    client.add_cog(info(client))