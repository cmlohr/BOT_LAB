import requests
import discord
import datetime as dt
import finnhub


my_secret = 'TOKEN'
client = discord.Client()
ALPHA_END_POINT = "https://www.alphavantage.co/query"

finnhub_client = finnhub.Client(api_key="SECRET")

UP = "🔺"
DOWN = "🔻"

# Getting the date
date = dt.datetime.now()

today_day = '{:02d}'.format(date.day)
today_month = '{:02d}'.format(date.month)
today_year = '{:02d}'.format(date.year)

current_date = today_year + '-' + today_month + '-' + today_day
# current_date minus 1 day
yesterday_date = dt.datetime.now() - dt.timedelta(days=1)
print(current_date)
time = dt.datetime.now() + dt.timedelta(hours=1)

hour = '{:02d}'.format(time.hour)
# hour plus one hour
next_hour = '{:02d}'.format(time.hour + 1)

minute = '{:02d}'.format(time.minute)
second = '{:02d}'.format(time.second)


@client.event
async def on_ready():
    print('We have logged in a {0.user}.'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$price"):
        x = message.content.split()
        stock = x[1]
        print(stock)
        get_price = finnhub_client.quote(stock)['c']


        await message.channel.send(f"{stock}: {get_price} @ close")




client.run(my_secret)


