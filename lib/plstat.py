import discord
import traceback
from random import randint

# !joinコマンド発行時にPlayerStatusインスタンスを生成してください。
# ステータスを決めるコマンド(未定)が発行された時はmessageとそのコマンドを呼び出す文言より後をstr型をもつリストでインスタンスメソッド渡してください。
# 引数はmessageを渡してください

class StatusManager:
    def __init__(self):
        self.inital_param = {"chikara":None,"power":None,"kinryoku":None,"yasei":None,"banana":None,"HP":None,"GP":None}
        self.param = {"chikara":None,"power":None,"kinryoku":None,"yasei":None,"banana":None,"HP":None,"GP":None}
    def get_status(self,param):
        pass



class PlayerStatus(StatusManager):
    def __init__(self, message):
        self.id = message.author.id
        self.name = message.author.display_name
        self.author = message.author
        self.type = "Player"
    def set_status(self,message):
        user_params = message.content.split()
        user_params.pop(0)
        if not len(user_params) == 4:
            return "ValueError" #筋力、パワー、力、野生
        if not set(user_params) == set([2, 3, 4, 5]):
            return "StatusError"
        self.kinryoku, self.power, self.chikara, self.yasei = user_params
        self.banana, self.GP, self.HP = 5, 5, int(self.power) * 3 + 10
        return "Success"





class EnemyStatus(StatusManager):
    def __init__(self):
        self.id = randint(100000000000000000, 599999999999999999)
        self.type = "Enemy"
        # 念の為敵にも(たぶん)ユニークなidをもたせておく