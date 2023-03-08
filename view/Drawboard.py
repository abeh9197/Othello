import readchar
from models.Board import Board
from models.Tile import Tile
from models.Manager import Manager
from models.Status import Status
from utils.log import logger


class DrawBoard:
    """View"""

    def __init__(self):
        self.manager = Manager()
        self.status = Status()

    def __draw(self, board: Board, input_tile: Tile, cursor_row: int, cursor_col: int):
        """
        NOTE: 盤面を描写する
        """
        board_ = board.cells[:]
        cursor = Tile.from_number(9)
        print("   1  2  3  4  5  6  7  8")
        print("  +--+--+--+--+--+--+--+--+")
        for i in range(board.board_size):
            print(i+1, "|", end="")
            for j in range(8):
                if i == cursor_row and j == cursor_col:
                    board_[i][j] = cursor
                print(board_[i][j], "|", end="")
            print("\n  +--+--+--+--+--+--+--+--+")

        where_you_can_put = list(
            set(self.manager.where_you_can_put(board=board, input_tile=input_tile))
        )
        where_you_can_put = [(position[0] + 1, position[1] + 1) for position in where_you_can_put]

        if len(where_you_can_put) > 0:
            logger.info(f"残り {self.status.count_cell_type(board=board)}")
            logger.info(f"置ける場所 {where_you_can_put}")
        else:
            logger.info(f"置ける場所がありません")

    def draw(self, board: Board, input_tile: Tile) -> None:
        cursor_row = 0
        cursor_col = 0
        self.__draw(board, input_tile, cursor_row, cursor_col)
        while True:
            key = readchar.readkey()
            if key == readchar.key.UP:
                cursor_row = max(0, cursor_row-1)
            elif key == readchar.key.DOWN:
                cursor_row = min(len(board.cells)-1, cursor_row+1)
            elif key == readchar.key.LEFT:
                cursor_col = max(0, cursor_col-1)
            elif key == readchar.key.RIGHT:
                cursor_col = min(len(board.cells[0])-1, cursor_col+1)
            elif key == '\r':
                # Enter key pressed
                break
            self.__draw(board, input_tile, cursor_row, cursor_col)