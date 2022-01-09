from typing import Tuple

class Player:
    """Controller"""

    def __init__(self):
        pass

    def player_input(self) -> Tuple:
        """
        TODO: need assertion error
        """
        x = int(input("入力してください x : "))
        y = int(input("入力してください y : "))
        return x, y

