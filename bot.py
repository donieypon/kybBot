# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='-', intents=intents)
name = 'KYB'
actives = ["Alex", "Amol", "Ashana", "Brandon", "Casey", "Cuong", "Derek", "Daniel", "Darren", "Donie", "Elizabeth", "Eloisa", "Eric"]

def randomPairs(diff):
  listofpairs = []
  tobepaired = actives
  length = len(tobepaired) - 2
  i = 0
  map = set()

  while i <= length:
    index = random.randint(0, (len(tobepaired) - 1))

    while i == index and tobepaired[index] in map:
        index = random.randint(0, (len(tobepaired) - 1))

    while(tobepaired[i] in map):
        i = i + 1
    pair = []
    pair.append(tobepaired[i])
    pair.append(tobepaired[index])
    listofpairs.append(pair)
    map.add(tobepaired[i])
    map.add(tobepaired[index])
    i = i + 1
  return listofpairs


def printPairs(listpairs):
    for pairs in listpairs:
        for pair in pairs:
            print(f'Pair: {pair}')
        print('\n')

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    for member in guild.members:
        for role in member.roles:
            if role.name == "Active":
                #actives.append(member.name)
                print(f'Role Active: {len(actives)}')

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.command()
async def pair(ctx, arg):
    # guild = ctx.message.guild
    # category = discord.utils.get(ctx.guild.categories, name=name)
    # await ctx.guild.create_text_channel(f'kyb {arg}', category=category)
    await ctx.send(f'Pairing!')
    list = randomPairs(arg)
    print(list)

client.run(TOKEN)


