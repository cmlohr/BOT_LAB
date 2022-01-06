import os
import discord
import random
import responses

my_secret = os.environ['TOKEN']
client = discord.Client()


def rand_8ball():
    random_8ball = random.choice(responses.predictions_8ball)
    print(random_8ball)
    return random_8ball


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$8ball"):
        await message.channel.send(rand_8ball())


client.run(my_secret)
