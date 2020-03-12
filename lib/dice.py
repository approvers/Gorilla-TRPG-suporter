from random import randint


class Dice:
    """
    ダイス処理を司るクラス
    いろんなことできるようにするつもり
    """
    def __init__(self, dice_formula, status=None, target=None):
        """
        ダイス式の初期化を行う
        この時点で使用ステータスと目標値の決定を行う
        Parameters
        ----------
        dice_formula: str
            ダイス式の文字列
        status : int
            使うステータスの補正値
        target : int
            目標値
        """
        self.dice_formula = dice_formula.split(", ")
        self.target       = target
        self.dice_results = []
        self.result       = 0
        if not target is None:
            self.target = target
        i = 0
        for d in dice_formula:
            dice_formula[i] = d[1:-1]
            i += 1
        if not status is None:
            self.dice_formula.append("+")
            self.dice_formula.append(str(status))

    def judge(self):
        dice_result = self.dice()
        if self.result >= self.target:
            return "成功:" + dice_result
        return "失敗:" + dice_result

    def _roll(self, dice_count, dice_max):
        """
        実際のダイス判定を行う

        Parameters
        ---------
        dice_count: int
            ダイスの数
        dice_max: int
            ダイスの面の数
        """
        for n in range(dice_count):
            r = randint(1, dice_max)
            self.dice_results.append(r)
            self.result += r

    def dice(self):
        """
        ダイス式からダイス判定を行う
        Parameters
        ----------
        dice_formula : list<str>
            ダイスの式を['2D6', '+', '3']という形に整形したもの
        Returns
        -------
        result : str
            ダイス判定の結果と出目をまとめた文字列
            またはエラー文
        """
        self._result_reset()
        i           = 0
        next_calc   = "+"
        for s in self.dice_formula:
            cache = 0
            if i % 2 == 0:
                if "D" in s:
                    splitted_dice_formula = s.split("D")
                    # Dの両サイドが自然数に変換できるか検証
                    if not splitted_dice_formula[0].isdecimal() or not splitted_dice_formula[1].isdecimal():
                        return "Error:1 can use only Natural number on dice formula"
                    dice_count = int(splitted_dice_formula[0])
                    dice_max   = int(splitted_dice_formula[1])

                    self._roll(dice_count, dice_max)

                else:
                    # 入力された値が自然数か検証
                    if not s.isdecimal():
                        return "Error:1 can use only Natural number on dice formula"
                    cache = int(s)
                self.result += eval("{}cache".format(next_calc), {}, {"cache":cache})
            else:
                if s in ["+", "-"]:
                    next_calc = s
                else:
                    return "Error:2 can use only Addition or Subtraction"

            i += 1
        return str(self.result)+str(self.dice_results)

    def _result_reset(self):
        self.result = 0
