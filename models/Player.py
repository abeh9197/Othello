from typing import Tuple
from utils.log import logger


class Player:
    """Controller"""

    def __init__(self):
        pass

    def player_input(self) -> Tuple:
        """
        TODO: need assertion error
        """
        x = input("入力してください x : ")
        y = input("入力してください y : ")

        if self.input_validation(x, y):
            return int(x)-1, int(y)-1

        else:
            logger.info("無効な入力がありました。もう一度入力してください。")
            return self.player_input()

    def input_validation(self, x, y) -> bool:
        return x != "" and y != ""
