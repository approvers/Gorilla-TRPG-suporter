import asyncio
import discord
import os

from lib.plstat import *
from lib.dice import Dice


token = os.environ["TOKEN"]
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
                    await channel.send("各コマンドごとのhelpメッセージ\n流石にこれはjson化する")

            elif user_command[0] == "join":
                if id in players:
                    await channel.send("{}さんはすでに参加を受け付けています！".format(players[id].name))  # ハードコーディング警察だ！！！
                else:
                    players[id] = PlayerStatus(message)
                    await channel.send("{}さんの参加を受け付けました！".format(players[id].name)) #ハードコーディング警察だ！！！

            elif user_command[0] == "quit":
                if id in players:
                    await channel.send("{}さんの参加を取り消しました！".format(players[id].name))  # ハードコーディング警察だ！！！
                    players.pop(id)
                else:
                    await channel.send("{}さんはゲームに参加していません！".format(author.display_name))  # ハードコーディング警察だ！！！

            elif user_command[0] == "set":
                if user_command[1] == "help":
                    await channel.send("```!set <筋力> <パワー> <力> <野生>```")  # ハードコーディング警察だ！！！
                elif id in players:
                    result = players[id].set_status(message)
                    if result == "ValueError":
                        await channel.send("ステータスの数が間違っています！")  # ハードコーディング警察だ！！！
                    elif result == "StatusError":
                        await channel.send("ステータスの値が間違っています！\n[2,3,4,5]すべてを一つずつどれかのステータスに振ってください。")  # ハードコーディング警察だ！！！
                    elif result == "Success":
                        await channel.send("ステータスの設定が完了しました！") #ハードコーディング警察だ！！！
                else:
                    await channel.send("先に```!join```で参加登録してください") #ハードコーディング警察だ！！！

            elif user_command[0] == "member":
                if players == {}:
                    await channel.send("参加登録している人はいません！")  # ハードコーディング警察だ！！！
                else:
                    display_text = "***参加者一覧***\n"
                    for player in players.values():  # ハードコーディング警察だ！！！
                        display_text += "・**{}**\n".format(player.name)  # ハードコーディング警察だ！！！
                    await channel.send(display_text)

            elif user_command[0] == "status" or "stat":
                if user_command[1] is None:
                    await channel.send(players[id].param)
                else:
                    await channel.send(players[id].get_status(user_command[1]))
            
            elif "D" in user_command[0]:
                p = None
                target = None

                if "力" in user_command:
                    p = channel[id].get_status("力")
                    user_command.remove("力")
                elif "筋力" in user_command:
                    p = channel[id].get_status("筋力")
                    user_command.remove("筋力")
                elif "パワー" in user_command:
                    p = channel[id].get_status("パワー")
                    user_command.remove("パワー")
                elif "野生" in user_command:
                    p = channel[id].get_status("野生")
                    user_command.remove("野生")
                
                if user_command[-1][0] == "(" and user_command[-1][-1] == ")":
                    if user_command[-1][1: -1].isdecimal():
                        target = int(user_command[-1][1:-1])
                        del user_command[-1]
                    await channel.send("Error:3 can set only Natural Number to target")
                    return 
                dice = Dice(str(user_command), p, target)
                if target is None:
                    await channel.send(dice.dice())
                else:
                    await channel.send(dice.judge())
                    

client.run(token)
