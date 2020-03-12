import json
from random import randint

import discord


class StatusManager:
    """
    ゲーム内のオブジェクト(プレイヤー,敵,GM)をつくるための親クラス
    直接このクラスのインスタンスを生成したりはしないでね♡
    """

    def __init__(self):
        """
        初期化処理を行う
        とりあえずすべてNoneの状態で param_initial param 辞書を宣言
        """
        param_none = {"kinryoku": None, "power": None, "chikara": None,
                      "yasei": None, "banana": 5, "GP": 5, "HP": None}
        self.param_initial = param_none
        self.param = param_none
        self.is_gm = False

    def get_status(self, param, is_initial=False):
        """
        該当するステータス(現在値)を返してくれる
        Parameters
        ---------
        param: str
            取得したいパラメーターの名前
        is_initial: bool
            取得したいのが初期値かどうかTrueで初期値を返すことになる、デフォルト値はFalse
        Returns
        ---------
        parameter: int
            実際のパラメーター 設定されていなければ None を返す
        """
        if not is_initial:
            if not param in self.param_initial:
                raise ValueError("指定されたパラメーターは存在しません")
            else:
                return self.param_initial[param]
        else:
            if not param in self.param:
                raise ValueError("指定されたパラメーターは存在しません")
            else:
                return self.param[param]


class PlayerStatus(StatusManager):
    def __init__(self, message):
        """
        Playerの状態を司るPlayerStatusオブジェクトを生成する
        !join 時に message を渡してこのクラスのインスタンスを生成してください
        Parameters
        ---------
        message: discord.message.Message
            discord.pyからもらえるやつ
        """
        super().__init__()
        self.type = "Player"
        self.user = message.author
        self.id = message.author.id
        self.name = message.author.display_name

    def set_status(self, message):
        """
        Playerの状態(初期状態)を定める
        !set 時に message を渡してインスタンス関数を呼び出してください
        Parameters
        ---------
        message: discord.message.Message
            discord.pyからもらえるやつ
        """
        user_params = message.content.split()
        user_params.pop(0)
        user_params = list(map(lambda x: int(x), user_params))

        if not len(user_params) == 4:
            return "ValueError"
        if not {2, 3, 4, 5} == set(user_params):
            return "StatusError"
        self.param_initial["kinryoku"], self.param_initial["power"], self.param_initial["chikara"], self.param_initial["yasei"] = user_params
        self.param_initial["HP"] = self.param_initial["power"] * 3 + 10
        self.param = self.param_initial
        return "Success"


class EnemyStatus(StatusManager):
    def __init__(self):
        super().__init__()
        self.id = randint(100000000000000000, 599999999999999999)
        self.type = "Enemy"
        # 念の為敵にも(たぶん)ユニークなidをもたせておく

    @classmethod
    def read_from_json(cls, name, file_path="statuses.json"):
        status = StatusManager()

        with open(file_path, mode="r") as f:
            json_raw = json.loads(f.read())

        status.param_initial["kinryoku"] = json_raw[name]["kinryoku"]
        status.param_initial["power"] = json_raw[name]["power"]
        status.param_initial["chikara"] = json_raw[name]["chikara"]
        status.param_initial["yasei"] = json_raw[name]["yasei"]
        status.param_initial["banana"] = json_raw[name]["banana"]
        status.param_initial["GP"] = json_raw[name]["GP"]

        status.param_initial["HP"] = status.param_initial["power"] * 3 + 10

        status.param = status.param_initial.copy()
        return status
