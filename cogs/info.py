import discord
from discord.ext import commands

class info(commands.Cog):
    
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on ready(self):
        await client.change_presence(activity=discord.Game('.helpme for more info'))
        print('Bot is ready.')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

    @client.command()
    async def helpme(self, ctx):
        await ctx.send("""
        Discord bot for Eroica game developed and maintained by Crow#2300
        __Command List__
        .ping  -> display bot latency
        .dl    -> apk download link
        .fback -> google forms dev feedback link
        .1-23  -> story 1-23 guide
        .carl  -> carriage combination list
        .drge  -> dimensional rift gold/equip guide
        .gift  -> affinity gift info
        .pport -> passport dupe guide

        A big thank you to those that contributed with guides :D
        v1.0.5
        """)

    @client.command()
    async def dl(self, ctx):
        await ctx.send('https://apkcombo.com/eroica/com.ftt.eroica.gl.aos/')

    @client.command()
    async def fback(self, ctx):
        await ctx.send('https://docs.google.com/forms/d/e/1FAIpQLScBFE1NZj8fwPMXVE8EI_gd2IflF8bl1rm1NeFVDGDNM_m_YQ/viewform')


def setup(client):
    client.add_cog(info(client))