import os
import requests
import discord
import asyncio

# url to retrieve messages from
URL = "http://foxhole-bounties.herokuapp.com/get_messages"

# Period to sleep for before sending more messages
PERIOD = 30

def request_messages():
    
    print("Sending Request...")

    headers= { "secret" : os.environ.get("MESSAGE_KEY") }

    r = requests.get(url=URL,headers=headers)

    print(r.json())

    data = r.json()["messages"]

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
