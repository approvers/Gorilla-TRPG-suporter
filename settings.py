import json


class JSONSettings(dict):
    """
    JSONと設定とをつなぎます
    世界平和だね
    当クラスではdictを継承するという最先端技術を取り入れています
    """

    def __init__(self, file_path="settings.json"):
        self.file_path = file_path
        self.settings_data = {}
        self.reload()

    def reload(self, file_path=None):
        if file_path is None:
            file_path = self.file_path
        with open(file_path, mode="r") as f:
            self.settings_data = json.loads(f.read())

    def save(self, file_path=None):
        if file_path is None:
            file_path = self.file_path
        json_raw = json.dumps(self.settings_data, indent=3)

        with open(self.file_path, mode="w") as f:
            f.write(json_raw)

    def __getitem__(self, k):
        return self.settings_data[k]

    def __setitem__(self, k, v):
        self.settings_data[k] = v
