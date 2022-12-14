import os
import discord
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'c/verify':
        user = message.author
        role = discord.utils.get(user.guild.roles, name="Verified")
        await user.add_roles(role)
        await message.add_reaction('\U00002705')

client.run(TOKEN)