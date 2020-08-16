# bot.py
import os
import time
import discord
from datetime import datetime as dt
import schedule
from dotenv import load_dotenv
import requests
import json
import hashlib

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

def get_quote():
    url="https://quotes.rest/qod?language=en"
    page = requests.get(url)    
    content = page.content.decode("utf-8")
    new_content = json.loads(content)
    quote = new_content["contents"]["quotes"][0]["quote"]
    return quote


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} is connected to the following guild:')
    while True:
        naive_dt = dt.now()
        current_time = naive_dt.strftime("%H:%M:%S")
        print
        if current_time == "00:10:00":
            message = get_quote()
            channel = client.get_channel(740299223337009172)
            await channel.send(message)
            time.sleep(1)


client.run(TOKEN)
