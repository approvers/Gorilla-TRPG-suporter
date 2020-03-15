import threading
from jsonmes import JSONMessage


class MessagesHolder(object):
    #messagesの保存用シングルトン

    __json_message = JSONMessage() 

    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
        
    def __init__(self):
        pass

    def get_message(self, scope, name, *kargs):
        return self.__json_message.get_message(scope, name, *kargs)