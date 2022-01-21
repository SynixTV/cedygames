import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Ok')

client.run('OTM0MDc2MjM0OTQwNDIwMTc2.Yeq0SA.UWRsCZHNvrdxUxPL77owAFAz3Bw')
