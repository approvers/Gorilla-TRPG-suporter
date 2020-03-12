import discord
import traceback
from random import randint

# !joinコマンド発行時にPlayerStatusインスタンスを生成してください。
# ステータスを決めるコマンド(未定)が発行された時はmessageとそのコマンドを呼び出す文言より後をstr型をもつリストでインスタンスメソッド渡してください。
# 引数はmessageを渡してください

class StatusManager:
    def __init__(self):
        self.param_initial = {"kinryoku":None,"power":None,"chikara":None,"yasei":None,"banana":5,"GP":5,"HP":None}
        self.param = {"kinryoku":None,"power":None,"chikara":None,"yasei":None,"banana":5,"GP":5,"HP":None}
    def get_status(self,param):
        pass



class PlayerStatus(StatusManager):
    def __init__(self, message):
        super().__init__()
        self.id = message.author.id
        self.name = message.author.display_name
        self.author = message.author
        self.type = "Player"
    def set_status(self,message):
        user_params = message.content.split()
        user_params.pop(0)
        user_params = list(map(lambda x: int(x),user_params))
        if not len(user_params) == 4:
            return "ValueError" #筋力、パワー、力、野生
        if not set(user_params) == set([2, 3, 4, 5]):
            return "StatusError"
        self.param_initial["kinryoku"], self.param_initial["power"],self.param_initial["chikara"], self.param_initial["yasei"] = user_params
        self.param_initial["HP"] = self.param_initial["power"] * 3 + 10
        self.param = self.param_initial



        return "Success"





class EnemyStatus(StatusManager):
    def __init__(self):
        super().__init__()
        self.id = randint(100000000000000000, 599999999999999999)
        self.type = "Enemy"
        # 念の為敵にも(たぶん)ユニークなidをもたせておく