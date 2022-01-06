import os
import discord
import random
import prob

my_secret = os.environ['TOKEN']
client = discord.Client()

def coin_flip():
    flip = random.choice(prob.coin_flipped)
    print(flip)
    return flip

def roll_dice(x):
    roll_array = []
    while x > 0:
        roll_array.append(random.choice(prob.dice_bag))
        x -= 1
    dice_rolled = " ".join(roll_array)
    return dice_rolled

@client.event
async def on_ready():
    print('We have logged in a {0.user}.'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return


# roll the dice
    if message.content.startswith("$roll 1"):
        await message.channel.send(roll_dice(1))   

    if message.content.startswith("$roll 2"):
        await message.channel.send(roll_dice(2))  

    if message.content.startswith("$roll 3"):
        await message.channel.send(roll_dice(3)) 

    if message.content.startswith("$roll 4"):
        await message.channel.send(roll_dice(4)) 

    if message.content.startswith("$roll 5"):
        await message.channel.send(roll_dice(5)) 

    if message.content.startswith("$roll 6"):
        await message.channel.send(roll_dice(6))  



# flip a coin 50/50
    if message.content.startswith("$flip"):
        await message.channel.send(coin_flip())
    
    if message.content.startswith("$Flip"):
        await message.channel.send(coin_flip())

    if message.content.startswith("$coin"):
        await message.channel.send(coin_flip())

    if message.content.startswith("$Coin"):
        await message.channel.send(coin_flip())

client.run(my_secret)
