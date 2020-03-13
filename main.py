import asyncio
import discord
import os

from lib.plstat import *
from jsonmes import *
from lib.dice import Dice


token = os.environ["TOKEN"]
game_master = None
msg = JSONMessage()
players = {}



client = discord.Client()



@client.event
async def on_ready():
    pass
    # ここに起動時(Discord接続完了時)に実行したい処理を書こうね



@client.event
async def on_message(message):

    global game_master  #まじでこめん
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

            elif user_command[0] == "open":
                if list(map((lambda x: x.is_gm),players.values())).count(True) >= 1:
                    await channel.send(msg.get_message("commands", "already_opened", game_master.display_name))
                else:
                    game_master = message.author
                    players[id] = GameMaster(message)
                    await channel.send(msg.get_message("commands", "opened", author.display_name))

            elif user_command[0] == "join":
                if id in players.keys():
                    await channel.send(msg.get_message("commands","already_joined",players[id].name))
                    if id == game_master.id:
                        await channel.send(msg.get_message("commands", "you_are_GM", players[id].name))
                else:
                    if game_master is None:
                        await channel.send(msg.get_message("commands","no_game_master"))
                    else:
                        players[id] = PlayerStatus(message)
                        await channel.send(msg.get_message("commands","joined",players[id].name))

            elif user_command[0] == "quit":
                if id in players:
                    await channel.send(msg.get_message("commands","quited", players[id].name))
                    if players[id].is_gm:
                        game_master = None
                    players.pop(id)
                else:
                    await channel.send(msg.get_message("commands","not_joined", format(author.display_name)))

            elif user_command[0] == "set":
                if user_command[1] == "help":
                    await channel.send(msg.get_message("help","set"))
                elif id in players:
                    result = players[id].set_status(message)
                    if result == "Success":
                        await channel.send(msg.get_message("status",result))
                    else:
                        await channel.send(result)
                else:
                    await channel.send(msg.get_message("commands","please_join"))

            elif user_command[0] == "member":
                if players == {}:
                    await channel.send(msg.get_message("commands","no_player"))
                else:
                    display_text = msg.get_message("member","list")
                    for player in players.values():
                        display_text += msg.get_message("member","player",player.name)
                    await channel.send(display_text)

            elif user_command[0] in ["status", "stat"]:
                if len(user_command) == 0:
                    await channel.send(players[id].param)
                else:
                    await channel.send(players[id].get_status(user_command[1]))

            elif user_command[0] == "gm":
                if game_master is None:
                    await channel.send(msg.get_message("commands","no_game_master"))
                else:
                    await channel.send(msg.get_message("commands","who_is_gm",game_master.display_name))


            elif "D" in user_command[0]:
                p = None
                target = None

                if "力" in user_command:
                    p = players[id].get_status("力")
                    user_command.remove("力")
                elif "筋力" in user_command:
                    p = players[id].get_status("筋力")
                    user_command.remove("筋力")
                elif "パワー" in user_command:
                    p = players[id].get_status("パワー")
                    user_command.remove("パワー")
                elif "野生" in user_command:
                    p = players[id].get_status("野生")
                    user_command.remove("野生")

                if user_command[-1][0] == "(" and user_command[-1][-1] == ")":
                    if user_command[-1][1: -1].isdecimal():
                        target = int(user_command[-1][1:-1])
                        del user_command[-1]
                    else:
                        await channel.send("Error:3 can set only Natural Number to target")
                        return
                dice = Dice(str(user_command)[1:-1], p, target)
                if target is None:
                    await channel.send(dice.dice())
                else:
                    await channel.send(dice.judge())

                    

client.run(token)
