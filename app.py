import os
import requests
import discord
import asyncio
from requests.structures import CaseInsensitiveDict

# Period to sleep for before sending more messages
PERIOD = 30

def request_messages():

    # url to retrieve messages from
    URL = os.environ.get("DJANGO_URL")

    data = {}
    
    print("Sending Request...")

    headers = CaseInsensitiveDict()
    headers["Origin"] = "https://foxhole-bounty-bot.herokuapp.com"
    headers["Access-Control-Request-Method"] = "GET"
    headers["secret"] = os.environ.get("MESSAGE_KEY")

    try:
        r = requests.get(url=URL,headers=headers)

        print(r)
        print(r.json())

        data = r.json()["messages"]
    except:
        print("Failed to send request")

    return data

client = discord.Client()

@client.event
async def on_ready():

    print(f'We have logged in as {client.user}')

    while True:
        await get_messages()

async def get_messages():
    
    messages = request_messages()

    for user in messages:
        await send_message(user,messages[user])

    print("Sleeping...")
    await asyncio.sleep(PERIOD)

async def send_message(target,payload):
    try:
        user = await client.fetch_user(target)
        await user.send(payload)
    except:
        print("Could not message user!")

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
client.run(DISCORD_BOT_TOKEN)
