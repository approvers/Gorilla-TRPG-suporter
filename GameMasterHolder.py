import threading


class GameMasterHolder(object):
    #GameMaster保存用のシングルトン

    __game_master = None 

    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
        
    def __init__(self):
        pass

    def get_master(self):
        return GameMasterHolder.__game_master
    def set_master(self, user):
        GameMasterHolder.__game_master = user