import asyncio
import discord
import os

from lib.plstat import *



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


client.run(token)