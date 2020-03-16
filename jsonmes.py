import json
import random


class JSONMessage:
    """
    JSONで提供されるメッセージを管理する。
    クラス分けをする必要はたぶんなかったすまん
    """

    def __init__(self, file_path="messages.json"):
        """
        JSONを読み込んでインスタンスを作る。

        :param file_path: メッセージ情報が格納されたJSON。通常指定する必要はない。
        """
        with open(file_path, mode="r", encoding="utf-8") as f:
            self.json_msg = json.loads(f.read())

    def get_message(self, scope, name, *kargs):
        """
        JSONからメッセージを読み込んで整形する。

        :param scope: JSONファイルの第一階層。
        :param name: JSONファイルの第二階層。
        :param kargs: 整形に使用するデータ。
        """
        msg = self.json_msg[scope][name]

        if isinstance(msg, str):
            return msg.format(*kargs)
        elif isinstance(msg, list):
            idx = random.randint(0, len(msg) - 1)
            return msg[idx].format(*kargs)
        else:
            raise RuntimeError("Illegal JSON message type!")
