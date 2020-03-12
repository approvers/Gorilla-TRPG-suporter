import discord

# !joinコマンド発行時にPlayerStatusインスタンスを生成してください。
# ステータスを決めるコマンド(未定)が発行された時はそのコマンドを呼び出す文言以降をstr型をもつリストでインスタンスメソッド渡してください。
# 引数はmessageを渡してください

class StatusManager:
    def __init__(self):
        self.param = {"chikara":None,"power":None,"kinryoku":None,"yasei":None,"banana":None,"HP":None,"GP":None}
    def get_status(self,param):
        pass

    @classmethod
    def get_player_names(cls):
        pass


class PlayerStatus(StatusManager):
    def __init__(self, message):
        self.message = message
        self.id = message.author.id
        self.name = message.author.display_name
        self.type = "Player"
    def set_status(self,message):


class EnemyStatus(StatusManager):
    def __init__(self):
        self.type = "Enemy"