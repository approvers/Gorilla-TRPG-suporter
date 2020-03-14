import asyncio
import discord
import os

from MessageReceiver import MessageReceiver



token = os.environ["TOKEN"]

client = discord.Client()


@client.event
async def on_ready():
    pass
    # ここに起動時(Discord接続完了時)に実行したい処理を書こうね



@client.event
async def on_message(message):
    receiver = MessageReceiver(message)

    if receiver.is_author_bot() and not receiver.is_our_CLI():
        return
    if not receiver.is_command():
        return

    if receiver.command_head_is("hi"):
        await receiver.send("Hi!")
        return

    if receiver.command_head_is("help"):
        await receiver.help()
        return
        
    if receiver.command_head_is("open"):
        await receiver.open()
        return

    if receiver.command_head_is("join"):
        await receiver.join()
        return
        
    if receiver.command_head_is("quit"):
        await receiver.quit()
        return
        
    if receiver.command_head_is("set"):
        await receiver.set_status()
        return
        
    if receiver.command_head_is("member"):
        await receiver.member()
        return
        
    if receiver.command_head_is_status():
        await receiver.status()
        return

    if receiver.command_head_is("gm"):
        await receiver.gm()
        return

    if receiver.D_in_command():
        await receiver.dice()
        return
        
                    

client.run(token)