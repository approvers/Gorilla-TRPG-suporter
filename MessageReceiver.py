from MessagesHolder import MessagesHolder
from PlayersHolder import PlayersHolder
from GameMasterHolder import GameMasterHolder
from lib.plstat import PlayerStatus, GameMaster
from lib.dice import Dice
import copy

class MessageReceiver:

    def __init__(self, message):
        self._msg = MessagesHolder()
        self._players_holder = PlayersHolder()
        self._game_master_holder = GameMasterHolder()

        self._message = message
        self._author = self._message.author
        self._content = self._message.content
        self._channel = self._message.channel
        self._id = self._author.id

        self._user_command = self.get_user_command()



    def get_user_command(self):
        user_command = self._content.split()
        user_command[0] = user_command[0][1:]
        return user_command

    def is_author_bot(self) -> bool:
        return self._author.bot
    def is_our_CLI(self) -> bool:
        return self._author.id in [685457071906619505,685429240908218368,684655652182032404] #ハードコーディング警察だ！！！
    def is_command(self) -> bool:
        return self._content.startswith("!")
    def command_head_is(self, string: str) -> bool:
        return self._user_command[0] == string
    def command_head_is_status(self) -> bool:
        return self._user_command[0] in ["status", "stat"]
    def D_in_command(self) -> bool:
        return "D" in self._user_command[0]

    async def send(self, content=None,):
        await self._channel.send(content)

    async def help(self):
        if not len(self._user_command) >= 2:
            await self.send("ここにhelpのメッセージ")  # ハードコーディング警察だ！！！
            return

        await self.send("各コマンドごとのhelpメッセージ\n流石にこれはjson化する")  # ハードコーディング警察だ！！！

    async def open(self):
        if list(map((lambda x: x.is_gm),self._players_holder.get_players().values())).count(True) >= 1:
            await self.send(self._msg.get_message("commands", "already_opened", self._game_master_holder.get_master().display_name))
            return
            
        self._game_master_holder.set_master(self._author)
        self._players = GameMaster(self._message)
        await self.send(self._msg.get_message("commands", "opened", self._author.display_name))
        
    async def join(self):
        if id in self._players_holder.get_players():
            await self.send(self._msg.get_message("commands", "already_joined", self._players_holder.get_players()[id].name))
            return

        self._players_holder.get_players()[id] = PlayerStatus(self._message)
        await self.send(self._msg.get_message("commands", "joined", self._players_holder.get_players()[id].name))

    async def quit(self):
        if not id in self._players_holder.get_players():
            await self.send(self._msg.get_message("commands","not_joined", format(self._author.display_name)))
            return

        await self.send(self._msg.get_message("commands","quited", self._players_holder.get_players()[id].name))
        if self._players_holder.get_players()[id].is_gm:
            self._game_master_holder.set_master(None)

        self._players_holder.get_players().pop(id)
        
    async def set_status(self):
        if not id in self._players_holder.get_players():
            await self.send(self._msg.get_message("commands", "please_join"))
            return
        
        result = self._players_holder.get_players()[id].set_status(self._message)
        if result == "Success":
            await self.send(self._msg.get_message("status", result))
            return

        await self.send(result)

    async def member(self):
        players = self._players_holder.get_players()
        if players == {}:
            await self.send(self._msg.get_message("commands","no_player"))
            return
            
        display_text = self._msg.get_message("member","list")
        for player in players.values():
            display_text += self._msg.get_message("member","player",player.name)
        await self.send(display_text)

    async def status(self):
        players = self._players_holder.get_players()
        if len(self._user_command) == 0:
            await self.send(players[id].param)
            return

        await self.send(players[id].get_status(self._user_command[1]))

    async def gm(self):
        game_master = self._game_master_holder.get_master()
        if game_master is None:
            await self.send(self._msg.get_message("commands","no_game_master"))
            return
            
        await self.send(self._msg.get_message("commands","who_is_gm",game_master.display_name))

    async def dice(self):
        user_command = self._user_command.copy()
        parameter = self.__read_dice_command(user_command)
        target = None

        if user_command[-1][0] == "(" and user_command[-1][-1] == ")":
            if not user_command[-1][1: -1].isdecimal():
                await self.send("Error:3 can set only Natural Number to target")
                return
            
            target = int(user_command[-1][1:-1])
            del user_command[-1]

        print("--------")
        print(str(user_command))
        print(parameter)
        print(target)
        print("--------")
        dice = Dice(str(user_command)[1:-1], parameter, target)
        if target is None:
            await self.send(dice.dice())
            return

        await self.send(dice.judge())

    def __read_dice_command(self, user_command) -> int:
        parameter = None
        players = self._players_holder.get_players()
        
        if "力" in user_command:
            parameter = players[id].get_status("力")
            user_command.remove("力")
            return parameter
        if "筋力" in user_command:
            parameter = players[id].get_status("筋力")
            user_command.remove("筋力")
            return parameter
        if "パワー" in user_command:
            parameter = players[id].get_status("パワー")
            user_command.remove("パワー")
            return parameter
        if "野生" in user_command:
            parameter = players[id].get_status("野生")
            user_command.remove("野生")
            return parameter