import asyncio
import discord
import os


first_channel = 687368620958941237  #ハードコーディング警察だ！！！
token = "TOKEN HERE" #ハードコーディング警察だ！！！



client = discord.Client()



@client.event
async def on_ready():
    channel = client.get_channel(first_channel)
    await channel.send("ログインしました")  #ハードコーディング警察だ！！！



@client.event
async def on_message(message):

    channel = message.channel
    author  = message.author
    content = message.content

    if not author.bot or author.id in [685457071906619505,685429240908218368,684655652182032404]: #ハードコーディング警察だ！！！
        if content.startswith("!"):

            user_command = content.split()
            user_command[0] = user_command[0][1:]

            if user_command[0] == "hi":
                await channel.send("Hi!")



client.run(token)