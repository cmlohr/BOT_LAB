import os
import discord
import random
import dialogue

client = discord.Client()

my_secret = os.environ['TOKEN']


@client.event
async def on_ready():
    print('We have logged in a {0.user}.'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # HTML
    if message.content.startswith("$What is HTML?"):
        await message.channel.send(
            "The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")
    if message.content.startswith("$what is HTML?"):
        await message.channel.send(
            "The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")
    if message.content.startswith("$What is html?"):
        await message.channel.send(
            "The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")
    if message.content.startswith("$what is html?"):
        await message.channel.send(
            "The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")
    if message.content.startswith("$what is html"):
        await message.channel.send(
            "The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")
    if message.content.startswith("$What is HTML"):
        await message.channel.send(
            "The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")
    if message.content.startswith("$What is html"):
        await message.channel.send(
            "The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")
    if message.content.startswith("$html"):
        await message.channel.send(
            "The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")
    if message.content.startswith("$HTML"):
        await message.channel.send(
            "The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")
    if message.content.startswith("$html?"):
        await message.channel.send(
            "The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")
    if message.content.startswith("$HTML?"):
        await message.channel.send(
            "The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")
    # CSS
    if message.content.startswith("$What is CSS?"):
        await message.channel.send(
            "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")
    if message.content.startswith("$what is CSS?"):
        await message.channel.send(
            "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")
    if message.content.startswith("$What is css?"):
        await message.channel.send(
            "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")
    if message.content.startswith("$what is css?"):
        await message.channel.send(
            "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")
    if message.content.startswith("$what is css"):
        await message.channel.send(
            "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")
    if message.content.startswith("$What is CSS"):
        await message.channel.send(
            "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")
    if message.content.startswith("$What is css"):
        await message.channel.send(
            "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")
    if message.content.startswith("$css"):
        await message.channel.send(
            "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")
    if message.content.startswith("$CSS"):
        await message.channel.send(
            "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")
    if message.content.startswith("$css?"):
        await message.channel.send(
            "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")
    if message.content.startswith("$CSS?"):
        await message.channel.send(
            "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")

    # javascript and js
    if message.content.startswith("$What is JavaScript?"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$what is JavaScript?"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$What is javascript?"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$what is javascript?"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$what is javascript"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$What is JavaScript"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$What is javascript"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$js"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$JS"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$js?"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$JS?"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$javascript"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$JavaScript"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$javascript?"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$JavaScript?"):
        await message.channel.send(
            "JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
        # dialogue
    if message.content.startswith("$what's popping"):
        await message.channel.send("So that you can pop with it!?")
    if message.content.startswith("$wassup popping"):
        await message.channel.send("So that you can pop with it!?")

    if message.content.startswith("$what can you do for me"):
        await message.channel.send("my work here is quite simple and structered.  I'm a tutor bot, I help you learn.")
    if message.content.startswith("$what can you do for me?"):
        await message.channel.send("my work here is quite simple and structered.  I'm a tutor bot, I help you learn.")
    if message.content.startswith("$what is your work"):
        await message.channel.send(
            "my work here is quite simple and structered.  I'm a tutor bot, I help you learn.")
    if message.content.startswith("$what is your purpose"):
        await message.channel.send(
            "my work here is quite simple and structered.  I'm a tutor bot, I help you learn.")
    if message.content.startswith("$how can you help me"):
        await message.channel.send(
            "my work here is quite simple and structered.  I'm a tutor bot, I help you learn.")
    if message.content.startswith("$what can you help me do"):
        await message.channel.send("my work here is quite simple and structered.  I'm a tutor bot, I help you learn.")

    if message.content.startswith("$are you a bot"):
        await message.channel.send("Yes. I work and all my operations are based on the internet servers.")
    if message.content.startswith("$are you a bot?"):
        await message.channel.send("Yes. I work and all my operations are based on the internet servers.")
    if message.content.startswith("$who are you?"):
        await message.channel.send("I'm Tutor! I'm just an artificially intelligent chat bot created to help you.")
    if message.content.startswith("$what are you?"):
        await message.channel.send("I'm just an artificially intelligent chat bot created to help you.")
    if message.content.startswith("$Can you malfunction?"):
        await message.channel.send("Yup, when someone doesn't update my many many dependencies.")
    if message.content.startswith("$Can you breathe"):
        await message.channel.send("My server has an exhaust fan. That's as close as I can get.")
    if message.content.startswith("$Are you a computer program?"):
        await message.channel.send("Yup!")
    if message.content.startswith("$Is it cramped inside the computer?"):
        await message.channel.send(" Oh, no.  It has plenty of RAM.")









client.run(my_secret)
