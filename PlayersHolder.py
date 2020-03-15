import threading


class PlayersHolder(object):
    #player保存用のシングルトン
    #playersよくわからないのでプレイヤー追加とかの関数は任せる
    #辞書型であれば参照渡しのはずなのでgetしてそのまま変更してもいいけどお勧めしない

    __players = {} 

    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
        
    def __init__(self):
        pass

    def get_players(self):
        return self.__players