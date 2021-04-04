import discord
from discord.ext import commands

class charas(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @client.command()
    async def airi(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\AiriCS.png'))

    @client.command()
    async def cascarson(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\CascarsonCS.png'))

    @client.command()
    async def chloe(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\ChloeCS.png'))

    @client.command()
    async def emuwald(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\EmuwaldCS.png'))

    @client.command()
    async def florence(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\FlorenceCS.png'))

    @client.command()
    async def freyja(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\FreyjaCS.png'))

    @client.command()
    async def gaffs(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\GaffsCS.png'))
    
    @client.command()
    async def guts(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\GutsCS.png'))

    @client.command()
    async def kipkirui(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\KipkiruiCS.png'))

    @client.command()
    async def lenn(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\LennCS.png'))

    @client.command()
    async def lisa(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\LisaCS.png'))
    
    @client.command()
    async def luna(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\LunaCS.png'))

    @client.command()
    async def marion(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\MarionCS.png'))

    @client.command()
    async def melavi(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\MelaviCS.png'))

    @client.command()
    async def milena(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\MilenaCS.png'))

    @client.command()
    async def muto(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\MutoCS.png'))

    @client.command()
    async def nene(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\NeneCS.png'))

    @client.command()
    async def nero(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\NeroCS.png'))

    @client.command()
    async def orslaha(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\OrslahaCS.png'))

    @client.command()
    async def retinya(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\RetinyaCS.png'))

    @client.command()
    async def sei(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\SeiCS.png'))

    @client.command()
    async def soare(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\SoareCS.png'))

    @client.command()
    async def stella(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\StellaCS.png'))

    @client.command()
    async def sumi(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\SumiCS.png'))

    @client.command()
    async def wraith(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\WraithCS.png'))

    @client.command()
    async def xenia(self, ctx):
        await ctx.send(file=discord.File('projects\\characters\\XeniaCS.png'))

def setup(client):
    client.add_cog(charas(client))