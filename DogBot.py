import discord
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!dogdors'):
        await client.send_message(message.channel, 'BORK BORK')

    if message.content.startswith('!goodboy'):
        await client.send_message(message.channel, '~Slobber~')

    if message.content.startswith('!votedjeff'):
        await client.send_message(message.channel, 'BORK BORK ~backflip~')

    if message.content.startswith('!scrunch'):
        await client.send_message(message.channel, 'http://orig05.deviantart.net/5703/f/2010/245/f/4/baby_cerberus_by_evolvana-d2xtxtt.jpg')

    if message.content.startswith('!fetch'):
        await client.send_message(message.channel, '~Looks at you and whines (in 3-part harmony)~')

    if message.content.startswith('!sit'):
        await client.send_message(message.channel, 'BORK BORK ~sits~')

    if message.content.startswith('!rollover'):
        await client.send_message(message.channel, '~Looks at you and whines (in 3-part harmony)~')

    if message.content.startswith('!help'):
        await client.send_message(message.channel, 'Commands are: !dogdors; !goodboy; !scrunch; !fetch; !sit; !rollover; !votedjeff')

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Hello {0.mention}, welcome to {1.name}! Check out the pinned messages at the top of this channel for info'
    await client.send_message(server, fmt.format(member, server))

client.run('MjY0NTU1NzQwNDQwNTU5NjI2.C0iSQQ.ljjikBCfW2LZ0Uv4G6JF24kRUrk')
