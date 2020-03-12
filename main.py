import asyncio
import discord
import os

from lib.plstat import *
from jsonmes import *



token = os.environ["TOKEN"]
msg = JSONMessage()
players = {}



client = discord.Client()



@client.event
async def on_ready():
    pass
    # ここに起動時(Discord接続完了時)に実行したい処理を書こうね



@client.event
async def on_message(message):

    channel = message.channel
    author  = message.author
    id = message.author.id
    content = message.content

    if not author.bot or id in [685457071906619505,685429240908218368,684655652182032404]: #ハードコーディング警察だ！！！
        if content.startswith("!"):

            user_command = content.split()
            user_command[0] = user_command[0][1:]

            if user_command[0] == "hi":
                await channel.send("Hi!")

            elif user_command[0] == "help":
                if not len(user_command) >= 2:
                    await channel.send("ここにhelpのメッセージ")  # ハードコーディング警察だ！！！
                else:
                    await channel.send("各コマンドごとのhelpメッセージ\n流石にこれはjson化する")  # ハードコーディング警察だ！！！

            elif user_command[0] == "join":
                if id in players:
                    await channel.send(msg.get_message("commands","already_joined").format(players[id].name))
                else:
                    players[id] = PlayerStatus(message)
                    print(msg.get_message("commands","joined"))
                    await channel.send(msg.get_message("commands","joined").format(players[id].name))

            elif user_command[0] == "quit":
                if id in players:
                    await channel.send(msg.get_message("commands","quited").format(players[id].name))
                    players.pop(id)
                else:
                    await channel.send(msg.get_message("commands","not_joined").format(author.display_name))

            elif user_command[0] == "set":
                if user_command[1] == "help":
                    await channel.send(msg.get_message("help","set"))
                elif id in players:
                    result = players[id].set_status(message)
                    if result == "ValueError":
                        await channel.send(msg.get_message("status",result))
                    elif result == "StatusError":
                        await channel.send(msg.get_message("status",result))
                    elif result == "Success":
                        await channel.send(msg.get_message("status",result))
                else:
                    await channel.send(msg.get_message("commands","please_join"))

            elif user_command[0] == "member":
                if players == {}:
                    await channel.send(msg.get_message("commands","no_player"))
                else:
                    display_text = msg.get_message("member","list")
                    for player in players.values():
                        display_text += msg.get_message("member","player").format(player.name)
                    await channel.send(display_text)

            elif user_command[0] == "status" or "stat":
                if user_command[1] is None:
                    await channel.send(players[id].param)
                else:
                    await channel.send(players[id].get_status(user_command[1]))


client.run(token)