import json
import random


class JSONMessage:
    """
    JSONで提供されるメッセージを管理する。
    クラス分けをする必要はたぶんなかったすまん
    """

    def __init__(self, file_path="messages.json"):
        with open(file_path, mode="r") as f:
            self.json_msg = json.loads(f.read())

    def get_message(self, scope, name, **kwargs):
        msg = self.json_msg[scope][name]

        if isinstance(msg, str):
            return msg
        elif isinstance(msg, list):
            idx = random.randint(0, len(msg) - 1)
            return msg[idx]
        else:
            raise RuntimeError("Illegal JSON message type!")
