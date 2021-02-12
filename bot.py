# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# represents connection to Discord
# handles events, tracks state, interacts with Discord APIs
client = discord.Client()

# event handler
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)