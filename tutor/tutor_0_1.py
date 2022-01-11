import os
import discord


my_secret = os.environ['TOKEN']
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in a {0.user}.'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

# HTML
    if message.content.startswith("$What is HTML?"):
        await message.channel.send("The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")   
    if message.content.startswith("$what is HTML?"):
        await message.channel.send("The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")   
    if message.content.startswith("$What is html?"):
        await message.channel.send("The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.")   
    if message.content.startswith("$what is html?"):
        await message.channel.send("The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.") 
    if message.content.startswith("$what is html"):
        await message.channel.send("The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.") 
    if message.content.startswith("$What is HTML"):
        await message.channel.send("The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.") 
    if message.content.startswith("$What is html"):
        await message.channel.send("The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.") 
    if message.content.startswith("$html"):
        await message.channel.send("The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.") 
    if message.content.startswith("$HTML"):
        await message.channel.send("The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.") 
    if message.content.startswith("$html?"):
        await message.channel.send("The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.") 
    if message.content.startswith("$HTML?"):
        await message.channel.send("The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.") 
# CSS
    if message.content.startswith("$What is CSS?"):
        await message.channel.send("Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")   
    if message.content.startswith("$what is CSS?"):
        await message.channel.send("Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")   
    if message.content.startswith("$What is css?"):
        await message.channel.send("Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")   
    if message.content.startswith("$what is css?"):
        await message.channel.send("Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.") 
    if message.content.startswith("$what is css"):
        await message.channel.send("Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.") 
    if message.content.startswith("$What is CSS"):
        await message.channel.send("Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.") 
    if message.content.startswith("$What is css"):
        await message.channel.send("Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.") 
    if message.content.startswith("$css"):
        await message.channel.send("Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.") 
    if message.content.startswith("$CSS"):
        await message.channel.send("Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.") 
    if message.content.startswith("$css?"):
        await message.channel.send("Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.") 
    if message.content.startswith("$CSS?"):
        await message.channel.send("Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.")

#javascript and js
    if message.content.startswith("$What is JavaScript?"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")   
    if message.content.startswith("$what is JavaScript?"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")   
    if message.content.startswith("$What is javascript?"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")   
    if message.content.startswith("$what is javascript?"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.") 
    if message.content.startswith("$what is javascript"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.") 
    if message.content.startswith("$What is JavaScript"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.") 
    if message.content.startswith("$What is javascript"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.") 
    if message.content.startswith("$js"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.") 
    if message.content.startswith("$JS"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.") 
    if message.content.startswith("$js?"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.") 
    if message.content.startswith("$JS?"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")
    if message.content.startswith("$javascript"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.") 
    if message.content.startswith("$JavaScript"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.") 
    if message.content.startswith("$javascript?"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.") 
    if message.content.startswith("$JavaScript?"):
        await message.channel.send("JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")



client.run(my_secret)
