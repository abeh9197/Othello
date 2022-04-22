from models.Tile import Tile
from typing import List
from copy import copy


class Board:
    """Model"""

    def __init__(self, cells=None):
        self.board_size: int = 8

        if cells is None:
            self.cells = self.init_board()
        else:
            self.cells = cells

    @property
    def _board_size(self):
        return self.board_size

    def init_board(self) -> List:
        blank_cell = Tile.from_number(-1)
        board = [
            [blank_cell for c in range(self.board_size)] for c in range(self.board_size)
        ]
        board[3][3] = Tile.from_number(0)
        board[3][4] = Tile.from_number(1)
        board[4][3] = Tile.from_number(1)
        board[4][4] = Tile.from_number(0)
        self.cells = board
        return self.cells

    def get_from_input(self, row: int, col: int, input_color: int):
        self.cells[col][row] = Tile.from_number(input_color)
        return copy(self)
