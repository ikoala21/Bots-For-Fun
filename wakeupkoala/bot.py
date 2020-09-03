# bot.py
import os
import time
import discord
from datetime import datetime as dt
from dotenv import load_dotenv
import requests
import json
import hashlib
import pytz
from requests.adapters import HTTPAdapter


IST = pytz.timezone('Asia/Kolkata')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

def get_quote():
    s = requests.Session()
    url="https://quotes.rest/qod?language=en"
    s.mount(url, HTTPAdapter(max_retries=5))
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
        naive_dt = dt.now(IST)
        current_time = naive_dt.strftime("%H:%M:%S")
        if current_time == "22:07:00":
            try:
                message = get_quote()
                channel = client.get_channel(740299223337009172)
                await channel.send(message)
                time.sleep(1)
            except:
                channel = client.get_channel(740299223337009172)
                await channel.send("API did not respond!")


client.run(TOKEN)