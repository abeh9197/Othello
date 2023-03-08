from __future__ import annotations
from enum import Enum


class TileValue(Enum):
    """Model"""

    BLANK = {"color": "blank", "vis": " ", "num": -1}
    DARK = {"color": "dark", "vis": "○", "num": 0}
    LIGHT = {"color": "light", "vis": "●", "num": 1}
    CURSOR = {"color": None, "vis": "★", "num": 9}

    @staticmethod
    def from_number(num: int):
        for t in TileValue:
            if t.value["num"] == num:
                return t
        raise ValueError("Invalid number. Expected number is 0 or 1")


class Tile:
    """Model"""

    def __init__(self, value):
        self.value: TileValue = value

    def __str__(self) -> str:
        return str(self.value.value["vis"])

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return int(self.value.value["num"])

    def __eq__(self, other: Tile) -> bool:
        return self.value == other.value

    @staticmethod
    def from_number(n: int):
        return Tile(TileValue.from_number(n))
