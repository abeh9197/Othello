from enum import Enum

class TileValue(Enum):
    dark = {'color': 'dark', 'num': 0}
    light = {'color': 'light', 'num': 1}

    @staticmethod
    def from_number(num: int):
        for t in TileValue:
            if t.value['num'] == num:
                return t
        raise ValueError('Invalid number. Expected number is 0 or 1.')


class Tile:

    def __init__(self, value):
        self.value: TileValue = value

    def __str__(self) -> str: 
        return str(self.value.value['color'])

    def __repr__(self) -> str:
        return str(self)

    @staticmethod
    def from_number(n: int):
        return Tile(TileValue.from_number(n))


class Board:
    def __init__(self, cells=None, size=8):
        if cells is None:
                self.cells = []
        else:
            self.cells = cells

        self.size = size

    def board(self):
        board = [[self.cells for m in range(self.size)] for n in range(self.size)]
        board[3][3] = Tile.from_number(0)
        board[3][4] = Tile.from_number(1)
        board[4][3] = Tile.from_number(1)
        board[4][4] = Tile.from_number(0)
        return board 


class BoardView:
    def __init__(self, board):
        self.board = board

    def 