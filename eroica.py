import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('.helpme for more info'))
    print('Bot is ready.')

@client.command()
async def helpme(ctx):
    await ctx.send("""
    Discord bot for Eroica game developed and maintained by Abir & Phuoc
    __Command List__
        .ping  -> display bot latency
        .dl    -> apk download link
        .fback -> google forms dev feedback link
        .character -> write a character name to pull up info courtesy of Sooby
        .1-23  -> story 1-23 guide
        .carl  -> carriage combination list
        .drge  -> dimensional rift gold/equip guide
        .gift  -> affinity gift info
        .pport -> passport dupe guide
        

    A big thank you to those that contributed with guides :D
    v1.1.0b
    This bot was built as the final project to the CIS1051 Course.
    """)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['1-23'])
async def storya1ch23(ctx):
    await ctx.send(file=discord.File('story1-23guide.png'))

@client.command()
async def drge(ctx):
    await ctx.send(file=discord.File('drge.png'))

@client.command()
async def gift(ctx):
    await ctx.send(file=discord.File('afty.png'))

@client.command()
async def dl(ctx):
    await ctx.send('https://apkcombo.com/eroica/com.ftt.eroica.gl.aos/')

@client.command()
async def pport(ctx):
    await ctx.send(file=discord.File('passport.png'))

@client.command()
async def carl(ctx):
    await ctx.send(file=discord.File('carriagelist.png'))

@client.command()
async def fback(ctx):
    await ctx.send('https://docs.google.com/forms/d/e/1FAIpQLScBFE1NZj8fwPMXVE8EI_gd2IflF8bl1rm1NeFVDGDNM_m_YQ/viewform')

@client.command()
async def airi(ctx):
    await ctx.send(file=discord.File('AiriCS.png'))

@client.command()
async def cascarson(ctx):
    await ctx.send(file=discord.File('CascarsonCS.png'))

@client.command()
async def chloe(ctx):
    await ctx.send(file=discord.File('ChloeCS.png'))

@client.command()
async def emuwald(ctx):
    await ctx.send(file=discord.File('EmuwaldCS.png'))

@client.command()
async def florence(ctx):
    await ctx.send(file=discord.File('FlorenceCS.png'))

@client.command()
async def freyja(ctx):
    await ctx.send(file=discord.File('FreyjaCS.png'))

@client.command()
async def gaffs(ctx):
    await ctx.send(file=discord.File('GaffsCS.png'))
    
@client.command()
async def guts(ctx):
    await ctx.send(file=discord.File('GutsCS.png'))

@client.command()
async def kipkirui(ctx):
    await ctx.send(file=discord.File('KipkiruiCS.png'))

@client.command()
async def lenn(ctx):
    await ctx.send(file=discord.File('LennCS.png'))

@client.command()
async def lisa(ctx):
    await ctx.send(file=discord.File('LisaCS.png'))
    
@client.command()
async def luna(ctx):
    await ctx.send(file=discord.File('LunaCS.png'))

@client.command()
async def marion(ctx):
    await ctx.send(file=discord.File('MarionCS.png'))

@client.command()
async def melavi(ctx):
    await ctx.send(file=discord.File('MelaviCS.png'))

@client.command()
async def milena(ctx):
    await ctx.send(file=discord.File('MilenaCS.png'))

@client.command()
async def muto(ctx):
    await ctx.send(file=discord.File('MutoCS.png'))

@client.command()
async def nene(ctx):
    await ctx.send(file=discord.File('NeneCS.png'))

@client.command()
async def nero(ctx):
    await ctx.send(file=discord.File('NeroCS.png'))

@client.command()
async def orslaha(ctx):
    await ctx.send(file=discord.File('OrslahaCS.png'))

@client.command()
async def retinya(ctx):
    await ctx.send(file=discord.File('RetinyaCS.png'))

@client.command()
async def sei(ctx):
    await ctx.send(file=discord.File('SeiCS.png'))

@client.command()
async def soare(ctx):
    await ctx.send(file=discord.File('SoareCS.png'))

@client.command()
async def stella(ctx):
    await ctx.send(file=discord.File('StellaCS.png'))

@client.command()
async def sumi(ctx):
    await ctx.send(file=discord.File('SumiCS.png'))

@client.command()
async def wraith(ctx):
    await ctx.send(file=discord.File('WraithCS.png'))

@client.command()
async def xenia(ctx):
    await ctx.send(file=discord.File('XeniaCS.png'))


#@client.event
#async def on_member_join(member):
#    print(f'{member} has joined the server.')

#@client.event
#async def on_member_remove(member):
#    print(f'{member} has left the server.')

client.run('ODE1Mjg0Mjg4MDg5ODgyNzE0.YDqKqQ.e755GdUbM3Cga1_ylAMyKb89Jr0')