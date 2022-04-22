import itertools
from models.Board import Board
from models.Tile import Tile


class Status:
    """Model"""

    def __init__(self) -> None:
        self.turn: int = 0
        self.current_player: int = 0
    
    def change_player(self):
        if self.current_player == 0:
            self.current_player = 1
        elif self.current_player == 1:
            self.current_player = 0
    
    def show_whos_turn(self) -> str:
        if self.current_player == 0:
            return "黒"
        if self.current_player == 1:
            return "白"

    def count_cell_type(self, board: Board) -> dict:
        cells_flatten = list(itertools.chain.from_iterable(board.cells))
        blank = cells_flatten.count(Tile.from_number(-1))
        dark =  cells_flatten.count(Tile.from_number(0))
        light = cells_flatten.count(Tile.from_number(1))
        return {"blank": blank, "dark": dark, "light": light}
