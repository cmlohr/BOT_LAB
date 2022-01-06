import os
import discord
import random
import wyr

my_secret = os.environ['TOKEN']
client = discord.Client()

def rand_would_you_rather():
    random_wyr = random.choice(wyr.would_you_rather_array)
    return random_wyr

@client.event
async def on_ready():
    print('We have logged in a {0.user}.'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$WYR"):
        await message.channel.send(rand_would_you_rather())

    if message.content.startswith("$wyr"):
        await message.channel.send(rand_would_you_rather())

client.run(my_secret)
